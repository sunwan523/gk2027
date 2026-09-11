# -*- coding: utf-8 -*-
"""间隔重复引擎 + 六类归因调度。

对应重构方案 2.2 / 4.3 / 5.2 / 5.5 节。

这是软件唯一无法被教辅书替代的功能：教辅能给你题，但不能告诉你
"你的失分 40% 来自计算失误，所以别再刷难题了"。

归因六类里只有"方法未掌握"能靠多刷题解决，其余五类需要完全不同的干预：

    概念不清     -> 回依赖图重学该节点，暂停刷题
    方法未掌握   -> C 类专项包加量（唯一靠刷题有效的）
    计算失误     -> 限时计算训练，不需要重学
    审题偏差     -> 圈画关键词训练
    时间不够     -> 取舍策略训练，与知识无关
    表述不规范   -> F 类表述规范包（赋分科目高发，A 级杀手）
"""
from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta
from typing import Any, Iterable, Sequence

from core import db

# ----------------------------------------------------------------------
# SM-2 变体间隔（方案 5.2：1 / 3 / 7 / 15 / 30 天，连续 3 次做对才出库）
# ----------------------------------------------------------------------
STEPS = [1.0, 3.0, 7.0, 15.0, 30.0]
GRADUATE_STREAK = 3        # 连续做对 3 次才出库
MAX_EASE = 3.0
MIN_EASE = 1.3


def _fmt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def _parse(s: str) -> datetime:
    for f in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, f)
        except (ValueError, TypeError):
            continue
    return datetime.now()


# ----------------------------------------------------------------------
# 卡片
# ----------------------------------------------------------------------
def add_card(
    conn: sqlite3.Connection,
    kind: str,
    subject: str,
    front: str,
    back: str = "",
    kp_id: str | None = None,
    question_id: int | None = None,
    image_path: str | None = None,
    due_at: datetime | None = None,
) -> int:
    front = front.strip()
    if not front:
        raise ValueError("卡片正面不能为空")
    row = conn.execute("SELECT id, retired FROM cards WHERE kind=? AND front=?", (kind, front)).fetchone()
    if row:
        if row["retired"]:
            conn.execute("UPDATE cards SET retired=0, due_at=? WHERE id=?",
                         (_fmt(due_at or datetime.now()), row["id"]))
            conn.commit()
        return int(row["id"])
    cur = conn.execute(
        "INSERT INTO cards(kind, subject, kp_id, question_id, front, back, image_path, due_at)"
        " VALUES(?,?,?,?,?,?,?,?)",
        (kind, subject, kp_id, question_id, front, back.strip(), image_path,
         _fmt(due_at or datetime.now())))
    conn.commit()
    return int(cur.lastrowid)


def card_from_wrong_question(conn: sqlite3.Connection, question_id: int, attribution: str) -> int:
    """错题自动生成一张卡片，正面是题干，背面是答案+解析+归因。"""
    q = conn.execute("SELECT * FROM questions WHERE id=?", (question_id,)).fetchone()
    if not q:
        raise ValueError("题目不存在：%d" % question_id)
    front = "【%s】%s" % (attribution, q["stem"])
    back = "答案：%s\n解析：%s" % (q["answer"], q["analysis"] or "（无解析）")
    return add_card(conn, "错题", q["subject"], front, back,
                    kp_id=q["kp_id"], question_id=question_id)


def due_cards(conn: sqlite3.Connection, subject: str | None = None,
              kinds: Sequence[str] | None = None, limit: int = 60,
              now: datetime | None = None) -> list[sqlite3.Row]:
    """今天该复习什么——按到期时间与逾期时长排序。

    注意：due_at 用 localtime 存储（与 DB 默认值一致），比较必须用
    本地时间；datetime.utcnow() 在东八区会少 8 小时导致永远查不到。
    """
    now = now or datetime.now()
    if limit is None:
        limit = 60
    sql = "SELECT * FROM cards WHERE retired=0 AND due_at <= ?"
    args: list[Any] = [_fmt(now)]
    if subject:
        sql += " AND subject=?"
        args.append(subject)
    if kinds:
        sql += " AND kind IN (%s)" % ",".join("?" * len(kinds))
        args += list(kinds)
    sql += " ORDER BY due_at ASC, lapses DESC LIMIT %d" % int(limit)
    return conn.execute(sql, args).fetchall()


