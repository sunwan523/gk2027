subjects_config = {
    "语文": {
        "color": "#8b5cf6",
        "name": "语文",
        "total_kps": 5
    },
    "数学": {
        "color": "#3b82f6",
        "name": "数学",
        "total_kps": 10
    },
    "英语": {
        "color": "#ec4899",
        "name": "英语",
        "total_kps": 5
    },
    "物理": {
        "color": "#ef4444",
        "name": "物理",
        "total_kps": 6
    },
    "化学": {
        "color": "#f59e0b",
        "name": "化学",
        "total_kps": 6
    },
    "生物": {
        "color": "#10b981",
        "name": "生物",
        "total_kps": 6
    }
}

def get_subjects():
    return list(subjects_config.keys())

def get_subject_color(subject):
    return subjects_config.get(subject, {}).get("color", "#666666")

def get_subject_total_kps(subject):
    return subjects_config.get(subject, {}).get("total_kps", 0)
