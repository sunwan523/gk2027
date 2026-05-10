import sys
sys.path.insert(0, 'd:/codex/gaokao')
from data.real_exam.化学 import get_real_exam_questions, get_exam_count

questions = get_real_exam_questions()
count = get_exam_count()

print(f"总共 {count} 道真题")

years = sorted(set(q["year"] for q in questions))
print(f"覆盖年份: {years}")

provinces = sorted(set(q["province"] for q in questions))
print(f"覆盖省份/试卷: {provinces}")

question_types = set(q["question_type"] for q in questions)
print(f"题型分布: {question_types}")

for year in years:
    year_count = len([q for q in questions if q["year"] == year])
    print(f"{year}年: {year_count}道题")