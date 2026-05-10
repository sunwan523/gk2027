wrong_questions = []

def add_wrong_question(subject, knowledge_point, question, options, user_answer, correct_answer, analysis, wrong_reason):
    wrong_questions.append({
        "subject": subject,
        "knowledge_point": knowledge_point,
        "question": question,
        "options": options,
        "user_answer": user_answer,
        "correct_answer": correct_answer,
        "analysis": analysis,
        "wrong_reason": wrong_reason,
        "timestamp": "2024-01-01",
        "review_count": 0
    })

def get_wrong_questions(subject=None, knowledge_point=None):
    result = wrong_questions[:]
    if subject:
        result = [q for q in result if q["subject"] == subject]
    if knowledge_point:
        result = [q for q in result if q["knowledge_point"] == knowledge_point]
    return result

def clear_wrong_questions():
    wrong_questions.clear()
