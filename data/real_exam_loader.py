import json
import os

COMPLETED_QUESTIONS_FILE = "data/completed_real_exam.json"

def load_real_exam_questions(subject):
    module_map = {
        "语文": "data.real_exam.语文",
        "数学": "data.real_exam.数学",
        "英语": "data.real_exam.英语",
        "物理": "data.real_exam.物理",
        "化学": "data.real_exam.化学",
        "生物": "data.real_exam.生物"
    }
    
    if subject in module_map:
        module = __import__(module_map[subject], fromlist=['get_real_exam_questions', 'get_exam_count'])
        return module.get_real_exam_questions()
    return []

def get_real_exam_count(subject):
    questions = load_real_exam_questions(subject)
    return len(questions)

def get_completed_questions():
    if os.path.exists(COMPLETED_QUESTIONS_FILE):
        with open(COMPLETED_QUESTIONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_completed_questions(completed):
    with open(COMPLETED_QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(completed, f, ensure_ascii=False)

def add_completed_question(subject, question_id):
    completed = get_completed_questions()
    if subject not in completed:
        completed[subject] = []
    if question_id not in completed[subject]:
        completed[subject].append(question_id)
    save_completed_questions(completed)

def is_question_completed(subject, question_id):
    completed = get_completed_questions()
    return subject in completed and question_id in completed[subject]

def get_uncompleted_questions(subject):
    all_questions = load_real_exam_questions(subject)
    completed = get_completed_questions().get(subject, [])
    return [q for q in all_questions if q['id'] not in completed]

def clear_completed_questions(subject=None):
    completed = get_completed_questions()
    if subject:
        if subject in completed:
            del completed[subject]
    else:
        completed = {}
    save_completed_questions(completed)