import sys
sys.path.insert(0, r'd:\codex\gaokao\data\real_exam')
import 英语

qs = 英语.get_real_exam_questions()
print('总题数:', len(qs))
print('年份范围:', sorted(set(q['year'] for q in qs)))
print('试卷类型:', set(q['province'] for q in qs))
print('题型:', set(q['question_type'] for q in qs))
print()
print('示例题目:')
for q in qs[:3]:
    print(f"年份: {q['year']}, 试卷: {q['province']}, 题型: {q['question_type']}")
    print(f"题目: {q['question']}")
    print(f"选项: {q['options']}")
    print(f"答案: {q['answer']}")
    print(f"解析: {q['analysis']}")
    print()

