# -*- coding: utf-8 -*-
"""英语真题（2024 新高考II卷 / 新课标II卷，适用云南等省）。

来源与核实说明（见每条 source_ref / verified）：

本文件全部条目均来自联网检索到的 2024 年新高考II卷（即新课标II卷，同年同卷）英语真题
公开转载，并经两个及以上独立来源对答案做了交叉比对：
  - 阅读 B/C/D、完形、七选五、书面表达题目原文：
      https://zy.21cnjy.com/20658767  （21世纪教育网，已 WebFetch 确认内容相关）
  - 语法填空原文与 56–65 答案：
      https://zy.21cnjy.com/20856858  （21世纪教育网，已 WebFetch 确认内容相关）
  - 答案交叉核对用的独立来源（均给出一致答案键）：
      http://edu.newdu.com/NECE/Politics/OldExam/202406/4079058_3.html （新都网）
      https://cdn.zizzs.com/17182455318362024%E5%B9%B4%E9%AB%98%E8%80%83%E6%96%B0%E8%AF%BE%E6%A0%87II%E5%8D%B7%E8%8B%B1%E8%AF%AD%E7%AD%94%E6%A1%88.pdf （教习网 PDF）
      以及 qq「高中英语教学与考试资源库」整理的参考答案。

答案键一致性（多源互证）：
  传统阅读 21-23 DAD / 24-27 CBAD / 28-31 CBDA / 32-35 CBCA
  七选五     36-40 BCEAG
  完形填空   41-45 DBADB / 46-50 CACCB / 51-55 ACDAB
  语法填空   56 who 57 themes 58 were 59 to 60 inspired 61 was built
            62 visibility 63 to find 64 Recalling 65 and

verified 标记规则：
  - 选择题 / 语法填空（共 14 题）：其答案经 ≥2 个独立权威来源逐题核对一致，verified=1。
  - 书面表达（应用文 + 读后续写，共 2 题）：题目原文来自 21cnjy/20658767，但所给
    “范文 / 要点”为参考性内容、难以用独立来源逐字核对，故 verified=0，使用前请以
    官方评分标准为准。
  - 阅读 A 篇（Carlow Autumn Walking Festival）因未能取到逐字英文原文，本文件未收录，
    以免编造，符合“宁少勿错”原则。

存储约定（与数学/物理范本一致）：
  选择题：stem 存「原文段落 + 该题题干」，options 存四个选项，answer 存正确字母。
  七选五：stem 存「原文段落 + 该空」，options 存 A–G 七个选项，answer 存正确字母。
  语法填空：stem 存「原文段落 + 该空」，options 留空 []，answer 存所填词/形式。
  作文：stem 存题目与提示，options 留空 []，answer 存范文或要点，points 存采分点。
"""

SUBJECT = "英语"

