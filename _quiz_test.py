# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import db
from core import seed_quiz as sq

c = db.init_db()
stats = sq.seed_self_quiz(c)
print("录入统计:", stats)
total = c.execute("SELECT COUNT(*) FROM questions WHERE source_type='自主命题练习'").fetchone()[0]
print("自检题总数:", total)
# 覆盖检查：哪些排程节点没有自检题
covered = {r["kp_id"] for r in c.execute("SELECT DISTINCT kp_id FROM questions WHERE kp_id IS NOT NULL")}
allkp = [r["id"] for r in c.execute("SELECT id FROM knowledge_points")]
miss = [k for k in allkp if k not in covered]
print("有题节点:", len(covered), "/", len(allkp))
print("缺题节点(%d):" % len(miss), miss)
c.close()
