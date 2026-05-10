import sys
sys.path.insert(0, 'd:/codex/gaokao')
from data.real_exam.物理 import get_real_exam_questions, get_exam_count

questions = get_real_exam_questions()
count = get_exam_count()
years = sorted(set(q["year"] for q in questions))
provinces = sorted(set(q["province"] for q in questions))
question_types = set(q["question_type"] for q in questions)

print(f"总共 {count} 道真题")
print(f"覆盖年份: {years}")
print(f"覆盖省份/试卷: {provinces}")
print(f"题型分布: {question_types}")