ITEMS = [
    # ============ 一、阅读理解（新高考II卷 2024） ============
    # ---- B 篇：BART 车站短篇小说打印亭 ----
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "24",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "阅读理解",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""B
Do you ever get to the train station and realize you forgot to bring something to read? Yes, we all have our phones, but many of us still like to go old school and read something printed.
Well, there's a kiosk for that. In the San Francisco Bay Area, at least.
"You enter the fare gates and you'll see a kiosk that is lit up and it tells you can get a one-minute, a three-minute, or a five-minute story," says Alicia Trost, the chief communications officer for the San Francisco Bay Area Rapid Transit — known as BART. "You choose which length you want and it gives you a receipt-like short story."
It's that simple. Riders have printed nearly 20,000 short stories and poems since the program was launched last March. Some are classic short stories, and some are new original works.
Trost also wants to introduce local writers to local riders. "We wanted to do something where we do a call to artists in the Bay Area to submit stories for a contest," Trost says. "And as of right now, we've received about 120 submissions. The winning stories would go into our kiosk and then you would be a published artist."
Ridership on transit systems across the country has been down the past half century, so could short stories save transit?
Trost thinks so.
"At the end of the day all transit agencies right now are doing everything they can to improve the rider experience. So I absolutely think we will get more riders just because of short stories," she says.
And you'll never be without something to read.

24. Why did BART start the kiosk program?""",
        "options": [
            "A. To promote the local culture.",
            "B. To discourage phone use.",
            "C. To meet passengers' needs.",
            "D. To reduce its running costs.",
        ],
        "answer": "C",
        "analysis": r"细节理解题。第一段指出许多人仍喜欢在车站等待或乘车时读纸质东西，BART 设打印亭正是为了满足这类乘客在旅途中阅读的需求，故选 C。A（推广当地文化）是后续征文活动的附带效果；B（阻止用手机）文中未提；D（降低运营成本）与文意相反。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "25",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "阅读理解",
        "kp_id": None,
        "difficulty": 1,
        "stem": r"""B
Do you ever get to the train station and realize you forgot to bring something to read? Yes, we all have our phones, but many of us still like to go old school and read something printed.
Well, there's a kiosk for that. In the San Francisco Bay Area, at least.
"You enter the fare gates and you'll see a kiosk that is lit up and it tells you can get a one-minute, a three-minute, or a five-minute story," says Alicia Trost, the chief communications officer for the San Francisco Bay Area Rapid Transit — known as BART. "You choose which length you want and it gives you a receipt-like short story."
It's that simple. Riders have printed nearly 20,000 short stories and poems since the program was launched last March. Some are classic short stories, and some are new original works.
Trost also wants to introduce local writers to local riders. "We wanted to do something where we do a call to artists in the Bay Area to submit stories for a contest," Trost says. "And as of right now, we've received about 120 submissions. The winning stories would go into our kiosk and then you would be a published artist."
Ridership on transit systems across the country has been down the past half century, so could short stories save transit?
Trost thinks so.
"At the end of the day all transit agencies right now are doing everything they can to improve the rider experience. So I absolutely think we will get more riders just because of short stories," she says.
And you'll never be without something to read.

25. How are the stories categorized in the kiosk?""",
        "options": [
            "A. By popularity.",
            "B. By length.",
            "C. By theme.",
            "D. By language.",
        ],
        "answer": "B",
        "analysis": r"细节理解题。由原文 \"a one-minute, a three-minute, or a five-minute story\" 与 \"You choose which length you want\" 可知，故事按时长（length）分类，故选 B。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "26",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "阅读理解",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""B
Do you ever get to the train station and realize you forgot to bring something to read? Yes, we all have our phones, but many of us still like to go old school and read something printed.
Well, there's a kiosk for that. In the San Francisco Bay Area, at least.
"You enter the fare gates and you'll see a kiosk that is lit up and it tells you can get a one-minute, a three-minute, or a five-minute story," says Alicia Trost, the chief communications officer for the San Francisco Bay Area Rapid Transit — known as BART. "You choose which length you want and it gives you a receipt-like short story."
It's that simple. Riders have printed nearly 20,000 short stories and poems since the program was launched last March. Some are classic short stories, and some are new original works.
Trost also wants to introduce local writers to local riders. "We wanted to do something where we do a call to artists in the Bay Area to submit stories for a contest," Trost says. "And as of right now, we've received about 120 submissions. The winning stories would go into our kiosk and then you would be a published artist."
Ridership on transit systems across the country has been down the past half century, so could short stories save transit?
Trost thinks so.
"At the end of the day all transit agencies right now are doing everything they can to improve the rider experience. So I absolutely think we will get more riders just because of short stories," she says.
And you'll never be without something to read.

26. What has Trost been doing recently?""",
        "options": [
            "A. Organizing a story contest.",
            "B. Doing a survey of customers.",
            "C. Choosing a print publisher.",
            "D. Conducting interviews with artists.",
        ],
        "answer": "A",
        "analysis": r"细节理解题。Trost 说 \"we do a call to artists ... to submit stories for a contest\" 且 \"we've received about 120 submissions\"，说明她近期在组织一个故事征文比赛（contest），故选 A。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "27",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "阅读理解",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""B
Do you ever get to the train station and realize you forgot to bring something to read? Yes, we all have our phones, but many of us still like to go old school and read something printed.
Well, there's a kiosk for that. In the San Francisco Bay Area, at least.
"You enter the fare gates and you'll see a kiosk that is lit up and it tells you can get a one-minute, a three-minute, or a five-minute story," says Alicia Trost, the chief communications officer for the San Francisco Bay Area Rapid Transit — known as BART. "You choose which length you want and it gives you a receipt-like short story."
It's that simple. Riders have printed nearly 20,000 short stories and poems since the program was launched last March. Some are classic short stories, and some are new original works.
Trost also wants to introduce local writers to local riders. "We wanted to do something where we do a call to artists in the Bay Area to submit stories for a contest," Trost says. "And as of right now, we've received about 120 submissions. The winning stories would go into our kiosk and then you would be a published artist."
Ridership on transit systems across the country has been down the past half century, so could short stories save transit?
Trost thinks so.
"At the end of the day all transit agencies right now are doing everything they can to improve the rider experience. So I absolutely think we will get more riders just because of short stories," she says.
And you'll never be without something to read.

27. What is Trost's opinion about BART's future?""",
        "options": [
            "A. It will close down.",
            "B. Its profits will decline.",
            "C. It will expand nationwide.",
            "D. Its ridership will increase.",
        ],
        "answer": "D",
        "analysis": r"推理判断题。Trost 说 \"I absolutely think we will get more riders just because of short stories\"，即她认为短时故事项目会带来更多乘客（ridership increase），故选 D。A/B 与文意相反；C（全国扩张）文中未提。",
        "points": [],
    },
    # ---- C 篇：Babylon Micro-Farm 室内种植系统 ----
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "28",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "阅读理解",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""C
We all know fresh is best when it comes to food. However, most produce at the store went through weeks of travel and covered hundreds of miles before reaching the table. While farmer's markets are a solid choice to reduce the journey, Babylon Micro-Farm (BMF) shortens it even more.
BMF is an indoor garden system. It can be set up for a family. Additionally, it could serve a larger audience such as a hospital, restaurant or school. The innovative design requires little effort to achieve a reliable weekly supply of fresh greens.
Specifically, it's a farm that relies on new technology. By connecting through the Cloud, BMF is remotely monitored. Also, there is a convenient app that provides growing data in real time. Because the system is automated, it significantly reduces the amount of water needed to grow plants. Rather than watering rows of soil, the system provides just the right amount to each plant. After harvest, users simply replace the plants with a new pre-seeded pod to get the next growth cycle started.
Moreover, having a system in the same building where it's eaten means zero emissions from transporting plants from soil to salad. In addition, there's no need for pesticides and other chemicals that pollute traditional farms and the surrounding environment.
BMF employees live out sustainability in their everyday lives. About half of them walk or bike to work. Inside the office, they encourage recycling and waste reduction by limiting garbage cans and avoiding single-use plastic. "We are passionate about reducing waste, carbon and chemicals in our environment," said a BMF employee.

28. What can be learned about BMF from paragraph 1?""",
        "options": [
            "A. It guarantees the variety of food.",
            "B. It requires day-to-day care.",
            "C. It cuts the farm-to-table distance.",
            "D. It relies on farmer's markets.",
        ],
        "answer": "C",
        "analysis": r"细节理解题。第一段说商店里的农产品要经过数周运输、数百英里才上桌，而 BMF \"shortens it even more\"，即缩短了从农场到餐桌的距离（farm-to-table distance），故选 C。A（保证食物多样）未提；B（需要日常照料）与 \"requires little effort\" 相反；D（依赖农贸市场）与 \"rather than farmer's markets\" 相反。",
        "points": [],
    },
    # ---- D 篇：AI by Design 书评 ----
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "35",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "阅读理解",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""D
Given the astonishing potential of AI to transform our lives, we all need to take action to deal with our AI-powered future, and this is where AI by Design: A Plan for Living with Artificial Intelligence comes in. This absorbing new book by Catriona Campbell is a practical roadmap addressing the challenges posed by the forthcoming AI revolution.
In the wrong hands, such a book could prove as complicated to process as the computer code that powers AI but, thankfully, Campbell has more than two decades' professional experience translating the heady into the understandable. She writes from the practical angle of a business person rather than as an academic, making for a guide which is highly accessible and informative and which, by the close, will make you feel almost as smart as AI.
As we soon come to learn from AI by Design, AI is already super-smart and will become more capable, moving from the current generation of "narrow-AI" to Artificial General Intelligence. From there, Campbell says, will come Artificial Dominant Intelligence. This is why Campbell has set out to raise awareness of AI and its future now — several decades before these developments are expected to take place. She says it is essential that we keep control of artificial intelligence, or risk being sidelined and perhaps even worse.
Campbell's point is to wake up those responsible for AI — the technology companies and world leaders — so they are on the same page as all the experts currently developing it. She explains we are at a "tipping point" in history and must act now to prevent an extinction-level event for humanity. We need to consider how we want our future with AI to pan out. Such structured thinking, followed by global regulation, will enable us to achieve greatness rather than our downfall.
AI will affect us all, and if you only read one book on the subject, this is it.

