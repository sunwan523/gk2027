# -*- coding: utf-8 -*-
"""空间（成长记录）：签到、随手记、体重、用户设置、照片存储、AI 整理、隐秘空间加密。"""
import base64, hashlib, io, json, os, re, uuid
from datetime import datetime, timedelta

from core import ai_quiz
from core.ai_quiz import _chat, API_URL, API_KEY, MODEL  # noqa: F401（_chat 复用）

try:
    from cryptography.fernet import Fernet, InvalidToken
    FERNET_OK = True
except Exception:
    FERNET_OK = False

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
PHOTO_ROOT = os.path.join(DATA_DIR, "photos")            # 常规照片（静态挂载）
PRIVATE_ROOT = os.path.join(DATA_DIR, "photos_private")  # 隐秘照片（不公开挂载）
MAX_PHOTO_BYTES = 8 * 1024 * 1024

KINDS = ("sign", "note")
CATEGORIES = ("学习总结", "心情", "想法", "反思", "灵感")
LOCKED_PLACEHOLDER = "🔒 隐秘内容，输入高级密码后可见"
_PBKDF2_ITER = 200_000


def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------------------------------------
# 建表
# ----------------------------------------------------------------------
def create_tables(conn):
    conn.execute("""CREATE TABLE IF NOT EXISTS profile (
        uid TEXT PRIMARY KEY,
        nickname TEXT DEFAULT '',
        birthday TEXT DEFAULT '',
        avatar_path TEXT DEFAULT '',
        cover_path TEXT DEFAULT '',
        private_pwd TEXT DEFAULT '',
        updated_at TEXT)""")
    conn.execute("""CREATE TABLE IF NOT EXISTS diary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT NOT NULL,
        date TEXT NOT NULL,
        kind TEXT NOT NULL,
        mood TEXT DEFAULT '',
        text TEXT DEFAULT '',
        category TEXT DEFAULT '',
        summary TEXT DEFAULT '',
        advice TEXT DEFAULT '',
        photos TEXT DEFAULT '[]',
        is_private INTEGER DEFAULT 0,
        cipher TEXT DEFAULT '',
        is_late INTEGER DEFAULT 0,
        created_at TEXT,
        UNIQUE(uid, date, kind))""")
    conn.execute("""CREATE TABLE IF NOT EXISTS weight (
        uid TEXT NOT NULL,
        date TEXT NOT NULL,
        value REAL NOT NULL,
        note TEXT DEFAULT '',
        created_at TEXT,
        PRIMARY KEY(uid, date))""")
    # 兼容旧库：profile 缺 cover_path 列时补充
    try:
        cols = [r["name"] for r in conn.execute("PRAGMA table_info(profile)")]
        if "cover_path" not in cols:
            conn.execute("ALTER TABLE profile ADD COLUMN cover_path TEXT DEFAULT ''")
    except Exception:
        pass
    conn.commit()


# ----------------------------------------------------------------------
# 照片存储（按 用户/类型/日期 分类，文件名带时间；隐秘照片独立目录）
# ----------------------------------------------------------------------
def _decode_b64(data_url: str) -> tuple[bytes, str]:
    m = re.match(r"data:image/(png|jpe?g|webp);base64,(.+)", data_url or "")
    if not m:
        raise ValueError("仅支持 png/jpg/webp 图片")
    try:
        raw = base64.b64decode(m.group(2))
    except Exception:
        raise ValueError("图片数据无效")
    if not raw or len(raw) > MAX_PHOTO_BYTES:
        raise ValueError("图片过大或为空（上限 8MB）")
    ext = "png" if m.group(1) == "png" else "jpg"
    return raw, ext


def save_photo(uid: str, kind: str, date: str, data_url: str) -> str:
    """kind: selfie / note / avatar / private。返回相对路径。"""
    raw, ext = _decode_b64(data_url)
    root = PRIVATE_ROOT if kind == "private" else PHOTO_ROOT
    if kind == "avatar":
        d = os.path.join(root, uid, "avatar")
    else:
        d = os.path.join(root, uid, kind, date)
    os.makedirs(d, exist_ok=True)
    stamp = datetime.now().strftime("%H%M%S")
    name = f"{stamp}_{uuid.uuid4().hex[:6]}.{ext}"
    path = os.path.join(d, name)
    with open(path, "wb") as f:
        f.write(raw)
    return os.path.relpath(path, DATA_DIR).replace("\\", "/")


