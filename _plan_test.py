# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datetime import date
from core import db
from core import scheduler as sc

c = db.init_db()
plans = sc.plan_round_one(c, date(2026, 9, 10), days=90, factor=0.55)

# 1) 覆盖检查
scheduled = {}
for p in plans:
    for it in p.items:
        scheduled.setdefault(it["kp_id"], []).append((p.day, it["minutes"]))
total_nodes = c.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
print("节点总数(含滚动):", total_nodes, "已排:", len(scheduled), "+滚动2 =", len(scheduled)+2)
missing = [r["id"] for r in c.execute("SELECT id FROM knowledge_points")
           if r["id"] not in scheduled and r["id"] not in sc.ROLLING_KP]
print("未排节点:", missing or "无")

# 2) 依赖顺序检查：requires 的完成日 <= 依赖者开始日
edges = c.execute("SELECT kp_id, requires_id FROM kp_requires").fetchall()
bad = []
for e in edges:
    a, b = e["kp_id"], e["requires_id"]
    if a in scheduled and b in scheduled:
        if min(x[0] for x in scheduled[a]) < max(x[0] for x in scheduled[b]):
            bad.append((b, a))
print("依赖颠倒:", bad or "无")

# 3) 每日学时检查
over = []
for p in plans:
    mins = sum(it["minutes"] for it in p.items)
    if mins > 6.5*60 + 5:
        over.append((p.day, mins))
print("超预算天数:", over or "无")
tot_min = sum(sum(it["minutes"] for it in p.items) for p in plans)
print("排入总学时: %.1f h（预算 6.5h x 80天 = 520h）" % (tot_min/60))

# 4) 每科天数分布
per = {}
for p in plans:
    for it in p.items:
        per.setdefault(it["subject"], [0,0])
        per[it["subject"]][0] += 1
        per[it["subject"]][1] += it["minutes"]
for s, (n, m) in sorted(per.items()):
    print("%-3s 条目%3d 学时%6.1f" % (s, n, m/60))

# 5) 抽样打印第 11-14 天
for p in plans[10:14]:
    print("\n第%d天 %s:" % (p.day, p.d))
    for it in p.items:
        print("   %s %s (%dmin)" % (it["subject"], it["name"], it["minutes"]))

# 6) 保存 + 重载
sc.save_plan(c, plans, start=date(2026,9,10), days=90, factor=0.55)
meta, plans2 = sc.load_plan(c)
print("\n重载:", meta, len(plans2), "天")
c.close()
