
import re
with open('d:\\codex\\gaokao\\data\\real_exam\\化学.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 统计add_exam_question调用次数
matches = re.findall(r'add_exam_question\(', content)
total_questions = len(matches)
print(f'题目总数: {total_questions}')

# 统计年份标记
year_markers = re.findall(r'# ==================== (\d{4})年 ====================', content)
print(f'年份数量: {len(year_markers)}个年份')
print(f'年份列表: {year_markers}')

# 统计试卷数量
paper_markers = re.findall(r'# \d{4}年[\u4e00-\u9fa5]+卷', content)
print(f'试卷总数: {len(paper_markers)}套')

# 计算平均每卷题目数
print(f'平均每卷题目数: {total_questions / len(paper_markers):.1f}')
