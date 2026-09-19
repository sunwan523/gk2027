import json
import os
from datetime import datetime, timedelta

PLAN_FILE = "data/plan_progress.json"

def generate_24day_plan():
    subjects = ["数学", "物理", "化学", "生物", "语文", "英语"]
    
    math_kps = ["集合", "函数基础", "二次函数", "数列", "概率统计", "立体几何", "解析几何", "导数", "向量", "三角函数"]
    physics_kps = ["运动学", "牛顿定律", "功和能", "电学基础", "磁场", "电磁感应"]
    chemistry_kps = ["物质结构", "氧化还原反应", "离子反应", "电化学", "化学反应速率", "化学平衡"]
    biology_kps = ["细胞结构", "细胞代谢", "遗传基础", "生态系统", "生命活动调节", "生物技术"]
    chinese_kps = ["现代文阅读", "文言文阅读", "古诗词鉴赏", "作文", "语言运用"]
    english_kps = ["词汇", "语法", "阅读理解", "完形填空", "写作"]
    
    kps_dict = {
        "数学": math_kps,
        "物理": physics_kps,
        "化学": chemistry_kps,
        "生物": biology_kps,
        "语文": chinese_kps,
        "英语": english_kps
    }
    
    plan = []
    start_date = datetime(2026, 5, 8)
    
    for day in range(1, 25):
        day_date = start_date + timedelta(days=day-1)
        day_plan = {
            "day": day,
            "date": day_date.strftime("%Y-%m-%d"),
            "weekday": day_date.strftime("%A"),
            "completed": False,
            "tasks": {}
        }
        
        if day <= 8:
            for subject in subjects:
                kp_list = kps_dict[subject]
                kp_index = (day - 1) % len(kp_list)
                day_plan["tasks"][subject] = {
                    "knowledge_point": kp_list[kp_index],
                    "questions_count": 5,
                    "completed": False
                }
        elif day <= 16:
            for subject in subjects:
                kp_list = kps_dict[subject]
                kp_index = ((day - 9) % len(kp_list)) + len(kp_list) // 2
                if kp_index >= len(kp_list):
                    kp_index = kp_index % len(kp_list)
                day_plan["tasks"][subject] = {
                    "knowledge_point": kp_list[kp_index],
                    "questions_count": 8,
                    "completed": False
                }
        else:
            for subject in subjects:
                if day <= 20:
                    day_plan["tasks"][subject] = {
                        "knowledge_point": "综合复习",
                        "questions_count": 10,
                        "completed": False
                    }
                else:
                    day_plan["tasks"][subject] = {
                        "knowledge_point": "模拟训练",
                        "questions_count": 15,
                        "completed": False
                    }
        
        plan.append(day_plan)
    
    return plan

def load_plan_progress():
    if os.path.exists(PLAN_FILE):
        try:
            with open(PLAN_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return generate_24day_plan()
    return generate_24day_plan()

def save_plan_progress(plan):
    os.makedirs(os.path.dirname(PLAN_FILE), exist_ok=True)
    with open(PLAN_FILE, 'w', encoding='utf-8') as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)

def get_current_day(plan):
    today = datetime.now().strftime("%Y-%m-%d")
    for day_plan in plan:
        if day_plan["date"] == today:
            return day_plan["day"]
    return 1

def mark_task_completed(plan, day, subject):
    if 0 <= day - 1 < len(plan):
        plan[day-1]["tasks"][subject]["completed"] = True
        check_day_completed(plan, day)
        save_plan_progress(plan)

def check_day_completed(plan, day):
    if 0 <= day - 1 < len(plan):
        day_plan = plan[day-1]
        all_completed = all(task["completed"] for task in day_plan["tasks"].values())
        day_plan["completed"] = all_completed
        if all_completed and day < len(plan):
            plan[day]["completed"] = False
            save_plan_progress(plan)

def get_next_day_tasks(plan, current_day):
    if current_day < len(plan):
        return plan[current_day]
    return None

def get_plan_summary(plan):
    completed_days = sum(1 for day in plan if day["completed"])
    total_days = len(plan)
    return {
        "completed_days": completed_days,
        "total_days": total_days,
        "progress_percent": (completed_days / total_days) * 100
    }

def get_day_plan(plan, day):
    if 0 <= day - 1 < len(plan):
        return plan[day-1]
    return None

def reset_plan():
    new_plan = generate_24day_plan()
    save_plan_progress(new_plan)
    return new_plan