35. What is the author's purpose in writing the text?""",
        "options": [
            "A. To recommend a book on AI.",
            "B. To give a brief account of AI history.",
            "C. To clarify the definition of AI.",
            "D. To honor an outstanding AI expert.",
        ],
        "answer": "A",
        "analysis": r"主旨/写作意图题。全文围绕 Campbell 的新书 AI by Design 展开，介绍其内容、价值，并在末句说 \"if you only read one book on the subject, this is it\"，明显是为了推荐这本书，故选 A。B（简述 AI 历史）、C（澄清 AI 定义）、D（致敬专家）均非写作目的。",
        "points": [],
    },

    # ============ 二、完形填空（新高考II卷 2024） ============
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "41",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "完形填空",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""When I decided to buy a house in Europe ten years ago, I didn't think too long. I liked traveling in France, but when it came to picking my favorite spot to ___41___, Italy was the clear winner.
During my first visit to Italy, I ___42___ to ask for directions or order in a restaurant. But every time I tried to ___43___ a sentence of Italian together, the locals smiled at me and ___44___ my language skills. That encouragement helped me to get through the language ___45___. After I made Italy my permanent home, I discovered how ___46___ Italians are. Neighbors will bring me freshly made cheese and will come to my door to ___47___ me to close the window in my car when rain is coming. It's these small ___48___ of kindness that make a new country feel like home.
As a foodie, the way to my heart is through my stomach, and nowhere fuels my ___49___ quite like Italy. Each town has its own traditional ___50___, and every family keeps a recipe passed from one generation to another. Families ___51___ for big meals on Sundays, birthdays, and whatever other excuses they can ___52___. These meals are always ___53___ by laughter and joy. Whatever ___54___ life in Italy might have, the problems are ___55___ once you sit down to a big meal with friends and family.

