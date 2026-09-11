# -*- coding: utf-8 -*-
"""抽样检查：随机打开6个知识点，看每条要点的实际内容质量。"""
import sys, importlib.util, random
sys.path.insert(0, r'D:\codex\gaokao\gk2027')

random.seed(42)
subjects = ['语文', '数学', '英语', '物理', '化学', '生物']

for s in subjects:
    path = r'D:\codex\gaokao\gk2027\core\content_%s.py' % s
    spec = importlib.util.spec_from_file_location('c', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    kp_ids = list(m.CONTENT.keys())
    kp = random.choice(kp_ids)
    pts = m.CONTENT[kp]
    print('=' * 70)
    print('【%s】%s (%d要点, %d字)' % (s, kp, len(pts), sum(len(p) for p in pts)))
    print('=' * 70)
    for i, p in enumerate(pts):
        print('--- 第%d条 (%d字) ---' % (i+1, len(p)))
        print(p[:150])
        if len(p) > 150:
            print('  ...(后续%d字)' % (len(p)-150))
        print()
