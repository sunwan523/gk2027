# -*- coding: utf-8 -*-
"""AI学习建议模块：把用户学习统计汇总成结构化摘要，交给 DeepSeek 生成学习建议。

隐私约定：只发送统计汇总（时长、正确率、掌握率、错题归因等聚合数据），
不包含姓名、账号、库路径等任何身份信息；页面展示时标注"AI 建议仅供参考"。
"""
from __future__ import annotations

import json
import re
import sqlite3
import urllib.request
import urllib.error
from datetime import date, timedelta

API_KEY = "sk-b975b7c022ca4815b3c8d75c1d89c3c7"
API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-chat"

SYSTEM_PROMPT = """你是一位高考复习规划老师。用户会给你一份学习统计摘要（JSON），请基于数据给出可执行的学习建议。

要求：
1. 输出四部分，用 Markdown 小标题：## 一、偏科预警 / ## 二、薄弱知识点 / ## 三、时间分配建议 / ## 四、下一步复习重点
2. 偏科预警：根据各科学习时长和掌握率，指出最需要补的科目，说明依据（引用数据）
3. 薄弱知识点：从"未掌握/掌握率低/错题多"的知识点中挑出最重要的3-5个，说明为什么薄弱、怎么补
4. 时间分配建议：结合每日时长和科目差距，给出具体到科目甚至时段的比例建议
5. 下一步复习重点：给出接下来一周可执行的动作（复习哪些、练什么、怎么练）
6. 语气务实、具体，不要空话套话；数据不足的地方如实说明，不要编造
7. 全文用简体中文，控制在600字以内"""


def build_summary(conn: sqlite3.Connection) -> dict:
    """聚合用户学习统计（不含任何身份信息），供 AI 分析。"""
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    today_s = today.isoformat()

    # ---- 时长 ----
    def secs_since(d: str | None) -> int:
        q = "SELECT COALESCE(SUM(seconds),0) FROM activity_log"
        args: list = []
        if d:
            q += " WHERE day>=?"; args.append(d)
        return int(conn.execute(q, args).fetchone()[0])

    total_sec = secs_since(None)
    rows = conn.execute(
        "SELECT day,page,subject,seconds FROM activity_log WHERE day>=? ORDER BY day",
        (week_start,)).fetchall()
    # 各科时长（本周）
    by_subject: dict[str, int] = {}
    by_day: dict[str, int] = {}
    for r in rows:
        sub = r["subject"] or "其他"
        by_subject[sub] = by_subject.get(sub, 0) + (r["seconds"] or 0)
        by_day[r["day"]] = by_day.get(r["day"], 0) + (r["seconds"] or 0)

    # ---- 掌握率 ----
    kp_rows = conn.execute(
        "SELECT subject, status, COUNT(*) n FROM knowledge_points"
        " WHERE id NOT IN ('eng_vocab','chn_dictation')"
        " GROUP BY subject, status").fetchall()
    by_subj_mastery: dict[str, dict] = {}
    for r in kp_rows:
        d = by_subj_mastery.setdefault(r["subject"], {"total": 0, "mastered": 0, "learning": 0, "review": 0})
        d["total"] += r["n"]
        if r["status"] == "已掌握":
            d["mastered"] += r["n"]
        elif r["status"] in ("学习中", "需复习"):
            d["learning"] += r["n"]
    mastery_list = [{
        "subject": s, "total": d["total"], "mastered": d["mastered"],
        "mastery_pct": round(d["mastered"] * 100 / max(1, d["total"])),
    } for s, d in sorted(by_subj_mastery.items())]

    # 未掌握知识点（按科目，每科最多5个）
    weak = conn.execute(
        "SELECT subject, name, status, ROUND(mastery*100) m FROM knowledge_points"
        " WHERE status NOT IN ('已掌握','未解锁') AND id NOT IN ('eng_vocab','chn_dictation')"
        " ORDER BY mastery, subject LIMIT 30").fetchall()
    weak_list = [{"subject": r["subject"], "name": r["name"],
                  "status": r["status"], "mastery": r["m"]} for r in weak]

    # ---- 错题归因（未解决） ----
    attrs = conn.execute(
        "SELECT attribution, COUNT(*) n FROM wrong_questions"
        " WHERE resolved=0 GROUP BY attribution ORDER BY n DESC").fetchall()
    attr_list = [{"attr": r["attribution"], "n": r["n"]} for r in attrs]
    open_wrong = sum(r["n"] for r in attrs)

    # ---- 作答正确率 ----
    att = conn.execute(
        "SELECT date(done_at) d, COUNT(*) n, SUM(correct) ok"
        " FROM attempts WHERE done_at>=date('now','-13 days')"
        " GROUP BY d ORDER BY d").fetchall()
    acc_list = [{"day": r["d"], "n": r["n"],
                 "correct_pct": round((r["ok"] or 0) * 100 / max(1, r["n"]))} for r in att]
    total_att = conn.execute("SELECT COUNT(*) FROM attempts").fetchone()[0]
    total_ok = conn.execute("SELECT SUM(correct) FROM attempts").fetchone()[0] or 0

    # ---- 复习待办 ----
    due = conn.execute("SELECT COUNT(*) FROM cards WHERE retired=0 AND due_at<=datetime('now','localtime')").fetchone()[0]

    return {
        "日期": today_s,
        "使用时长": {
            "今日分钟": round(secs_since(today_s) / 60, 1),
            "本周分钟": round(secs_since(week_start) / 60, 1),
            "累计分钟": round(total_sec / 60, 1),
            "本周各科分钟": {k: round(v / 60, 1) for k, v in sorted(by_subject.items())},
        },
        "掌握情况": {"各科掌握率": mastery_list, "未掌握知识点": weak_list},
        "错题与作答": {
            "未解决错题数": open_wrong,
            "错题归因分布": attr_list,
            "总作答次数": total_att,
            "总正确率": round(total_ok * 100 / max(1, total_att), 1),
            "近14天正确率": acc_list,
        },
        "复习待办卡片": due,
    }


def get_advice(summary: dict, timeout: int = 45) -> str:
    """调用 DeepSeek 生成学习建议，返回 Markdown 文本。"""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "我的学习统计摘要（JSON）：\n"
                                        + json.dumps(summary, ensure_ascii=False)},
        ],
        "temperature": 0.6,
        "max_tokens": 1200,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + API_KEY},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError("DeepSeek API错误 %d: %s" % (e.code, err_body[:200]))
    except Exception as e:
        raise RuntimeError("API调用失败: %s" % e)

    text = result["choices"][0]["message"]["content"]
    return text.strip()