def review_card(conn: sqlite3.Connection, card_id: int, correct: bool,
                now: datetime | None = None) -> dict[str, Any]:
    """一次复习。答对拉长间隔，答错重置并加大难度系数惩罚。"""
    now = now or datetime.now()
    row = conn.execute("SELECT * FROM cards WHERE id=?", (card_id,)).fetchone()
    if not row:
        raise ValueError("卡片不存在：%d" % card_id)

    reps = row["reps"] + 1
    ease = row["ease"]
    lapses = row["lapses"]
    streak = row["streak"]

    if correct:
        streak += 1
        ease = min(MAX_EASE, ease + 0.1)
        if reps <= len(STEPS):
            interval = STEPS[min(reps - 1, len(STEPS) - 1)]
        else:
            interval = STEPS[-1] * (ease ** (reps - len(STEPS)))
        interval = min(interval, 180.0)
        retired = 1 if streak >= GRADUATE_STREAK and reps >= len(STEPS) else 0
    else:
        streak = 0
        lapses += 1
        ease = max(MIN_EASE, ease - 0.25)
        interval = STEPS[0]
        retired = 0

    due = now + timedelta(days=interval)
    conn.execute(
        "UPDATE cards SET reps=?, ease=?, lapses=?, streak=?, interval_days=?, due_at=?, retired=?"
        " WHERE id=?",
        (reps, round(ease, 3), lapses, streak, round(interval, 2), _fmt(due), retired, card_id))

    if row["question_id"] is not None:
        db.record_attempt(conn, row["question_id"], correct)
    conn.commit()
    return {"interval": interval, "due": _fmt(due), "retired": bool(retired),
            "streak": streak, "ease": round(ease, 3)}


def card_stats(conn: sqlite3.Connection) -> dict[str, int]:
    def one(sql: str, *a: Any) -> int:
        r = conn.execute(sql, a).fetchone()
        return int(r[0]) if r and r[0] is not None else 0
    return {
        "卡片总数": one("SELECT COUNT(*) FROM cards"),
        "今日到期": one("SELECT COUNT(*) FROM cards WHERE retired=0 AND due_at <= datetime('now','localtime')"),
        "未到期": one("SELECT COUNT(*) FROM cards WHERE retired=0 AND due_at > datetime('now','localtime')"),
        "已出库": one("SELECT COUNT(*) FROM cards WHERE retired=1"),
        "错题卡": one("SELECT COUNT(*) FROM cards WHERE kind='错题' AND retired=0"),
    }


# ----------------------------------------------------------------------
# 归因 -> 干预措施映射（方案 5.5）
# ----------------------------------------------------------------------
INTERVENTIONS = {
    "概念不清": {
        "action": "回依赖图重学该节点，暂停刷题",
        "pack": None,
        "why": "不知道该用哪个原理，刷题无效——刷再多也不会突然懂",
        "urgent": 2,
    },
    "方法未掌握": {
        "action": "C 类专项包加量：同类题 10—15 道",
        "pack": "C",
        "why": "知道原理但不会用，这是唯一能靠刷题解决的一类",
        "urgent": 1,
    },
    "计算失误": {
        "action": "限时计算训练（不是难题）",
        "pack": "CALC",
        "why": "思路对、算错了，重学知识是浪费时间，需要的是准确度和速度",
        "urgent": 1,
    },
    "审题偏差": {
        "action": "圈画关键词训练",
        "pack": "READ",
        "why": "看漏条件或理解错题意，需要习惯训练而非知识补充",
        "urgent": 1,
    },
    "时间不够": {
        "action": "取舍策略训练，停止加难度",
        "pack": "TIME",
        "why": "会做但没做完，与知识无关。云南选考 75 分钟 100 分，每分 45 秒",
        "urgent": 2,
    },
    "表述不规范": {
        "action": "F 类表述规范包：对照教材原文改写",
        "pack": "F",
        "why": "赋分科目按点给分，一道 8 分简答丢 2 分就足以挤出 A 级",
        "urgent": 2,
    },
}


