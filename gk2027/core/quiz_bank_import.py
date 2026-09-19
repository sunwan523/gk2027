# -*- coding: utf-8 -*-
"""题库批量导入：扫描 core/quizbank/ 下所有题库文件，写入主库和全部用户库。

题库文件格式：每个文件定义 BANK = {kp_id: [题目dict, ...], ...}
题目dict字段：qtype, difficulty, stem, options(选择题), answer, analysis
导入时自动补 subject、source_type，并按题干去重（db.add_questions 已处理）。
"""
from __future__ import annotations

import os
import re
import glob
import random
import hashlib
import importlib.util

from core import db, users

BANK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quizbank")

# kp_id 前缀 -> 科目
PREFIX_SUBJECT = {
    "mat": "数学", "phy": "物理", "che": "化学",
    "bio": "生物", "eng": "英语", "chn": "语文",
}

_OPT_PREFIX = re.compile(r"^[A-D][.、．]\s*")


def balance_options(q: dict) -> None:
    """对四选一选择题做确定性乱序，使正确答案位置均衡，避免正确选项固化在某一字母。

    正确选项的文本内容保持不变，仅重新排列 A-D 的位置并改写答案字母。
    乱序种子取题干哈希，故同一题结果稳定、可复现；非四选一或多答案题保持原样。
    """
    if q.get("qtype") != "选择题":
        return
    opts = q.get("options")
    if not isinstance(opts, list) or len(opts) != 4:
        return
    ans = str(q.get("answer", "")).strip()
    if len(ans) != 1 or ans not in "ABCD":
        return
    bodies = [_OPT_PREFIX.sub("", str(o)) for o in opts]
    if len(set(bodies)) != 4:
        # 选项有重复，乱序会导致答案无法唯一定位，跳过
        return
    correct_body = bodies["ABCD".index(ans)]
    seed = int(hashlib.md5(str(q.get("stem", "")).encode("utf-8")).hexdigest()[:12], 16)
    rng = random.Random(seed)
    rng.shuffle(bodies)
    new_idx = bodies.index(correct_body)
    q["options"] = ["%s. %s" % ("ABCD"[i], b) for i, b in enumerate(bodies)]
    q["answer"] = "ABCD"[new_idx]


def _subject_of(kp_id: str) -> str:
    prefix = kp_id.split("_")[0]
    return PREFIX_SUBJECT.get(prefix, "")


def load_all_banks() -> dict[str, list[dict]]:
    """合并 quizbank 目录下所有题库，返回 {kp_id: [题目...]}。"""
    merged: dict[str, list[dict]] = {}
    files = sorted(glob.glob(os.path.join(BANK_DIR, "*.py")))
    for path in files:
        name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location("quizbank_" + name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        bank = getattr(mod, "BANK", {})
        for kp_id, qs in bank.items():
            merged.setdefault(kp_id, []).extend(qs)
    return merged


def normalize(kp_id: str, qs: list[dict]) -> list[dict]:
    """补齐 subject / source_type 字段。"""
    out = []
    subject = _subject_of(kp_id)
    for q in qs:
        item = dict(q)
        item.setdefault("subject", subject)
        item["kp_id"] = kp_id
        item.setdefault("source_type", "自主命题练习")
        item.setdefault("verified", 1)
        item.setdefault("difficulty", 2)
        item.setdefault("options", [])
        item.setdefault("analysis", "")
        # 入库前对四选一选项做确定性乱序，均衡正确答案位置
        balance_options(item)
        out.append(item)
    return out


def import_to_conn(conn, bank: dict[str, list[dict]]) -> dict[str, int]:
    total = {"inserted": 0, "duplicate": 0, "error": 0}
    for kp_id, qs in bank.items():
        rows = normalize(kp_id, qs)
        r = db.add_questions(conn, rows)
        for k in total:
            total[k] += r[k]
    return total


def import_all(include_users: bool = True) -> None:
    bank = load_all_banks()
    n_kp = len(bank)
    n_q = sum(len(v) for v in bank.values())
    print("题库装载：%d 个知识点，%d 道题" % (n_kp, n_q))

    # 主库
    from config import DB_PATH
    import sqlite3
    main_conn = sqlite3.connect(DB_PATH)
    main_conn.row_factory = sqlite3.Row
    r = import_to_conn(main_conn, bank)
    print("主库：新增 %d，重复 %d，错误 %d" % (r["inserted"], r["duplicate"], r["error"]))
    main_conn.close()

    # 全部用户库
    if include_users:
        for u in users.list_users():
            upath = users.db_path(u["id"])
            if not os.path.exists(upath):
                continue
            import sqlite3
            uc = sqlite3.connect(upath)
            uc.row_factory = sqlite3.Row
            r = import_to_conn(uc, bank)
            print("用户 %s：新增 %d，重复 %d" % (u["name"], r["inserted"], r["duplicate"]))
            uc.close()


if __name__ == "__main__":
    import_all()
