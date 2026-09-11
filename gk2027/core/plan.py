# -*- coding: utf-8 -*-
"""日程引擎：从考试日动态反推。

对应重构方案 4.1 / 4.2 / 4.4 节。

旧项目把 start_date 硬编码成 datetime(2026,5,8)，导致计划一夜作废。
本模块所有日期都从 EXAM_DATE 反推，且基础期天数可由诊断测试实测结果覆盖。

90 天基础期能否守住，取决于第 4—10 天诊断测试，不取决于决心：
    物理真题 >=50 分 -> 90 天    35—49 分 -> 110 天    <35 分 -> 140 天
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Any, Sequence

from config import (ADMIN_DEADLINES, EXAM_DATE, FOUNDATION_DAYS_DEFAULT,
                    MILESTONES, SUBJECTS, TARGET_SCORES, today)
from core import db, graph

# ----------------------------------------------------------------------
# 阶段定义（方案 4.1 / 4.2）
# ----------------------------------------------------------------------
PHASES = [
    ("第一阶段·基础重建", "六科完成一轮系统学习，不留结构性空白"),
    ("第二阶段·练习与补漏", "180 天约 1080 小时，全部用于实战化提分"),
]

PRACTICE_DAYS = 180

# 练习期三轮（方案 4.2）
PRACTICE_ROUNDS = [
    ("第一轮·专项突破", 0.39, "按归因数据定位漏洞，按错误率排序攻克，不按章节顺序刷"),
    ("第二轮·套卷训练", 0.33, "每周 3 套限时卷，严格按高考时长；错题清零"),
    ("第三轮·全真模考与守分", 0.28, "每 5 天一次全真模考；考前 7 天停止新知识"),
]

# 第一阶段每日学时分配（方案 4.1 表）
FOUNDATION_HOURS = {
    "数学": {"整块": 2.25, "碎片": 0.0,  "占比": "27%"},
    "化学": {"整块": 1.25, "碎片": 0.25, "占比": "17%"},
    "物理": {"整块": 1.00, "碎片": 0.17, "占比": "15%"},
    "生物": {"整块": 1.00, "碎片": 0.42, "占比": "15%"},
    "英语": {"整块": 0.50, "碎片": 0.67, "占比": "13%"},
    "语文": {"整块": 0.50, "碎片": 0.50, "占比": "13%"},
}

# A 类碎片记忆包的科目轮换（方案 5.2，双 A 目标下化学生物权重提高）
FRAGMENT_ROTATION = {
    0: "化学+语文",   # 周一
    1: "生物+英语",   # 周二
    2: "物理+数学",   # 周三
    3: "化学+语文",   # 周四
    4: "生物+英语",   # 周五
    5: "物理+数学",   # 周六
    6: "综合默写",    # 周日
}


# ----------------------------------------------------------------------
# 诊断 -> 基础期天数（方案 2.1 判读表）
# ----------------------------------------------------------------------
def foundation_days_from_diagnosis(physics_score: float | None) -> tuple[int, str]:
    """按 2026 云南选考物理真题实测分决定基础期长度。"""
    if physics_score is None:
        return FOUNDATION_DAYS_DEFAULT, "尚未诊断，暂用默认 %d 天" % FOUNDATION_DAYS_DEFAULT
    if physics_score >= 50:
        return 90, "物理真题 %d 分 ≥50：通路完好，90 天一轮可执行" % physics_score
    if physics_score >= 35:
        return 110, "物理真题 %d 分（35—49）：通路部分保留，基础期延至 110 天" % physics_score
    return 140, ("物理真题 %d 分 <35：需按新学路径重排，基础期 140 天，"
                 "练习期压缩至 130 天" % physics_score)


def set_foundation_days(conn: sqlite3.Connection, days: int) -> None:
    db.set_setting(conn, "foundation_days", int(days))


def get_foundation_days(conn: sqlite3.Connection) -> int:
    val = db.get_setting(conn, "foundation_days", None)
    return int(val) if val else FOUNDATION_DAYS_DEFAULT


def auto_set_foundation_from_diagnosis(conn: sqlite3.Connection) -> tuple[int, str]:
    """读取已录入的物理诊断成绩，自动设定基础期天数。"""
    row = conn.execute(
        "SELECT score FROM exam_records WHERE kind='诊断' AND subject='物理' "
        "ORDER BY taken_at DESC LIMIT 1").fetchone()
    days, reason = foundation_days_from_diagnosis(row["score"] if row else None)
    if row:
        set_foundation_days(conn, days)
    return days, reason


# ----------------------------------------------------------------------
# 日程计算
# ----------------------------------------------------------------------
@dataclass
class Schedule:
    exam_date: date
    foundation_days: int
    practice_days: int
    start_date: date
    foundation_end: date
    today: date
    day_index: int          # 第几天，从 1 开始
    days_left: int
    phase: str
    phase_day: int
    phase_total: int
    round_name: str = ""
    round_hint: str = ""


def compute_schedule(conn: sqlite3.Connection, on: date | None = None) -> Schedule:
    on = on or today()
    fdays = get_foundation_days(conn)
    total = fdays + PRACTICE_DAYS
    start = EXAM_DATE - timedelta(days=total - 1)
    fend = start + timedelta(days=fdays - 1)
    idx = (on - start).days + 1
    left = (EXAM_DATE - on).days

    if idx <= 0:
        phase, pday, ptot = "尚未开始", 0, total
    elif idx <= fdays:
        phase, pday, ptot = PHASES[0][0], idx, fdays
    elif idx <= total:
        phase, pday, ptot = PHASES[1][0], idx - fdays, PRACTICE_DAYS
    else:
        phase, pday, ptot = "考试期间或已结束", 0, total

    rname = rhint = ""
    if phase == PHASES[1][0] and pday > 0:
        acc = 0.0
        for name, frac, hint in PRACTICE_ROUNDS:
            acc += frac
            if pday <= int(PRACTICE_DAYS * acc):
                rname, rhint = name, hint
                break
        else:
            rname, rhint = PRACTICE_ROUNDS[-1][0], PRACTICE_ROUNDS[-1][2]

    return Schedule(EXAM_DATE, fdays, PRACTICE_DAYS, start, fend, on,
                    idx, left, phase, pday, ptot, rname, rhint)


# ----------------------------------------------------------------------
# 今日任务（方案 2.2：碎片做记忆，整块做理解与演算）
# ----------------------------------------------------------------------
def today_tasks(conn: sqlite3.Connection, on: date | None = None) -> dict[str, Any]:
    from core import srs
    sch = compute_schedule(conn, on)
    # 当天末尾作为"现在"：否则今天晚些时候到期的卡（如 seed 时写入的当前时刻）
    # 会被 due_at <= 00:00 排除，导致今日到期数显示为 0。
    now = datetime.combine(sch.today, datetime.max.time()).replace(microsecond=0)
    queue = srs.daily_queue(conn, now=now)

    rotation = FRAGMENT_ROTATION.get(sch.today.weekday(), "综合默写")
    available = graph.available_nodes(conn)

    solid_hours = sum(v["整块"] for v in FOUNDATION_HOURS.values())
    frag_hours = sum(v["碎片"] for v in FOUNDATION_HOURS.values())

    allocation = []
    if sch.phase == PHASES[0][0]:
        allocation = [
            {"科目": k, "整块学时": v["整块"], "碎片学时": v["碎片"], "周占比": v["占比"]}
            for k, v in FOUNDATION_HOURS.items()
        ]
    else:
        allocation = [
            {"科目": "数学", "整块学时": 2.5, "碎片学时": 0.0, "周占比": "27%"},
            {"科目": "物理", "整块学时": 1.5, "碎片学时": 0.17, "周占比": "18%"},
            {"科目": "化学", "整块学时": 1.25, "碎片学时": 0.25, "周占比": "17%"},
            {"科目": "生物", "整块学时": 1.0, "碎片学时": 0.42, "周占比": "15%"},
            {"科目": "英语", "整块学时": 0.75, "碎片学时": 0.67, "周占比": "12%"},
            {"科目": "语文", "整块学时": 0.5, "碎片学时": 0.5, "周占比": "11%"},
        ]

    return {
        "schedule": sch,
        "碎片记忆轮换": rotation,
        "整块总学时": round(solid_hours, 2),
        "碎片总学时": round(frag_hours, 2),
        "学时分配": allocation,
        "今日队列": queue,
        "可学知识点数": len(available),
        "行政提醒": upcoming_deadlines(sch.today),
        "里程碑": milestone_status(conn, sch),
    }


# ----------------------------------------------------------------------
# 里程碑与行政日期
# ----------------------------------------------------------------------
def upcoming_deadlines(on: date | None = None, window: int = 30) -> list[dict]:
    on = on or today()
    out = []
    for d, text in sorted(ADMIN_DEADLINES):
        delta = (d - on).days
        if -3 <= delta <= window:
            out.append({
                "date": d.isoformat(),
                "days": delta,
                "text": text,
                "state": "已过期" if delta < 0 else ("今天" if delta == 0 else "剩 %d 天" % delta),
            })
    return out


def milestone_status(conn: sqlite3.Connection, sch: Schedule | None = None) -> list[dict]:
    """里程碑状态。

    注意（方案 4.4）：未达标的应对是「换方法」或「加资源」，不是「降目标」。
    上一版设的"降级到傣医学/中药学"机制已删除——那把学习变成随时可撤退的心态。
    """
    sch = sch or compute_schedule(conn)
    out = []
    for m in MILESTONES:
        delta = (m.on_date - sch.today).days
        state = "已过期" if delta < 0 else ("今天" if delta == 0 else "剩 %d 天" % delta)
        actual = None
        if m.targets and "总分" in m.targets:
            r = conn.execute(
                "SELECT SUM(score) AS s FROM exam_records WHERE kind='全真模考' "
                "AND date(taken_at) <= date(?)", (m.on_date.isoformat(),)).fetchone()
            actual = r["s"] if r and r["s"] is not None else None
        out.append({
            "label": m.label, "date": m.on_date.isoformat(), "days": delta,
            "state": state, "targets": m.targets, "actual": actual,
            "remedy": ("未达标 → 定位失分最集中的科目，重排时间配比；"
                       "必要时请家教补该科。不降目标。"
                       if m.targets and actual is not None and
                       any(actual < v for v in m.targets.values()) else ""),
        })
    return out


def target_table(conn: sqlite3.Connection) -> dict[str, Any]:
    """目标分解表（方案 3.4 双 A 版）+ 最近实测对比。"""
    latest: dict[str, float] = {}
    for r in conn.execute(
            "SELECT subject, score FROM exam_records WHERE kind IN ('全真模考','单科实测','诊断') "
            "ORDER BY taken_at DESC"):
        latest.setdefault(r["subject"], r["score"])
    rows = []
    for s in SUBJECTS:
        rows.append({
            "科目": s, "计分": "赋分" if s in ("化学", "生物") else "原始分",
            "目标": TARGET_SCORES[s], "最近实测": latest.get(s),
            "差距": (round(TARGET_SCORES[s] - latest[s], 1) if s in latest else None),
        })
    total_actual = sum(v for k, v in latest.items() if k in SUBJECTS) if latest else None
    return {
        "rows": rows,
        "目标总分": sum(TARGET_SCORES.values()),
        "实测总分": round(total_actual, 1) if latest else None,
        "对外目标": 600, "内部瞄准": 615,
    }


def phase_progress(conn: sqlite3.Connection) -> dict[str, Any]:
    sch = compute_schedule(conn)
    total_nodes = conn.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
    mastered = conn.execute(
        "SELECT COUNT(*) FROM knowledge_points WHERE status='已掌握'").fetchone()[0]
    return {
        "第几天": sch.day_index, "总天数": sch.phase_total and (sch.foundation_days + sch.practice_days),
        "剩余天数": sch.days_left, "阶段": sch.phase, "练习轮次": sch.round_name,
        "知识点已掌握": mastered, "知识点总数": total_nodes,
        "整体进度": round(mastered / total_nodes * 100, 1) if total_nodes else 0.0,
    }
