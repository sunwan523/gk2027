# -*- coding: utf-8 -*-
"""多邻国式动态学习队列。

与 scheduler.py（预排 90 天日历、打印用）是两套并行机制：
  - scheduler：一次性把知识点铺到日历上，输出 PDF 总表（可选导出，不再是主入口）；
  - queue（本模块）：手机每天打开时实时算出"现在能学什么"，做完记录、
    没做完的自然滚到明天，有空可以多做——状态驱动，没有固定日期。

核心思想：学习进度完全由数据库状态决定，不预排日历。
  知识点 status ∈ {未解锁, 可学, 学习中, 需复习, 已掌握}；
  前置全部达标才解锁（graph.refresh_unlock）；
  答完自检题 → record_attempt → update_mastery → 自动解锁后继。
  "少学的后面学"＝没做完的节点 status 不变，明天仍在队列里；
  "时间多的多学"＝队列不封顶，愿意就往下刷。

游戏化：XP（每答对一题累计）、每日目标、连胜天数（连续打卡）。
"""
from __future__ import annotations

import json
import sqlite3
from datetime import date, datetime, timedelta
from typing import Any

from config import SUBJECTS
from core import db, graph

DAILY_XP_GOAL = 60          # 每日 XP 目标（约 15—20 题）
XP_PER_CORRECT = 5
XP_PER_LESSON = 20          # 完成一节课（一个知识点全部自检题）额外奖励

# 滚动任务不进入课程队列（词汇/默写每天碎片推进，无固定自检题）
ROLLING_KP = {"eng_vocab", "chn_dictation"}


# ----------------------------------------------------------------------
# XP 与连胜（存 settings 表，JSON）
# ----------------------------------------------------------------------
def _today() -> str:
    return date.today().isoformat()


def xp_on(conn: sqlite3.Connection, day: str) -> int:
    log = db.get_setting(conn, "xp_log", {}) or {}
    return int(log.get(day, 0))


def add_xp(conn: sqlite3.Connection, amount: int, day: str | None = None) -> int:
    day = day or _today()
    log = db.get_setting(conn, "xp_log", {}) or {}
    log[day] = int(log.get(day, 0)) + amount
    db.set_setting(conn, "xp_log", log)
    _touch_streak(conn, day)
    return log[day]


def _touch_streak(conn: sqlite3.Connection, day: str) -> None:
    """当天首次活动更新连胜：昨天有打卡则 +1，否则重置为 1。"""
    s = db.get_setting(conn, "streak", {}) or {}
    last = s.get("last")
    if last == day:
        return
    if last:
        try:
            gap = (date.fromisoformat(day) - date.fromisoformat(last)).days
        except ValueError:
            gap = 99
        s["count"] = (s.get("count", 0) + 1) if gap == 1 else 1
    else:
        s["count"] = 1
    s["last"] = day
    db.set_setting(conn, "streak", s)


def get_streak(conn: sqlite3.Connection) -> int:
    s = db.get_setting(conn, "streak", {}) or {}
    last = s.get("last")
    if not last:
        return 0
    # 断一天即清零（多邻国规则）
    gap = (date.today() - date.fromisoformat(last)).days
    return int(s.get("count", 0)) if gap <= 1 else 0


def today_state(conn: sqlite3.Connection) -> dict[str, Any]:
    day = _today()
    xp = xp_on(conn, day)
    return {
        "date": day,
        "xp_today": xp,
        "xp_goal": DAILY_XP_GOAL,
        "goal_done": xp >= DAILY_XP_GOAL,
        "streak": get_streak(conn),
    }


# ----------------------------------------------------------------------
# 课程队列：已解锁且有自检题的知识点
# ----------------------------------------------------------------------
def _has_quiz(conn: sqlite3.Connection) -> set[str]:
    rows = conn.execute(
        "SELECT DISTINCT kp_id FROM questions WHERE kp_id IS NOT NULL").fetchall()
    return {r["kp_id"] for r in rows}


