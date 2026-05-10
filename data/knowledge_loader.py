def load_knowledge(subject):
    module_map = {
        "语文": "data.knowledge.语文",
        "数学": "data.knowledge.数学",
        "英语": "data.knowledge.英语",
        "物理": "data.knowledge.物理",
        "化学": "data.knowledge.化学",
        "生物": "data.knowledge.生物"
    }
    
    if subject in module_map:
        module = __import__(module_map[subject], fromlist=['get_knowledge_points', 'get_kp_names'])
        return module.get_knowledge_points(), module.get_kp_names()
    return {}, []

def get_kp_names(subject):
    _, names = load_knowledge(subject)
    return names

def get_kp_data(subject, kp_name):
    kp_dict, _ = load_knowledge(subject)
    if kp_name in kp_dict:
        return kp_dict[kp_name]
    return None
