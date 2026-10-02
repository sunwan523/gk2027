# -*- coding: utf-8 -*-
"""高考复习系统 · FastAPI 后端（替代 Streamlit 界面层）。

架构：core/ 下的题库、知识点、作答判分、AI 出题、学习统计全部原样复用，
本文件只把它们包成 HTTP 接口；前端是 web/ 下的单页应用（原生 JS，无框架）。

运行（开发）：  python server.py
生产（后台）：  svc.py start / restart / stop （自动用 uvicorn 拉起）
"""
from __future__ import annotations

import os
import sys
import time
from datetime import date, timedelta

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
sys.path.insert(0, os.path.join(BASE, "_vendor"))   # fastapi/uvicorn 本地依赖

from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from config import SUBJECTS, ATTRIBUTIONS, EXAM_DURATION, EXAM_FULL_MARK
import config
from core import db, graph, queue, content, users, ai_quiz, study_advisor, recite_lib

try:
    import edge_tts  # 在线语音（微软 Edge TTS，音色丰富）
except Exception:
    edge_tts = None

app = FastAPI(title="高考复习", docs_url=None, redoc_url=None)

WEB_DIR = os.path.join(BASE, "web")
os.makedirs(WEB_DIR, exist_ok=True)

# ----------------------------------------------------------------------
# 用户会话：uid 写进 cookie（家庭内部使用，无敏感数据）
# ----------------------------------------------------------------------
COOKIE = "gk_uid"
MAX_AGE = 365 * 24 * 3600


def _user_from(req: Request):
    """从签名 cookie 还原用户。uid 可预测，所以只认带正确签名的 token。"""
    uid = users.verify_token(req.cookies.get(COOKIE, ""))
    if not uid:
        return None
    for u in users.list_users():
        if u["id"] == uid:
            return u
    return None


from functools import lru_cache


@lru_cache(maxsize=16)
def _conn(uid: str):
    """每个用户独立 SQLite 库连接（连接缓存，避免每次请求重建）。"""
    return db.init_db(users.db_path(uid), seed=False)


def _conn_for(req: Request):
    u = _user_from(req)
    if not u:
        return None, None
    return _conn(u["id"]), u


# ----------------------------------------------------------------------
# 在线朗读（Edge TTS）
# ----------------------------------------------------------------------
TTS_VOICES = [
    {"short": "zh-CN-XiaoxiaoNeural", "name": "晓晓 · 温柔女声"},
    {"short": "zh-CN-XiaoyiNeural", "name": "晓伊 · 自然女声"},
    {"short": "zh-CN-YunxiNeural", "name": "云希 · 阳光男声"},
    {"short": "zh-CN-YunjianNeural", "name": "云健 · 浑厚男声"},
    {"short": "zh-CN-YunyangNeural", "name": "云扬 · 新闻男声"},
    {"short": "zh-CN-YunxiaNeural", "name": "云夏 · 少年男声"},
    {"short": "zh-TW-HsiaoChenNeural", "name": "曉臻 · 台湾女声"},
]
_TTS_CACHE: dict = {}


@app.get("/api/tts_voices")
async def api_tts_voices():
    return {"voices": TTS_VOICES}


@app.post("/api/tts")
async def api_tts(req: Request):
    body = await req.json() or {}
    text = (body.get("text") or "").strip()
    voice = body.get("voice") or "zh-CN-XiaoxiaoNeural"
    rate = body.get("rate") or "+0%"
    if not text:
        return JSONResponse({"error": "文本为空"}, status_code=400)
    if len(text) > 1500:
        text = text[:1500]
    if edge_tts is None:
        return JSONResponse({"error": "在线语音组件未安装"}, status_code=501)
    key = (voice, rate, text)
    if key in _TTS_CACHE:
        return Response(content=_TTS_CACHE[key], media_type="audio/mpeg")
    try:
        buf = bytearray()
        comm = edge_tts.Communicate(text, voice, rate=rate)
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                buf.extend(chunk["data"])
        if not buf:
            return JSONResponse({"error": "语音生成失败，请稍后重试"}, status_code=502)
        data = bytes(buf)
        if len(_TTS_CACHE) > 200:
            _TTS_CACHE.clear()
        _TTS_CACHE[key] = data
        return Response(content=data, media_type="audio/mpeg")
    except Exception as e:
        return JSONResponse({"error": "在线语音暂不可用（可改用系统音色）"}, status_code=502)


# ----------------------------------------------------------------------
# 页面与静态资源
# ----------------------------------------------------------------------
@app.get("/")
def index():
    return FileResponse(os.path.join(WEB_DIR, "index.html"))


@app.get("/web/app.js")
def web_appjs():
    return FileResponse(os.path.join(WEB_DIR, "app.js"),
                        headers={"Cache-Control": "no-cache"})

@app.get("/web/style.css")
def web_css():
    return FileResponse(os.path.join(WEB_DIR, "style.css"),
                        headers={"Cache-Control": "no-cache"})