def _lesson_row(conn: sqlite3.Connection, r: sqlite3.Row) -> dict[str, Any]:
    qs = conn.execute(
        "SELECT id FROM questions WHERE kp_id=? ORDER BY difficulty, id",
        (r["id"],)).fetchall()
    total = len(qs)
    done = conn.execute(
        "SELECT COUNT(DISTINCT q.id) FROM questions q JOIN attempts a ON a.question_id=q.id "
        "WHERE q.kp_id=?", (r["id"],)).fetchone()[0]
    return {
        "kp_id": r["id"], "subject": r["subject"], "tier": r["tier"],
        "name": r["name"], "weight": r["weight"], "status": r["status"],
        "mastery": round((r["mastery"] or 0) * 100),
        "q_total": total, "q_done": done,
        "minutes": max(2, round((r["est_hours"] or 2) * 0.55 * 60 / 5) * 5),
        "finished": r["status"] == "已掌握",
    }


def available_lessons(conn: sqlite3.Connection,
                      subject: str | None = None) -> list[dict[str, Any]]:
    """现在可学的课程（前置已满足、有自检题、未掌握）。

    排序：先"学习中/需复习"（把没做完的接着做完）再"可学"，
    同层内高频考点优先。这样"少学的后面学"天然成立。
    """
    graph.refresh_unlock(conn)
    has = _has_quiz(conn)
    rows = graph.available_nodes(conn, subject=subject)
    lessons = [_lesson_row(conn, r) for r in rows
               if r["id"] in has and r["id"] not in ROLLING_KP]
    order = {"学习中": 0, "需复习": 1, "可学": 2}
    worder = {"高频考点": 0, "常规": 1, "低频": 2}
    lessons.sort(key=lambda x: (order.get(x["status"], 3),
                                worder.get(x["weight"], 1), x["subject"]))
    return lessons