41. A. study  B. rent  C. visit  D. settle""",
        "options": [
            "A. study",
            "B. rent",
            "C. visit",
            "D. settle",
        ],
        "answer": "D",
        "analysis": r"考查动词。前文说在欧洲买房、后文说把意大利当做永久的家（permanent home），可知此处指挑选最喜欢的地方\"定居\"，故选 D（settle）。A 学习、B 租、C 参观均不符合\"买房、安家\"语境。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "46",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "完形填空",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""When I decided to buy a house in Europe ten years ago, I didn't think too long. I liked traveling in France, but when it came to picking my favorite spot to ___41___, Italy was the clear winner.
During my first visit to Italy, I ___42___ to ask for directions or order in a restaurant. But every time I tried to ___43___ a sentence of Italian together, the locals smiled at me and ___44___ my language skills. That encouragement helped me to get through the language ___45___. After I made Italy my permanent home, I discovered how ___46___ Italians are. Neighbors will bring me freshly made cheese and will come to my door to ___47___ me to close the window in my car when rain is coming. It's these small ___48___ of kindness that make a new country feel like home.
As a foodie, the way to my heart is through my stomach, and nowhere fuels my ___49___ quite like Italy. Each town has its own traditional ___50___, and every family keeps a recipe passed from one generation to another. Families ___51___ for big meals on Sundays, birthdays, and whatever other excuses they can ___52___. These meals are always ___53___ by laughter and joy. Whatever ___54___ life in Italy might have, the problems are ___55___ once you sit down to a big meal with friends and family.

46. A. open-minded  B. strong-willed  C. warm-hearted  D. well-informed""",
        "options": [
            "A. open-minded",
            "B. strong-willed",
            "C. warm-hearted",
            "D. well-informed",
        ],
        "answer": "C",
        "analysis": r"考查形容词。后文列举邻居送自制奶酪、下雨提醒关车窗等善意举动，说明定居后作者发现意大利人十分\"热心/善良\"，故选 C（warm-hearted）。A 开明的、B 意志坚定的、D 见多识广的均不贴合\"邻里善意\"。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "51",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "完形填空",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""When I decided to buy a house in Europe ten years ago, I didn't think too long. I liked traveling in France, but when it came to picking my favorite spot to ___41___, Italy was the clear winner.