# ----------------------------------------------------------------------
# 登录 / 退出
# ----------------------------------------------------------------------
@app.get("/api/me")
async def api_me(req: Request):
    u = _user_from(req)
    if not u:
        return {"user": None}
    from core import diary as diary_mod
    prof = diary_mod.get_profile(_conn(u["id"]), u["id"])
    return {"user": {"id": u["id"], "name": u["name"], "nickname": prof["nickname"],
                     "birthday": prof["birthday"], "avatar": prof["avatar"]}}


@app.post("/api/login")
async def api_login(req: Request, res: Response):
    body = await req.json() or {}
    name = (body.get("name") or "").strip()
    if not name:
        return JSONResponse({"ok": False, "error": "名字不能为空"}, status_code=400)
    try:
        u = users.login(name, body.get("password", ""), body.get("code", ""))
    except ValueError as e:
        return JSONResponse({"ok": False, "error": str(e)}, status_code=401)
    # 首次使用灌入知识图谱与题库种子（幂等）
    db.init_db(users.db_path(u["id"]), seed=True)
    res.set_cookie(COOKIE, users.make_token(u["id"]),
                   max_age=MAX_AGE, httponly=True, samesite="lax")
    return {"ok": True, "user": {"id": u["id"], "name": u["name"]}}


@app.post("/api/logout")
def api_logout(res: Response):
    res.delete_cookie(COOKIE)
    return {"ok": True}


@app.get("/api/users")
async def api_users(req: Request):
    """登录后才能看到账号列表（避免公网匿名枚举 uid + 姓名）。"""
    if not _user_from(req):
        return JSONResponse({"error": "未登录"}, status_code=401)
    return {"users": [{"id": u["id"], "name": u["name"]} for u in users.list_users()]}


@app.post("/api/password")
async def api_password(req: Request):
    """修改密码。忘记密码时用 access code 重置（old_pwd 留空 + 传 code）。"""
    body = await req.json() or {}
    new_pwd = (body.get("new_pwd") or "").strip()
    name = (body.get("name") or "").strip()
    code = (body.get("code") or "").strip()
    try:
        if name and code:                       # 自助重置
            if users.ACCESS_CODE and code != users.ACCESS_CODE:
                return JSONResponse({"ok": False, "error": "准入码不正确"}, status_code=403)
            users.set_password(name, new_pwd)
        else:                                   # 已登录改密
            u = _user_from(req)
            if not u:
                return JSONResponse({"error": "未登录"}, status_code=401)
            users.change_password(u["id"], body.get("old_pwd", ""), new_pwd)
    except ValueError as e:
        return JSONResponse({"ok": False, "error": str(e)}, status_code=400)
    return {"ok": True}


@app.get("/api/auth_mode")
def api_auth_mode():
    """告诉前端是否需要准入码，登录页据此显示对应输入框。"""
    return {"need_code": bool(users.ACCESS_CODE)}


# ----------------------------------------------------------------------
# 顶栏
# ----------------------------------------------------------------------
@app.get("/api/header")
async def api_header(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    stt = queue.today_state(c)
    row = c.execute(
        "SELECT SUM(status='已掌握') m, COUNT(*) n FROM knowledge_points"
        " WHERE id NOT IN ('eng_vocab','chn_dictation')").fetchone()
    ratio = min(100, round(stt["xp_today"] / stt["xp_goal"] * 100))
    return {"uname": u["name"], "streak": stt["streak"],
            "mastered": row["m"] or 0, "total": row["n"] or 0,
            "xp_today": stt["xp_today"], "xp_goal": stt["xp_goal"],
            "goal_done": stt["goal_done"], "ratio": ratio}


# ----------------------------------------------------------------------
# 学习：课程队列
# ----------------------------------------------------------------------
@app.get("/api/lessons")
async def api_lessons(req: Request, subject: str = "全部"):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    s = None if subject == "全部" else subject
    lessons = queue.available_lessons(c, subject=s)
    # 追加已掌握课程（列表尾部带 ✅ 标记，可点击复习），让"学完的"在首页可见
    try:
        dq = ("SELECT * FROM knowledge_points WHERE status='已掌握'"
              " AND id NOT IN ('eng_vocab','chn_dictation')")
        args: tuple = ()
        if s:
            dq += " AND subject=?"
            args = (s,)
        lessons = lessons + [queue._lesson_row(c, r)
                             for r in c.execute(dq, args).fetchall()]
    except Exception:
        pass
    if not lessons:
        state = {"empty": True, "kind": "done"}
        if s:
            total = c.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE subject=? AND id NOT IN ('eng_vocab','chn_dictation')",
                (s,)).fetchone()[0]
            mastered = c.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE subject=? AND status='已掌握' AND id NOT IN ('eng_vocab','chn_dictation')",
                (s,)).fetchone()[0]
            locked = c.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE subject=? AND status='未解锁' AND id NOT IN ('eng_vocab','chn_dictation')",
                (s,)).fetchone()[0]
            no_quiz = c.execute(
                "SELECT COUNT(*) FROM knowledge_points k WHERE subject=? AND id NOT IN ('eng_vocab','chn_dictation')"
                " AND id NOT IN (SELECT DISTINCT kp_id FROM questions WHERE kp_id IS NOT NULL)",
                (s,)).fetchone()[0]
            if mastered >= total and total > 0:
                state = {"empty": True, "kind": "done"}
            elif locked > 0 and mastered == 0:
                state = {"empty": True, "kind": "locked", "n": locked}
            elif no_quiz > 0:
                state = {"empty": True, "kind": "no_quiz", "n": no_quiz}
            else:
                state = {"empty": True, "kind": "done"}
        return {"lessons": [], "empty": state}
    return {"lessons": lessons, "empty": None}