def photo_abs_path(rel: str) -> str:
    full = os.path.normpath(os.path.join(DATA_DIR, rel))
    if not full.startswith(os.path.normpath(DATA_DIR)):
        raise ValueError("非法路径")
    return full


def delete_photos(paths):
    for p in paths or []:
        full = photo_abs_path(p)
        try:
            if os.path.isfile(full):
                os.remove(full)
        except (OSError, ValueError):
            pass


# ----------------------------------------------------------------------
# 隐秘空间：密码派生密钥 + Fernet 加密
# ----------------------------------------------------------------------
def _hash_pwd(pwd: str, salt: bytes) -> str:
    dk = hashlib.pbkdf2_hmac("sha256", pwd.encode("utf-8"), salt, _PBKDF2_ITER)
    return f"pbkdf2${_PBKDF2_ITER}${base64.b64encode(salt).decode()}${base64.b64encode(dk).decode()}"


def _verify_hash(stored: str, pwd: str) -> bool:
    try:
        _, it, salt, want = stored.split("$")
        dk = hashlib.pbkdf2_hmac("sha256", pwd.encode("utf-8"),
                                 base64.b64decode(salt), int(it))
        return base64.b64encode(dk).decode() == want
    except Exception:
        return False


def _derive_key(pwd: str, salt: bytes):
    if not FERNET_OK:
        raise RuntimeError("加密库不可用（cryptography 未安装）")
    dk = hashlib.pbkdf2_hmac("sha256", pwd.encode("utf-8"), salt, _PBKDF2_ITER)
    return Fernet(base64.urlsafe_b64encode(dk))


def get_private_status(conn, uid: str) -> dict:
    row = conn.execute("SELECT private_pwd FROM profile WHERE uid=?", (uid,)).fetchone()
    return {"enabled": bool(row and row["private_pwd"])}


def set_private_pwd(conn, uid: str, new_pwd: str, old_pwd: str = "") -> dict:
    """设置/修改高级密码。已有密码时必须校验旧密码。改密时用旧密钥解密再重加密。"""
    if not new_pwd or len(new_pwd) < 4:
        raise ValueError("高级密码至少 4 位")
    row = conn.execute("SELECT private_pwd FROM profile WHERE uid=?", (uid,)).fetchone()
    old_stored = row["private_pwd"] if row else ""
    if old_stored:
        if not old_pwd or not _verify_hash(old_stored, old_pwd):
            raise ValueError("旧密码不正确")
        old_salt = base64.b64decode(old_stored.split("$")[2])
        old_key = _derive_key(old_pwd, old_salt)
        # 用旧密钥解出全部隐秘正文
        cipher_rows = conn.execute(
            "SELECT id,cipher FROM diary WHERE uid=? AND is_private=1", (uid,)).fetchall()
        plaintexts = {}
        for r in cipher_rows:
            try:
                plaintexts[r["id"]] = old_key.decrypt(r["cipher"].encode()).decode("utf-8")
            except Exception:
                pass
    else:
        plaintexts = {}
    salt = os.urandom(16)
    stored = _hash_pwd(new_pwd, salt)
    key = _derive_key(new_pwd, salt)
    for did, txt in plaintexts.items():
        conn.execute("UPDATE diary SET cipher=? WHERE id=?",
                     (key.encrypt(txt.encode("utf-8")).decode(), did))
    conn.execute("""INSERT INTO profile(uid,private_pwd,updated_at) VALUES(?,?,?)
                    ON CONFLICT(uid) DO UPDATE SET private_pwd=?, updated_at=?""",
                 (uid, stored, _now(), stored, _now()))
    conn.commit()
    return {"ok": True}


def verify_private_pwd(conn, uid: str, pwd: str):
    """校验通过返回解密密钥（Fernet），失败抛 ValueError。"""
    row = conn.execute("SELECT private_pwd FROM profile WHERE uid=?", (uid,)).fetchone()
    if not row or not row["private_pwd"]:
        raise ValueError("尚未设置高级密码")
    if not _verify_hash(row["private_pwd"], pwd):
        raise ValueError("高级密码不正确")
    salt = base64.b64decode(row["private_pwd"].split("$")[2])
    return _derive_key(pwd, salt)


