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

add_exam_question(2024, "全国甲卷", "选择题", "下列物质中，属于电解质的是（）", ["A. 蔗糖", "B. 氯化钠", "C. 酒精", "D. 铜"], "B", "电解质是在水溶液中或熔融状态下能导电的化合物。氯化钠是离子化合物，溶于水可导电，是电解质。")
add_exam_question(2024, "全国乙卷", "选择题", "下列反应中，属于氧化还原反应的是（）", ["A. CaCO₃ → CaO + CO₂", "B. NaOH + HCl → NaCl + H₂O", "C. Fe + CuSO₄ → FeSO₄ + Cu", "D. AgNO₃ + NaCl → AgCl↓ + NaNO₃"], "C", "C项中铁元素化合价从0变为+2，铜元素从+2变为0，有电子转移，是氧化还原反应。")
add_exam_question(2023, "全国甲卷", "选择题", "下列关于原子结构的说法，正确的是（）", ["A. 原子核由质子和电子组成", "B. 质子数决定元素种类", "C. 核外电子数等于中子数", "D. 原子的质量主要集中在核外电子"], "B", "原子核由质子和中子组成；质子数决定元素种类；原子质量主要集中在原子核。")
add_exam_question(2023, "全国乙卷", "选择题", "下列离子方程式书写正确的是（）", ["A. 铁与稀硫酸反应：2Fe + 6H⁺ → 2Fe³⁺ + 3H₂↑", "B. 氢氧化钡与稀硫酸反应：Ba²⁺ + SO₄²⁻ → BaSO₄↓", "C. 碳酸钙与盐酸反应：CaCO₃ + 2H⁺ → Ca²⁺ + CO₂↑ + H₂O", "D. 氯化铁溶液与氢氧化钠溶液反应：Fe³⁺ + 3OH⁻ → Fe(OH)₃"], "C", "A项铁与稀硫酸反应生成Fe²⁺；B项漏掉OH⁻与H⁺的反应；D项Fe(OH)₃是沉淀需标↓。")
add_exam_question(2022, "全国甲卷", "选择题", "下列说法正确的是（）", ["A. 酸性：H₂CO₃ > HClO", "B. 碱性：NaOH < Mg(OH)₂", "C. 稳定性：H₂S > H₂O", "D. 还原性：Cl⁻ > Br⁻"], "A", "碳酸酸性强于次氯酸；NaOH碱性强于Mg(OH)₂；H₂O稳定性强于H₂S；Br⁻还原性强于Cl⁻。")
add_exam_question(2024, "全国甲卷", "选择题", "下列关于化学平衡的说法正确的是（）", ["A. 化学平衡是动态平衡", "B. 达到平衡时，正反应速率为零", "C. 达到平衡时，各物质浓度相等", "D. 达到平衡时，各物质浓度不再变化"], "A", "化学平衡是动态平衡，正逆反应速率相等但不为零，各物质浓度保持不变但不一定相等。")
add_exam_question(2024, "全国乙卷", "选择题", "设Nₐ为阿伏加德罗常数的值，下列说法正确的是（）", ["A. 1mol H₂O中含有的质子数为10Nₐ", "B. 常温常压下，22.4L CO₂含有的分子数为Nₐ", "C. 1mol/L NaCl溶液中含有的Na⁺数目为Nₐ", "D. 1mol Fe与足量稀盐酸反应转移的电子数为3Nₐ"], "A", "1个H₂O分子含10个质子；常温常压下22.4L不是1mol；未给出溶液体积无法计算；Fe与稀盐酸反应生成Fe²⁺，转移2Nₐ电子。")
add_exam_question(2023, "新课标I卷", "选择题", "下列物质中，既能与酸反应又能与碱反应的是（）", ["A. Al₂O₃", "B. Fe₂O₃", "C. CuO", "D. CaO"], "A", "Al₂O₃是两性氧化物，既能与酸反应又能与碱反应。")
add_exam_question(2023, "新课标II卷", "选择题", "下列关于化学反应速率的说法正确的是（）", ["A. 反应速率与反应物浓度无关", "B. 温度升高，反应速率一定加快", "C. 催化剂只能加快反应速率", "D. 反应速率可以用单位时间内反应物浓度的变化来表示"], "D", "反应速率与浓度有关；温度升高反应速率通常加快；催化剂可加快或减慢反应速率。")
add_exam_question(2022, "北京卷", "选择题", "下列实验操作正确的是（）", ["A. 用嘴吹灭酒精灯", "B. 将实验剩余药品放回原瓶", "C. 加热时试管口对着自己", "D. 取用固体药品用药匙"], "D", "不能用嘴吹灭酒精灯；剩余药品不能放回原瓶；加热时试管口不能对着人。")