# -*- coding: utf-8 -*-
"""把 core/exam_bank/real_<科目>.py 里的真题灌进题库。

用法（在本机 Windows 上，用 Python 3.14 或任意装了依赖的解释器）：

    python tools/import_exam.py                 # 灌入所有用户库 + 主库
    python tools/import_exam.py --user 孙本瑞     # 只灌指定用户
    python tools/import_exam.py --subject 数学    # 只灌某一科
    python tools/import_exam.py --dry-run        # 只统计不写库

导入是幂等的：题干重复（UNIQUE 约束）会自动跳过，重复执行不会注水。
缺年份卷别或缺 source_ref 出处的条目会被拒绝入库并计入 skipped —— 这是刻意的，
不能溯源的题不该顶着真题的名义出现。
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_vendor"))

from config import DATA_DIR, DB_PATH           # noqa: E402
from core import db, exam_bank, users          # noqa: E402


def targets(user: str | None) -> list[tuple[str, str]]:
    """返回 [(显示名, 库路径)]。"""
    out: list[tuple[str, str]] = []
    if user:
        u = users.find_by_name(user)
        if not u:
            raise SystemExit("找不到用户：%s" % user)
        out.append((u["name"], users.db_path(u["id"])))
        return out
    for u in users.list_users():
        out.append((u["name"], users.db_path(u["id"])))
    out.append(("主库(默认)", DB_PATH))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="", help="只灌指定用户（名字）")
    ap.add_argument("--subject", default="", help="只灌某科目")
    ap.add_argument("--dry-run", action="store_true", help="只统计不写库")
    args = ap.parse_args()

    items = exam_bank.load_items(args.subject or None)
    if not items:
        print("core/exam_bank/ 下还没有真题数据文件（real_<科目>.py）")
        return 1

    by_subj: dict[str, int] = {}
    for it in items:
        by_subj[it.get("subject", "?")] = by_subj.get(it.get("subject", "?"), 0) + 1
    print("数据文件读到 %d 条真题：%s"
          % (len(items), "、".join("%s %d" % (k, v) for k, v in sorted(by_subj.items()))))

    if args.dry_run:
        ok = sum(1 for it in items if exam_bank._row_to_question(it))
        print("校验通过 %d 条，缺出处/缺年份卷别 %d 条（dry-run，未写库）"
              % (ok, len(items) - ok))
        return 0

    for name, path in targets(args.user or None):
        if not os.path.exists(path):
            print("- %s：库不存在，跳过（%s）" % (name, path))
            continue
        conn = db.init_db(path, seed=False)
        stat = exam_bank.import_to(conn, args.subject or None, verbose=False)
        real = conn.execute(
            "SELECT COUNT(*) FROM questions WHERE source_type='真题'").fetchone()[0]
        print("- %-8s 新入库 %d，刷新 %d，校验未过 %d，报错 %d ｜ 库内真题合计 %d"
              % (name, stat["inserted"], stat["updated"], stat["skipped"],
                 stat["error"], real))
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