# ----------------------------------------------------------------------
# 用户设置
# ----------------------------------------------------------------------
def get_profile(conn, uid: str) -> dict:
    row = conn.execute("SELECT nickname,birthday,avatar_path,cover_path,private_pwd FROM profile WHERE uid=?", (uid,)).fetchone()
    return {"nickname": row["nickname"] if row else "",
            "birthday": row["birthday"] if row else "",
            "avatar": row["avatar_path"] if row else "",
            "cover": row["cover_path"] if row else "",
            "private_enabled": bool(row and row["private_pwd"])}


def save_profile(conn, uid: str, nickname: str = "", birthday: str = "", cover_path: str = "") -> dict:
    conn.execute("""INSERT INTO profile(uid,nickname,birthday,cover_path,updated_at) VALUES(?,?,?,?,?)
                    ON CONFLICT(uid) DO UPDATE SET nickname=?, birthday=?, cover_path=?, updated_at=?""",
                 (uid, (nickname or "").strip()[:20], (birthday or "").strip()[:10], cover_path, _now(),
                  (nickname or "").strip()[:20], (birthday or "").strip()[:10], cover_path, _now()))
    conn.commit()
    return get_profile(conn, uid)


def set_avatar(conn, uid: str, data_url: str) -> str:
    p = save_photo(uid, "avatar", "", data_url)
    old = conn.execute("SELECT avatar_path FROM profile WHERE uid=?", (uid,)).fetchone()
    conn.execute("""INSERT INTO profile(uid,avatar_path,updated_at) VALUES(?,?,?)
                    ON CONFLICT(uid) DO UPDATE SET avatar_path=?, updated_at=?""",
                 (uid, p, _now(), p, _now()))
    conn.commit()
    if old and old["avatar_path"] and old["avatar_path"] != p:
        delete_photos([old["avatar_path"]])
    return p


def set_cover(conn, uid: str, data_url: str) -> str:
    p = save_photo(uid, "cover", "", data_url)
    old = conn.execute("SELECT cover_path FROM profile WHERE uid=?", (uid,)).fetchone()
    conn.execute("""INSERT INTO profile(uid,cover_path,updated_at) VALUES(?,?,?)
                    ON CONFLICT(uid) DO UPDATE SET cover_path=?, updated_at=?""",
                 (uid, p, _now(), p, _now()))
    conn.commit()
    if old and old["cover_path"] and old["cover_path"] != p:
        delete_photos([old["cover_path"]])
    return p


# ----------------------------------------------------------------------
# 日记：签到 / 随手记 / 体重
# ----------------------------------------------------------------------
def _photo_paths(d):
    try:
        # sqlite3.Row 无 .get()，用下标；dict 用 .get()
        v = d["photos"] if hasattr(d, "keys") else d.get("photos")
        return json.loads(v or "[]")
    except Exception:
        return []


def save_diary(conn, uid: str, date: str, kind: str, *, mood="", text="",
               photos=None, category="", summary="", advice="", is_late=0,
               is_private=0, key=None):
    """is_private=1 时正文必须用 key（Fernet）加密后存 cipher，text 不落明文。"""
    if kind not in KINDS:
        raise ValueError("kind 只能是 sign/note")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        raise ValueError("日期格式应为 YYYY-MM-DD")
    if kind == "sign" and not photos:
        raise ValueError("签到需要一张照片")
    paths = json.dumps(photos or [], ensure_ascii=False)
    priv = 1 if is_private else 0
    cipher = ""
    if priv:
        if key is None:
            raise ValueError("隐秘内容需先解锁高级密码")
        cipher = key.encrypt((text or "").encode("utf-8")).decode()
    # 覆盖时先清掉旧照片（不同列表的旧文件）
    old = conn.execute("SELECT photos FROM diary WHERE uid=? AND date=? AND kind=?",
                       (uid, date, kind)).fetchone()
    conn.execute("""INSERT INTO diary(uid,date,kind,mood,text,photos,category,summary,advice,
                    is_private,cipher,is_late,created_at)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ON CONFLICT(uid,date,kind) DO UPDATE SET
                      mood=?, text=?, photos=?, category=?, summary=?, advice=?,
                      is_private=?, cipher=?, is_late=?, created_at=?""",
                 (uid, date, kind, mood[:50], ("" if priv else text[:2000]), paths,
                  (category or "")[:10], (summary or "")[:200], (advice or "")[:200],
                  priv, cipher, int(is_late), _now(),
                  mood[:50], ("" if priv else text[:2000]), paths,
                  (category or "")[:10], (summary or "")[:200], (advice or "")[:200],
                  priv, cipher, int(is_late), _now()))
    conn.commit()
    # 旧照片清理（新照片列表变化时）
    if old:
        old_paths = _photo_paths(old)
        new_set = set(paths or [])
        to_del = [p for p in old_paths if p not in new_set]
        if to_del:
            delete_photos(to_del)