def lesson_tree(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    """全部知识点按科目分组（进度树用），标注课程状态。"""
    has = _has_quiz(conn)
    out = []
    for s in SUBJECTS:
        rows = conn.execute(
            "SELECT * FROM knowledge_points WHERE subject=? "
            "ORDER BY CASE status WHEN '已掌握' THEN 0 WHEN '学习中' THEN 1 "
            "WHEN '需复习' THEN 2 WHEN '可学' THEN 3 ELSE 4 END, tier", (s,)).fetchall()
        items = []
        for r in rows:
            if r["id"] in ROLLING_KP:
                continue
            items.append({
                "kp_id": r["id"], "name": r["name"], "status": r["status"],
                "mastery": round((r["mastery"] or 0) * 100),
                "has_quiz": r["id"] in has,
            })
        mastered = sum(1 for i in items if i["status"] == "已掌握")
        out.append({"subject": s, "items": items,
                    "mastered": mastered, "total": len(items)})
    return out


# ----------------------------------------------------------------------
# 答题：取题 / 判分 / 提交
# ----------------------------------------------------------------------
def _letter_of(opt: str) -> str:
    """从 'A. 2个' 提取选项字母 A。"""
    for i, ch in enumerate(opt):
        if ch in ".、)）:：":
            return opt[:i].strip().upper()
        if i >= 2:
            break
    return opt[:1].upper()


def normalize(text: str) -> str:
    """填空题答案归一化：全角转半角、去空格、统一大小写。"""
    if text is None:
        return ""
    table = {ord(c): ord(c) - 0xFEE0 for c in "ＡＢＣＤＥＦａｂｃｄｅｆ０１２３４５６７８９（）；：，．！？"}
    table[0x3000] = 0x20
    t = str(text).translate(table).strip().lower()
    return "".join(t.split())


def start_lesson(conn: sqlite3.Connection, kp_id: str) -> list[dict[str, Any]]:
    """一节课 = 该知识点全部自检题，按难度升序。"""
    rows = conn.execute(
        "SELECT * FROM questions WHERE kp_id=? ORDER BY difficulty, id",
        (kp_id,)).fetchall()
    out = []
    for q in rows:
        opts = db.decode_options(q)
        out.append({
            "qid": q["id"], "qtype": q["qtype"], "stem": q["stem"],
            "options": opts, "option_letters": [_letter_of(o) for o in opts],
            "answer": q["answer"], "analysis": q["analysis"] or "",
            "difficulty": q["difficulty"],
            "auto_grade": q["qtype"] == "选择题",
        })
    return out


def grade_choice(user_letter: str, answer: str) -> bool:
    """选择题判分：提取正确答案首字母比较。"""
    if not user_letter:
        return False
    a = (answer or "").strip().upper()
    # 答案可能是 'B' / 'AB' / 'B（...）'，取首个字母判定
    for ch in a:
        if ch.isalpha():
            return user_letter.strip().upper() == ch
    return False


def grade_fill(user_text: str, answer: str) -> bool:
    """填空题严格判分：归一化后比较（多答案用；分隔，任一命中即对）。"""
    u = normalize(user_text)
    if not u:
        return False
    for part in str(answer).replace("；", ";").split(";"):
        if normalize(part) and normalize(part) == u:
            return True
    return False


def submit_answer(conn: sqlite3.Connection, qid: int, correct: bool,
                  kp_id: str | None = None, attribution: str | None = None) -> dict[str, Any]:
    """记录一次作答，更新掌握度与解锁，结算 XP。

    答错需归因（六选一）——但若在手机快速练习中未选，默认按"概念不清"
    兜底记录，避免打断心流；正式错题分析仍应在归因页复核。
    """
    if not correct and not attribution:
        attribution = "概念不清"
    db.record_attempt(conn, qid, correct, attribution=attribution)
    if not correct:
        srs_card = _maybe_wrong_card(conn, qid, attribution)
    else:
        srs_card = None

    if kp_id is None:
        r = conn.execute("SELECT kp_id FROM questions WHERE id=?", (qid,)).fetchone()
        kp_id = r["kp_id"] if r else None
    mastery = graph.update_mastery(conn, kp_id) if kp_id else 0.0
    graph.refresh_unlock(conn)

    xp = XP_PER_CORRECT if correct else 0
    if xp:
        add_xp(conn, xp)
    return {"correct": correct, "xp_gained": xp, "mastery": round(mastery * 100),
            "kp_id": kp_id, "wrong_card": srs_card}


def _maybe_wrong_card(conn: sqlite3.Connection, qid: int, attribution: str) -> int | None:
    from core import srs
    try:
        return srs.card_from_wrong_question(conn, qid, attribution)
    except Exception:
        return None


def set_wrong_attribution(conn: sqlite3.Connection, qid: int, attribution: str) -> None:
    """手机快速练习中答错先按默认归因入库，用户可随后修正归因类型。"""
    if attribution not in ("概念不清", "方法未掌握", "计算失误",
                           "审题偏差", "时间不够", "表述不规范"):
        return
    conn.execute("UPDATE wrong_questions SET attribution=? WHERE question_id=?",
                 (attribution, qid))
    # 最近一次该题的错误作答同步改归因
    last = conn.execute(
        "SELECT id FROM attempts WHERE question_id=? AND correct=0 "
        "ORDER BY id DESC LIMIT 1", (qid,)).fetchone()
    if last:
        conn.execute("UPDATE attempts SET attribution=? WHERE id=?",
                     (attribution, last["id"]))
    conn.commit()


def finish_lesson(conn: sqlite3.Connection, kp_id: str, all_correct: bool) -> dict[str, Any]:
    """一节课全部题目作答完毕：奖励通关 XP，返回新解锁课程数。"""
    before = {r["id"] for r in conn.execute(
        "SELECT id FROM knowledge_points WHERE status IN ('可学','学习中','需复习')")}
    bonus = XP_PER_LESSON + (10 if all_correct else 0)
    add_xp(conn, bonus)
    graph.refresh_unlock(conn)
    after = {r["id"] for r in conn.execute(
        "SELECT id FROM knowledge_points WHERE status IN ('可学','学习中','需复习')")}
    return {"bonus": bonus, "newly_unlocked": len(after - before)}


# ----------------------------------------------------------------------
# 复习队列（到期卡片，间隔重复）
# ----------------------------------------------------------------------
def due_reviews(conn: sqlite3.Connection, limit: int = 20) -> list[dict[str, Any]]:
    from core import srs
    cards = srs.due_cards(conn, limit=limit)
    out = []
    for c in cards:
        out.append({
            "card_id": c["id"], "kind": c["kind"], "subject": c["subject"],
            "front": c["front"], "back": c["back"], "question_id": c["question_id"],
            "kp_id": c["kp_id"],
        })
    return out


def review_result(conn: sqlite3.Connection, card_id: int, correct: bool) -> dict[str, Any]:
    from core import srs
    res = srs.review_card(conn, card_id, correct)
    if correct:
        add_xp(conn, XP_PER_CORRECT)
    return res
