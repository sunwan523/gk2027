import sys
sys.path.insert(0, 'd:/codex/gaokao/data/real_exam')
import 语文

qs = 语文.get_real_exam_questions()
questions_by_year = {}
for q in qs:
    year = q['year']
    if year not in questions_by_year:
        questions_by_year[year] = []
    questions_by_year[year].append(q)

with open('d:/codex/gaokao/data/real_exam/语文.py', 'w', encoding='utf-8') as f:
    f.write('real_exam_questions = []\n')
    f.write('\n')
    f.write('def get_real_exam_questions():\n')
    f.write('    return real_exam_questions\n')
    f.write('\n')
    f.write('def get_exam_count():\n')
    f.write('    return len(real_exam_questions)\n')
    f.write('\n')
    f.write('def add_exam_question(year, province, question_type, question, options, answer, analysis):\n')
    f.write('    real_exam_questions.append({\n')
    f.write('        "year": year,\n')
    f.write('        "province": province,\n')
    f.write('        "question_type": question_type,\n')
    f.write('        "question": question,\n')
    f.write('        "options": options,\n')
    f.write('        "answer": answer,\n')
    f.write('        "analysis": analysis,\n')
    f.write('        "id": f"{year}_{province}_{len(real_exam_questions)}"\n')
    f.write('    })\n')
    f.write('\n')

    for year in sorted(questions_by_year.keys(), reverse=True):
        f.write(f'# ==================== {year}年 ====================\n')
        for q in questions_by_year[year]:
            f.write('add_exam_question(\n')
            f.write(f'    year={year},\n')
            f.write(f'    province="{q["province"]}",\n')
            f.write(f'    question_type="{q["question_type"]}",\n')
            
            question_text = q['question'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            f.write(f'    question="{question_text}",\n')
            
            f.write('    options=[\n')
            for opt in q['options']:
                opt_text = opt.replace('\\', '\\\\').replace('"', '\\"')
                f.write(f'        "{opt_text}",\n')
            f.write('    ],\n')
            
            f.write(f'    answer="{q["answer"]}",\n')
            
            analysis_text = q['analysis'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            f.write(f'    analysis="{analysis_text}"\n')
            f.write(')\n')
            f.write('\n')

print(f'整理完成！共 {len(qs)} 道题目，按 {len(questions_by_year)} 个年份分段组织。')
