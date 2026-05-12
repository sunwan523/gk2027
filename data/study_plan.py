import json
import os
from datetime import datetime, timedelta

PLAN_FILE = "data/plan_progress.json"

def generate_24day_plan():
    subjects = ["数学", "物理", "化学", "生物", "语文", "英语"]
    
    math_kps = ["实数与代数式", "方程与不等式", "一次函数与反比例函数", "几何图形基础", "三角形与四边形", "圆", "图形变换与坐标", "统计与概率基础", "集合与常用逻辑用语", "函数概念与性质", "二次函数与指数函数", "对数函数与幂函数", "三角函数", "数列", "不等式", "平面向量", "解三角形", "空间几何体", "点线面位置关系", "直线与方程", "圆与方程", "椭圆与双曲线", "抛物线", "计数原理", "概率", "统计", "导数及其应用", "积分", "复数", "推理与证明"]
    physics_kps = ["运动的描述", "匀变速直线运动", "相互作用", "牛顿运动定律", "曲线运动", "万有引力与航天", "功和功率", "动能定理", "机械能守恒定律", "动量守恒定律", "电场", "电路", "磁场", "电磁感应", "交变电流", "机械振动", "机械波", "光", "热学", "动量守恒与碰撞", "近代物理初步"]
    chemistry_kps = ["物质的变化和性质", "原子结构与元素", "化学式与化合价", "化学方程式", "常见气体", "水与溶液", "酸碱盐基础", "碳及其化合物", "金属与金属活动性", "物质的分类与转化", "离子反应", "氧化还原反应", "物质的量", "元素周期律与周期表", "化学键", "化学反应与能量", "化学反应速率", "化学平衡", "弱电解质的电离", "水的电离与溶液酸碱性", "盐类水解", "沉淀溶解平衡", "原电池", "电解池", "金属腐蚀与防护", "常见无机物推断", "化学实验基础"]
    biology_kps = ["组成细胞的元素和化合物", "蛋白质结构与功能", "核酸的结构与功能", "糖类和脂质", "水和无机盐的作用", "细胞的基本结构", "细胞膜的结构与功能", "细胞器的结构与功能", "细胞核的结构与功能", "物质跨膜运输方式", "酶与ATP", "细胞呼吸", "光合作用", "细胞的分化、衰老和凋亡", "细胞的增殖", "减数分裂和受精作用", "孟德尔遗传定律", "伴性遗传", "人类遗传病", "生物变异", "育种", "现代生物进化理论"]
    chinese_kps = ["现代文阅读·论述类文本", "现代文阅读·文学类文本", "现代文阅读·实用类文本", "文言文阅读·实词", "文言文阅读·虚词", "文言文阅读·特殊句式", "文言文阅读·翻译", "文言文阅读·断句与文化常识", "古诗词鉴赏·意象与意境", "古诗词鉴赏·表达技巧", "古诗词鉴赏·情感把握", "古诗词鉴赏·炼字", "古诗词鉴赏·题材与体裁", "名句名篇默写", "作文·审题立意", "作文·议论文写作", "作文·记叙文写作", "语言文字运用·字音字形", "语言文字运用·词语成语", "语言文字运用·病句辨析"]
    english_kps = ["名词与冠词", "代词", "数词", "形容词与副词", "介词", "连词", "动词分类", "动词时态", "被动语态", "非谓语动词", "句子成分与句型", "定语从句", "状语从句", "名词性从句", "虚拟语气", "情态动词", "主谓一致", "阅读理解·主旨大意", "阅读理解·细节理解", "阅读理解·推理判断", "阅读理解·词义猜测", "完形填空·语境理解", "写作·应用文", "写作·议论文"]
    
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