def save_weight(conn, uid: str, date: str, value: float, note: str = ""):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        raise ValueError("日期格式应为 YYYY-MM-DD")
    if not (20 <= float(value) <= 300):
        raise ValueError("体重应在 20-300 kg 之间")
    conn.execute("""INSERT INTO weight(uid,date,value,note,created_at) VALUES(?,?,?,?,?)
                    ON CONFLICT(uid,date) DO UPDATE SET value=?, note=?, created_at=?""",
                 (uid, date, float(value), (note or "").strip()[:100], _now(),
                  float(value), (note or "").strip()[:100], _now()))
    conn.commit()


def _decrypt_text(key, cipher: str) -> str:
    try:
        return key.decrypt(cipher.encode()).decode("utf-8")
    except Exception:
        return LOCKED_PLACEHOLDER


def get_month(conn, uid: str, ym: str) -> dict:
    if not re.match(r"^\d{4}-\d{2}$", ym):
        raise ValueError("月份格式应为 YYYY-MM")
    days, sign_cnt = {}, 0
    for row in conn.execute(
            "SELECT date,kind FROM diary WHERE uid=? AND substr(date,1,7)=?", (uid, ym)):
        d = days.setdefault(row["date"], {"sign": False, "note": False, "weight": None})
        if row["kind"] == "sign":
            d["sign"] = True
            sign_cnt += 1
        elif row["kind"] == "note":
            d["note"] = True
    for row in conn.execute(
            "SELECT date,value FROM weight WHERE uid=? AND substr(date,1,7)=?", (uid, ym)):
        d = days.setdefault(row["date"], {"sign": False, "note": False, "weight": None})
        d["weight"] = row["value"]
    streak = 0
    today = datetime.now().strftime("%Y-%m-%d")
    for i in range(0, 366):
        d = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        r = conn.execute("SELECT 1 FROM diary WHERE uid=? AND date=? AND kind='sign'",
                         (uid, d)).fetchone()
        if r:
            streak += 1
        elif i == 0:
            continue
        else:
            break
    total = conn.execute("SELECT COUNT(*) n FROM diary WHERE uid=? AND kind='sign'", (uid,)).fetchone()["n"]
    return {"ym": ym, "days": days, "streak": streak, "total_sign": total}


def get_day(conn, uid: str, date: str, key=None) -> dict:
    rows = conn.execute(
        "SELECT id,date,kind,mood,text,category,summary,advice,photos,is_private,cipher,is_late,created_at "
        "FROM diary WHERE uid=? AND date=? ORDER BY kind", (uid, date)).fetchall()
    w = conn.execute("SELECT value,note FROM weight WHERE uid=? AND date=?", (uid, date)).fetchone()
    return {"date": date,
            "sign": _row_dict(rows, "sign", key),
            "note": _row_dict(rows, "note", key),
            "weight": {"value": w["value"], "note": w["note"]} if w else None}


def _row_dict(rows, kind, key=None):
    for r in rows:
        if r["kind"] == kind:
            priv = bool(r["is_private"])
            text = ""
            if priv:
                text = _decrypt_text(key, r["cipher"]) if key else LOCKED_PLACEHOLDER
            else:
                text = r["text"]
            return {"id": r["id"], "mood": r["mood"], "text": text,
                    "category": r["category"], "summary": r["summary"], "advice": r["advice"],
                    "photos": _photo_paths(r), "is_private": priv,
                    "locked": priv and not key, "is_late": r["is_late"], "created_at": r["created_at"]}
    return None


