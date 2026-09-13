# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import db, graph
from core.plan import FOUNDATION_HOURS

c = db.init_db()
rows = c.execute("SELECT subject, tier, weight, est_hours, COUNT(*) n FROM knowledge_points GROUP BY subject, tier").fetchall()
tot = {}
for r in rows:
    tot.setdefault(r["subject"], {"初中":0,"高中":0,"n":0})
    key = "初中" if r["tier"]=="初中" else "高中"
    tot[r["subject"]][key] += r["est_hours"]*r["n"]
    tot[r["subject"]]["n"] += r["n"]
print("科目   节点  初中学时 高中学时 合计  日整块  需天数")
gs=0
for s,v in tot.items():
    h = v["初中"]+v["高中"]
    daily = FOUNDATION_HOURS[s]["整块"]
    gs += h
    print("%-4s %3d  %6.0f  %6.0f  %5.0f  %4.2f  %5.1f" % (s, v["n"], v["初中"], v["高中"], h, daily, h/daily))
print("总学时:", gs, " 总节点:", sum(v['n'] for v in tot.values()))
# 可用：90天，扣除1-10诊断，11-90=80天；日整块合计
day_solid = sum(v["整块"] for v in FOUNDATION_HOURS.values())
print("日整块合计 %.2f h，80天可用整块 %.0f h" % (day_solid, day_solid*80))
c.close()
