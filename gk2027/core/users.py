# -*- coding: utf-8 -*-
"""多用户支持：用户注册表 + 每用户独立数据库。

设计（2026-09-12）：
  - 用户注册表 data/users.json：{users:[{id,name,created}], current:"<id>"}
  - 每用户一个完整 SQLite 库：data/users/<id>.db
    （知识点掌握度、答题记录、错题本、SRS 卡片全部隔离；
      题库/图谱靠 seed 灌入，讲解内容 content_*.py 本来就全局共享）
  - 隔离粒度选"分库"而非"表加 user_id 列"：现有全部 SQL 零改动，
    单人本地场景下最简单可靠；备份=拷一个文件。
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
from datetime import date

from config import DATA_DIR

USERS_DIR = os.path.join(DATA_DIR, "users")
REGISTRY = os.path.join(DATA_DIR, "users.json")
os.makedirs(USERS_DIR, exist_ok=True)

# 家庭准入码（可选）。设置后，任何建号/登录都必须同时提供正确的准入码，
# 相当于给公网部署再加一道门。容器里用环境变量 GK_ACCESS_CODE 注入。
#
# 取值优先级：
#   1) 环境变量 GK_ACCESS_CODE
#   2) data/access_code.txt（挂载卷内的文件，内容即准入码）
# 之所以加文件兜底：容器是 docker run 无 -e 重建的（见 tools/deploy.ps1），
# 只靠环境变量的话，每次部署重建容器都会把这道门悄悄丢掉。
def _load_access_code() -> str:
    code = os.environ.get("GK_ACCESS_CODE", "").strip()
    if code:
        return code
    try:
        with open(os.path.join(DATA_DIR, "access_code.txt"), encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


ACCESS_CODE = _load_access_code()

# 免密模式（家庭自用部署）：data/no_pwd.txt 存在时，登录不再校验准入码和密码，
# 点名字即进（新名字直接建号）。需要恢复密码门时删除该文件并重启容器即可。
LOGIN_NO_PWD = os.path.exists(os.path.join(DATA_DIR, "no_pwd.txt"))

_PBKDF2_ITER = 200_000
MIN_PWD_LEN = 4


# ---------------------------------------------------------------- 口令
def _hash_pwd(pwd: str, salt: bytes) -> str:
    dk = hashlib.pbkdf2_hmac("sha256", pwd.encode("utf-8"), salt, _PBKDF2_ITER)
    return "pbkdf2$%d$%s$%s" % (
        _PBKDF2_ITER,
        base64.b64encode(salt).decode(),
        base64.b64encode(dk).decode(),
    )


def _verify_pwd(pwd: str, stored: str) -> bool:
    try:
        _, it, salt, want = stored.split("$")
    except (ValueError, AttributeError):
        return False
    dk = hashlib.pbkdf2_hmac("sha256", str(pwd).encode("utf-8"),
                             base64.b64decode(salt), int(it))
    return hmac.compare_digest(base64.b64encode(dk).decode(), want)


# ---------------------------------------------------------------- registry
def _load() -> dict:
    try:
        with open(REGISTRY, encoding="utf-8") as f:
            reg = json.load(f)
        if isinstance(reg.get("users"), list):
            return reg
    except (OSError, ValueError):
        pass
    return {"users": [], "current": None}


def _save(reg: dict) -> None:
    tmp = REGISTRY + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)
    os.replace(tmp, REGISTRY)


def _uid(name: str) -> str:
    """用户 id：名字哈希短码，避免中文名进文件名带来的编码/路径问题。"""
    return "u" + hashlib.md5(name.encode("utf-8")).hexdigest()[:8]


# ---------------------------------------------------------------- CRUD
def list_users() -> list[dict]:
    return _load()["users"]


def _check_pwd(pwd: str) -> str:
    pwd = (pwd or "").strip()
    if len(pwd) < MIN_PWD_LEN:
        raise ValueError("密码至少 %d 位" % MIN_PWD_LEN)
    return pwd


def add_user(name: str, password: str = "") -> dict:
    name = name.strip()
    if not name:
        raise ValueError("名字不能为空")
    if not re.fullmatch(r"[\w\u4e00-\u9fff·\s-]{1,20}", name):
        raise ValueError("名字只能是 1—20 个中文/字母/数字")
    reg = _load()
    if any(u["name"] == name for u in reg["users"]):
        raise ValueError("已存在同名用户：%s" % name)
    u = {"id": _uid(name), "name": name, "created": date.today().isoformat(),
         "pwd": _hash_pwd(_check_pwd(password), os.urandom(16))}
    reg["users"].append(u)
    reg["current"] = u["id"]
    _save(reg)
    return u


def set_password(name: str, password: str) -> None:
    """直接重置口令（已过准入码校验后调用）。"""
    reg = _load()
    hit = False
    for u in reg["users"]:
        if u["name"] == name.strip():
            u["pwd"] = _hash_pwd(_check_pwd(password), os.urandom(16))
            hit = True
    if not hit:
        raise ValueError("用户不存在：%s" % name)
    _save(reg)


def login(name: str, password: str, code: str = "") -> dict:
    """登录/建号入口：校验准入码 + 口令，成功返回 user。

    历史账号（registry 里没有 pwd 字段）在通过准入码后，
    用本次输入的口令完成初始化，之后正常校验。
    免密模式（LOGIN_NO_PWD）：跳过准入码与密码校验，直接进入/建号。
    """
    if LOGIN_NO_PWD:
        u = find_by_name(name)
        if u is None:
            return add_user(name, "no-pwd-01")   # 免密建号占位口令
        return u
    if ACCESS_CODE and (code or "").strip() != ACCESS_CODE:
        raise ValueError("准入码不正确")
    u = find_by_name(name)
    if u is None:
        return add_user(name, password)
    stored = u.get("pwd")
    if stored:
        if not _verify_pwd(password or "", stored):
            raise ValueError("密码不正确")
        return u
    # 老账号首次登录：初始化口令
    _check_pwd(password)
    reg = _load()
    for x in reg["users"]:
        if x["name"] == u["name"]:
            x["pwd"] = _hash_pwd(password, os.urandom(16))
    _save(reg)
    return find_by_name(name)


# ---------------------------------------------------------------- 会话签名
# uid 由名字 md5 前 8 位生成，是可预测的；因此 cookie 必须带服务端签名，
# 否则任何人知道用户名就能伪造 gk_uid 读取他人数据。
def _secret() -> bytes:
    p = os.path.join(DATA_DIR, "session.secret")
    try:
        with open(p, "rb") as f:
            s = f.read().strip()
        if s:
            return s
    except OSError:
        pass
    s = os.urandom(32).hex().encode()
    with open(p, "wb") as f:
        f.write(s)
    return s


def sign(uid: str) -> str:
    return hmac.new(_secret(), uid.encode("utf-8"), hashlib.sha256).hexdigest()[:32]


def make_token(uid: str) -> str:
    return "%s.%s" % (uid, sign(uid))


def verify_token(token: str) -> str | None:
    """校验 cookie 里的 token，通过返回 uid，否则 None。"""
    if not token or "." not in token:
        return None
    uid, _, sig = token.rpartition(".")
    if not uid or not hmac.compare_digest(sig, sign(uid)):
        return None
    return uid


def change_password(uid: str, old_pwd: str, new_pwd: str) -> None:
    reg = _load()
    u = next((x for x in reg["users"] if x["id"] == uid), None)
    if not u:
        raise ValueError("用户不存在")
    if u.get("pwd") and not _verify_pwd(old_pwd or "", u["pwd"]):
        raise ValueError("原密码不正确")
    u["pwd"] = _hash_pwd(_check_pwd(new_pwd), os.urandom(16))
    _save(reg)


def remove_user(uid: str) -> None:
    reg = _load()
    reg["users"] = [u for u in reg["users"] if u["id"] != uid]
    if reg["current"] == uid:
        reg["current"] = reg["users"][0]["id"] if reg["users"] else None
    _save(reg)
    p = db_path(uid)
    try:
        if os.path.exists(p):
            os.rename(p, p + ".deleted")   # 不物理删，留一手
    except OSError:
        pass   # 服务占用中：注册表已移除，文件留待下次清理


def get_current() -> dict | None:
    reg = _load()
    cid = reg.get("current")
    return next((u for u in reg["users"] if u["id"] == cid), None)


def set_current(uid: str) -> None:
    reg = _load()
    if not any(u["id"] == uid for u in reg["users"]):
        raise ValueError("用户不存在：%s" % uid)
    reg["current"] = uid
    _save(reg)


def find_by_name(name: str) -> dict | None:
    return next((u for u in list_users() if u["name"] == name.strip()), None)


# ---------------------------------------------------------------- paths
def db_path(uid: str) -> str:
    return os.path.join(USERS_DIR, "%s.db" % uid)


def ensure_user(name: str) -> dict:
    """取已有用户或创建新用户（幂等，手机端登录页用）。"""
    u = find_by_name(name)
    return u or add_user(name)
