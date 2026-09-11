# -*- coding: utf-8 -*-
"""全局配置。

设计原则（对应重构方案 5.7 节）：
- 考试日期可配置，所有日程从考试日动态反推，杜绝旧项目硬编码 datetime(2026,5,8) 的问题。
- PDF 字体：正文用微软雅黑（msyh），化学/数学特殊符号（⇌ ₂ ₃ ⁻ ⊗ 等）
  实测雅黑与宋体均缺失，必须靠 Segoe UI Symbol（seguisym）内联回退。
  此项已经过 charToGlyph 实测验证，stringWidth 检查是假阳性，勿再依赖。
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date

# --------------------------------------------------------------------------
# 路径
# --------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "gk2027.db")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")          # 生成的训练包 PDF
IMAGE_DIR = os.path.join(DATA_DIR, "images")            # 几何图/电路图/结构图

for _d in (DATA_DIR, OUTPUT_DIR, IMAGE_DIR):
    os.makedirs(_d, exist_ok=True)

# --------------------------------------------------------------------------
# 考试日期与节奏（方案 4.1 / 4.2 节）
# --------------------------------------------------------------------------
EXAM_DATE = date(2027, 6, 7)          # 云南 2027 高考首日
TODAY_OVERRIDE: date | None = None    # 仅测试用；生产环境保持 None

# 基础期天数。默认 90（方案 4.1），须由第 4—10 天诊断测试实测结果覆盖：
#   物理真题 >=50 分 -> 90    35-49 分 -> 110    <35 分 -> 140
FOUNDATION_DAYS_DEFAULT = 90

# 初中层放行阈值（方案 4.1：掌握度 75% 即放行，不追求 100%）
JUNIOR_PASS_MASTERY = 0.75
# 高中层放行阈值
SENIOR_PASS_MASTERY = 0.60

# --------------------------------------------------------------------------
# 目标分（方案 3.4 双 A 版）
# --------------------------------------------------------------------------
SUBJECTS = ["语文", "数学", "英语", "物理", "化学", "生物"]

TARGET_SCORES = {
    "语文": 120, "数学": 128, "英语": 122,
    "物理": 85, "化学": 90, "生物": 92,
}
TARGET_TOTAL = sum(TARGET_SCORES.values())   # 637
GOAL_SCORE = 600                             # 对外显示目标
AIM_SCORE = 615                              # 内部瞄准值（抗通胀）

# 化学/生物训练盯卷面分，不盯赋分等级（方案 3.3）
RAW_SCORE_TARGETS = {"化学": 92, "生物": 94}

# 计分方式：scaled = 等级赋分, raw = 原始分
SCORING = {
    "语文": "raw", "数学": "raw", "英语": "raw",
    "物理": "raw", "化学": "scaled", "生物": "scaled",
}

# 考试时长（分钟）——云南 3+1+2 实际安排
EXAM_DURATION = {
    "语文": 150, "数学": 120, "英语": 120,
    "物理": 75, "化学": 75, "生物": 75,
}
EXAM_FULL_MARK = {
    "语文": 150, "数学": 150, "英语": 150,
    "物理": 100, "化学": 100, "生物": 100,
}

# --------------------------------------------------------------------------
# 里程碑（方案 4.4：评估结果用于纠偏，不用于降级目标）
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Milestone:
    day: int          # 距考试日还有多少天时触发
    label: str
    targets: dict     # 科目 -> 目标分；空 dict 表示非分数型里程碑

    @property
    def on_date(self) -> date:
        from datetime import timedelta
        return EXAM_DATE - timedelta(days=self.day)


MILESTONES = [
    Milestone(260, "诊断完成", {}),
    Milestone(180, "一轮结束·章节测试平均≥60%", {}),
    Milestone(110, "单科实测", {"数学": 105, "物理": 68, "化学": 78, "生物": 82}),
    Milestone(50, "全真模考", {"总分": 560}),
    Milestone(20, "全真模考", {"总分": 600}),
]

# --------------------------------------------------------------------------
# 关键行政日期（方案 4.5）
# --------------------------------------------------------------------------
ADMIN_DEADLINES = [
    (date(2026, 9, 17), "色觉自查（一票否决项，与分数无关）"),
    (date(2026, 9, 17), "联系户籍地招考办确认往届生报名资格与材料"),
    (date(2026, 11, 10), "云南高考报名（往年 11 月上旬，以官方通知为准）"),
    (date(2027, 3, 10), "高考体检（色觉结论正式生效）"),
    (EXAM_DATE, "高考 6月7—9日"),
]

# --------------------------------------------------------------------------
# PDF 字体（勿改为宋体，理由见文件头）
# --------------------------------------------------------------------------
FONT_REGULAR = ("msyh", r"C:\Windows\Fonts\msyh.ttc", 0)
FONT_BOLD = ("msyhbd", r"C:\Windows\Fonts\msyhbd.ttc", 0)

# --------------------------------------------------------------------------
# 来源类型（方案 5.3：AI 生成题永不带年份卷别）
# --------------------------------------------------------------------------
SOURCE_TYPES = ("真题", "教辅录入", "自主命题练习", "AI生成")
SOURCES_ALLOWING_YEAR = ("真题",)

# 六类归因（方案 4.3 / 5.5）
ATTRIBUTIONS = (
    "概念不清", "方法未掌握", "计算失误",
    "审题偏差", "时间不够", "表述不规范",
)

# --------------------------------------------------------------------------
def today() -> date:
    return TODAY_OVERRIDE or date.today()


def days_to_exam() -> int:
    return (EXAM_DATE - today()).days


def exam_day_index() -> int:
    """已过天数，从备考第 1 天开始计。"""
    start = EXAM_DATE - total_plan_days()
    return (today() - start).days + 1


def total_plan_days() -> int:
    from datetime import timedelta
    return (EXAM_DATE - (EXAM_DATE - timedelta(days=FOUNDATION_DAYS_DEFAULT + 180))).days


def foundation_days() -> int:
    """实际基础期天数，可被诊断结果写入数据库覆盖。"""
    return FOUNDATION_DAYS_DEFAULT


# --------------------------------------------------------------------------
# 服务访问地址
# --------------------------------------------------------------------------
SERVER_PORT = 8577
# 外网访问地址（域名/端口映射），出门在外用这个访问；局域网用 _lan_ip() 自动获取
PUBLIC_URL = "http://p.mhtc.top:8577"
