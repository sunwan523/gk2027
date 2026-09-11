# -*- coding: utf-8 -*-
"""知识依赖图。

对应重构方案 5.4 节。这张图的核心价值是跨学科依赖：

    物理·电场   依赖 数学·向量分解 + 数学·函数图像
    化学·化学平衡 依赖 数学·对数 + 化学·物质的量
    化学·电化学  依赖 化学·氧化还原 + 物理·电路
    生物·遗传计算 依赖 数学·概率 + 生物·减数分裂
    物理·动量守恒 依赖 数学·方程组 + 物理·牛顿定律

界面只显示"前置全部满足"的节点，因此永远不会出现"打开书发现看不懂，
因为前面有个东西没学"——这是自学者最常见的卡死原因。

⚠️ 在 90 天一轮的节奏下（方案 4.1），依赖图的准确性至关重要：
   一轮过去没有回头路，若顺序错误，漏洞会固化。
"""
from __future__ import annotations

import sqlite3
from collections import deque
from typing import Iterable, Sequence

from config import JUNIOR_PASS_MASTERY, SENIOR_PASS_MASTERY
from core import db


# ----------------------------------------------------------------------
# 节点定义：(id, 学科, 层级, 名称, 权重, 预计学时, [前置依赖])
# ----------------------------------------------------------------------
# 权重说明：'高频考点' 出题密度最高，'常规' 标准，'低频' 可后置。
# 层级说明：初中层为诊断优先（先测后学），高中层为系统学习。