During my first visit to Italy, I ___42___ to ask for directions or order in a restaurant. But every time I tried to ___43___ a sentence of Italian together, the locals smiled at me and ___44___ my language skills. That encouragement helped me to get through the language ___45___. After I made Italy my permanent home, I discovered how ___46___ Italians are. Neighbors will bring me freshly made cheese and will come to my door to ___47___ me to close the window in my car when rain is coming. It's these small ___48___ of kindness that make a new country feel like home.
As a foodie, the way to my heart is through my stomach, and nowhere fuels my ___49___ quite like Italy. Each town has its own traditional ___50___, and every family keeps a recipe passed from one generation to another. Families ___51___ for big meals on Sundays, birthdays, and whatever other excuses they can ___52___. These meals are always ___53___ by laughter and joy. Whatever ___54___ life in Italy might have, the problems are ___55___ once you sit down to a big meal with friends and family.

51. A. gather  B. cheer  C. leave  D. wait""",
        "options": [
            "A. gather",
            "B. cheer",
            "C. leave",
            "D. wait",
        ],
        "answer": "A",
        "analysis": r"考查动词。由后文 \"a big meal with friends and family\" 可知，家人在周日、生日等场合会聚在一起（gather）吃大餐，故选 A。B 欢呼、C 离开、D 等待均不符合聚餐语境。",
        "points": [],
    },

    # ============ 三、七选五（新高考II卷 2024，过度旅游） ============
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "36",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "七选五",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""Overtourism Is For Real: How Can You Help
Travel promotes understanding, expands our minds, makes us better people, and boosts local economies and communities, but the rapid growth of travel has led to overtourism in certain regions and destinations. ___36___ Certainly not. The loss of what travel offers would be unacceptable in today's world. Here are some tips on making wise decisions to minimize pressure on the places we visit and improve our experience.
●Choose mindfully. Overvisited destinations are that way for a reason: they're special. With so many online posts featuring the same places, it's easy to feel like you're missing out. Go somewhere only when the landscape, culture or food deeply draws you. ___37___
●Get creative. The best way to ease pressure on over-touristed destinations is to go somewhere else. Though overtourism is described as a problem affecting the entire world, it's actually concentrated to a small number of extremely popular spots. That means you have tons of less-visited options to choose from. ___38___ Why not try a regional alternative or check out a popular destination's lesser-known sights?
●___39___ Minimize impact and maximize experience by skipping major holidays or rush hour. You'll compete with fewer tourists, save money, experience a different side of a popular place, and boost the economy when tourism is traditionally slower.
Visiting a place that others call home is a privilege. Do your part to preserve what makes a destination special in the first place. ___40___ You may be amazed how much closer you'll feel to the people there.

（本小题为第 36 空：从 options A–G 中选出应填入该空的一项）""",
        "options": [
            "A. Visit during off-peak times.",
            "B. So, should we stop traveling?",
            "C. Travel for you and no one else.",
            "D. Can overtourism be avoided then?",
            "E. You can still find relatively undiscovered places.",
            "F. You'll find yourself virtually alone, or close to it.",
            "G. Consider giving back to the communities you're visiting.",
        ],
        "answer": "B",
        "analysis": r"空格后 \"Certainly not.\" 是对一般疑问句的回答，且后句说失去旅行带来的好处不可接受，可推知空格处应为 \"那么我们该停止旅行吗？\"，故选 B。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "38",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "七选五",
        "kp_id": None,
        "difficulty": 3,
        "stem": r"""Overtourism Is For Real: How Can You Help
Travel promotes understanding, expands our minds, makes us better people, and boosts local economies and communities, but the rapid growth of travel has led to overtourism in certain regions and destinations. ___36___ Certainly not. The loss of what travel offers would be unacceptable in today's world. Here are some tips on making wise decisions to minimize pressure on the places we visit and improve our experience.
●Choose mindfully. Overvisited destinations are that way for a reason: they're special. With so many online posts featuring the same places, it's easy to feel like you're missing out. Go somewhere only when the landscape, culture or food deeply draws you. ___37___
●Get creative. The best way to ease pressure on over-touristed destinations is to go somewhere else. Though overtourism is described as a problem affecting the entire world, it's actually concentrated to a small number of extremely popular spots. That means you have tons of less-visited options to choose from. ___38___ Why not try a regional alternative or check out a popular destination's lesser-known sights?
●___39___ Minimize impact and maximize experience by skipping major holidays or rush hour. You'll compete with fewer tourists, save money, experience a different side of a popular place, and boost the economy when tourism is traditionally slower.
Visiting a place that others call home is a privilege. Do your part to preserve what makes a destination special in the first place. ___40___ You may be amazed how much closer you'll feel to the people there.

（本小题为第 38 空：从 options A–G 中选出应填入该空的一项）""",
        "options": [
            "A. Visit during off-peak times.",
            "B. So, should we stop traveling?",
            "C. Travel for you and no one else.",
            "D. Can overtourism be avoided then?",
            "E. You can still find relatively undiscovered places.",
            "F. You'll find yourself virtually alone, or close to it.",
            "G. Consider giving back to the communities you're visiting.",
        ],
        "answer": "E",
        "analysis": r"本段讲 \"Get creative\"，说过度旅游集中在少数热门地，因此\"你还有很多少有人去的选择\"，空格后 \"Why not try ... lesser-known sights\" 进一步建议探索冷门景点，故选 E（你仍能找到相对未被发现的地方）。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "40",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "七选五",
        "kp_id": None,
        "difficulty": 3,
        "stem": r"""Overtourism Is For Real: How Can You Help
Travel promotes understanding, expands our minds, makes us better people, and boosts local economies and communities, but the rapid growth of travel has led to overtourism in certain regions and destinations. ___36___ Certainly not. The loss of what travel offers would be unacceptable in today's world. Here are some tips on making wise decisions to minimize pressure on the places we visit and improve our experience.
●Choose mindfully. Overvisited destinations are that way for a reason: they're special. With so many online posts featuring the same places, it's easy to feel like you're missing out. Go somewhere only when the landscape, culture or food deeply draws you. ___37___
●Get creative. The best way to ease pressure on over-touristed destinations is to go somewhere else. Though overtourism is described as a problem affecting the entire world, it's actually concentrated to a small number of extremely popular spots. That means you have tons of less-visited options to choose from. ___38___ Why not try a regional alternative or check out a popular destination's lesser-known sights?
●___39___ Minimize impact and maximize experience by skipping major holidays or rush hour. You'll compete with fewer tourists, save money, experience a different side of a popular place, and boost the economy when tourism is traditionally slower.
Visiting a place that others call home is a privilege. Do your part to preserve what makes a destination special in the first place. ___40___ You may be amazed how much closer you'll feel to the people there.

（本小题为第 40 空：从 options A–G 中选出应填入该空的一项）""",
        "options": [
            "A. Visit during off-peak times.",
            "B. So, should we stop traveling?",
            "C. Travel for you and no one else.",
            "D. Can overtourism be avoided then?",
            "E. You can still find relatively undiscovered places.",
            "F. You'll find yourself virtually alone, or close to it.",
            "G. Consider giving back to the communities you're visiting.",
        ],
        "answer": "G",
        "analysis": r"本段首句说\"到别人称之为家的地方旅行是一种荣幸，要尽自己一份力保护当地特色\"，空格处应承接\"回馈当地社区\"，且 \"the communities\" 与后文 \"the people there\" 呼应，故选 G。",
        "points": [],
    },

    # ============ 四、语法填空（新高考II卷 2024，汤显祖与莎士比亚） ============
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "56",
        "source_ref": "https://zy.21cnjy.com/20856858",
        "verified": 1,
        "qtype": "语法填空",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""Chinese cultural elements commemorating Tang Xianzu, ___56___ is known as "the Shakespeare of Asia," add an international character to Stratford-upon-Avon, William Shakespeare's hometown. Tang and Shakespeare were contemporaries and both died in 1616. Although they could never have met, there are common ___57___ (theme) in their works, said Paul Edmondson, head of research for the Shakespeare Birthplace Trust. "Some of the things that Tang was writing about ___58___ (be) also Shakespeare's concerns. I happen to know that Tang's play The Peony Pavilion is similar in some ways ___59___ Romeo and Juliet." A statue commemorating Shakespeare and Tang was put up at Shakespeare's Birthplace Garden in 2017. Two years later, a six-meter-tall pavilion, ___60___ (inspire) by The Peony Pavilion, ___61___ (build) at the Firs Garden, just ten minutes' walk from Shakespeare's birthplace. Those cultural elements have increased Stratford's international ___62___ (visible), said Edmondson, adding that visitors walking through the Birthplace Garden were often amazed ___63___ (find) the connection between the two great writers. ___64___ (recall) watching a Chinese opera version of Shakespeare's play Richard III in Shanghai and meeting Chinese actors who came to Stratford a few years ago to perform parts of The Peony Pavilion, Edmondson said, "It was very exciting to hear the Chinese language ___65___ see how Tang's play was being performed."

