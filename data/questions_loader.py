def load_questions(subject):
    module_map = {
        "语文": "data.questions.语文",
        "数学": "data.questions.数学",
        "英语": "data.questions.英语",
        "物理": "data.questions.物理",
        "化学": "data.questions.化学",
        "生物": "data.questions.生物"
    }
    
    if subject in module_map:
        module = __import__(module_map[subject], fromlist=['get_questions', 'get_kp_names', 'get_question_count'])
        return module.get_questions(), module.get_kp_names()
    return {}, []

def get_kp_names(subject):
    _, names = load_questions(subject)
    return names

def get_questions_by_kp(subject, kp_name):
    questions_dict, _ = load_questions(subject)
    if kp_name in questions_dict:
        return questions_dict[kp_name]
    return []

def get_question_count(subject=None):
    if subject:
        _, _, count = get_questions_with_count(subject)
        return count
    total = 0
    for subj in ["语文", "数学", "英语", "物理", "化学", "生物"]:
        total += get_question_count(subj)
    return total

def get_questions_with_count(subject):
    module_map = {
        "语文": "data.questions.语文",
        "数学": "data.questions.数学",
        "英语": "data.questions.英语",
        "物理": "data.questions.物理",
        "化学": "data.questions.化学",
        "生物": "data.questions.生物"
    }
    
    if subject in module_map:
        module = __import__(module_map[subject], fromlist=['get_questions', 'get_kp_names', 'get_question_count'])
        questions = module.get_questions()
        kp_names = module.get_kp_names()
        count = module.get_question_count()
        return questions, kp_names, count
    return {}, [], 0
