import sys
sys.path.insert(0, 'd:/codex/gaokao')
from data.real_exam.数学 import get_real_exam_questions

questions = get_real_exam_questions()

year_stats = {}
province_stats = {}

for q in questions:
    year = q['year']
    province = q['province']
    
    if year not in year_stats:
        year_stats[year] = {'count': 0, 'provinces': set()}
    year_stats[year]['count'] += 1
    year_stats[year]['provinces'].add(province)
    
    if province not in province_stats:
        province_stats[province] = 0
    province_stats[province] += 1

print('=== 各年份题目分布 ===')
for year in sorted(year_stats.keys()):
    stats = year_stats[year]
    print(f'{year}年: {stats["count"]}题, 涉及{len(stats["provinces"])}套试卷')

print()
print('=== 各试卷类型题目数量 ===')
for province, count in sorted(province_stats.items(), key=lambda x: x[1], reverse=True):
    print(f'{province}: {count}题')

print()
print(f'总计: {len(questions)}道题')
print(f'覆盖年份: {min(year_stats.keys())}-{max(year_stats.keys())}（共{len(year_stats)}年）')
print(f'试卷类型总数: {len(province_stats)}种')