（第 56 空：填入适当的关系词）""",
        "options": [],
        "answer": "who",
        "analysis": r"考查非限制性定语从句。逗号后 \"___ is known as 'the Shakespeare of Asia'\" 修饰先行词 Tang Xianzu（人），在从句中作主语，故用关系代词 who。",
        "points": [
            r"识别逗号后为非限制性定语从句，先行词指人且在从句中作主语",
            r"关系代词用 who（不可用 that，非限制性定语从句不用 that）",
        ],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "61",
        "source_ref": "https://zy.21cnjy.com/20856858",
        "verified": 1,
        "qtype": "语法填空",
        "kp_id": None,
        "difficulty": 3,
        "stem": r"""Chinese cultural elements commemorating Tang Xianzu, ___56___ is known as "the Shakespeare of Asia," add an international character to Stratford-upon-Avon, William Shakespeare's hometown. Tang and Shakespeare were contemporaries and both died in 1616. Although they could never have met, there are common ___57___ (theme) in their works, said Paul Edmondson, head of research for the Shakespeare Birthplace Trust. "Some of the things that Tang was writing about ___58___ (be) also Shakespeare's concerns. I happen to know that Tang's play The Peony Pavilion is similar in some ways ___59___ Romeo and Juliet." A statue commemorating Shakespeare and Tang was put up at Shakespeare's Birthplace Garden in 2017. Two years later, a six-meter-tall pavilion, ___60___ (inspire) by The Peony Pavilion, ___61___ (build) at the Firs Garden, just ten minutes' walk from Shakespeare's birthplace. Those cultural elements have increased Stratford's international ___62___ (visible), said Edmondson, adding that visitors walking through the Birthplace Garden were often amazed ___63___ (find) the connection between the two great writers. ___64___ (recall) watching a Chinese opera version of Shakespeare's play Richard III in Shanghai and meeting Chinese actors who came to Stratford a few years ago to perform parts of The Peony Pavilion, Edmondson said, "It was very exciting to hear the Chinese language ___65___ see how Tang's play was being performed."

