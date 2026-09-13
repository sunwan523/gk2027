# -*- coding: utf-8 -*-
"""90 天一轮排程器（方案 4.1）。

把依赖图的 152 个知识点铺到日历上：
- 拓扑序保证前置永远排在后面（一轮没有回头路，顺序错了漏洞固化）；
- 每日学时预算按方案 4.1 配比分配，提前学完的科目自动让出时间；
- 唤醒系数：90 天节奏的前提是"唤醒而非新学"（方案 2.1），
  节点有效学时 = est_hours × factor。默认 0.55 恰好压进 80 个排程日
  （第 1—10 天是行政+诊断周，不排知识点）。
  诊断实测后按 2.1 判读表调整：物理≥50 分 factor=0.55；
  35—49 分 --days 110 --factor 0.7；<35 分 --days 140 --factor 1.0。

滚动任务（英语 3500 词、语文 64 篇默写）不占单日槽位，每天碎片时段进行。
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from config import SUBJECTS
from core.plan import FOUNDATION_HOURS

# 每天碎片时段滚动推进、不进入单日排程的节点
ROLLING_KP = {
    "eng_vocab": "每天 50 词滚动（新词+复习），碎片 40min，270 天不断",
    "chn_dictation": "每天 1—2 篇默写滚动，碎片 30min，64 篇零错误",
}

# 方案 4.1：第 1—3 天行政、第 4—10 天诊断，第 11 天起排知识点
DIAGNOSIS_DAYS = 10

# 节点在队列内的优先级：高频考点 > 常规 > 低频；初中层优先（依赖天然在前）
_WEIGHT_RANK = {"高频考点": 0, "常规": 1, "低频": 2}


@dataclass
class DayPlan:
    day: int                     # 备考第几天（从 1 开始）
    d: date
    items: list[dict] = field(default_factory=list)   # {subject,kp_id,name,minutes,tier,weight}
    rolling: list[str] = field(default_factory=list)  # 滚动任务提示
    label: str = ""              # 行政/诊断周标注


def plan_round_one(conn: sqlite3.Connection, start: date, days: int = 90,
                   factor: float = 0.55) -> list[DayPlan]:
    """生成第 1—days 天的排程。第 11 天起铺知识点，预算耗尽即止。

    逐日模拟：节点只有在前置全部"完成"（分钟清零）后才可排入，
    跨学科依赖（如 生物·细胞 ← 化学·物质变化）因此天然满足。
    每日总预算 = sum(FOUNDATION_HOURS[s]['整块']) 小时，
    学完的科目自动让出时间（按剩余科目基础配比归一化）。
    """
    rows = conn.execute(
        "SELECT id, subject, tier, name, weight, est_hours FROM knowledge_points"
    ).fetchall()
    nodes = {r["id"]: dict(r) for r in rows}
    edges = conn.execute("SELECT kp_id, requires_id FROM kp_requires").fetchall()
    req = {i: set() for i in nodes}
    children = {i: [] for i in nodes}
    for e in edges:
        if e["kp_id"] in req and e["requires_id"] in nodes:
            req[e["kp_id"]].add(e["requires_id"])
            children[e["requires_id"]].append(e["kp_id"])

    todo = {i: nodes[i]["est_hours"] * factor * 60.0
            for i in nodes if i not in ROLLING_KP}
    # 滚动节点（词汇/默写）每天推进，其依赖视为已满足，否则英语语法链永远锁死
    left_req = {i: {r for r in req[i] if r not in ROLLING_KP} for i in todo}
    done: set[str] = set(ROLLING_KP)

    base_budget = {s: FOUNDATION_HOURS[s]["整块"] for s in SUBJECTS}
    total_budget = sum(base_budget.values())

    plans: list[DayPlan] = []
    admin = {
        1: "色觉自查（一票否决项）＋ 联系招考办确认报名材料",
        2: "联系户籍地招考办确认往届生报名资格与材料",
        3: "整理教辅与真题卷；熟悉打印流程",
    }
    diag = {
        4: "诊断：2026 云南选考物理真题（限时 75 分钟）",
        5: "诊断：化学真题卷（限时 75 分钟）",
        6: "诊断：生物真题卷（限时 75 分钟）",
        7: "诊断：高一数学必修一卷（限时 120 分钟）",
        8: "诊断：初中数学毕业卷 + 物理错题自查",
        9: "诊断：2026 全国二卷语文（150 分钟）",
        10: "诊断：2026 全国二卷英语（120 分钟）；汇总判读，确定 factor",
    }
    for day in range(1, min(DIAGNOSIS_DAYS, days) + 1):
        plans.append(DayPlan(
            day=day, d=start + timedelta(days=day - 1),
            label=admin.get(day) or diag.get(day) or "",
            rolling=["英语 3500 词每日滚动（碎片 40min，第 1 天起不断）",
                     "语文默写每日 1—2 篇滚动（碎片 30min）"]))

    def rank(i: str):
        return (_WEIGHT_RANK.get(nodes[i]["weight"], 1),
                0 if nodes[i]["tier"] == "初中" else 1,
                nodes[i]["name"])

    # 贪心推进：每天每科从"已解锁且未完成"节点里取排名最前的，
    # 用满本科当日预算（预算随其他科目学完动态放大）。节点天然按
    # 依赖顺序完成——前置分钟清零才解锁后继，跨学科依赖因此满足。
    cur: dict[str, str | None] = {s: None for s in SUBJECTS}

    def eligible(s: str) -> list[str]:
        return sorted((i for i in todo
                       if nodes[i]["subject"] == s and i not in done
                       and not left_req[i]), key=rank)

    def finish(i: str):
        done.add(i)
        for c in children[i]:
            left_req.get(c, set()).discard(i)

    for day in range(DIAGNOSIS_DAYS + 1, days + 1):
        d = start + timedelta(days=day - 1)
        dp = DayPlan(day=day, d=d)
        unfinished = {s for s in SUBJECTS
                      if any(i for i in todo
                             if nodes[i]["subject"] == s and i not in done)}
        if not unfinished:
            dp.label = "一轮知识点已全部排完——转入错题清零与章节测试"
            dp.rolling = list(ROLLING_KP.values())
            plans.append(dp)
            continue
        # 只有"今天能推进"的科目参与预算分配；被依赖锁死的科目预算
        # 自动流向其他科目（否则锁定期内整块时间白白蒸发）。
        active = [s for s in unfinished if cur[s] or eligible(s)]
        if not active:
            dp.label = "⚠ 剩余节点全部被依赖锁死，请检查依赖图"
            dp.rolling = list(ROLLING_KP.values())
            plans.append(dp)
            continue
        wsum = sum(base_budget[s] for s in active)

        for s in SUBJECTS:
            if s not in active:
                continue
            left = total_budget * base_budget[s] / wsum * 60.0   # 本科当日分钟预算
            while left >= 15:
                i = cur[s]
                if i is None:
                    elig = eligible(s)
                    if not elig:
                        break
                    i = cur[s] = elig[0]
                take = min(left, todo[i])
                # 避免 1—5 分钟的无意义小尾巴：若剩余量装得进当日预算就一次做完
                if 0 < todo[i] - take < 15 and todo[i] <= left:
                    take = todo[i]
                todo[i] -= take
                left -= take
                finished = todo[i] <= 0.5
                if finished:
                    finish(i)
                    cur[s] = None
                dp.items.append({
                    "subject": s, "kp_id": i, "name": nodes[i]["name"],
                    "tier": nodes[i]["tier"], "weight": nodes[i]["weight"],
                    "minutes": int(round(take)), "split": not finished,
                    "cont": False})
        dp.rolling = list(ROLLING_KP.values())
        plans.append(dp)

    unscheduled = [i for i in todo if i not in done]
    if unscheduled:
        print("⚠ %d 个节点在 %d 天内排不下（factor=%.2f 太乐观）：%s" % (
            len(unscheduled), days, factor,
            "、".join(nodes[i]["name"] for i in unscheduled[:10])))
    return plans


def save_plan(conn: sqlite3.Connection, plans: list[DayPlan], *,
              start: date, days: int, factor: float) -> None:
    """排程落库（幂等：整表重建）。"""
    conn.execute("DROP TABLE IF EXISTS round_plan")
    conn.execute("""
        CREATE TABLE round_plan (
            day        INTEGER NOT NULL,
            d          TEXT    NOT NULL,
            subject    TEXT,
            kp_id      TEXT,
            name       TEXT,
            tier       TEXT,
            weight     TEXT,
            minutes    INTEGER,
            split      INTEGER NOT NULL DEFAULT 0,
            label      TEXT,
            PRIMARY KEY (day, subject, kp_id)
        )""")
    for p in plans:
        if not p.items:
            conn.execute(
                "INSERT OR REPLACE INTO round_plan(day,d,subject,kp_id,name,minutes,label)"
                " VALUES(?,?,?,?,?,?,?)",
                (p.day, p.d.isoformat(), None, None, None, 0, p.label))
        for it in p.items:
            conn.execute(
                "INSERT OR REPLACE INTO round_plan(day,d,subject,kp_id,name,tier,weight,minutes,split)"
                " VALUES(?,?,?,?,?,?,?,?,?)",
                (p.day, p.d.isoformat(), it["subject"], it["kp_id"], it["name"],
                 it["tier"], it["weight"], it["minutes"], 1 if it["split"] else 0))
    conn.execute(
        "INSERT INTO settings(key,value) VALUES('round_plan_meta',?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        ('{"start":"%s","days":%d,"factor":%s}' % (start.isoformat(), days, factor),))
    conn.commit()


def load_plan(conn: sqlite3.Connection) -> tuple[dict[str, Any], list[DayPlan]] | None:
    row = conn.execute("SELECT value FROM settings WHERE key='round_plan_meta'").fetchone()
    if not row:
        return None
    import json
    meta = json.loads(row["value"])
    rows = conn.execute(
        "SELECT * FROM round_plan ORDER BY day, "
        "CASE subject WHEN '数学' THEN 0 WHEN '化学' THEN 1 WHEN '物理' THEN 2 "
        "WHEN '生物' THEN 3 WHEN '英语' THEN 4 WHEN '语文' THEN 5 ELSE 6 END").fetchall()
    plans: dict[int, DayPlan] = {}
    for r in rows:
        p = plans.setdefault(r["day"], DayPlan(
            day=r["day"], d=date.fromisoformat(r["d"]), label=r["label"] or ""))
        if r["kp_id"]:
            p.items.append({"subject": r["subject"], "kp_id": r["kp_id"],
                            "name": r["name"], "tier": r["tier"],
                            "weight": r["weight"], "minutes": r["minutes"],
                            "split": bool(r["split"]), "cont": False})
        p.rolling = list(ROLLING_KP.values())
    return meta, [plans[k] for k in sorted(plans)]
