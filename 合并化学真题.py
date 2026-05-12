import os

# 读取所有分段文件
files = [
    'd:\\codex\\gaokao\\data\\real_exam\\化学_2005-2010.py',
    'd:\\codex\\gaokao\\data\\real_exam\\化学_2011-2015.py',
    'd:\\codex\\gaokao\\data\\real_exam\\化学_2016-2020.py',
    'd:\\codex\\gaokao\\data\\real_exam\\化学_2021-2025.py',
]

# 主文件头部
header = '''real_exam_questions = []

def get_real_exam_questions():
    return real_exam_questions

def get_exam_count():
    return len(real_exam_questions)

def add_exam_question(year, province, question_type, question, options, answer, analysis):
    real_exam_questions.append({
        "year": year,
        "province": province,
        "question_type": question_type,
        "question": question,
        "options": options,
        "answer": answer,
        "analysis": analysis,
        "id": f"{year}_{province}_{len(real_exam_questions)}"
    })

'''

# 读取所有内容
all_content = [header]
for f in files:
    print(f"正在读取 {f}...")
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        # 跳过头部（因为每个文件都有相同的头部）
        lines = content.split('\n')
        # 找到第一个年份标记的位置
        start_idx = 0
        for i, line in enumerate(lines):
            if '# ==================== 20' in line:
                start_idx = i
                break
        # 只取年份数据部分
        all_content.append('\n'.join(lines[start_idx:]))

# 合并所有内容
final_content = '\n'.join(all_content)

# 写入主文件
output_file = 'd:\\codex\\gaokao\\data\\real_exam\\化学.py'
print(f"正在写入 {output_file}...")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("合并完成！")

# 验证
import re
q_count = final_content.count('add_exam_question(')
print(f"题目总数: {q_count}")

# 统计年份
years = re.findall(r'# ==================== (\d{4})年 ====================', final_content)
print(f"年份: {years}")
print(f"年份数量: {len(years)}")

# 统计试卷
papers = re.findall(r'# \d{4}年([\u4e00-\u9fa5]+卷)', final_content)
print(f"试卷总数: {len(papers)}")