KNOWLEDGE_GRAPH: list[tuple] = [
    # ================= 数学 · 初中层（诊断优先）=================
    ("mat_jr_num",      "数学", "初中", "实数与运算",        "高频考点", 4, []),
    ("mat_jr_alg",      "数学", "初中", "整式与因式分解",    "高频考点", 5, ["mat_jr_num"]),
    ("mat_jr_frac",     "数学", "初中", "分式与二次根式",    "高频考点", 4, ["mat_jr_alg"]),
    ("mat_jr_eq",       "数学", "初中", "方程与不等式",      "高频考点", 6, ["mat_jr_frac"]),
    ("mat_jr_func1",    "数学", "初中", "一次函数与反比例函数", "高频考点", 5, ["mat_jr_eq"]),
    ("mat_jr_quad",     "数学", "初中", "二次函数",          "高频考点", 6, ["mat_jr_func1"]),
    ("mat_jr_geo",      "数学", "初中", "平面几何基础",      "常规",     6, ["mat_jr_eq"]),
    ("mat_jr_sim",      "数学", "初中", "相似与三角函数初步", "高频考点", 5, ["mat_jr_geo"]),
    ("mat_jr_circle",   "数学", "初中", "圆",                "常规",     4, ["mat_jr_sim"]),
    ("mat_jr_stat",     "数学", "初中", "统计与概率基础",    "高频考点", 4, ["mat_jr_eq"]),

    # ================= 数学 · 高中 =================
    ("mat_set",         "数学", "高中必修", "集合与常用逻辑用语", "高频考点", 3, ["mat_jr_num"]),
    ("mat_func",        "数学", "高中必修", "函数概念与性质",   "高频考点", 8, ["mat_jr_quad", "mat_set"]),
    ("mat_exp_log",     "数学", "高中必修", "指数函数与对数函数", "高频考点", 6, ["mat_func"]),
    ("mat_trig",        "数学", "高中必修", "三角函数",         "高频考点", 8, ["mat_jr_sim", "mat_func"]),
    ("mat_trig_id",     "数学", "高中必修", "三角恒等变换",     "高频考点", 4, ["mat_trig"]),
    ("mat_vector",      "数学", "高中必修", "平面向量",         "高频考点", 6, ["mat_trig", "mat_func"]),
    ("mat_vector_dec",  "数学", "高中必修", "向量的分解与坐标运算", "高频考点", 4, ["mat_vector"]),
    ("mat_seq",         "数学", "高中必修", "数列",             "高频考点", 8, ["mat_func"]),
    ("mat_ineq",        "数学", "高中必修", "不等式与线性规划", "常规",     4, ["mat_jr_eq", "mat_func"]),
    ("mat_solid",       "数学", "高中必修", "立体几何",         "高频考点", 8, ["mat_jr_geo", "mat_vector_dec"]),
    ("mat_line_eq",     "数学", "高中必修", "直线与方程",       "高频考点", 5, ["mat_jr_func1", "mat_vector_dec"]),
    ("mat_circle_eq",   "数学", "高中必修", "圆与方程",         "高频考点", 4, ["mat_line_eq", "mat_jr_circle"]),
    ("mat_conic",       "数学", "高中选择性", "椭圆与双曲线",   "高频考点", 8, ["mat_circle_eq"]),
    ("mat_parabola",    "数学", "高中选择性", "抛物线",         "高频考点", 4, ["mat_conic"]),
    ("mat_space_vec",   "数学", "高中选择性", "空间向量与立体几何", "高频考点", 6, ["mat_solid", "mat_vector_dec"]),
    ("mat_count",       "数学", "高中选择性", "计数原理与二项式定理", "高频考点", 5, ["mat_jr_stat"]),
    ("mat_prob",        "数学", "高中选择性", "概率",           "高频考点", 6, ["mat_count"]),
    ("mat_stat2",       "数学", "高中选择性", "统计与回归",     "常规",     4, ["mat_prob"]),
    ("mat_deriv",       "数学", "高中选择性", "导数及其应用",   "高频考点", 10, ["mat_func", "mat_ineq"]),
    ("mat_complex",     "数学", "高中必修", "复数",             "常规",     2, ["mat_jr_num"]),
    ("mat_solve_tri",   "数学", "高中必修", "解三角形",         "高频考点", 4, ["mat_trig_id", "mat_vector"]),
    ("mat_eq_sys",      "数学", "高中必修", "方程组与消元",     "高频考点", 3, ["mat_jr_eq"]),

    # ================= 物理 · 初中层 =================
    ("phy_jr_mech",     "物理", "初中", "初中力学基础",   "高频考点", 5, ["mat_jr_num"]),
    ("phy_jr_motion",   "物理", "初中", "运动和力",       "高频考点", 5, ["phy_jr_mech"]),
    ("phy_jr_pressure", "物理", "初中", "压强与浮力",     "常规",     4, ["phy_jr_motion"]),
    ("phy_jr_work",     "物理", "初中", "功和机械能",     "高频考点", 4, ["phy_jr_motion"]),
    ("phy_jr_circuit",  "物理", "初中", "电流和电路",     "高频考点", 4, ["mat_jr_eq"]),
    ("phy_jr_ohm",      "物理", "初中", "欧姆定律",       "高频考点", 5, ["phy_jr_circuit"]),
    ("phy_jr_power",    "物理", "初中", "电功率",         "高频考点", 4, ["phy_jr_ohm"]),
    ("phy_jr_magnet",   "物理", "初中", "电与磁",         "常规",     3, ["phy_jr_ohm"]),
    ("phy_jr_light",    "物理", "初中", "光现象",         "常规",     3, ["mat_jr_geo"]),
    ("phy_jr_heat",     "物理", "初中", "热现象",         "低频",     2, ["mat_jr_num"]),

    # ================= 物理 · 高中 =================
    ("phy_kinematics",  "物理", "高中必修", "匀变速直线运动", "高频考点", 6, ["phy_jr_motion", "mat_jr_quad"]),
    ("phy_force",       "物理", "高中必修", "受力分析",       "高频考点", 6, ["phy_jr_motion", "mat_vector_dec"]),
    ("phy_newton2",     "物理", "高中必修", "牛顿运动定律",   "高频考点", 8, ["phy_force", "phy_kinematics"]),
    ("phy_curve",       "物理", "高中必修", "曲线运动",       "高频考点", 6, ["phy_newton2"]),
    ("phy_gravity",     "物理", "高中必修", "万有引力与航天", "高频考点", 5, ["phy_curve"]),
    ("phy_work_power",  "物理", "高中必修", "功和功率",       "高频考点", 5, ["phy_newton2", "mat_vector_dec"]),
    ("phy_energy",      "物理", "高中必修", "动能定理与机械能守恒", "高频考点", 8, ["phy_work_power"]),
    ("phy_momentum",    "物理", "高中必修", "动量守恒定律",   "高频考点", 6, ["mat_eq_sys", "phy_newton2"]),
    ("phy_efield",      "物理", "高中选择性", "电场",         "高频考点", 8, ["phy_energy", "mat_vector_dec", "mat_func"]),
    ("phy_circuit",     "物理", "高中选择性", "电路",         "高频考点", 6, ["phy_jr_ohm", "phy_jr_power"]),
    ("phy_bfield",      "物理", "高中选择性", "磁场",         "高频考点", 7, ["phy_efield", "phy_jr_magnet"]),
    ("phy_emind",       "物理", "高中选择性", "电磁感应",     "高频考点", 8, ["phy_bfield", "phy_energy"]),
    ("phy_complex_field","物理","高中选择性", "带电粒子在复合场中的运动", "高频考点", 8, ["phy_efield", "phy_bfield", "phy_energy"]),
    ("phy_ac",          "物理", "高中选择性", "交变电流",     "常规",     4, ["phy_emind", "mat_trig"]),
    ("phy_wave",        "物理", "高中选择性", "机械振动与机械波", "常规",   5, ["mat_trig", "phy_kinematics"]),
    ("phy_optics",      "物理", "高中选择性", "光学",         "常规",     4, ["phy_jr_light", "phy_wave"]),
    ("phy_thermal",     "物理", "高中选择性", "热学",         "低频",     4, ["phy_jr_heat"]),
    ("phy_modern",      "物理", "高中选择性", "近代物理初步", "常规",     4, ["phy_optics"]),
    # 实验是独立命题板块（方案核查后补）：力学实验←运动学/受力，电学实验←电路
    ("phy_experiment",  "物理", "高中必修", "物理实验（打点/平行四边形/测电动势内阻）", "高频考点", 6,
     ["phy_kinematics", "phy_force", "phy_circuit"]),

    # ================= 化学 · 初中层 =================
    ("che_jr_matter",   "化学", "初中", "物质的变化和性质", "高频考点", 3, ["mat_jr_num"]),
    ("che_jr_atom",     "化学", "初中", "原子结构与元素",   "高频考点", 4, ["che_jr_matter"]),
    ("che_jr_formula",  "化学", "初中", "化学式与化合价",   "高频考点", 4, ["che_jr_atom"]),
    ("che_jr_equation", "化学", "初中", "化学方程式与配平", "高频考点", 5, ["che_jr_formula"]),
    ("che_jr_solution", "化学", "初中", "水与溶液",         "高频考点", 4, ["che_jr_equation"]),
    ("che_jr_acid",     "化学", "初中", "酸碱盐基础",       "高频考点", 5, ["che_jr_solution"]),
    ("che_jr_metal",    "化学", "初中", "金属与金属活动性", "常规",     3, ["che_jr_acid"]),

    # ================= 化学 · 高中 =================
    ("che_mole",        "化学", "高中必修", "物质的量",       "高频考点", 8, ["che_jr_equation", "mat_jr_frac"]),
    ("che_ion",         "化学", "高中必修", "离子反应",       "高频考点", 5, ["che_mole", "che_jr_acid"]),
    ("che_redox",       "化学", "高中必修", "氧化还原反应",   "高频考点", 6, ["che_ion"]),
    ("che_periodic",    "化学", "高中必修", "元素周期律与周期表", "高频考点", 5, ["che_jr_atom", "che_redox"]),
    ("che_bond",        "化学", "高中必修", "化学键",         "高频考点", 4, ["che_periodic"]),
    ("che_energy_rxn",  "化学", "高中必修", "化学反应与能量", "高频考点", 5, ["che_redox", "phy_work_power"]),
    ("che_rate",        "化学", "高中选择性", "化学反应速率", "高频考点", 5, ["che_mole", "mat_deriv"]),
    ("che_equilibrium", "化学", "高中选择性", "化学平衡",     "高频考点", 8, ["che_rate", "mat_exp_log"]),
    ("che_ionization",  "化学", "高中选择性", "弱电解质的电离", "高频考点", 5, ["che_equilibrium"]),
    ("che_ph",          "化学", "高中选择性", "水的电离与溶液酸碱性", "高频考点", 5, ["che_ionization", "mat_exp_log"]),
    ("che_hydrolysis",  "化学", "高中选择性", "盐类水解",     "高频考点", 5, ["che_ph"]),
    ("che_ksp",         "化学", "高中选择性", "沉淀溶解平衡", "高频考点", 4, ["che_hydrolysis"]),
    ("che_battery",     "化学", "高中选择性", "原电池",       "高频考点", 5, ["che_redox", "phy_circuit"]),
    ("che_electrolysis","化学", "高中选择性", "电解池",       "高频考点", 5, ["che_battery"]),
    ("che_corrosion",   "化学", "高中选择性", "金属腐蚀与防护", "常规",   3, ["che_electrolysis", "che_jr_metal"]),
    ("che_organic_alk", "化学", "高中选择性", "烃（烷烯炔芳香烃）", "高频考点", 6, ["che_bond"]),
    ("che_organic_func","化学", "高中选择性", "烃的衍生物（卤代烃醇酚醛羧酸酯）", "高频考点", 8, ["che_organic_alk"]),
    ("che_biomol",      "化学", "高中选择性", "糖类蛋白质与高分子", "常规",   4, ["che_organic_func"]),
    ("che_experiment",  "化学", "高中必修", "化学实验基础",   "高频考点", 6, ["che_mole", "che_ion"]),
    ("che_infer",       "化学", "高中必修", "常见无机物推断", "高频考点", 5, ["che_redox", "che_periodic"]),
    ("che_calc",        "化学", "高中选择性", "化学综合计算", "高频考点", 6, ["che_mole", "che_equilibrium", "che_ph"]),
    # 选择性必修2 物质结构与性质：云南卷"结构大题"独立命题（电子排布/晶体/晶胞计算）
    ("che_structure",   "化学", "高中选择性", "原子结构与核外电子排布", "高频考点", 5,
     ["che_jr_atom", "che_periodic"]),
    ("che_crystal",     "化学", "高中选择性", "分子间作用力与晶体类型（晶胞计算）", "高频考点", 6,
     ["che_bond", "che_structure"]),
    ("che_coordination","化学", "高中选择性", "配合物与杂化轨道、空间构型", "高频考点", 5,
     ["che_structure", "mat_jr_geo"]),
    ("che_element_metal","化学","高中必修","金属元素化合物（钠铝铁铜）","高频考点",8,
     ["che_redox","che_periodic","che_jr_metal"]),
    ("che_element_nonmetal","化学","高中必修","非金属元素化合物（硅氯硫氮）","高频考点",8,
     ["che_redox","che_periodic"]),
    ("che_experiment_adv","化学","高中必修","化学实验综合（制备/分离/检验/滴定）","高频考点",8,
     ["che_experiment","che_element_metal","che_element_nonmetal"]),

    # ================= 生物 · 初中层 =================
    ("bio_jr_cell",     "生物", "初中", "初中细胞结构",     "高频考点", 3, ["che_jr_matter"]),
    ("bio_jr_digest",   "生物", "初中", "人体消化系统",     "常规",     3, ["bio_jr_cell"]),
    ("bio_jr_resp",     "生物", "初中", "人体呼吸系统",     "常规",     2, ["bio_jr_cell"]),
    ("bio_jr_circ",     "生物", "初中", "人体循环系统",     "常规",     3, ["bio_jr_cell"]),
    ("bio_jr_urin",     "生物", "初中", "人体泌尿系统",     "常规",     2, ["bio_jr_cell"]),
    ("bio_jr_nerve",    "生物", "初中", "人体神经系统",     "高频考点", 3, ["bio_jr_cell"]),
    ("bio_jr_hormone",  "生物", "初中", "人体激素调节",     "高频考点", 3, ["bio_jr_nerve"]),
    ("bio_jr_heredity", "生物", "初中", "生物的遗传和变异", "高频考点", 4, ["bio_jr_cell"]),
    ("bio_jr_eco",      "生物", "初中", "生物多样性与生态", "常规",     3, ["bio_jr_cell"]),
    ("bio_jr_microbe",  "生物", "初中", "微生物",           "常规",     2, ["bio_jr_cell"]),

    # ================= 生物 · 高中 =================
    ("bio_molecule",    "生物", "高中必修", "组成细胞的元素和化合物", "高频考点", 5, ["bio_jr_cell", "che_jr_matter"]),
    ("bio_protein",     "生物", "高中必修", "蛋白质结构与功能", "高频考点", 5, ["bio_molecule"]),
    ("bio_nucleic",     "生物", "高中必修", "核酸的结构与功能", "高频考点", 4, ["bio_molecule"]),
    ("bio_membrane",    "生物", "高中必修", "细胞膜与物质跨膜运输", "高频考点", 5, ["bio_protein"]),
    ("bio_organelle",   "生物", "高中必修", "细胞器的结构与功能", "高频考点", 4, ["bio_membrane"]),
    ("bio_nucleus",     "生物", "高中必修", "细胞核与细胞增殖", "高频考点", 6, ["bio_nucleic", "bio_organelle"]),
    ("bio_enzyme",      "生物", "高中必修", "酶与ATP",        "高频考点", 4, ["bio_protein"]),
    ("bio_resp",        "生物", "高中必修", "细胞呼吸",       "高频考点", 6, ["bio_enzyme", "bio_organelle"]),
    ("bio_photo",       "生物", "高中必修", "光合作用",       "高频考点", 6, ["bio_resp"]),
    ("bio_meiosis",     "生物", "高中必修", "减数分裂与受精作用", "高频考点", 6, ["bio_nucleus"]),
    ("bio_dna_struct",  "生物", "高中必修", "DNA分子结构与复制", "高频考点", 5, ["bio_nucleic"]),
    ("bio_gene_expr",   "生物", "高中必修", "基因的表达",     "高频考点", 5, ["bio_dna_struct"]),
    ("bio_mendel",      "生物", "高中必修", "孟德尔遗传定律", "高频考点", 8, ["bio_meiosis", "mat_prob"]),
    ("bio_sex_link",    "生物", "高中必修", "伴性遗传",       "高频考点", 5, ["bio_mendel", "bio_gene_expr"]),
    ("bio_mutation",    "生物", "高中必修", "基因突变与染色体变异", "高频考点", 5, ["bio_dna_struct", "bio_meiosis"]),
    ("bio_breeding",    "生物", "高中必修", "育种",           "高频考点", 4, ["bio_mutation", "bio_mendel"]),
    ("bio_evolution",   "生物", "高中必修", "现代生物进化理论", "常规",   4, ["bio_mendel", "mat_prob"]),
    ("bio_homeostasis", "生物", "高中必修", "人体内环境与稳态", "高频考点", 4, ["bio_jr_circ", "bio_jr_urin"]),
    ("bio_neuro",       "生物", "高中必修", "神经调节",       "高频考点", 6, ["bio_membrane", "bio_jr_nerve"]),
    ("bio_humoral",     "生物", "高中必修", "体液调节",       "高频考点", 5, ["bio_homeostasis", "bio_jr_hormone"]),
    ("bio_immune",      "生物", "高中必修", "免疫调节",       "高频考点", 6, ["bio_humoral"]),
    ("bio_plant_hormone","生物","高中必修", "植物生命活动的调节", "高频考点", 5, ["bio_humoral", "bio_photo"]),
    ("bio_population",  "生物", "高中选择性", "种群和群落",   "高频考点", 5, ["bio_evolution", "mat_stat2"]),
    ("bio_ecosystem",   "生物", "高中选择性", "生态系统结构与功能", "高频考点", 6, ["bio_population", "bio_photo"]),
    ("bio_eco_protect", "生物", "高中选择性", "生态保护",     "常规",     2, ["bio_ecosystem"]),
    ("bio_gene_eng",    "生物", "高中选择性", "基因工程",     "高频考点", 5, ["bio_gene_expr", "bio_mutation"]),
    ("bio_cell_eng",    "生物", "高中选择性", "细胞工程与胚胎工程", "常规",   4, ["bio_nucleus", "bio_gene_eng"]),
    # 选择性必修3 生物技术实践：微生物培养/无菌技术/计数筛选，高考必考实验专题
    ("bio_biotech",     "生物", "高中选择性", "生物技术实践（微生物培养与发酵）", "高频考点", 5,
     ["bio_jr_microbe", "bio_resp"]),

    # ================= 语文 =================
    ("chn_dictation",   "语文", "高中必修", "名句名篇默写",       "高频考点", 8, []),
    ("chn_wenyan_word", "语文", "高中必修", "文言文实词",         "高频考点", 8, []),
    ("chn_wenyan_func", "语文", "高中必修", "文言文虚词",         "高频考点", 5, ["chn_wenyan_word"]),
    ("chn_wenyan_sent", "语文", "高中必修", "文言文特殊句式与翻译", "高频考点", 6, ["chn_wenyan_func"]),
    ("chn_wenyan_punc", "语文", "高中必修", "文言文断句与文化常识", "常规",     4, ["chn_wenyan_sent"]),
    ("chn_poem_image",  "语文", "高中必修", "古诗词鉴赏·意象与意境", "高频考点", 4, ["chn_wenyan_word"]),
    ("chn_poem_tech",   "语文", "高中必修", "古诗词鉴赏·表达技巧", "高频考点", 4, ["chn_poem_image"]),
    ("chn_poem_emotion","语文", "高中必修", "古诗词鉴赏·情感与炼字", "高频考点", 4, ["chn_poem_tech"]),
    ("chn_read_argue",  "语文", "高中必修", "现代文阅读·论述类文本", "高频考点", 6, []),
    ("chn_read_lit",    "语文", "高中必修", "现代文阅读·文学类文本", "高频考点", 6, []),
    ("chn_read_prac",   "语文", "高中必修", "现代文阅读·实用类文本", "高频考点", 4, []),
    ("chn_lang_word",   "语文", "高中必修", "语言文字运用·字音字形成语", "高频考点", 5, []),
    ("chn_lang_sick",   "语文", "高中必修", "语言文字运用·病句辨析", "高频考点", 4, ["chn_lang_word"]),
    ("chn_lang_cohere", "语文", "高中必修", "语言文字运用·语句衔接与表达得体", "常规", 4, ["chn_lang_sick"]),
    ("chn_essay_topic", "语文", "高中必修", "作文·审题立意",      "高频考点", 6, []),
    ("chn_essay_argue", "语文", "高中必修", "作文·议论文写作",    "高频考点", 10, ["chn_essay_topic"]),
    ("chn_essay_material","语文","高中必修", "作文·素材积累与运用", "高频考点", 8, ["chn_essay_argue"]),
    ("chn_whole_book",  "语文", "高中必修", "整本书阅读（乡土中国/红楼梦）", "高频考点", 6, ["chn_read_argue"]),

    # ================= 英语 =================
    ("eng_vocab",       "英语", "高中必修", "高考核心词汇3500",   "高频考点", 40, []),
    ("eng_grammar_base","英语", "高中必修", "语法体系·时态与语态", "高频考点", 8, ["eng_vocab"]),
    ("eng_grammar_nonp","英语", "高中必修", "语法体系·非谓语动词", "高频考点", 5, ["eng_grammar_base"]),
    ("eng_grammar_clau","英语", "高中必修", "语法体系·三大从句",  "高频考点", 6, ["eng_grammar_base"]),
    ("eng_grammar_adv", "英语", "高中必修", "语法体系·虚拟语气倒装强调", "常规", 4, ["eng_grammar_clau"]),
    ("eng_grammar_modal","英语", "高中必修", "语法体系·情态动词与主谓一致", "高频考点", 4, ["eng_grammar_base"]),
    ("eng_grammar_other","英语", "高中必修", "语法体系·冠词代词介词与形副词", "高频考点", 5, ["eng_grammar_base"]),
    ("eng_read",        "英语", "高中必修", "阅读理解",           "高频考点", 15, ["eng_vocab", "eng_grammar_clau"]),
    ("eng_seven_five",  "英语", "高中必修", "七选五（补全短文）", "高频考点", 4, ["eng_read"]),
    ("eng_cloze",       "英语", "高中必修", "完形填空",           "高频考点", 8, ["eng_read"]),
    ("eng_grammar_fill","英语", "高中必修", "语法填空",           "高频考点", 5, ["eng_grammar_adv"]),
    ("eng_write_apply", "英语", "高中必修", "写作·应用文",        "高频考点", 8, ["eng_vocab"]),
    ("eng_write_cont",  "英语", "高中必修", "写作·读后续写",      "高频考点", 10, ["eng_write_apply"]),
    ("eng_listening",   "英语", "高中必修", "听力",               "高频考点", 10, ["eng_vocab"]),
]