# ----------------------------------------------------------------------
# 一节课：要点 + 题目
# ----------------------------------------------------------------------
@app.post("/api/lesson/start")
async def api_lesson_start(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    kp_id = body.get("kp_id", "")
    if not kp_id:
        return JSONResponse({"error": "缺少 kp_id"}, status_code=400)
    row = c.execute("SELECT subject, name FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
    qs = queue.start_lesson(c, kp_id)
    if not qs:
        return JSONResponse({"error": "该知识点暂无自检题"}, status_code=400)
    pts = content.get_content(kp_id) or []
    return {"kp_id": kp_id,
            "subject": row["subject"] if row else "数学",
            "name": row["name"] if row else kp_id,
            "points": pts, "questions": qs}


# ----------------------------------------------------------------------
# 作答：选择/填空自动判分，解答类自评
# ----------------------------------------------------------------------
@app.post("/api/answer")
async def api_answer(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    qid = int(body.get("qid", 0))
    kp_id = body.get("kp_id", "")
    qtype = body.get("qtype", "选择题")
    if qtype == "选择题":
        letter = (body.get("letter") or "").strip()
        ok = queue.grade_choice(letter, body.get("answer", ""))
    else:
        ok = queue.grade_fill(body.get("text", ""), body.get("answer", ""))
    res = queue.submit_answer(c, qid, ok, kp_id=kp_id)
    row = c.execute("SELECT analysis, answer FROM questions WHERE id=?", (qid,)).fetchone()
    res["analysis"] = row["analysis"] if row else ""
    res["answer"] = body.get("answer", "")
    return res


@app.post("/api/answer_self")
async def api_answer_self(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    qid = int(body.get("qid", 0))
    ok = bool(body.get("correct"))
    res = queue.submit_answer(c, qid, ok, kp_id=body.get("kp_id", ""))
    return res


@app.post("/api/wrong_attr")
async def api_wrong_attr(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    qid = int(body.get("qid", 0))
    attr = body.get("attribution", "")
    if attr in ATTRIBUTIONS:
        queue.set_wrong_attribution(c, qid, attr)
    return {"ok": True}


@app.post("/api/lesson/finish")
async def api_lesson_finish(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    r = queue.finish_lesson(c, body.get("kp_id", ""), bool(body.get("all_correct")))
    row = c.execute("SELECT mastery, status FROM knowledge_points WHERE id=?",
                    (body.get("kp_id", ""),)).fetchone()
    r["mastery"] = round((row["mastery"] if row else 0) * 100)
    r["status"] = row["status"] if row else ""
    return r


# ----------------------------------------------------------------------
# 复习：到期卡片
# ----------------------------------------------------------------------
@app.get("/api/reviews")
async def api_reviews(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    cards = queue.due_reviews(c)
    return {"cards": cards, "total": len(cards)}


@app.post("/api/review")
async def api_review(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    queue.review_result(c, int(body.get("card_id", 0)), bool(body.get("remembered")))
    return {"ok": True}


# ----------------------------------------------------------------------
# AI 出题（本地题库：3 选择 + 2 填空，稳定不依赖在线 AI）
# ----------------------------------------------------------------------
@app.post("/api/ai_quiz")
async def api_ai_quiz(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    kp_id = body.get("kp_id", "")
    row = c.execute("SELECT subject, name FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
    if not row:
        return JSONResponse({"error": "知识点不存在"}, status_code=400)
    qs = queue.start_lesson(c, kp_id)
    if not qs:
        return JSONResponse({"error": "该知识点暂无题库题目"}, status_code=404)
    choices = [q for q in qs if q["qtype"] == "选择题"]
    fills = [q for q in qs if q["qtype"] == "填空题"]
    pick = choices[:3] + fills[:2]
    used = {q["qid"] for q in pick}
    pick += [q for q in qs if q["qid"] not in used][: max(0, 5 - len(pick))]
    out = [{"qid": q["qid"], "qtype": q["qtype"], "stem": q["stem"],
            "options": q["options"], "answer": q["answer"],
            "analysis": q["analysis"], "source": "题库"} for q in pick]
    return {"questions": out}


@app.post("/api/ai_explain")
async def api_ai_explain(req: Request):
    from core import explain
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    text = (body.get("text") or "").strip()
    kp_id = body.get("kp_id", "")
    if not text:
        return JSONResponse({"error": "缺少要讲解的内容"}, status_code=400)
    subject, name = "", ""
    if kp_id:
        row = c.execute("SELECT subject, name FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
        if row:
            subject, name = row["subject"], row["name"]
    try:
        return {"explain": explain.explain_point(subject, name, text)}
    except Exception as e:
        return JSONResponse({"error": "AI讲解失败：%s" % str(e)[:200]}, status_code=500)

# ----------------------------------------------------------------------
# 学习统计 + AI 建议
# ----------------------------------------------------------------------
@app.get("/api/stats")
async def api_stats(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    today_s = today.isoformat()

    def secs_since(d):
        if d:
            return int(c.execute("SELECT COALESCE(SUM(seconds),0) FROM activity_log WHERE day>=?", (d,)).fetchone()[0])
        return int(c.execute("SELECT COALESCE(SUM(seconds),0) FROM activity_log").fetchone()[0])

    days14 = [(today - timedelta(days=k)).isoformat() for k in range(13, -1, -1)]
    per_day = {}
    for r in c.execute("SELECT day, SUM(seconds) s FROM activity_log WHERE day>=? GROUP BY day", (days14[0],)):
        per_day[r["day"]] = round((r["s"] or 0) / 60, 1)
    subj_secs = {}
    for r in c.execute("SELECT subject, SUM(seconds) s FROM activity_log WHERE day>=? GROUP BY subject", (days14[0],)):
        subj_secs[r["subject"] or "其他"] = round((r["s"] or 0) / 60, 1)

    mastery = []
    for r in c.execute(
        "SELECT subject, SUM(status='已掌握') m, COUNT(*) n FROM knowledge_points"
        " WHERE id NOT IN ('eng_vocab','chn_dictation') GROUP BY subject ORDER BY subject"):
        mastery.append({"subject": r["subject"], "mastered": r["m"] or 0, "total": r["n"],
                        "pct": round((r["m"] or 0) * 100 / max(1, r["n"]))})
    weak = [{"subject": r["subject"], "name": r["name"], "status": r["status"],
             "mastery": round((r["mastery"] or 0) * 100)}
            for r in c.execute(
        "SELECT subject, name, status, mastery FROM knowledge_points"
        " WHERE status NOT IN ('已掌握','未解锁') AND id NOT IN ('eng_vocab','chn_dictation')"
        " ORDER BY subject, mastery LIMIT 40")]
    attrs = {r["attribution"]: r["n"] for r in c.execute(
        "SELECT attribution, COUNT(*) n FROM wrong_questions WHERE resolved=0"
        " GROUP BY attribution ORDER BY n DESC")}
    acc_day = {r["d"][5:]: round((r["ok"] or 0) * 100 / max(1, r["n"]))
               for r in c.execute(
        "SELECT date(done_at) d, COUNT(*) n, SUM(correct) ok FROM attempts"
        " WHERE done_at>=date('now','-13 days') GROUP BY d ORDER BY d")}
    total_ok = c.execute("SELECT SUM(correct) FROM attempts").fetchone()[0] or 0
    total_n = c.execute("SELECT COUNT(*) FROM attempts").fetchone()[0] or 0

    tree = queue.lesson_tree(c)
    prog_m = sum(t["mastered"] for t in tree)
    prog_n = sum(t["total"] for t in tree)
    xp14 = (db.get_setting(c, "xp_log", {}) or {})
    return {"time": {"today_min": round(secs_since(today_s) / 60),
                     "week_min": round(secs_since(week_start) / 60),
                     "total_min": round(secs_since(None) / 60),
                     "per_day": {d[5:]: per_day.get(d, 0) for d in days14},
                     "per_subject": subj_secs},
            "mastery": {"by_subject": mastery, "weak": weak},
            "wrong": {"attributions": attrs, "open_count": sum(attrs.values())},
            "accuracy": {"per_day": acc_day, "total_n": total_n,
                         "total_ok": total_ok,
                         "total_pct": round(total_ok * 100 / max(1, total_n))},
            "progress": {"mastered": prog_m, "total": prog_n, "tree": tree},
            "xp14": {d[5:]: xp14.get(d, 0) for d in days14}}


@app.post("/api/ai_advice")
async def api_ai_advice(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    try:
        summary = study_advisor.build_summary(c)
        advice = study_advisor.get_advice(summary)
        return {"advice": advice}
    except Exception as e:
        return JSONResponse({"error": "AI建议生成失败：%s" % str(e)[:200]}, status_code=500)


# ----------------------------------------------------------------------
# 真题模考：选卷 → 限时作答 → 交卷判分 → 归因进错题本
# ----------------------------------------------------------------------
@app.get("/api/exam/packs")
async def api_exam_packs(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    from core import exam_bank
    packs = exam_bank.stats(c)
    for p in packs:
        p["duration"] = EXAM_DURATION.get(p["subject"], 75)
        p["label"] = "%d·%s" % (p["year"], p["paper"])
        # verified=0 表示还没跟原始卷子逐字核对过，前端要显式标注，
        # 免得把待校对的题当成标准答案背。
        p["verified_n"] = int(p.get("n_verified") or 0)
        p["warn"] = "" if p.get("all_verified") else "待核对"
    return {"packs": packs}


@app.get("/api/exam/records")
async def api_exam_records(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    rows = c.execute(
        "SELECT id, taken_at, kind, subject, score, full_mark, duration_min, raw_score "
        "FROM exam_records ORDER BY id DESC LIMIT 30").fetchall()
    return {"items": [dict(r) for r in rows]}


@app.post("/api/exam/start")
async def api_exam_start(req: Request):
    """开考：返回题目（隐藏答案与解析，交卷后统一给出）。"""
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    subj, year, paper = body.get("subject"), body.get("year"), body.get("paper")
    if not (subj and year and paper):
        return JSONResponse({"error": "缺少 subject/year/paper"}, status_code=400)
    rows = c.execute(
        "SELECT * FROM questions WHERE source_type='真题' AND subject=? AND year=? AND paper=? "
        "ORDER BY CASE qtype WHEN '选择题' THEN 0 WHEN '填空题' THEN 1 ELSE 2 END, question_no, id",
        (subj, int(year), paper)).fetchall()
    if not rows:
        return JSONResponse({"error": "这套卷子还没有题目"}, status_code=404)
    qs = [{
        "qid": r["id"], "qtype": r["qtype"], "stem": r["stem"],
        "options": db.decode_options(r), "question_no": r["question_no"],
        "difficulty": r["difficulty"], "kp_id": r["kp_id"],
        "has_points": bool(r["points"]), "verified": int(r["verified"] or 0),
        "source_ref": r["source_ref"] or "",
    } for r in rows]
    return {"subject": subj, "year": int(year), "paper": paper,
            "duration": EXAM_DURATION.get(subj, 75), "questions": qs}


@app.post("/api/exam/submit")
async def api_exam_submit(req: Request):
    """交卷：选择/填空自动判，解答题按自评（0 / 0.5 / 1）给分。

    得分 = 各题得分 / 题数 × 100（卷内分值权重暂未建模，先按题数等比）。
    """
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    qids = body.get("qids") or []
    answers = body.get("answers") or {}
    selfscore = body.get("self") or {}
    seconds = int(body.get("seconds", 0) or 0)
    subj = body.get("subject") or ""
    if not qids:
        return JSONResponse({"error": "没有题目"}, status_code=400)

    details, got, total = [], 0.0, 0
    for qid in qids:
        qid = int(qid)
        r = c.execute("SELECT * FROM questions WHERE id=?", (qid,)).fetchone()
        if not r:
            continue
        total += 1
        val = str(answers.get(str(qid), answers.get(qid, "")) or "")
        if r["qtype"] == "选择题":
            ok = queue.grade_choice(val, r["answer"])
            score = 1.0 if ok else 0.0
        elif r["qtype"] == "填空题":
            ok = queue.grade_fill(val, r["answer"])
            score = 1.0 if ok else 0.0
        else:
            score = float(selfscore.get(str(qid), selfscore.get(qid, 0)) or 0)
            score = 0.0 if score < 0 else (1.0 if score > 1 else score)
            ok = score >= 0.5
        got += score
        # 归因要在入库那一刻就传进去：错题卡片的标题会带上归因，
        # 事后用 set_wrong_attribution 改只会改错题本，卡片标题还是旧的。
        attr = (body.get("attr") or {}).get(str(qid), "") or "概念不清"
        queue.submit_answer(c, qid, ok, kp_id=r["kp_id"], attribution=attr)
        details.append({
            "qid": qid, "qtype": r["qtype"], "stem": r["stem"],
            "options": db.decode_options(r), "your": val,
        "answer": r["answer"], "analysis": r["analysis"],
        "points": json_points(r["points"]), "score": score,
        "question_no": r["question_no"], "kp_id": r["kp_id"],
        "verified": int(r["verified"] or 0), "source_ref": r["source_ref"] or "",
    })
    if not total:
        return JSONResponse({"error": "题目不存在"}, status_code=400)

    pct = round(got / total * 100, 1)
    full = EXAM_FULL_MARK.get(subj, 100)
    c.execute(
        "INSERT INTO exam_records(kind, subject, score, full_mark, duration_min, raw_score, detail)"
        " VALUES(?,?,?,?,?,?,?)",
        ("单科实测", subj, round(pct / 100 * full, 1), full,
         max(1, round(seconds / 60)), pct,
         "%d/%d 题" % (round(got), total)))
    c.commit()
    queue.add_xp(c, int(got * 5))
    return {"score": pct, "full_mark": full,
            "converted": round(pct / 100 * full, 1),
            "correct": round(got), "total": total, "details": details}


def json_points(raw: str | None) -> list[str]:
    import json as _json
    try:
        v = _json.loads(raw or "[]")
        return v if isinstance(v, list) else []
    except (ValueError, TypeError):
        return []


# ----------------------------------------------------------------------
# 解答题训练：按科目/知识点取主观题，写完对照采分点自评
# ----------------------------------------------------------------------
FREE_TYPES = ("解答题", "实验题", "作文")


@app.get("/api/free_response")
async def api_free_response(req: Request, subject: str = "", kp_id: str = "",
                            n: int = 6, real: int = 0):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    n = max(1, min(20, int(n)))
    sql = "SELECT * FROM questions WHERE qtype IN ('解答题','实验题','作文')"
    args: list = []
    if subject:
        sql += " AND subject=?"; args.append(subject)
    if kp_id:
        sql += " AND kp_id=?"; args.append(kp_id)
    if real:
        sql += " AND source_type='真题'"
    # 优先没做过的，再做正确率低的
    sql += (" ORDER BY (SELECT COUNT(*) FROM attempts a WHERE a.question_id=questions.id),"
            " difficulty DESC, id LIMIT ?")
    args.append(n)
    rows = c.execute(sql, args).fetchall()
    return {"items": [{
        "qid": r["id"], "subject": r["subject"], "kp_id": r["kp_id"],
        "qtype": r["qtype"], "stem": r["stem"], "difficulty": r["difficulty"],
        "source_type": r["source_type"],
        "verified": int(r["verified"] or 0), "source_ref": r["source_ref"] or "",
        "year": r["year"], "paper": r["paper"], "question_no": r["question_no"],
        "answer": r["answer"], "analysis": r["analysis"],
        "points": json_points(r["points"]),
    } for r in rows]}


@app.post("/api/free_response/submit")
async def api_free_submit(req: Request):
    """自评提交：score ∈ {0, 0.5, 1}，答错必须归因（写进错题本与 SRS）。"""
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    qid = int(body.get("qid", 0))
    score = float(body.get("score", 0) or 0)
    score = 0.0 if score < 0 else (1.0 if score > 1 else score)
    attr = body.get("attribution", "") or "表述不规范"
    r = c.execute("SELECT kp_id FROM questions WHERE id=?", (qid,)).fetchone()
    if not r:
        return JSONResponse({"error": "题目不存在"}, status_code=404)
    queue.submit_answer(c, qid, score >= 0.5, kp_id=r["kp_id"], attribution=attr)
    return {"ok": True, "score": score}


# ----------------------------------------------------------------------
# 背诵内容
# ----------------------------------------------------------------------
def _recite_cats():
    """{科目: [[全局cat_id, 分类名, 条目数]]}，cat_id 跨科目唯一"""
    out = {}
    gid = 0
    for subj, cats in recite_lib.RECITE_LIB.items():
        out[subj] = []
        for cname, items in cats.items():
            out[subj].append([gid, cname, len(items)])
            gid += 1
    return out


def _recite_cat_by_id(cid: int):
    gid = 0
    for cats in recite_lib.RECITE_LIB.values():
        for cname, items in cats.items():
            if gid == cid:
                return cname, items
            gid += 1
    return None, []


@app.get("/api/recite_catalog")
async def api_recite_catalog(req: Request):
    c, u = _conn_for(req)
    done = set(db.get_setting(c, "recite_done", []) or []) if c else set()
    out = {}
    gid = 0
    for subj, cats in recite_lib.RECITE_LIB.items():
        out[subj] = []
        for cname, items in cats.items():
            d = sum(1 for it in items if it["id"] in done)
            out[subj].append([gid, cname, len(items), d])
            gid += 1
    return out


@app.get("/api/recite/{cat_id}")
def api_recite(cat_id: int):
    cname, items = _recite_cat_by_id(int(cat_id))
    return {"cat": cname, "items": items or []}


SETTING_KEYS = ["tts_rate", "tts_font", "tts_auto", "tts_voices_multi"]


@app.get("/api/settings")
async def api_settings_get(req: Request):
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    return {k: db.get_setting(c, k, None) for k in SETTING_KEYS}


@app.post("/api/settings")
async def api_settings_post(req: Request):
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    body = await req.json() or {}
    for k in SETTING_KEYS:
        if k in body and body[k] is not None:
            db.set_setting(c, k, body[k])
    return {"ok": True}


@app.get("/api/ai_config")
async def api_ai_config_get(req: Request):
    """返回当前生效的 AI 配置（key 只给是否已设置，不回显明文）。"""
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    cfg = config.load_ai_config()
    return {"ok": True, "base": cfg["base"], "model": cfg["model"],
            "key_set": bool(cfg["key"])}


@app.post("/api/ai_config")
async def api_ai_config_post(req: Request):
    """保存 AI 运行时配置（设置页可改，改完立即生效，无需重启/部署）。
    key 传空字符串表示保留原 key 不覆盖。"""
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    body = await req.json() or {}
    base = str(body.get("base") or "").strip()
    model = str(body.get("model") or "").strip()
    key = str(body.get("key") or "").strip()
    new = config.save_ai_config(base, model, key)
    return {"ok": True, "base": new["base"], "model": new["model"],
            "key_set": bool(new.get("key"))}


@app.get("/api/recite_progress")
async def api_recite_progress(req: Request):
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    return {"done": db.get_setting(c, "recite_done", []) or []}


@app.post("/api/recite_done")
async def api_recite_done(req: Request):
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    body = await req.json() or {}
    item_id = str(body.get("item_id", ""))
    done = bool(body.get("done"))
    if not item_id:
        return {"ok": False}
    arr = db.get_setting(c, "recite_done", []) or []
    arr = [x for x in arr if x != item_id]
    if done:
        arr.append(item_id)
    db.set_setting(c, "recite_done", arr)
    return {"ok": True}


# ----------------------------------------------------------------------
# 时长埋点：前端在切页/关闭时上报停留秒数（上限 5 分钟）
# ----------------------------------------------------------------------
@app.post("/api/activity")
async def api_activity(req: Request):
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    body = await req.json() or {}
    db.add_activity(c, date.today().isoformat(),
                    page=body.get("page", "浏览"),
                    subject=body.get("subject", ""),
                    kp_id=body.get("kp_id", ""),
                    seconds=int(body.get("seconds", 0)),
                    hour=time.localtime().tm_hour)
    return {"ok": True}


# ----------------------------------------------------------------------
# PDF 导出
# ----------------------------------------------------------------------
def _export(req: Request, fn):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    try:
        path = fn(c)
        if not path or not os.path.exists(path):
            return JSONResponse({"error": "生成失败"}, status_code=500)
        return FileResponse(path, filename=os.path.basename(path),
                            media_type="application/pdf")
    except Exception as e:
        return JSONResponse({"error": "生成失败：%s" % str(e)[:200]}, status_code=500)


@app.get("/api/export/daily")
async def api_export_daily(req: Request, days: int = 30):
    from core import daily, pdf
    days = max(7, min(90, days))
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    try:
        plans = daily.build_daily_plan(c, date.today(), days=days)
        if not plans:
            return JSONResponse({"error": "没有待学内容（都已掌握？）"}, status_code=400)
        path = pdf.build_daily_plan_pdf(c, plans, start=date.today())
        return FileResponse(path, filename=os.path.basename(path),
                            media_type="application/pdf")
    except Exception as e:
        return JSONResponse({"error": "生成失败：%s" % str(e)[:200]}, status_code=500)


@app.get("/api/export/review")
async def api_export_review(req: Request):
    from core import pdf
    return _export(req, pdf.build_review_book_pdf)


@app.get("/api/export/dictation")
async def api_export_dictation(req: Request):
    from core import pdf
    return _export(req, pdf.build_dictation_pdf)


# ----------------------------------------------------------------------
# 📖 空间（成长记录）：签到 / 随手记 / 体重 / 用户设置 / AI整理 / 隐秘空间
# ----------------------------------------------------------------------
from core import diary as diary_mod

PHOTO_DIR = os.path.join(BASE, "data", "photos")
os.makedirs(PHOTO_DIR, exist_ok=True)
app.mount("/photos", StaticFiles(directory=PHOTO_DIR), name="photos")

# 隐秘空间解锁会话（单进程内存，30 分钟；重启后重新解锁一次即可）
PRIVATE_SESSIONS = {}
PRIVATE_TTL = 30 * 60


def _priv_key(uid: str):
    s = PRIVATE_SESSIONS.get(uid)
    if s and s["exp"] > time.time():
        return s["key"]
    return None


@app.get("/api/profile")
async def api_profile(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    return diary_mod.get_profile(c, u["id"])


@app.post("/api/profile/save")
async def api_profile_save(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    return diary_mod.save_profile(c, u["id"],
                                  nickname=body.get("nickname", ""),
                                  birthday=body.get("birthday", ""),
                                  cover_path=body.get("cover", ""))


@app.post("/api/profile/avatar")
async def api_profile_avatar(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    try:
        p = diary_mod.set_avatar(c, u["id"], body.get("data", ""))
        return {"ok": True, "avatar": p}
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)


@app.post("/api/profile/cover")
async def api_profile_cover(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    try:
        p = diary_mod.set_cover(c, u["id"], body.get("data", ""))
        return {"ok": True, "cover": p}
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)


@app.post("/api/diary/save")
async def api_diary_save(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    try:
        date = body["date"]
        kind = body.get("kind", "note")
        is_private = 1 if body.get("is_private") else 0
        key = _priv_key(u["id"]) if is_private else None
        if is_private and key is None:
            return JSONResponse({"error": "隐秘内容需先解锁高级密码"}, status_code=403)
        photos = []
        for ph in (body.get("photos") or [])[:6]:
            if isinstance(ph, str) and ph.startswith("data:image/"):
                kind_dir = "private" if is_private else ("selfie" if kind == "sign" else "note")
                photos.append(diary_mod.save_photo(u["id"], kind_dir, date, ph))
        diary_mod.save_diary(c, u["id"], date, kind,
                             mood=body.get("mood", ""),
                             text=body.get("text", ""),
                             photos=photos,
                             category=body.get("category", ""),
                             summary=body.get("summary", ""),
                             advice=body.get("advice", ""),
                             is_late=1 if body.get("is_late") else 0,
                             is_private=is_private, key=key)
        return {"ok": True}
    except KeyError:
        return JSONResponse({"error": "缺少 date"}, status_code=400)
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)


@app.post("/api/diary/ai_organize")
async def api_diary_organize(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    text = (body.get("text") or "").strip()
    if not text:
        return JSONResponse({"error": "内容为空"}, status_code=400)
    if len(text) > 1500:
        return JSONResponse({"error": "内容过长（限1500字）"}, status_code=400)
    try:
        return diary_mod.organize(text)
    except Exception as e:
        return JSONResponse({"error": "AI整理失败：%s" % str(e)[:120]}, status_code=502)


@app.get("/api/diary/month")
async def api_diary_month(req: Request, ym: str = ""):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    try:
        return diary_mod.get_month(c, u["id"], ym or date.today().strftime("%Y-%m"))
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)


@app.get("/api/diary/day")
async def api_diary_day(req: Request, date: str = ""):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    try:
        return diary_mod.get_day(c, u["id"], date or date.today().isoformat(),
                                 key=_priv_key(u["id"]))
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)


@app.get("/api/diary/list")
async def api_diary_list(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    return {"items": diary_mod.list_all(c, u["id"], key=_priv_key(u["id"]))}


@app.post("/api/diary/delete")
async def api_diary_delete(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    return {"ok": bool(diary_mod.delete_diary(c, u["id"], int(body.get("id", 0))))}


@app.post("/api/weight/save")
async def api_weight_save(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    try:
        diary_mod.save_weight(c, u["id"], body["date"], float(body.get("value", 0)),
                              note=body.get("note", ""))
        return {"ok": True}
    except (KeyError, ValueError) as e:
        return JSONResponse({"error": str(e)}, status_code=400)


@app.get("/api/weight/list")
async def api_weight_list(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    return {"items": diary_mod.get_weights(c, u["id"])}


@app.post("/api/weight/delete")
async def api_weight_delete(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    diary_mod.delete_weight(c, u["id"], body.get("date", ""))
    return {"ok": True}


# ---- 隐秘空间 ----
@app.get("/api/diary/private/status")
async def api_private_status(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    st = diary_mod.get_private_status(c, u["id"])
    return {"enabled": st["enabled"], "unlocked": _priv_key(u["id"]) is not None}


@app.post("/api/diary/private/config")
async def api_private_config(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    try:
        diary_mod.set_private_pwd(c, u["id"], body.get("new_pwd", ""),
                                  old_pwd=body.get("old_pwd", ""))
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)
    PRIVATE_SESSIONS.pop(u["id"], None)  # 改密后旧解锁立即失效
    return {"ok": True}


@app.post("/api/diary/private/unlock")
async def api_private_unlock(req: Request):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    body = await req.json() or {}
    try:
        key = diary_mod.verify_private_pwd(c, u["id"], body.get("pwd", ""))
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=403)
    PRIVATE_SESSIONS[u["id"]] = {"key": key, "exp": time.time() + PRIVATE_TTL}
    return {"ok": True}


@app.post("/api/diary/private/lock")
async def api_private_lock(req: Request):
    c, u = _conn_for(req)
    if not c:
        return {"ok": False}
    PRIVATE_SESSIONS.pop(u["id"], None)
    return {"ok": True}


@app.get("/api/diary/private/photo")
async def api_private_photo(req: Request, p: str = ""):
    c, u = _conn_for(req)
    if not c:
        return JSONResponse({"error": "未登录"}, status_code=401)
    if _priv_key(u["id"]) is None:
        return JSONResponse({"error": "需要解锁"}, status_code=403)
    try:
        full = diary_mod.photo_abs_path(p)
    except ValueError:
        return JSONResponse({"error": "非法路径"}, status_code=400)
    if not os.path.isfile(full):
        return JSONResponse({"error": "文件不存在"}, status_code=404)
    return FileResponse(full)


if __name__ == "__main__":
    import uvicorn
    print("高考复习服务启动：http://127.0.0.1:8577")
    uvicorn.run(app, host="0.0.0.0", port=8577, log_level="warning")
