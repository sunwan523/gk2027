
import sys
sys.path.insert(0, 'd:\\codex\\gaokao\\data\\real_exam')

from 语文 import get_real_exam_questions, get_exam_count

questions = get_real_exam_questions()
print(f"总题数: {get_exam_count()}")
print()

# 按年份统计
year_stats = {}
for q in questions:
    year = q['year']
    if year not in year_stats:
        year_stats[year] = {'total': 0, 'provinces': set()}
    year_stats[year]['total'] += 1
    year_stats[year]['provinces'].add(q['province'])

print("按年份统计:")
for year in sorted(year_stats.keys()):
    print(f"{year}年: {year_stats[year]['total']}题, 试卷: {sorted(year_stats[year]['provinces'])}")

print()
print("检查是否覆盖2005-2025年:")
for year in range(2005, 2026):
    if year not in year_stats:
        print(f"  ❌ 缺失 {year}年")
    else:
        print(f"  ✅ {year}年: {year_stats[year]['total']}题")