def get_weights(conn, uid: str) -> list:
    rows = conn.execute(
        "SELECT date,value,note FROM weight WHERE uid=? ORDER BY date", (uid,)).fetchall()
    return [{"date": r["date"], "value": r["value"], "note": r["note"]} for r in rows]


def list_all(conn, uid: str, limit=120, key=None) -> list:
    rows = conn.execute(
        "SELECT id,date,kind,mood,text,category,summary,photos,is_private,cipher,is_late,created_at "
        "FROM diary WHERE uid=? ORDER BY date DESC, id DESC LIMIT ?", (uid, int(limit))).fetchall()
    out = []
    for r in rows:
        priv = bool(r["is_private"])
        txt = ""
        if priv:
            txt = _decrypt_text(key, r["cipher"]) if key else LOCKED_PLACEHOLDER
        else:
            txt = r["text"]
        d = {"id": r["id"], "date": r["date"], "kind": r["kind"], "mood": r["mood"],
             "text": txt, "category": r["category"], "summary": r["summary"],
             "photos": _photo_paths(r), "is_private": priv, "locked": priv and not key,
             "is_late": r["is_late"], "created_at": r["created_at"]}
        d["label"] = "📷 签到" if d["kind"] == "sign" else "📝 随手记"
        if priv:
            d["label"] += " 🔒"
        out.append(d)
    return out


def delete_diary(conn, uid: str, did: int):
    row = conn.execute("SELECT photos FROM diary WHERE id=? AND uid=?", (did, uid)).fetchone()
    if row:
        delete_photos(_photo_paths(row))
        conn.execute("DELETE FROM diary WHERE id=?", (did,))
        conn.commit()
        return True
    return False


def delete_weight(conn, uid: str, date: str):
    conn.execute("DELETE FROM weight WHERE uid=? AND date=?", (uid, date))
    conn.commit()


# ----------------------------------------------------------------------
# AI 整理（分类 + 摘要 + 建议）；隐秘内容禁止调用
# ----------------------------------------------------------------------
def organize(text: str) -> dict:
    sys = ("你是文字规范化助手。用户输入一段口语化的文字（可能来自语音输入，可能已有轻微整理）。\n"
           "你的核心任务是把这段文字改写成规范的书面语，硬性要求：\n"
           "1. 保留全部内容和信息，不改变原意，不删减、不添加任何实质内容；\n"
           "2. 只做语言规范化：修正口语词、语病、重复啰嗦、错别字、标点，理顺句式，适当分段；\n"
           "3. 不追求华丽文风，保持朴素、准确、通顺，贴近原文的语气但更书面；\n"
           "4. 绝对不能缩写、总结成短句或丢失任何细节。\n"
           "随后附加：category 只能从【学习总结、心情、想法、反思、灵感】中选一个最贴切的；"
           "summary 给一句话摘要（不超过30字）；若对复习有帮助给一句简短建议 advice，否则空字符串。\n"
           "只输出JSON：{\"category\":\"\",\"summary\":\"\",\"advice\":\"\",\"text\":\"规范化后的完整正文\"}")
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": sys},
            {"role": "user", "content": (text or "")[:2000]},
        ],
        "temperature": 0.3, "max_tokens": 900,
    }
    body = _chat(payload)
    content = (body["choices"][0]["message"]["content"] or "").strip()
    m = re.search(r"\{.*\}", content, re.S)
    if m:
        try:
            j = json.loads(m.group(0))
            c = j.get("category", "")
            if c not in CATEGORIES:
                c = "想法"
            ntext = (j.get("text") or "").strip()
            return {"category": c, "summary": (j.get("summary") or "")[:200],
                    "advice": (j.get("advice") or "")[:200],
                    "text": ntext if ntext else (text or "").strip()}
        except Exception:
            pass
    return {"category": "想法", "summary": (text or "").strip()[:60], "advice": "",
            "text": (text or "").strip()}
