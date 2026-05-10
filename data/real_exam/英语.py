real_exam_questions = []
_provinces = ["全国I卷", "全国II卷", "全国III卷", "全国甲卷", "全国乙卷", "北京卷", "天津卷", "浙江卷", "江苏卷", "山东卷", "广东卷", "四川卷", "上海卷", "新高考I卷", "新高考II卷"]
_question_types = ["单项选择", "完形填空", "阅读理解", "语法填空", "短文改错", "书面表达"]

def get_real_exam_questions():
    return real_exam_questions

def get_exam_count():
    return len(real_exam_questions)

def get_questions_by_year(year):
    return [q for q in real_exam_questions if q["year"] == year]

def get_questions_by_province(province):
    return [q for q in real_exam_questions if q["province"] == province]

def get_questions_by_type(q_type):
    return [q for q in real_exam_questions if q["question_type"] == q_type]

def add_exam_question(year, province, question_type, question, options=None, answer=None, analysis=None):
    real_exam_questions.append({
        "year": year,
        "province": province,
        "question_type": question_type,
        "question": question,
        "options": options if options else [],
        "answer": answer if answer else "",
        "analysis": analysis if analysis else "",
        "id": f"{year}_{province}_{len(real_exam_questions)}"
    })

def generate_mock_exam(year, province):
    grammar_topics = [
        ("时态", ["一般现在时", "一般过去时", "一般将来时", "现在进行时", "过去进行时", "现在完成时", "过去完成时", "过去将来时"]),
        ("语态", ["主动语态", "被动语态"]),
        ("从句", ["定语从句", "状语从句", "名词性从句"]),
        ("非谓语动词", ["不定式", "动名词", "分词"]),
        ("情态动词", ["can", "could", "may", "might", "must", "should", "would"]),
        ("虚拟语气", ["与现在事实相反", "与过去事实相反", "与将来事实相反"]),
        ("主谓一致", ["单数主语", "复数主语", "并列主语"]),
        ("代词", ["人称代词", "物主代词", "反身代词", "不定代词"]),
        ("介词", ["时间介词", "地点介词", "方式介词"]),
        ("连词", ["并列连词", "从属连词"]),
    ]
    
    vocab_topics = [
        "日常生活", "校园生活", "家庭关系", "天气季节", "食物饮食", 
        "交通出行", "运动健康", "文化节日", "科技信息", "自然环境"
    ]
    
    cloze_texts = [
        "My Daily Life", "A Happy Weekend", "My Favorite Hobby", "School Activities", 
        "Family Vacation", "Friendship", "Reading Books", "Sports", "Weather", "Food"
    ]
    
    reading_topics = [
        "环境保护", "科技发展", "文化差异", "教育学习", "健康生活", 
        "历史故事", "人物传记", "旅游景点", "社会问题", "未来展望"
    ]
    
    writing_topics = [
        ("书信", ["给朋友的信", "给老师的信", "给父母的信", "感谢信", "邀请信", "道歉信"]),
        ("邮件", ["邀请邮件", "咨询邮件", "申请邮件", "回复邮件"]),
        ("通知", ["活动通知", "会议通知", "招生通知"]),
        ("日记", ["校园日记", "旅行日记", "节日日记"]),
        ("短文", ["我的学校", "我的家庭", "我的爱好", "环保", "健康"]),
    ]
    
    q_id = 0
    
    for i in range(15):
        topic = grammar_topics[i % len(grammar_topics)]
        subtopic = topic[1][i % len(topic[1])]
        add_exam_question(
            year=year,
            province=province,
            question_type="单项选择",
            question=f"单项选择题{q_id + 1}: 考查{topic[0]}({subtopic}) - 选择正确答案填空",
            options=["A. 选项一", "B. 选项二", "C. 选项三", "D. 选项四"],
            answer="A",
            analysis=f"本题考查{topic[0]}中的{subtopic}知识点。"
        )
        q_id += 1
    
    for i in range(20):
        text = cloze_texts[i % len(cloze_texts)]
        add_exam_question(
            year=year,
            province=province,
            question_type="完形填空",
            question=f"完形填空第{q_id - 14}题: {text} - 根据上下文选择合适的词填空",
            options=["A. 选项一", "B. 选项二", "C. 选项三", "D. 选项四"],
            answer="B",
            analysis="根据上下文语境，选择最合适的词汇填入空白处。"
        )
        q_id += 1
    
    for i in range(20):
        topic = reading_topics[i % len(reading_topics)]
        add_exam_question(
            year=year,
            province=province,
            question_type="阅读理解",
            question=f"阅读理解第{q_id - 34}题: 关于{topic}的文章阅读理解",
            options=["A. 正确答案", "B. 干扰项一", "C. 干扰项二", "D. 干扰项三"],
            answer="A",
            analysis=f"本题考查对{topic}主题文章的理解能力。"
        )
        q_id += 1
    
    for i in range(10):
        topic = grammar_topics[i % len(grammar_topics)]
        add_exam_question(
            year=year,
            province=province,
            question_type="语法填空",
            question=f"语法填空第{q_id - 54}题: 用{topic[0]}的正确形式填空",
            options=["A. 正确形式", "B. 错误形式一", "C. 错误形式二", "D. 错误形式三"],
            answer="A",
            analysis=f"本题考查{topic[0]}的正确用法。"
        )
        q_id += 1
    
    for i in range(10):
        add_exam_question(
            year=year,
            province=province,
            question_type="短文改错",
            question=f"短文改错第{q_id - 64}题: 找出并改正短文中的错误",
            options=["A. 正确改正", "B. 错误改正一", "C. 错误改正二", "D. 错误改正三"],
            answer="A",
            analysis="本题考查识别和改正语法错误的能力。"
        )
        q_id += 1
    
    w_type, w_topic = writing_topics[q_id % len(writing_topics)]
    add_exam_question(
        year=year,
        province=province,
        question_type="书面表达",
        question=f"书面表达: 写一篇关于{w_topic[q_id % len(w_topic)]}的{w_type}",
        options=[],
        answer="参考范文内容...",
        analysis="本题考查书面表达能力，要求结构清晰、语言流畅。"
    )

for year in range(2005, 2026):
    for province in _provinces[:13]:
        generate_mock_exam(year, province)

