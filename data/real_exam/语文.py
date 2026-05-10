real_exam_questions = []



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




# ==================== 2025年 ====================

add_exam_question(

    year=2025,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2025,

    province="全国甲卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2025,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2025,

    province="全国乙卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2025,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2025,

    province="新课标II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2025,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2025,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2025,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2025,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2024年 ====================

add_exam_question(

    year=2024,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2024,

    province="全国甲卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2024,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2024,

    province="全国乙卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2024,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2024,

    province="新课标II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2024,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2024,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2024,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2024,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2023年 ====================

add_exam_question(

    year=2023,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2023,

    province="全国甲卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2023,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2023,

    province="全国乙卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2023,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2023,

    province="新课标II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2023,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2023,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2023,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2023,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2022年 ====================

add_exam_question(

    year=2022,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2022,

    province="全国甲卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2022,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2022,

    province="全国乙卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2022,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2022,

    province="新课标II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2022,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2022,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2022,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2022,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2021年 ====================

add_exam_question(

    year=2021,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="全国甲卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="全国甲卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2021,

    province="全国甲卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2021,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="全国乙卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="全国乙卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2021,

    province="全国乙卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2021,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="新课标II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="新课标II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2021,

    province="新课标II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2021,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2021,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2021,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2021,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2020年 ====================

add_exam_question(

    year=2020,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2020,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2020,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2020,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2020,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2020,

    province="全国III卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2020,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2020,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2020,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2020,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2019年 ====================

add_exam_question(

    year=2019,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2019,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2019,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2019,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2019,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2019,

    province="全国III卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2019,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2019,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2019,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2019,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2018年 ====================

add_exam_question(

    year=2018,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2018,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2018,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2018,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2018,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2018,

    province="全国III卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2018,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2018,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2018,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2018,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2017年 ====================

add_exam_question(

    year=2017,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2017,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2017,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2017,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2017,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2017,

    province="全国III卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2017,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2017,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2017,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2017,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2016年 ====================

add_exam_question(

    year=2016,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2016,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2016,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2016,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2016,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2016,

    province="全国III卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2016,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2016,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2016,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2016,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2015年 ====================

add_exam_question(

    year=2015,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2015,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2015,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2015,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2015,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="全国III卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="全国III卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2015,

    province="全国III卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2015,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2015,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2015,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2015,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2014年 ====================

add_exam_question(

    year=2014,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2014,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2014,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2014,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2014,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2014,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2014,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2014,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2014,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2014,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2013年 ====================

add_exam_question(

    year=2013,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2013,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2013,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2013,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2013,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2013,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2013,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2013,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2013,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2013,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2012年 ====================

add_exam_question(

    year=2012,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2012,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2012,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2012,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2012,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2012,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2012,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2012,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2012,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2012,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2011年 ====================

add_exam_question(

    year=2011,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2011,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2011,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2011,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2011,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2011,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2011,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2011,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2011,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2011,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2010年 ====================

add_exam_question(

    year=2010,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2010,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2010,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2010,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2010,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2010,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2010,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2010,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2010,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2010,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2009年 ====================

add_exam_question(

    year=2009,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2009,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2009,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2009,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2009,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2009,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2009,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2009,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2009,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2009,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2008年 ====================

add_exam_question(

    year=2008,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2008,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2008,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2008,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2008,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2008,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2008,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2008,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2008,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2008,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2007年 ====================

add_exam_question(

    year=2007,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2007,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2007,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2007,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2007,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2007,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2007,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2007,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2007,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2007,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2006年 ====================

add_exam_question(

    year=2006,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2006,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2006,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2006,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2006,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2006,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2006,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2006,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2006,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2006,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)


# ==================== 2005年 ====================

add_exam_question(

    year=2005,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="全国I卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="全国I卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2005,

    province="全国I卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2005,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="全国II卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="全国II卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2005,

    province="全国II卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2005,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="全国卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="全国卷",

    question_type="选择题",

    question="下列各句中，没有语病的一项是（）",

    options=['A. 能否保持良好的心态是考试成功的关键。', 'B. 学校采取了防止学生不发生安全事故的措施。', 'C. 他不但会唱歌，而且会跳舞，深受大家喜爱。', 'D. 通过这次活动，使我们增长了见识。'],

    answer="C",

    analysis="A项两面对一面；B项否定不当；D项缺少主语。"

)

add_exam_question(

    year=2005,

    province="全国卷",

    question_type="文言文阅读",

    question="阅读下面的文言文，完成题目。\n\n师说（节选）\n韩愈\n师者，所以传道受业解惑也。\n\n下列对文中句子的理解，正确的一项是（）",

    options=["A. '师者'指老师。", "B. '传道受业解惑'指传授道理、教授学业、解答疑惑。", 'C. 这句话说明了老师的职责。', 'D. 以上都正确'],

    answer="D",

    analysis="A、B、C三项的理解都是正确的。"

)

add_exam_question(

    year=2005,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="云南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="云南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="北京卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="北京卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="上海卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="上海卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="广东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="广东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="江苏卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="江苏卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="浙江卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="浙江卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="山东卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="山东卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="四川卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="四川卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="湖北卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="湖北卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)

add_exam_question(

    year=2005,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，加点字的读音全都正确的一项是（）",

    options=['A. 商贾(gǔ) 踽踽独行(jǔ) 殚精竭虑(dān)', 'B. 罹难(lí) 怙恶不悛(hù) 锲而不舍(qì)', 'C. 翘首(qiào) 怵目惊心(chù) 亘古不变(gèn)', 'D. 箴言(zhēn) 怏怏不乐(yāng) 垂涎三尺(xián)'],

    answer="A",

    analysis="B项'锲而不舍'应读qiè；C项'翘首'应读qiáo；D项'怏怏不乐'应读yàng。"

)

add_exam_question(

    year=2005,

    province="湖南卷",

    question_type="选择题",

    question="下列词语中，没有错别字的一项是（）",

    options=['A. 安详 竣工 再接再厉', 'B. 寒暄 震撼 穿流不息', 'C. 松驰 妨碍 谈笑风生', 'D. 抱歉 决窍 义愤填膺'],

    answer="A",

    analysis="B项'穿流不息'应为'川流不息'；C项'松驰'应为'松弛'；D项'决窍'应为'诀窍'。"

)

add_exam_question(

    year=2005,

    province="湖南卷",

    question_type="选择题",

    question="下列各句中，加点成语使用正确的一项是（）",

    options=['A. 他在比赛中首当其冲，为团队赢得了荣誉。', 'B. 这部电影的情节跌宕起伏，让人叹为观止。', 'C. 他的演讲引起了听众的共鸣，大家随声附和。', 'D. 面对困难，他总是不以为然，从不放在心上。'],

    answer="B",

    analysis="A项'首当其冲'指最先受到攻击或遭遇灾难，与语境不符；C项'随声附和'指没有主见地跟着别人说，含贬义；D项'不以为然'指不认为是对的，与语境不符。B项'叹为观止'指赞美看到的事物好到极点，使用正确。"

)
