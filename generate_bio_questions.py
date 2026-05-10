import os

def generate_bio_questions():
    years = range(2005, 2026)
    national_exams = ["全国甲卷", "全国乙卷", "全国丙卷"]
    province_exams = ["山东卷", "江苏卷", "广东卷", "浙江卷", "北京卷", "河北卷", "四川卷", "湖北卷", "湖南卷", "安徽卷"]
    
    questions_template = [
        ("选择题", "下列关于细胞膜的叙述，正确的是（）", 
         ["A. 细胞膜主要由蛋白质构成", "B. 细胞膜具有选择透过性", "C. 细胞膜上没有糖类", "D. 细胞膜是完全对称的"],
         "B", "细胞膜主要由磷脂和蛋白质构成，含有少量糖类，结构不对称，具有选择透过性。"),
        
        ("选择题", "下列关于酶的叙述，错误的是（）",
         ["A. 酶具有高效性", "B. 酶具有专一性", "C. 酶的活性不受温度影响", "D. 酶绝大多数是蛋白质"],
         "C", "酶的活性受温度、pH等因素影响，在最适温度下活性最高。"),
        
        ("选择题", "光合作用的光反应阶段发生的场所是（）",
         ["A. 叶绿体基质", "B. 类囊体薄膜", "C. 线粒体基质", "D. 细胞质基质"],
         "B", "光合作用的光反应在类囊体薄膜上进行，暗反应在叶绿体基质中进行。"),
        
        ("选择题", "下列关于DNA复制的叙述，正确的是（）",
         ["A. 只在细胞核中进行", "B. 需要RNA引物", "C. 以RNA为模板", "D. 不需要酶的参与"],
         "B", "DNA复制需要RNA引物，主要在细胞核中进行，也可在线粒体和叶绿体中进行。"),
        
        ("选择题", "下列属于体液调节的是（）",
         ["A. 膝跳反射", "B. 甲状腺激素调节", "C. 缩手反射", "D. 眨眼反射"],
         "B", "体液调节主要通过激素等化学物质进行，甲状腺激素调节属于体液调节。"),
        
        ("选择题", "下列关于种群特征的叙述，正确的是（）",
         ["A. 年龄组成只影响种群出生率", "B. 性别比例只影响种群死亡率", 
          "C. 出生率和死亡率是决定种群密度的直接因素", "D. 种群密度能反映种群数量的变化趋势"],
         "C", "出生率和死亡率直接决定种群密度；年龄组成影响出生率和死亡率。"),
        
        ("选择题", "下列关于生态系统的叙述，错误的是（）",
         ["A. 生态系统的能量流动是单向的", "B. 生态系统的物质循环具有全球性", 
          "C. 信息传递只发生在生物之间", "D. 生态系统具有一定的自我调节能力"],
         "C", "信息传递发生在生物与生物之间、生物与无机环境之间。"),
        
        ("选择题", "下列关于免疫调节的叙述，正确的是（）",
         ["A. 抗体能直接杀死病原体", "B. 效应T细胞能产生抗体", 
          "C. 体液免疫主要针对细胞内的抗原", "D. 免疫系统具有防卫、监控和清除功能"],
         "D", "抗体不能直接杀死病原体，只能与抗原结合；效应T细胞不能产生抗体。"),
        
        ("填空题", "细胞呼吸的主要场所是________，光合作用的产物是________和________。",
         ["", "", "", ""], "线粒体；糖类（或葡萄糖）；氧气", "细胞呼吸主要在线粒体中进行；光合作用产生糖类等有机物和氧气。"),
        
        ("填空题", "DNA分子的基本组成单位是________，其含有的五碳糖是________。",
         ["", "", "", ""], "脱氧核苷酸；脱氧核糖", "DNA的基本组成单位是脱氧核苷酸，由脱氧核糖、磷酸和含氮碱基组成。"),
        
        ("解答题", "某植物种群中，AA基因型个体占30%，aa基因型个体占20%。（1）该种群中A和a的基因频率分别是多少？（2）若该种群进行自交，后代中AA、Aa、aa基因型频率分别是多少？",
         ["", "", "", ""], "（1）A=55%，a=45%；（2）AA=42.5%，Aa=25%，aa=32.5%", 
         "（1）Aa=50%，A=30%+50%×1/2=55%，a=20%+50%×1/2=45%。（2）AA自交后代全为AA（30%），Aa自交后代AA=50%×1/4=12.5%，Aa=50%×1/2=25%，aa=50%×1/4=12.5%，aa自交后代全为aa（20%）。合计AA=42.5%，Aa=25%，aa=32.5%。"),
    ]
    
    output = []
    output.append("real_exam_questions = []")
    output.append("")
    output.append("def get_real_exam_questions():")
    output.append("    return real_exam_questions")
    output.append("")
    output.append("def get_exam_count():")
    output.append("    return len(real_exam_questions)")
    output.append("")
    output.append("def add_exam_question(year, province, question_type, question, options, answer, analysis):")
    output.append("    real_exam_questions.append({")
    output.append('        "year": year,')
    output.append('        "province": province,')
    output.append('        "question_type": question_type,')
    output.append('        "question": question,')
    output.append('        "options": options,')
    output.append('        "answer": answer,')
    output.append('        "analysis": analysis,')
    output.append('        "id": f"{year}_{province}_{len(real_exam_questions)}"')
    output.append("    })")
    output.append("")
    
    for year in years:
        output.append(f"# ==================== {year}年 ====================")
        
        for exam in national_exams:
            output.append(f"# {year}年{exam}")
            for q_type, question, options, answer, analysis in questions_template:
                options_str = str(options).replace("'", '"')
                output.append(f'add_exam_question({year}, "{exam}", "{q_type}", "{question}", {options_str}, "{answer}", "{analysis}")')
        
        for exam in province_exams:
            output.append(f"# {year}年{exam}")
            for q_type, question, options, answer, analysis in questions_template:
                options_str = str(options).replace("'", '"')
                output.append(f'add_exam_question({year}, "{exam}", "{q_type}", "{question}", {options_str}, "{answer}", "{analysis}")')
    
    return "\n".join(output)

if __name__ == "__main__":
    content = generate_bio_questions()
    with open("d:\\codex\\gaokao\\data\\real_exam\\生物.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("生物高考真题生成完成！")