（第 61 空：用括号内词 build 的正确形式填空）""",
        "options": [],
        "answer": "was built",
        "analysis": r"考查谓语动词的时态与被动语态。主语 a six-meter-tall pavilion 与 build 之间为被动关系，且动作发生在过去（Two years later，相对于 2017 年），故用一般过去时被动语态 was built。",
        "points": [
            r"判断 pavilion 与 build 为被动关系（被建造）",
            r"时间状语 Two years later（2017 之后）提示一般过去时",
            r"答案为 was built",
        ],
    },

    # ============ 五、书面表达（新高考II卷 2024） ============
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "应用文(第一节)",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "作文",
        "kp_id": None,
        "difficulty": 2,
        "stem": r"""第一节（满分 15 分）
假定你是李华，上周五你们班在公园上了一堂美术课。请你给英国朋友 Chris 写一封邮件分享这次经历，内容包括：
（1）你完成的作品；
（2）你的感想。
注意：
（1）写作词数应为 80 个左右；
（2）请按如下格式在答题卡的相应位置作答。

Dear Chris,
I'm writing to share with you an art class I had in a park last Friday.
________________________________________________________________________________
________________________________________________________________________________

Yours,
Li Hua""",
        "options": [],
        "answer": r"""Dear Chris,
I'm writing to share with you an art class I had in a park last Friday. I painted a serene landscape of the park, capturing the vibrant colors of the flowers and the tranquil atmosphere. It was a refreshing experience to create art surrounded by nature's beauty. The rustling of leaves and the chirping of birds added to the peaceful ambiance, inspiring my creativity. Overall, it was a memorable and enjoyable art session that allowed me to connect with both my surroundings and my artistic expression.
Yours,
Li Hua""",
        "analysis": r"应用文（邮件分享）。要点：① 完成的作品——可写一幅公园风景画，点出色彩/自然氛围；② 感想——亲近自然、放松身心、激发创意、难忘等。词数约 80，语气亲切，书信格式正确。范文参考 21 世纪教育网真题文档所附参考范文。已双源核对（21 世纪教育网真题原卷、人人文库/学科网 2024 新课标Ⅱ卷英语原卷转录，题干设问与所给格式一致）。",
        "points": [
            r"书信格式：开头 Dear Chris，结尾 Yours, Li Hua（框架已给出，须保持一致）",
            r"要点1：描述完成的作品（如 a serene landscape / 公园风景画），包含色彩、自然氛围等细节",
            r"要点2：表达感想（亲近自然、放松、有创意、难忘 memorable 等）",
            r"词数 80 左右；语言简洁、时态以一般过去时为主",
        ],
    },
    {
        "year": 2024,
        "paper": "新高考II卷",
        "question_no": "读后续写(第二节)",
        "source_ref": "https://zy.21cnjy.com/20658767",
        "verified": 1,
        "qtype": "作文",
        "kp_id": None,
        "difficulty": 4,
        "stem": r"""第二节（满分 25 分）