def seed_graph(conn: sqlite3.Connection, *, reset: bool = False) -> dict[str, int]:
    """写入依赖图。幂等：已存在的节点只更新元数据，不覆盖学习状态。"""
    ids = {row[0] for row in KNOWLEDGE_GRAPH}
    inserted = updated = 0
    for kp_id, subject, tier, name, weight, hours, requires in KNOWLEDGE_GRAPH:
        bad = [r for r in requires if r not in ids]
        if bad:
            raise ValueError("节点 %s 引用了不存在的前置：%s" % (kp_id, bad))
        cur = conn.execute("SELECT id FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
        if cur:
            conn.execute(
                "UPDATE knowledge_points SET subject=?, tier=?, name=?, weight=?, est_hours=? "
                "WHERE id=?", (subject, tier, name, weight, hours, kp_id))
            updated += 1
        else:
            conn.execute(
                "INSERT INTO knowledge_points(id, subject, tier, name, weight, est_hours, status)"
                " VALUES(?,?,?,?,?,?,?)",
                (kp_id, subject, tier, name, weight, hours, "未解锁"))
            inserted += 1

    if reset:
        conn.execute("DELETE FROM kp_requires")
    for kp_id, *_rest, requires in KNOWLEDGE_GRAPH:
        for r in requires:
            conn.execute(
                "INSERT OR IGNORE INTO kp_requires(kp_id, requires_id) VALUES(?,?)", (kp_id, r))
    conn.commit()
    refresh_unlock(conn)
    return {"inserted": inserted, "updated": updated, "edges": count_edges(conn)}


def count_edges(conn: sqlite3.Connection) -> int:
    return int(conn.execute("SELECT COUNT(*) FROM kp_requires").fetchone()[0])


# ----------------------------------------------------------------------
# 解锁逻辑
# ----------------------------------------------------------------------
def pass_threshold(tier: str) -> float:
    """初中层 75% 放行，高中层 60%（方案 4.1：初中不追求 100%）。"""
    return JUNIOR_PASS_MASTERY if tier == "初中" else SENIOR_PASS_MASTERY


def prerequisites(conn: sqlite3.Connection, kp_id: str) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT k.* FROM knowledge_points k JOIN kp_requires r ON r.requires_id=k.id "
        "WHERE r.kp_id=? ORDER BY k.subject, k.id", (kp_id,)).fetchall()


