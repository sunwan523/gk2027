# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datetime import date
from core import db
from core import scheduler as sc

c = db.init_db()
plans = sc.plan_round_one(c, date(2026, 9, 10), days=90, factor=0.55)
seen = []
for p in plans:
    if p.day > 32:
        break
    for it in p.items:
        if it["kp_id"] not in [x[0] for x in seen]:
            seen.append((it["kp_id"], it["subject"], it["name"]))
print("第11-32天首次出现的节点（按顺序）:")
for i, (kid, s, n) in enumerate(seen, 1):
    print("%2d %-4s %-20s %s" % (i, s, kid, n))
# 最后一天有内容的天
last = max((p.day for p in plans if p.items), default=0)
print("\n排程最后一天(有内容):", last)
c.close()