def diagnose(conn: sqlite3.Connection, subject: str | None = None) -> dict[str, Any]:
    """按归因分布给出下一步该练什么的结论。"""
    rows = db.attribution_distribution(conn, subject)
    total = sum(r["n"] for r in rows) or 0
    dist = []
    for r in rows:
        pct = (r["n"] / total * 100) if total else 0.0
        item = dict(r)
        item["percent"] = round(pct, 1)
        item.update(INTERVENTIONS.get(r["attribution"], {}))
        dist.append(item)

    verdict = ""
    top = dist[0] if dist else None
    if top:
        if top["attribution"] == "概念不清" and top["percent"] >= 30:
            verdict = ("停止刷题。%d%% 的错题源于概念不清，说明存在知识断层，"
                       "回依赖图重学对应节点比继续刷题有效得多。" % top["percent"])
        elif top["attribution"] == "时间不够" and top["percent"] >= 25:
            verdict = ("主要失分是时间不够，不是不会做。停止加难度，"
                       "转做取舍策略训练——云南选考 75 分钟 100 分，练的是分配不是深度。")
        elif top["attribution"] == "计算失误" and top["percent"] >= 25:
            verdict = ("主要失分是计算失误。不要刷新题，每天 10 道纯计算限时训练更有效，"
                       "化学 A 级要求卷面 92 分，计算准确度是门槛。")
        elif top["attribution"] == "表述不规范" and top["percent"] >= 20:
            verdict = ("主要失分是表述不规范。这是赋分科目的 A 级杀手，"
                       "增加 F 类表述规范包，对照教材原文逐句改写。")
        elif top["attribution"] == "方法未掌握":
            verdict = ("主要失分是方法未掌握——这是唯一能靠刷题解决的一类，"
                       "C 类专项包加量，同类题每次 10—15 道。")
        else:
            verdict = "错题归因分布较均衡，按 C 类专项包正常推进。"
    else:
        verdict = "暂无未解决错题。"

    return {"total": total, "distribution": dist, "verdict": verdict,
            "by_kind": {r["attribution"]: r["n"] for r in rows}}


# ----------------------------------------------------------------------
# 每日队列
# ----------------------------------------------------------------------
def daily_queue(conn: sqlite3.Connection, now: datetime | None = None) -> dict[str, Any]:
    """每天打开软件第一个界面：今天该复习什么、该练什么。

    碎片时段只推送 A/D 类（记忆 + 错题快速回顾），
    整块时段推送 B/C/E/F 类（需要演算）。见方案 2.2 / 风险 8。
    """
    from core import graph
    now = now or datetime.now()
    cards = due_cards(conn, now=now)
    wrongs = db.open_wrongs(conn)
    available = graph.available_nodes(conn)

    frag = [c for c in cards if c["kind"] in ("默写", "词汇", "公式", "概念")]
    solid_cards = [c for c in cards if c["kind"] not in ("默写", "词汇", "公式", "概念")]

    by_attr: dict[str, int] = {}
    for w in wrongs:
        by_attr[w["attribution"]] = by_attr.get(w["attribution"], 0) + 1

    return {
        "date": now.strftime("%Y-%m-%d"),
        "weekday": "一二三四五六日"[now.weekday()],
        "碎片时段": {
            "A类记忆包": len(frag),
            "D类错题速览": min(len(solid_cards), 15),
            "cards": frag[:30],
        },
        "整块时段": {
            "可学知识点": [
                {"id": r["id"], "name": r["name"], "subject": r["subject"],
                 "tier": r["tier"], "weight": r["weight"], "hours": r["est_hours"]}
                for r in available[:12]
            ],
            "待重做错题": len(solid_cards),
            "cards": solid_cards[:40],
        },
        "错题归因分布": by_attr,
        "card_stats": card_stats(conn),
    }