def is_unlocked(conn: sqlite3.Connection, kp_id: str) -> bool:
    """前置全部达到放行阈值，该节点才可学。

    初中层节点一律视为已解锁（六科同时起步，诊断优先，不被跨科依赖阻塞）。
    滚动任务（eng_vocab/chn_dictation）永远视为满足：它们无自检题、
    掌握度不更新，若参与阻塞会把整个英语/语文分支永久锁死（2026-09-12 修）。
    """
    tier = conn.execute("SELECT tier FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
    if tier and tier["tier"] == "初中":
        return True
    blocked = conn.execute(
        "SELECT COUNT(*) FROM kp_requires r JOIN knowledge_points k ON k.id=r.requires_id "
        "WHERE r.kp_id=? AND k.mastery < CASE WHEN k.tier='初中' THEN ? ELSE ? END "
        "AND k.id NOT IN ('eng_vocab','chn_dictation')",
        (kp_id, JUNIOR_PASS_MASTERY, SENIOR_PASS_MASTERY)).fetchone()[0]
    return blocked == 0


def refresh_unlock(conn: sqlite3.Connection) -> int:
    """重算全图解锁状态。返回本次新解锁的节点数。"""
    rows = conn.execute("SELECT id, tier, status, mastery FROM knowledge_points").fetchall()
    newly = 0
    for r in rows:
        ok = is_unlocked(conn, r["id"])
        new_status = r["status"]
        if ok and r["status"] == "未解锁":
            new_status = "可学"
            newly += 1
        elif not ok and r["status"] in ("可学",):
            new_status = "未解锁"
        if new_status != r["status"]:
            conn.execute("UPDATE knowledge_points SET status=? WHERE id=?", (new_status, r["id"]))
    conn.commit()
    return newly


def available_nodes(conn: sqlite3.Connection, subject: str | None = None) -> list[sqlite3.Row]:
    """今天可以学什么——只显示前置已满足的节点（方案 5.4）。"""
    sql = "SELECT * FROM knowledge_points WHERE status IN ('可学','学习中','需复习')"
    args: list = []
    if subject:
        sql += " AND subject=?"
        args.append(subject)
    sql += (" ORDER BY CASE weight WHEN '高频考点' THEN 0 WHEN '常规' THEN 1 ELSE 2 END,"
            " tier, subject")
    return conn.execute(sql, args).fetchall()


def blocked_nodes(conn: sqlite3.Connection, subject: str | None = None) -> list[dict]:
    """被阻塞的节点及其缺失的前置，用于自查依赖图是否合理。"""
    sql = "SELECT * FROM knowledge_points WHERE status='未解锁'"
    args: list = []
    if subject:
        sql += " AND subject=?"; args.append(subject)
    out = []
    for r in conn.execute(sql, args):
        missing = conn.execute(
            "SELECT k.id, k.name, k.subject, k.mastery FROM kp_requires r "
            "JOIN knowledge_points k ON k.id=r.requires_id "
            "WHERE r.kp_id=? AND k.mastery < CASE WHEN k.tier='初中' THEN ? ELSE ? END",
            (r["id"], JUNIOR_PASS_MASTERY, SENIOR_PASS_MASTERY)).fetchall()
        if missing:
            out.append({"node": dict(r), "missing": [dict(m) for m in missing]})
    return out


# ----------------------------------------------------------------------
# 掌握度计算
# ----------------------------------------------------------------------
def update_mastery(conn: sqlite3.Connection, kp_id: str) -> float:
    """按该节点下题目的加权正确率 × 覆盖率计算掌握度。

    权重设计（对应方案 4.3）：
      - 近期作答权重更高（遗忘曲线）
      - 难度越高的题，答对贡献越大
      - 覆盖率 = 已作答的不同题数 / 该节点总题数。做对一题≠掌握：
        只答过一半题目时，掌握度最多一半。（旧版按"作答次数<3 打五折"，
        但手机课程模式下多数节点只有 2—3 题，会导致永远达不到放行线、
        后继永久锁死——2026-09-11 改为覆盖率缩放。）
    """
    rows = conn.execute(
        "SELECT a.correct, a.done_at, q.difficulty FROM attempts a "
        "JOIN questions q ON q.id=a.question_id WHERE q.kp_id=? "
        "ORDER BY a.done_at DESC LIMIT 40", (kp_id,)).fetchall()
    if not rows:
        mastery = 0.0
    else:
        num = den = 0.0
        for i, r in enumerate(rows):
            recency = 1.0 / (1.0 + 0.15 * i)          # 越新权重越高
            diff_w = 0.6 + 0.2 * int(r["difficulty"] or 3)
            w = recency * diff_w
            num += w * (1.0 if r["correct"] else 0.0)
            den += w
        accuracy = num / den if den else 0.0
        answered = conn.execute(
            "SELECT COUNT(DISTINCT a.question_id) FROM attempts a "
            "JOIN questions q ON q.id=a.question_id WHERE q.kp_id=?",
            (kp_id,)).fetchone()[0]
        total_q = conn.execute(
            "SELECT COUNT(*) FROM questions WHERE kp_id=?", (kp_id,)).fetchone()[0]
        coverage = min(1.0, answered / total_q) if total_q else 1.0
        mastery = accuracy * coverage

    tier = conn.execute("SELECT tier, status FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
    if tier:
        status = tier["status"]
        if mastery >= pass_threshold(tier["tier"]):
            status = "已掌握" if mastery >= 0.85 else "学习中"
        elif status == "已掌握":
            status = "需复习"
        conn.execute(
            "UPDATE knowledge_points SET mastery=?, status=? WHERE id=?",
            (round(mastery, 4), status, kp_id))
    else:
        conn.execute("UPDATE knowledge_points SET mastery=? WHERE id=?", (round(mastery, 4), kp_id))
    conn.commit()
    return round(mastery, 4)


def refresh_all_mastery(conn: sqlite3.Connection) -> None:
    for r in conn.execute("SELECT id FROM knowledge_points"):
        update_mastery(conn, r["id"])
    refresh_unlock(conn)


def detect_cycles(conn: sqlite3.Connection) -> list[str]:
    """环检测。依赖图出现环会导致永久阻塞，必须能在录入时发现。"""
    edges: dict[str, list[str]] = {}
    nodes: set[str] = set()
    for r in conn.execute("SELECT id FROM knowledge_points"):
        nodes.add(r["id"]); edges.setdefault(r["id"], [])
    for r in conn.execute("SELECT kp_id, requires_id FROM kp_requires"):
        nodes.add(r["kp_id"]); nodes.add(r["requires_id"])
        edges.setdefault(r["kp_id"], []).append(r["requires_id"])

    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in nodes}
    cyclic: list[str] = []

    def dfs(u: str, stack: list[str]) -> None:
        color[u] = GRAY
        stack.append(u)
        for v in edges.get(u, []):
            if color.get(v) == GRAY:
                idx = stack.index(v) if v in stack else -1
                cyclic.append(" -> ".join(stack[idx:] + [v]) if idx >= 0 else "%s -> %s" % (u, v))
            elif color.get(v, WHITE) == WHITE:
                dfs(v, stack)
        stack.pop()
        color[u] = BLACK

    for n in sorted(nodes):
        if color[n] == WHITE:
            dfs(n, [])
    return cyclic


def topological_order(conn: sqlite3.Connection, subject: str | None = None) -> list[sqlite3.Row]:
    """按依赖顺序返回学习路径（Kahn 算法）。"""
    rows = conn.execute(
        "SELECT * FROM knowledge_points" + (" WHERE subject=?" if subject else ""),
        (subject,) if subject else ()).fetchall()
    ids = {r["id"] for r in rows}
    indeg = {i: 0 for i in ids}
    graph: dict[str, list[str]] = {i: [] for i in ids}
    for r in conn.execute("SELECT kp_id, requires_id FROM kp_requires"):
        a, b = r["kp_id"], r["requires_id"]
        if a in ids and b in ids:
            graph[b].append(a)
            indeg[a] += 1
    q = deque(sorted(i for i in ids if indeg[i] == 0))
    order: list[str] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(graph[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    by_id = {r["id"]: r for r in rows}
    return [by_id[i] for i in order if i in by_id]


def cross_subject_dependencies(conn: sqlite3.Connection) -> list[dict]:
    """列出所有跨学科依赖，便于核对（方案 5.4 的重点）。"""
    rows = conn.execute(
        "SELECT k.id AS kid, k.name AS kname, k.subject AS ksub, "
        "r.id AS rid, r.name AS rname, r.subject AS rsub "
        "FROM kp_requires e JOIN knowledge_points k ON k.id=e.kp_id "
        "JOIN knowledge_points r ON r.id=e.requires_id WHERE k.subject <> r.subject "
        "ORDER BY k.subject, k.id").fetchall()
    return [dict(r) for r in rows]


def graph_summary(conn: sqlite3.Connection) -> list[dict]:
    out = []
    for r in conn.execute(
            "SELECT subject, tier, COUNT(*) AS n, ROUND(AVG(mastery),3) AS avg_mastery, "
            "SUM(CASE WHEN status='已掌握' THEN 1 ELSE 0 END) AS mastered, "
            "SUM(CASE WHEN status='可学' THEN 1 ELSE 0 END) AS available, "
            "SUM(est_hours) AS hours "
            "FROM knowledge_points GROUP BY subject, tier ORDER BY subject, tier"):
        out.append(dict(r))
    return out
