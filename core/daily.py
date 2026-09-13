# -*- coding: utf-8 -*-
"""按进度动态生成"每日学习单"（先学后练）。

与 scheduler.plan_round_one（一次性预排 90 天、含行政诊断周）不同：
  - 起点是"当前进度"——已掌握的节点自动排除，只排还没学完的；
  - 每天从各科目已解锁节点里各取，保证"每天每科都有"；
  - 每个条目 = 一个知识点（讲解 + 自检题），先学后练；
  - 输出交给 pdf.build_daily_plan_pdf 生成可打印 PDF。

贪心逻辑：节点前置全部"完成"（当日分钟清零）后才可排入，跨学科依赖天然满足；
学完的科目让出时间，按剩余科目基础配比归一化放大预算。
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from config import SUBJECTS, SENIOR_PASS_MASTERY, JUNIOR_PASS_MASTERY
from core.plan import FOUNDATION_HOURS
from core.scheduler import ROLLING_KP

_WEIGHT_RANK = {"高频考点": 0, "常规": 1, "低频": 2}

# 每日滚动任务：不依赖排程、不占整块预算（碎片时间完成），每天都出现
ROLLING_DAILY = [
    ("英语", "eng_vocab", "英语词汇·每日背记 20 个（碎片时间，利用 App/卡片）", 15),
    ("语文", "chn_dictation", "语文默写·每日滚动 1 篇（早读或睡前）", 10),
]


@dataclass
class DailyItem:
    subject: str
    kp_id: str
    name: str
    tier: str
    weight: str
    minutes: int


@dataclass
class DailyPlan:
    day: int
    d: date
    items: list[DailyItem] = field(default_factory=list)


def _threshold(tier: str) -> float:
    return JUNIOR_PASS_MASTERY if tier == "初中" else SENIOR_PASS_MASTERY


def build_daily_plan(conn: sqlite3.Connection, start: date, days: int = 30,
                     factor: float = 0.55, *, include_mastered: bool = False) -> list[DailyPlan]:
    """从 start 起排 days 天。默认跳过已掌握节点（按当前进度续排）。"""
    rows = conn.execute(
        "SELECT id, subject, tier, name, weight, est_hours, mastery, status "
        "FROM knowledge_points").fetchall()
    nodes = {r["id"]: dict(r) for r in rows}
    edges = conn.execute("SELECT kp_id, requires_id FROM kp_requires").fetchall()
    req = {i: set() for i in nodes}
    children = {i: [] for i in nodes}
    for e in edges:
        if e["kp_id"] in req and e["requires_id"] in nodes:
            req[e["kp_id"]].add(e["requires_id"])
            children[e["requires_id"]].append(e["kp_id"])

    # 已完成集合：已掌握（或达标）视为前置满足，不重排
    done: set[str] = set(ROLLING_KP)
    todo: dict[str, float] = {}
    for i, n in nodes.items():
        if i in ROLLING_KP:
            continue
        mastered = n["status"] == "已掌握" or (n["mastery"] or 0) >= _threshold(n["tier"])
        if mastered and not include_mastered:
            done.add(i)
            continue
        todo[i] = (n["est_hours"] or 2) * factor * 60.0

    # 依赖分级：同科前置=硬阻塞（必须先学完），跨科前置=软偏好（不阻塞，仅排后）。
    # 理由：一轮总复习里"学生物细胞"不必等"化学物质的变化"学完才开，
    # 跨科边只是提示先后，硬卡会让物理/化学/生物第 1 天全被数学链锁死（2026-09-12 修）。
    hard_req: dict[str, set[str]] = {i: set() for i in todo}
    soft_req: dict[str, set[str]] = {i: set() for i in todo}
    for i in todo:
        for r in req[i]:
            if r in todo:  # r 不在 todo（已掌握/滚动）→ 天然满足
                if nodes[r]["subject"] == nodes[i]["subject"]:
                    hard_req[i].add(r)
                else:
                    soft_req[i].add(r)

    base_budget = {s: FOUNDATION_HOURS[s]["整块"] for s in SUBJECTS}
    total_budget = sum(base_budget.values())

    def rank(i: str):
        # 软前置未满足的排后面（同科硬前置已保证在前）
        return (1 if (soft_req[i] - done) else 0,
                _WEIGHT_RANK.get(nodes[i]["weight"], 1),
                0 if nodes[i]["tier"] == "初中" else 1,
                nodes[i]["subject"], nodes[i]["name"])

    def eligible(s: str) -> list[str]:
        return sorted((i for i in todo if nodes[i]["subject"] == s
                       and i not in done and not (hard_req[i] - done)), key=rank)

    def finish(i: str):
        done.add(i)

    plans: list[DailyPlan] = []
    cur: dict[str, str | None] = {s: None for s in SUBJECTS}
    for day in range(1, days + 1):
        dp = DailyPlan(day=day, d=start + timedelta(days=day - 1))
        unfinished = {s for s in SUBJECTS if any(
            i for i in todo if nodes[i]["subject"] == s and i not in done)}
        if not unfinished:
            break
        active = [s for s in SUBJECTS if cur[s] or eligible(s)]
        if not active:
            break
        wsum = sum(base_budget[s] for s in active)
        for s in SUBJECTS:
            if s not in active:
                continue
            left = total_budget * base_budget[s] / wsum * 60.0
            first = True
            while left >= 15:
                i = cur[s]
                if i is None:
                    elig = eligible(s)
                    if not elig:
                        break
                    i = cur[s] = elig[0]
                take = min(left, todo[i])
                if 0 < todo[i] - take < 15 and todo[i] <= left:
                    take = todo[i]
                todo[i] -= take
                left -= take
                finished = todo[i] <= 0.5
                dp.items.append(DailyItem(
                    subject=s, kp_id=i, name=nodes[i]["name"],
                    tier=nodes[i]["tier"], weight=nodes[i]["weight"],
                    minutes=int(round(take))))
                if finished:
                    finish(i)
                    cur[s] = None
                    if first:
                        # 保证"每天每科都有"：首节点当天学完后，
                        # 若已解锁新节点则继续排第二个（依赖已满足才成立）
                        first = False
                        continue
        # 日内补排：当天被解锁但没分到时间的科目，保底 30 分钟
        # （从当日"未学完"的最大条目让渡，不破坏依赖顺序）
        for s in SUBJECTS:
            if s in active or not eligible(s):
                continue
            donors = [it for it in dp.items
                      if it.subject in active and todo[it.kp_id] > 0.5
                      and it.minutes >= 45]
            if not donors:
                continue
            big = max(donors, key=lambda it: it.minutes)
            big.minutes -= 30
            todo[big.kp_id] += 30
            i = eligible(s)[0]
            take = min(30.0, todo[i])
            todo[i] -= take
            dp.items.append(DailyItem(
                subject=s, kp_id=i, name=nodes[i]["name"],
                tier=nodes[i]["tier"], weight=nodes[i]["weight"],
                minutes=int(round(take))))
            if todo[i] <= 0.5:
                finish(i)
                cur[s] = None
        # 每日滚动任务（词汇/默写）：固定出现，不占整块预算
        for subj, kid, nm, mins in ROLLING_DAILY:
            dp.items.append(DailyItem(subject=subj, kp_id=kid, name=nm,
                                      tier="滚动", weight="每日", minutes=mins))
        plans.append(dp)
    return plans