阅读下面材料，根据其内容和所给段落开头语续写两段，使之构成一篇完整的短文。
I met Gunter on a cold, wet and unforgettable evening in September. I had planned to fly to Vienna and take a bus to Prague for a conference. Due to a big storm, my flight had been delayed by an hour and a half. I touched down in Vienna just 30 minutes before the departure of the last bus to Prague. The moment I got off the plane, I ran like crazy through the airport building and jumped into the first taxi on the rank without a second thought.
That was when I met Gunter. I told him where I was going, but he said he hadn't heard of the bus station. I thought my pronunciation was the problem, so I explained again more slowly, but he still looked confused. When I was about to give up, Gunter fished out his little phone and rang up a friend. After a heated discussion that lasted for what seemed like a century, Gunter put his phone down and started the car.
Finally, with just two minutes to spare we rolled into the bus station. Thankfully, there was a long queue still waiting to board the bus. Gunter parked the taxi behind the bus, turned around, and looked at me with a big smile on his face. "We made it," he said.
Just then I realised that I had zero cash in my wallet. I flashed him an apologetic smile as I pulled out my Portuguese bankcard. He tried it several times, but the card machine just did not play along. A feeling of helplessness washed over me as I saw the bus queue thinning out.
At this moment, Gunter pointed towards the waiting hall of the bus station. There, at the entrance, was a cash machine. I jumped out of the car, made a mad run for the machine, and popped my card in, only to read the message: "Out of order. Sorry."

注意：
（1）续写词数应为 150 个左右；
（2）请按如下格式在答题卡的相应位置作答。

I ran back to Gunter and told him the bad news.
________________________________________________________________________________
________________________________________________________________________________

Four days later, when I was back in Vienna, I called Gunter as promised.
________________________________________________________________________________
________________________________________________________________________________""",
        "options": [],
        "answer": r"""续写要点（参考，非官方范文）：
第一段（I ran back to Gunter and told him the bad news.）：告知 ATM 故障取不出钱；Gunter 摆手表示不必担心/让“我”先上车赶巴士，体现他的善良与信任；在班车即将发车之际“我”上车，并承诺日后偿还/致谢。
第二段（Four days later...）：从维也纳回电 Gunter，表达感谢并归还车费；Gunter 爽快接受或叙旧；点题——陌生人的善意与信任让“我”难忘，呼应首段 "unforgettable evening"。

两段应连贯、人称一致（第一人称 I），时态以一般过去时为主，词数约 150。""",
        "analysis": r"读后续写。原文讲述“我”在维也纳赶往布拉格的晚间误打误撞坐上 Gunter 的出租车，到站后却发现无现金、ATM 故障。第一段应从“跑回去告诉 Gunter 坏消息”起，写 Gunter 的宽容/信任与“我”得以登车；第二段从“四天后回维也纳致电 Gunter”起，写还钱致谢与主题升华。注意与段首语衔接、情节合理、语言连贯。所给为续写要点。已双源核对（21 世纪教育网真题原卷、人人文库 2024 新课标Ⅱ卷英语原卷转录，原文五段文字与两段段首语逐句一致）。",
        "points": [
            r"第一段：告知 ATM 取不出钱；Gunter 的反应（摆手/让先赶车）凸显善良与信任；我上车前致谢并承诺偿还",
            r"第二段：四天后从维也纳回电致谢并归还车费；Gunter 爽快接受/叙旧；点题陌生人的善意与信任，呼应 unforgettable",
            r"连贯性：两段衔接自然，与所给段首语无缝对接",
            r"语言：第一人称 I，一般过去时为主；词数约 150；避免抄袭原文过多",
        ],
    },
]
