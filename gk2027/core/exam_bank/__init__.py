# -*- coding: utf-8 -*-
"""真题库：把 core/exam_bank/real_<科目>.py 里的真题灌进用户库。

设计要点（对应体检发现的「0 真题」缺口）：
  - 数据以 Python 模块形式存放，每个科目一个文件，`ITEMS` 是题目列表；
    这样分科并行补题互不冲突，也不需要额外的文件解析。
  - 入库走 `db.add_questions`，受三道硬约束保护：
      1. `UNIQUE(stem)` —— 重复题干自动跳过，不会注水；
      2. 非真题不得带 year/paper（此处恒为真题，仅作兜底）；
      3. 真题必须填 `source_ref` —— 缺出处的条目直接拒绝入库并计入 error，
         宁可少一道题，也不让无法溯源的题混进来。
  - 导入幂等：任何时候（新用户建库、手动执行工具）重复调用都安全。
"""
from __future__ import annotations

import importlib.util
import os
import sqlite3
from typing import Any, Iterable

HERE = os.path.dirname(os.path.abspath(__file__))

QTYPE_OK = ("选择题", "填空题", "解答题", "实验题", "作文", "默写")

# 原始题型 → 库内标准题型。英语卷的阅读/完形/七选五本质是选择题，
# 语法填空本质是填空题（判分走文本比对而非选项字母），作文/主观题按解答题自评。
QTYPE_MAP = {
    "阅读理解": "选择题",
    "完形填空": "选择题",
    "七选五": "选择题",
    "语法填空": "填空题",
    "写作": "解答题",
    "主观题": "解答题",
}


# ---------------------------------------------------------------- 加载
def modules() -> list[str]:
    """目录下所有 real_*.py 的路径（按文件名排序）。"""
    out = []
    for fn in sorted(os.listdir(HERE)):
        if fn.startswith("real_") and fn.endswith(".py"):
            out.append(os.path.join(HERE, fn))
    return out


def load_items(subject: str | None = None) -> list[dict[str, Any]]:
    """读取全部（或指定科目的）真题条目。"""
    items: list[dict[str, Any]] = []
    for path in modules():
        spec = importlib.util.spec_from_file_location("exam_bank_" + os.path.basename(path)[:-3], path)
        if spec is None or spec.loader is None:
            continue
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:      # 单个科目文件写坏不影响其他科目
            print("[exam_bank] 加载失败 %s: %s" % (os.path.basename(path), e))
            continue
        subj = getattr(mod, "SUBJECT", "") or os.path.basename(path)[5:-3]
        for it in getattr(mod, "ITEMS", []) or []:
            row = dict(it)
            row.setdefault("subject", subj)
            if subject and row["subject"] != subject:
                continue
            items.append(row)
    return items


# ---------------------------------------------------------------- 入库
def _row_to_question(it: dict[str, Any]) -> dict[str, Any] | None:
    """校验并转成 add_question 的入参；不合规返回 None。"""
    stem = (it.get("stem") or "").strip()
    if not stem:
        return None
    qtype = it.get("qtype") or "选择题"
    if qtype not in QTYPE_OK:
        qtype = QTYPE_MAP.get(qtype, "选择题")
    if not it.get("year") or not it.get("paper"):
        return None                       # 真题必须有年份卷别，否则无法定位
    if not (it.get("source_ref") or "").strip():
        return None                       # 触发器硬要求：真题必须可溯源
    return {
        "source_type": "真题",
        "year": int(it["year"]),
        "paper": str(it["paper"]),
        "question_no": str(it.get("question_no") or ""),
        "source_ref": str(it["source_ref"]).strip(),
        "verified": 1 if it.get("verified") else 0,
        "subject": it.get("subject") or "",
        "kp_id": it.get("kp_id") or None,
        "difficulty": int(it.get("difficulty") or 3),
        "qtype": qtype,
        "stem": stem,
        "options": list(it.get("options") or []),
        "answer": str(it.get("answer") or ""),
        "analysis": str(it.get("analysis") or ""),
        "points": list(it.get("points") or []),
    }


def import_to(conn: sqlite3.Connection, subject: str | None = None,
              verbose: bool = True) -> dict[str, int]:
    """把真题灌进题库。返回 {loaded, inserted, updated, skipped, error}。

    loaded   = 数据文件里读到的条目数
    inserted = 本次新入库
    updated  = 题干已存在，刷新了出处/核对状态/解析/采分点
    skipped  = 未通过校验（缺年份卷别/缺出处）而未尝试入库
    error    = 入库时报错

    之所以要 update 而不是简单跳过：真题会随人工校对不断修正
    （比如把 verified 从 0 改到 1、补更可靠的出处），题干不变时
    必须能把这些更正刷进库里，否则校对永远不生效。
    """
    from core import db

    raw = load_items(subject)
    rows, skipped = [], 0
    for it in raw:
        r = _row_to_question(it)
        if r is None:
            skipped += 1
        else:
            rows.append(r)
    if not rows:
        if verbose:
            print("[exam_bank] 没有可入库的真题（共读取 %d 条，跳过 %d 条）" % (len(raw), skipped))
        return {"loaded": len(raw), "inserted": 0, "updated": 0,
                "skipped": skipped, "error": 0}

    inserted = updated = error = 0
    for r in rows:
        try:
            db.add_question(conn, _commit=False, **r)
            inserted += 1
        except db.DuplicateStem:
            import json as _json
            conn.execute(
                "UPDATE questions SET year=?, paper=?, question_no=?, source_ref=?,"
                " verified=?, kp_id=?, difficulty=?, qtype=?, options=?, answer=?,"
                " analysis=?, points=? WHERE stem=?",
                (r["year"], r["paper"], r["question_no"], r["source_ref"],
                 r["verified"], r["kp_id"], r["difficulty"], r["qtype"],
                 _json.dumps(r["options"], ensure_ascii=False), r["answer"],
                 r["analysis"], _json.dumps(r["points"], ensure_ascii=False),
                 r["stem"]))
            updated += 1
        except sqlite3.IntegrityError:
            error += 1
        except Exception:
            error += 1
    conn.commit()
    stat = {"loaded": len(raw), "inserted": inserted, "updated": updated,
            "skipped": skipped, "error": error}
    if verbose:
        print("[exam_bank] 读取 %d 条 → 新入库 %d，刷新 %d，校验未过 %d，报错 %d"
              % (stat["loaded"], inserted, updated, skipped, error))
    return stat


def stats(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    """库内真题按「科目 × 年份 × 卷别」汇总，供前端选卷。"""
    cur = conn.execute(
        "SELECT subject, year, paper, COUNT(*) n, "
        " SUM(qtype='选择题') n_choice, SUM(qtype='填空题') n_fill, "
        " SUM(qtype='解答题') n_solve, SUM(qtype='实验题') n_exp, "
        " SUM(qtype='作文') n_essay, SUM(qtype='默写') n_dict, "
        " SUM(verified) n_verified "
        "FROM questions WHERE source_type='真题' "
        "GROUP BY subject, year, paper ORDER BY subject, year DESC, paper")
    cols = [d[0] for d in cur.description]
    out = []
    for r in cur.fetchall():
        d = dict(zip(cols, r))
        d["all_verified"] = int(d["n_verified"] or 0) == int(d["n"])
        out.append(d)
    return out
