# -*- coding: utf-8 -*-
"""A4 纸质训练包生成器。

对应重构方案 2.3 / 5.1 / 5.2 / 5.7 节。

学习发生在纸上，软件只负责排程、生成、归因。你有大复印机，打印成本为零，
所以系统输出的核心形态就是 A4 PDF。

⚠️ 字体：正文用微软雅黑（msyh / msyhbd），但实测雅黑与宋体均缺失
   ⇌（可逆符号）、₂ ₃（下标）、⁻ ⁺（上标正负号）、⊗、₀ ₁ 等符号。
   这些字符必须内联回退到 Segoe UI Symbol（seguisym），
   否则化学方程式与物理向量印出来是空白方块（方案标记的最大单点风险）。
   判定用 charToGlyph，勿用 stringWidth——缺失字形宽度仍为正，是假阳性。

六种训练包（方案 5.2）：
   A 碎片记忆包  5—15min   默写/词汇/公式/概念/方程式   看店间隙
   B 唤醒包      15—20min  单知识点 10—15 题            短空隙
   C 专项包      30—40min  单章节 20—25 题              整块空隙
   D 错题重做包  20—30min  间隔重复抽取                 每天必做
   E 限时套卷    75/120/150min 全真模拟+答题卡           打烊后/周日
   F 表述规范包  20min     主观题对照教材原文改写        练习期第二轮起
"""
from __future__ import annotations

import os
from datetime import date, datetime
from typing import Any, Iterable, Sequence

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, Image,
                               KeepTogether, PageBreak, PageTemplate,
                               Paragraph, Spacer, Table, TableStyle)

from config import (EXAM_DURATION, EXAM_FULL_MARK, FONT_BOLD, FONT_DIR,
                    FONT_REGULAR, IMAGE_DIR, OUTPUT_DIR, SUBJECTS)
from core import db, srs

_FONTS_READY = False
# msyh 未覆盖、需回退到 seguisym 的字符集合（ensure_fonts 计算）。
# 上一会话误判"雅黑全覆盖"：stringWidth 对缺失字形仍返回默认宽度，是假阳性。
# 实测 charToGlyph：雅黑缺 ⇌ ₂ ₃ ⁻ ⁺ ⊗ ₀ ₁ 等；Segoe UI Symbol 全覆盖。
_FALLBACK_CHARS: frozenset[str] = frozenset()

# 数学/化学/生物常用记号，用于计算回退集合（覆盖不到的才回退）。
_SYMBOL_PROBE = (
    "⇌₂₃⁻⁺₀₁₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⊗√∝∞≈≠≤≥±×÷→←↑↓"
    "ΔαβγθλμξπρστφωΩ′″℃"
)


def ensure_fonts() -> tuple[str, str]:
    """注册中文字体与符号回退字体。返回 (常规体名, 粗体名)。"""
    global _FONTS_READY, _FALLBACK_CHARS
    if _FONTS_READY:
        return FONT_REGULAR[0], FONT_BOLD[0]
    for name, path, idx in (FONT_REGULAR, FONT_BOLD):
        if not os.path.exists(path):
            raise RuntimeError("字体文件缺失：%s。PDF 无法保证符号完整渲染。" % path)
        try:
            pdfmetrics.registerFont(TTFont(name, path, subfontIndex=idx))
        except Exception:
            pdfmetrics.registerFont(TTFont(name, path))
    # 符号回退字体：Segoe UI Symbol 覆盖雅黑缺失的 ⇌ ₂ ₃ ⁻ ⊗ 等。
    fallback_path = os.path.join(FONT_DIR, "seguisym.ttf")
    if os.path.exists(fallback_path):
        pdfmetrics.registerFont(TTFont("seguisym", fallback_path))
        sym = TTFont("seguisym_probe", fallback_path).face.charToGlyph
        main = TTFont(FONT_REGULAR[0], FONT_REGULAR[1],
                      subfontIndex=FONT_REGULAR[2]).face.charToGlyph
        _FALLBACK_CHARS = frozenset(
            ch for ch in _SYMBOL_PROBE
            if not (ord(ch) in main and main[ord(ch)] != 0)
            and (ord(ch) in sym and sym[ord(ch)] != 0)
        )
    _FONTS_READY = True
    return FONT_REGULAR[0], FONT_BOLD[0]


REG, BOLD = "msyh", "msyhbd"


def _styles() -> dict[str, ParagraphStyle]:
    ensure_fonts()
    return {
        "title": ParagraphStyle("title", fontName=BOLD, fontSize=17, leading=24,
                                alignment=TA_CENTER, spaceAfter=2),
        "subtitle": ParagraphStyle("subtitle", fontName=REG, fontSize=9.5, leading=14,
                                   alignment=TA_CENTER, textColor=colors.HexColor("#555555")),
        "source_warn": ParagraphStyle("source_warn", fontName=BOLD, fontSize=9.5, leading=14,
                                      alignment=TA_CENTER, textColor=colors.HexColor("#b00020")),
        "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=12.5, leading=19,
                             spaceBefore=8, spaceAfter=3),
        "h3": ParagraphStyle("h3", fontName=BOLD, fontSize=11, leading=17,
                             spaceBefore=6, spaceAfter=2),
        "body": ParagraphStyle("body", fontName=REG, fontSize=10.5, leading=17),
        "stem": ParagraphStyle("stem", fontName=REG, fontSize=10.5, leading=17.5,
                               spaceBefore=5, spaceAfter=2),
        "option": ParagraphStyle("option", fontName=REG, fontSize=10.5, leading=16.5,
                                 leftIndent=6*mm),
        "blank": ParagraphStyle("blank", fontName=REG, fontSize=10.5, leading=22,
                                leftIndent=6*mm),
        "analysis": ParagraphStyle("analysis", fontName=REG, fontSize=9.5, leading=15,
                                   textColor=colors.HexColor("#333333")),
        "answer": ParagraphStyle("answer", fontName=BOLD, fontSize=10, leading=16),
        "small": ParagraphStyle("small", fontName=REG, fontSize=8.5, leading=12.5,
                                textColor=colors.HexColor("#666666")),
        "box": ParagraphStyle("box", fontName=REG, fontSize=9.5, leading=15),
    }


PACK_META = {
    "A": ("碎片记忆包", "5—15 分钟", "看店间隙｜默写·词汇·公式·概念·方程式"),
    "B": ("唤醒包", "15—20 分钟", "短空隙｜单知识点 10—15 题，基础+中档"),
    "C": ("专项包", "30—40 分钟", "整块空隙｜单章节 20—25 题，中档为主"),
    "D": ("错题重做包", "20—30 分钟", "每天必做｜间隔重复算法抽取"),
    "E": ("限时套卷", "75/120/150 分钟", "打烊后或周日｜全真模拟，配答题卡"),
    "F": ("表述规范包", "20 分钟", "赋分科目专用｜对照教材原文逐句改写"),
    "CALC": ("限时计算训练", "15 分钟", "归因=计算失误｜只练准确度，不是难题"),
    "READ": ("审题训练包", "15 分钟", "归因=审题偏差｜圈画关键词后再作答"),
    "TIME": ("取舍策略训练", "30 分钟", "归因=时间不够｜限时抢分，练放弃"),
}


def esc(text: str) -> str:
    """XML 转义 + 符号字体回退。

    题干含 < > & 时不转义会导致 PDF 构建失败；
    雅黑缺失的符号（⇌ ₂ ₃ ⁻ ⊗ 等）必须用 <font face="seguisym"> 包裹，
    否则印出来是空白方块——这是方案标记的最大单点风险。
    """
    out = str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if _FALLBACK_CHARS:
        ensure_fonts()
        buf = []
        run = []
        for ch in out:
            if ch in _FALLBACK_CHARS:
                if run:
                    buf.append("".join(run)); run = []
                buf.append('<font face="seguisym">%s</font>' % ch)
            else:
                run.append(ch)
        if run:
            buf.append("".join(run))
        out = "".join(buf)
    return out


def source_banner(source_type: str) -> str:
    """来源横幅（方案 5.3）：打印出的卷子右上角必须显示来源类型，
    让你在纸上做题时就能分辨这是真题还是练习。AI 生成题必须醒目标注。"""
    if source_type == "真题":
        return "真题"
    if source_type == "AI生成":
        return "⚠ AI 生成练习题（非真题，无年份卷别）"
    return esc(source_type)


# ----------------------------------------------------------------------
# 页眉页脚
# ----------------------------------------------------------------------
class PackDoc(BaseDocTemplate):
    def __init__(self, path: str, header_left: str, header_right: str, **kw: Any):
        super().__init__(path, pagesize=A4,
                         leftMargin=17*mm, rightMargin=15*mm,
                         topMargin=20*mm, bottomMargin=15*mm, **kw)
        self.header_left = header_left
        self.header_right = header_right
        frame = Frame(self.leftMargin, self.bottomMargin,
                      self.width, self.height, id="body")
        self.addPageTemplates([PageTemplate(id="p", frames=[frame],
                                            onPage=self._decorate)])

    def _decorate(self, canv, doc) -> None:
        w, h = A4
        canv.saveState()
        canv.setFont(REG, 8.5)
        canv.setFillColor(colors.HexColor("#666666"))
        canv.drawString(17*mm, h - 13*mm, self.header_left)
        canv.drawRightString(w - 15*mm, h - 13*mm, self.header_right)
        canv.setStrokeColor(colors.HexColor("#cccccc"))
        canv.setLineWidth(0.5)
        canv.line(17*mm, h - 15*mm, w - 15*mm, h - 15*mm)
        canv.setFont(REG, 8)
        canv.drawString(17*mm, 9*mm, "做完后回填错题归因（六选一，不可跳过）——这是软件唯一无法被教辅替代的功能")
        canv.drawRightString(w - 15*mm, 9*mm, "第 %d 页" % doc.page)
        canv.restoreState()


def _answer_area(qtype: str, s: dict) -> list:
    """答题区留白。理科必须手算，屏幕点选项无法训练（方案 2.3）。"""
    out = []
    if qtype in ("解答题", "实验题"):
        for _ in range(7):
            out.append(Paragraph("　", s["blank"]))
    elif qtype == "作文":
        for _ in range(22):
            out.append(Paragraph("　", s["blank"]))
    elif qtype == "填空题":
        for _ in range(2):
            out.append(Paragraph("　", s["blank"]))
    else:
        out.append(Paragraph("作答：＿＿＿＿＿＿", s["blank"]))
    return out


def _image(path: str, s: dict) -> list:
    """几何图/电路图/生物结构图。纯文本存不下，必须支持插图。"""
    if not path:
        return []
    full = path if os.path.isabs(path) else os.path.join(IMAGE_DIR, path)
    if not os.path.exists(full):
        return [Paragraph("［图片缺失：%s］" % esc(os.path.basename(full)), s["small"])]
    try:
        img = Image(full)
        max_w, max_h = 150*mm, 90*mm
        ratio = min(max_w / img.imageWidth, max_h / img.imageHeight, 1.0)
        img.drawWidth *= ratio
        img.drawHeight *= ratio
        return [img]
    except Exception as e:
        return [Paragraph("［图片读取失败：%s］" % esc(str(e)[:60]), s["small"])]


def _render_question(idx: int, q, s: dict, *, with_answer: bool = False,
                     answer_space: bool = True) -> list:
    """渲染单题。选项、答题区、图片、来源标注齐备。"""
    flow: list = []
    tag = source_banner(q["source_type"])
    prov = ""
    if q["source_type"] == "真题" and (q["year"] or q["paper"]):
        prov = "　<span fontColor='#888888'>%s%s%s</span>" % (
            q["year"] or "", " " if q["year"] and q["paper"] else "", q["paper"] or "")
    flow.append(Paragraph("<b>%d.</b> %s%s　<font size=8 color='#b00020'>[%s]</font>"
                          % (idx, esc(q["stem"]), prov, tag), s["stem"]))
    for opt in db.decode_options(q):
        if str(opt).strip():
            flow.append(Paragraph(esc(str(opt)), s["option"]))
    flow.extend(_image(q["image_path"], s))
    if answer_space:
        flow.extend(_answer_area(q["qtype"], s))
    if with_answer:
        flow.append(Spacer(1, 1.5*mm))
        flow.append(Paragraph("答案：%s" % esc(q["answer"]), s["answer"]))
        if q["analysis"]:
            flow.append(Paragraph("解析：%s" % esc(q["analysis"]), s["analysis"]))
    return flow


def _header_block(title: str, meta: tuple, extra: Sequence[str], s: dict) -> list:
    name, dur, scene = meta
    flow = [Paragraph(title, s["title"])]
    flow.append(Paragraph("%s｜建议用时 %s｜%s" % (esc(name), esc(dur), esc(scene)), s["subtitle"]))
    for line in extra:
        flow.append(Paragraph(esc(line), s["subtitle"]))
    flow.append(Spacer(1, 2*mm))
    flow.append(HRFlowable(width="100%", thickness=0.8,
                           color=colors.HexColor("#999999"), spaceAfter=3*mm))
    return flow


def _write(path: str, story: list, header_left: str, header_right: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    doc = PackDoc(path, header_left, header_right)
    doc.build(story)
    return path


def _safe_name(text: str) -> str:
    bad = '\\/:*?"<>|\r\n\t'
    return "".join("_" if c in bad else c for c in str(text)).strip()[:60]


# ----------------------------------------------------------------------
# 六种训练包
# ----------------------------------------------------------------------
def build_pack_A(conn, cards: Sequence[Any], subject: str | None = None,
                 out_dir: str | None = None, title: str | None = None) -> str:
    """A 碎片记忆包。碎片时段专用，不做需要演算的题（方案 2.2 / 风险 8）。"""
    s = _styles()
    day = date.today().strftime("%m月%d日")
    story = _header_block(
        title or "碎片记忆包 · %s" % day, PACK_META["A"],
        ["今日到期 %d 张卡｜碎片时段只做记忆，不做演算题" % len(cards),
         "A 级门槛不在难题，而在基础题一分不丢"], s)

    by_subject: dict[str, list] = {}
    for c in cards:
        by_subject.setdefault(c["subject"], []).append(c)
    for subj in sorted(by_subject):
        story.append(Paragraph("%s（%d 张）" % (esc(subj), len(by_subject[subj])), s["h2"]))
        for i, c in enumerate(by_subject[subj], 1):
            block = [Paragraph("%d. %s" % (i, esc(c["front"])), s["body"])]
            img = _image(c["image_path"], s)
            block.extend(img)
            block.append(Paragraph("答：＿＿＿＿＿＿＿＿＿＿", s["blank"]))
            story.append(KeepTogether(block))

    story.append(Spacer(1, 5*mm))
    story.append(HRFlowable(width="100%", thickness=0.6,
                            color=colors.HexColor("#bbbbbb"), spaceAfter=2*mm))
    story.append(Paragraph("对照答案（做完再看）", s["h3"]))
    for i, c in enumerate(cards, 1):
        if c["back"]:
            story.append(Paragraph("%d. %s" % (i, esc(c["back"]).replace("\n", "　")), s["analysis"]))

    name = "A_碎片记忆_%s%s.pdf" % (date.today().strftime("%Y%m%d"),
                                    "_" + _safe_name(subject) if subject else "")
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "碎片记忆包 · %s" % day, "每天 10 分钟 · 不可中断超过 2 天")


def build_pack_B(conn, kp_id: str, out_dir: str | None = None, limit: int = 15) -> str | None:
    """B 唤醒包。单知识点 10—15 题，基础+中档。唤醒而非新学（方案 2.1）。"""
    kp = conn.execute("SELECT * FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
    if not kp:
        return None
    qs = db.list_questions(conn, kp_id=kp_id, difficulty=(1, 3), limit=limit)
    if not qs:
        return None
    s = _styles()
    story = _header_block(
        "唤醒包 · %s · %s" % (kp["subject"], kp["name"]), PACK_META["B"],
        ["层级：%s｜权重：%s｜难度 1—3（唤醒用，不含难题）" % (kp["tier"], kp["weight"]),
         "唤醒 ≠ 新学：概念识别 → 通路恢复 → 熟练化"], s)
    for i, q in enumerate(qs, 1):
        story.extend(_render_question(i, q, s))
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.6,
                            color=colors.HexColor("#bbbbbb"), spaceAfter=2*mm))
    story.append(Paragraph("答案与解析", s["h3"]))
    for i, q in enumerate(qs, 1):
        story.append(Paragraph("%d. %s　%s" % (i, esc(q["answer"]),
                                               esc(q["analysis"] or "")), s["analysis"]))
    name = "B_唤醒_%s_%s.pdf" % (_safe_name(kp["subject"]), _safe_name(kp["name"]))
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "唤醒包 · %s" % kp["name"], "掌握度 75%%（初中）/ 60%%（高中）即放行")


def build_pack_C(conn, kp_id: str, out_dir: str | None = None, limit: int = 25) -> str | None:
    """C 专项包。单章节 20—25 题，中档为主。练习期主力（方案 4.2）。"""
    kp = conn.execute("SELECT * FROM knowledge_points WHERE id=?", (kp_id,)).fetchone()
    if not kp:
        return None
    qs = db.list_questions(conn, kp_id=kp_id, difficulty=(2, 5), limit=limit)
    if not qs:
        return None
    s = _styles()
    story = _header_block(
        "专项包 · %s · %s" % (kp["subject"], kp["name"]), PACK_META["C"],
        ["难度 2—5｜共 %d 题｜当前掌握度 %.0f%%" % (len(qs), (kp["mastery"] or 0) * 100),
         "按错误率排序攻克，不是按章节顺序刷"], s)
    for i, q in enumerate(qs, 1):
        story.extend(_render_question(i, q, s))
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.6,
                            color=colors.HexColor("#bbbbbb"), spaceAfter=2*mm))
    story.append(Paragraph("答案与解析", s["h3"]))
    for i, q in enumerate(qs, 1):
        story.append(Paragraph("%d. %s　%s" % (i, esc(q["answer"]),
                                               esc(q["analysis"] or "")), s["analysis"]))
    name = "C_专项_%s_%s.pdf" % (_safe_name(kp["subject"]), _safe_name(kp["name"]))
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "专项包 · %s" % kp["name"], "%s · %s" % (kp["subject"], kp["tier"]))


def build_pack_D(conn, out_dir: str | None = None, limit: int = 30) -> str | None:
    """D 错题重做包。整个系统的核心闭环（方案 5.2）。

    连续 3 次做对才出库。你有复印机，"昨天的错题今天重印一遍"成本为零，
    这是普通考生做不到的练习密度。
    """
    cards = srs.due_cards(conn, kinds=("错题",), limit=limit)
    if not cards:
        return None
    s = _styles()
    story = _header_block(
        "错题重做包 · %s" % date.today().strftime("%m月%d日"), PACK_META["D"],
        ["到期 %d 张｜连续做对 3 次才出库",
         "重做时先遮住答案，独立写完再对照"], s)
    qids = [c["question_id"] for c in cards if c["question_id"]]
    qmap = {}
    if qids:
        ph = ",".join("?" * len(qids))
        for q in conn.execute("SELECT * FROM questions WHERE id IN (%s)" % ph, qids):
            qmap[q["id"]] = q
    idx = 0
    for c in cards:
        q = qmap.get(c["question_id"]) if c["question_id"] else None
        idx += 1
        if q:
            story.extend(_render_question(idx, q, s))
        else:
            story.append(Paragraph("%d. %s" % (idx, esc(c["front"])), s["stem"]))
            story.extend(_image(c["image_path"], s))
            story.extend(_answer_area("解答题", s))
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.6,
                            color=colors.HexColor("#bbbbbb"), spaceAfter=2*mm))
    story.append(Paragraph("答案与解析（做完再看）", s["h3"]))
    for i, c in enumerate(cards, 1):
        story.append(Paragraph("%d. %s" % (i, esc(c["back"]).replace("\n", "　") if c["back"] else ""),
                               s["analysis"]))
    name = "D_错题重做_%s.pdf" % date.today().strftime("%Y%m%d")
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "错题重做包", "无归因的刷题会退化成重复做已经会的题")


def build_pack_E(conn, subject: str, questions: Sequence[Any],
                 out_dir: str | None = None, title: str | None = None) -> str:
    """E 限时套卷。全真模拟 + 答题卡。

    ⚠️ 云南选考 75 分钟 100 分 = 每分 45 秒。这是最容易被忽视的失分点，
       很多人不是不会做，是做不完。卷面必须印出时长与取舍提示。
    """
    s = _styles()
    dur = EXAM_DURATION.get(subject, 75)
    full = EXAM_FULL_MARK.get(subject, 100)
    per = (dur * 60) / max(1, len(questions))
    story = _header_block(
        title or "限时套卷 · %s" % subject, PACK_META["E"],
        ["满分 %d 分｜限时 %d 分钟｜共 %d 题｜平均每题 %.1f 分钟" % (full, dur, len(questions), per),
         "严格计时，到点停笔。取舍策略：秒答题先做，3 分钟无思路直接跳过"], s)

    groups: dict[str, list] = {}
    for q in questions:
        groups.setdefault(q["qtype"], []).append(q)
    order = ["选择题", "填空题", "实验题", "解答题", "默写", "作文"]
    idx = 0
    for qt in [g for g in order if g in groups] + [g for g in groups if g not in order]:
        items = groups[qt]
        story.append(Paragraph("%s（共 %d 题）" % (esc(qt), len(items)), s["h2"]))
        for q in items:
            idx += 1
            story.extend(_render_question(idx, q, s))

    story.append(Spacer(1, 5*mm))
    story.append(HRFlowable(width="100%", thickness=0.8,
                            color=colors.HexColor("#999999"), spaceAfter=2*mm))
    story.append(Paragraph("答题卡（限时结束后填写）", s["h3"]))
    choice_n = len(groups.get("选择题", []))
    data = [["题号"] + [str(i) for i in range(1, min(choice_n, 12) + 1)],
            ["答案"] + [""] * min(choice_n, 12)]
    if choice_n > 12:
        data.append(["题号"] + [str(i) for i in range(13, choice_n + 1)])
        data.append(["答案"] + [""] * (choice_n - 12))
    t = Table(data, colWidths=[14*mm] + [11*mm] * 12, rowHeights=[8*mm] * len(data))
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), REG), ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#888888")),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#f0f0f0")),
    ]))
    story.append(t)
    story.append(Spacer(1, 4*mm))
    info = Table([["实际用时", "＿＿＿ 分钟"], ["自评得分", "＿＿＿ / %d" % full],
                  ["未做完题号", "＿＿＿＿＿＿＿＿"],
                  ["主要失分归因", "□概念不清 □方法未掌握 □计算失误 □审题偏差 □时间不够 □表述不规范"]],
                 colWidths=[26*mm, 140*mm])
    info.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), REG), ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#888888")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#f0f0f0")),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(info)
    name = "E_限时套卷_%s_%s.pdf" % (_safe_name(subject), date.today().strftime("%Y%m%d"))
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "限时套卷 · %s · %d 分钟" % (subject, dur),
                  "训练介质必须与考试介质一致：纸笔")


def build_pack_F(conn, questions: Sequence[Any], subject: str,
                 out_dir: str | None = None) -> str:
    """F 表述规范包。为双 A 目标新增（方案 5.2 / 风险 3）。

    赋分科目按点给分，一道 8 分生物简答因表述不规范丢 2 分，
    就足以把你挤出 A 级。化学的实验现象描述、生物的原因分析题是重灾区。
    """
    s = _styles()
    story = _header_block(
        "表述规范包 · %s" % subject, PACK_META["F"],
        ["共 %d 题｜先独立写完整答案，再逐句对照标准答案" % len(questions),
         "标记每一处丢分点：漏关键词 / 表述与教材不一致 / 逻辑链断裂 / 单位或符号错误"], s)
    for i, q in enumerate(questions, 1):
        block = [Paragraph("<b>%d.</b> %s" % (i, esc(q["stem"])), s["stem"])]
        block.extend(_image(q["image_path"], s))
        for _ in range(6):
            block.append(Paragraph("　", s["blank"]))
        story.append(KeepTogether(block))
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.8,
                            color=colors.HexColor("#999999"), spaceAfter=2*mm))
    story.append(Paragraph("标准答案 · 逐句对照（做完再看）", s["h3"]))
    for i, q in enumerate(questions, 1):
        story.append(Paragraph("%d. 【答案】%s" % (i, esc(q["answer"])), s["answer"]))
        if q["analysis"]:
            story.append(Paragraph("　　【评分点】%s" % esc(q["analysis"]), s["analysis"]))
        story.append(Paragraph("　　丢分点自查：□漏关键词 □表述偏离教材 □逻辑断裂 □符号单位错",
                               s["small"]))
    name = "F_表述规范_%s_%s.pdf" % (_safe_name(subject), date.today().strftime("%Y%m%d"))
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "表述规范包 · %s" % subject, "表述不规范是赋分科目的 A 级杀手")


def build_calc_pack(conn, subject: str, limit: int = 12, out_dir: str | None = None) -> str | None:
    """限时计算训练。归因=计算失误时的干预（方案 5.5）。

    化学失分大头是计算失误而非概念不懂。每天 10 道纯计算限时训练，
    比刷新题更有效——化学 A 级要求卷面 92 分，计算准确度是门槛。
    """
    qs = conn.execute(
        "SELECT * FROM questions WHERE subject=? AND qtype IN ('填空题','解答题') "
        "AND difficulty BETWEEN 2 AND 4 ORDER BY RANDOM() LIMIT ?", (subject, limit)).fetchall()
    if not qs:
        return None
    s = _styles()
    story = _header_block(
        "限时计算训练 · %s" % subject, PACK_META["CALC"],
        ["共 %d 题｜限时 15 分钟｜只求准确，不求难题" % len(qs),
         "每题必须写出完整步骤，有效数字与单位一并检查"], s)
    for i, q in enumerate(qs, 1):
        block = [Paragraph("<b>%d.</b> %s" % (i, esc(q["stem"])), s["stem"])]
        for _ in range(4):
            block.append(Paragraph("　", s["blank"]))
        story.append(KeepTogether(block))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("答案：%s" % "　".join(
        "%d.%s" % (i, esc(q["answer"])) for i, q in enumerate(qs, 1)), s["analysis"]))
    name = "CALC_限时计算_%s_%s.pdf" % (_safe_name(subject), date.today().strftime("%Y%m%d"))
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "限时计算训练 · %s" % subject, "思路对但算错 → 重学知识是浪费时间")


# ----------------------------------------------------------------------
# 90 天一轮总表（排程 + 每日自检练习）
# ----------------------------------------------------------------------
_WEEK = "一二三四五六日"


def build_round_plan_pdf(conn, plans: Sequence[Any], *, start: date,
                         days: int, factor: float,
                         out_dir: str | None = None) -> str:
    """《90 天基础知识总梳理 · 一轮总表》。

    两部分：
      一、总排程表——每天学哪些知识点、各多少分钟，一页页翻完全程；
      二、每日自检——某个知识点"当天学完"（最后一段）才配练习，
          合上书做题验证"唤醒"是否成功，答案附在当日小节末尾。
    """
    s = _styles()
    story: list = []

    # ---------- 封面 + 使用说明 ----------
    total_min = sum(sum(it["minutes"] for it in p.items) for p in plans)
    kp_total = conn.execute(
        "SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
    story.append(Paragraph("90 天基础知识总梳理 · 一轮总表", s["title"]))
    story.append(Paragraph(
        "2027 云南高考（6月7—9日）｜起始 %s｜%d 天｜唤醒系数 %.2f｜共 %d 个知识点｜%.0f 学时"
        % (start.isoformat(), days, factor, kp_total, total_min / 60), s["subtitle"]))
    story.append(Spacer(1, 3 * mm))
    story.append(HRFlowable(width="100%", thickness=0.8,
                            color=colors.HexColor("#999999"), spaceAfter=3 * mm))
    for line in (
        "使用方法（软件排程，纸上学习）：",
        "① 第 1—3 天办行政（色觉自查、报名资格），第 4—10 天做六科诊断卷并定 factor；",
        "② 第 11 天起按本表推进：每天先复习前一天错题，再学当日知识点，学完立刻做该节自检题；",
        "③ 自检题合上书做，答错的当场归因（六选一）并抄进错题本，次日进入 D 包重做；",
        "④ 英语 3500 词、语文默写是每日滚动任务（碎片时段），不占整块时间、不进自检；",
        "⑤ 某节点跨多天（标注 †）表示当日只学一部分，次日接着学，练习只在学完那天做。",
    ):
        story.append(Paragraph(esc(line), s["body"]))
    story.append(Spacer(1, 2 * mm))

    # ---------- 第一部分：总排程表 ----------
    story.append(Paragraph("第一部分 · 90 天总排程表", s["h2"]))
    cell = ParagraphStyle("cell", fontName=REG, fontSize=8.5, leading=12)
    cellb = ParagraphStyle("cellb", fontName=BOLD, fontSize=8.5, leading=12)
    head = ["天", "日期", "星期", "当日任务（科目·知识点 分钟）", "合计"]
    data = [head]
    for p in plans:
        if p.items:
            lines = []
            for it in p.items:
                mark = "†" if it.get("split") else ""
                lines.append("%s·%s%s %d′" % (
                    it["subject"], esc(it["name"]), mark, it["minutes"]))
            task = Paragraph("<br/>".join(lines), cell)
            mins = sum(it["minutes"] for it in p.items)
            mins_txt = "%.1fh" % (mins / 60)
        else:
            txt = p.label or "—"
            task = Paragraph(esc(txt), cellb if p.label else cell)
            mins_txt = ""
        data.append([str(p.day), p.d.strftime("%m-%d"), _WEEK[p.d.weekday()],
                     task, mins_txt])
    widths = [8 * mm, 14 * mm, 9 * mm, 138 * mm, 12 * mm]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), BOLD),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#aaaaaa")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (2, -1), "CENTER"),
        ("ALIGN", (4, 0), (4, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(t)
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("† = 该知识点跨天，次日接着学", s["small"]))
    story.append(PageBreak())

    # ---------- 第二部分：每日自检练习 ----------
    story.append(Paragraph("第二部分 · 每日自检练习", s["h2"]))
    story.append(Paragraph(
        "只在该知识点【学完当天】做。合上书、限时、写完整步骤；"
        "答案与解析在当日小节末尾，做完再看。", s["subtitle"]))
    story.append(Spacer(1, 2 * mm))

    q_cache: dict[str, list] = {}

    def quiz(kp_id: str) -> list:
        if kp_id not in q_cache:
            q_cache[kp_id] = conn.execute(
                "SELECT * FROM questions WHERE kp_id=? AND source_type='自主命题练习' "
                "ORDER BY id", (kp_id,)).fetchall()
        return q_cache[kp_id]

    day_blocks: list = []   # 攒一天的 flow，整体 KeepTogether 太大会失效，逐题控制
    any_day = False
    for p in plans:
        finished = [it for it in p.items if not it.get("split")]
        blocks: list = []
        n = 0
        answers: list = []
        for it in finished:
            qs = quiz(it["kp_id"])
            if not qs:
                continue
            blocks.append(Paragraph("%s·%s（%d 题）" % (
                esc(it["subject"]), esc(it["name"]), len(qs)), s["h3"]))
            for q in qs:
                n += 1
                blocks.append(KeepTogether(_render_question(n, q, s)))
                answers.append("%d. %s　%s" % (
                    n, esc(q["answer"]), esc(q["analysis"] or "")))
        if not blocks:
            continue
        any_day = True
        day_blocks.append(Paragraph("第 %d 天自检 · %s 星期%s" % (
            p.day, p.d.isoformat(), _WEEK[p.d.weekday()]), s["h2"]))
        day_blocks.extend(blocks)
        if answers:
            day_blocks.append(HRFlowable(width="100%", thickness=0.5,
                                         color=colors.HexColor("#bbbbbb"),
                                         spaceBefore=2 * mm, spaceAfter=1.5 * mm))
            day_blocks.append(Paragraph("当日答案（做完再看）", s["answer"]))
            for a in answers:
                day_blocks.append(Paragraph(a, s["analysis"]))
        day_blocks.append(Spacer(1, 4 * mm))

    if not any_day:
        day_blocks.append(Paragraph("题库中暂无自检题，请先运行 seed-quiz。", s["body"]))
    story.extend(day_blocks)

    name = "90天一轮总表_%s.pdf" % start.strftime("%Y%m%d")
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "90 天一轮总表 · 起始 %s" % start.isoformat(),
                  "软件排程，纸上学习")


# ----------------------------------------------------------------------
# 总复习文档（按科目分章：知识点详解 + 自检题）
# ----------------------------------------------------------------------
def build_review_book_pdf(conn, out_dir: str | None = None) -> str:
    """《高考总复习 · 知识点详解》——按科目分章，每节=讲解要点+自检题。

    打印后可作案头参考书：先读"学"再做题，与手机端内容同源（core/content_*.py）。
    """
    from core import content as content_mod
    s = _styles()
    story: list = []
    covered = sum(1 for r in conn.execute(
        "SELECT id FROM knowledge_points") if content_mod.get_content(r["id"]))
    total = conn.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
    story.append(Paragraph("高考总复习 · 知识点详解", s["title"]))
    story.append(Paragraph(
        "2027 云南（物化生）｜%d 个知识点（%d 个已配详解）｜先学后练，按科目分章"
        % (total, covered), s["subtitle"]))
    story.append(Spacer(1, 2 * mm))
    story.append(HRFlowable(width="100%", thickness=0.8,
                            color=colors.HexColor("#999999"), spaceAfter=3 * mm))

    for subj in SUBJECTS:
        rows = conn.execute(
            "SELECT * FROM knowledge_points WHERE subject=? "
            "ORDER BY CASE tier WHEN '初中' THEN 0 WHEN '高中必修' THEN 1 ELSE 2 END, id",
            (subj,)).fetchall()
        story.append(PageBreak())
        story.append(Paragraph("【%s】共 %d 个知识点" % (subj, len(rows)), s["title"]))
        story.append(Spacer(1, 2 * mm))
        for r in rows:
            if r["id"] in ("eng_vocab", "chn_dictation"):
                story.append(Paragraph("◆ %s（每日滚动任务：碎片时段坚持，无固定章节）"
                                       % esc(r["name"]), s["h3"]))
                continue
            head = "◆ %s" % esc(r["name"])
            meta = []
            if r["tier"] == "初中":
                meta.append("初中衔接")
            if r["weight"] == "高频考点":
                meta.append("高频")
            meta.append("约 %g 学时" % (r["est_hours"] or 2))
            story.append(Paragraph(
                "%s　<font size=8 color='#888888'>%s</font>" % (head, "｜".join(meta)),
                s["h3"]))
            pts = content_mod.get_content(r["id"])
            if pts:
                for p in pts:
                    story.append(Paragraph("· " + esc(p), s["body"]))
            else:
                story.append(Paragraph("（详解整理中，请对照教材本节内容学习）", s["small"]))
            qs = conn.execute(
                "SELECT * FROM questions WHERE kp_id=? ORDER BY difficulty, id",
                (r["id"],)).fetchall()
            if qs:
                story.append(Paragraph("自检练习：", s["answer"]))
                for i, q in enumerate(qs, 1):
                    story.extend(_render_question(i, q, s, with_answer=False))
                story.append(Paragraph(
                    "答案：" + "　".join("%d.%s" % (i, esc(q["answer"]))
                                       for i, q in enumerate(qs, 1)), s["analysis"]))
            story.append(Spacer(1, 3 * mm))

    name = "高考总复习_知识点详解_%s.pdf" % date.today().strftime("%Y%m%d")
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "高考总复习 · 知识点详解", "先学后练 · 按科目分章")


# ----------------------------------------------------------------------
# 每日学习单（按当前进度排 N 天，每天多科、先学后练、可打印）
# ----------------------------------------------------------------------
def build_daily_plan_pdf(conn, plans: Sequence[Any], *, start: date,
                         out_dir: str | None = None) -> str:
    """《每日学习单》——每天一节：各科知识点讲解 + 自检题 + 答案。

    plans 来自 core.daily.build_daily_plan（自动跳过已掌握内容）。
    """
    from core import content as content_mod
    s = _styles()
    story: list = []
    story.append(Paragraph("每日学习单 · 先学后练", s["title"]))
    story.append(Paragraph(
        "起始 %s｜共 %d 天｜按当前进度排（已掌握的不再出现）｜每天各科都有，学完再做"
        % (start.isoformat(), len(plans)), s["subtitle"]))
    story.append(Spacer(1, 2 * mm))
    for line in ("用法：每天撕下当日一页。先读知识点要点（合上答案），"
                 "再做题，做完对答案并归因错题。"):
        story.append(Paragraph(esc(line), s["body"]))
    story.append(HRFlowable(width="100%", thickness=0.8,
                            color=colors.HexColor("#999999"), spaceAfter=3 * mm))

    for p in plans:
        if not p.items:
            continue
        story.append(PageBreak())
        total_min = sum(it.minutes for it in p.items)
        story.append(Paragraph("第 %d 天 · %s 星期%s　<font size=9>约 %d 分钟</font>" % (
            p.day, p.d.isoformat(), _WEEK[p.d.weekday()], total_min), s["title"]))
        story.append(Spacer(1, 2 * mm))
        answers: list[str] = []
        for it in p.items:
            story.append(Paragraph("【%s】%s　<font size=8 color='#888888'>约 %d 分钟</font>"
                                   % (esc(it.subject), esc(it.name), it.minutes), s["h2"]))
            if it.tier == "滚动":
                story.append(Paragraph("（每日坚持：不占整块时间，碎片时段完成即可）", s["small"]))
                story.append(Spacer(1, 2 * mm))
                continue
            pts = content_mod.get_content(it.kp_id)
            if pts:
                for pt in pts:
                    story.append(Paragraph("· " + esc(pt), s["body"]))
            else:
                story.append(Paragraph("（详解整理中，请对照教材本节学习）", s["small"]))
            qs = conn.execute(
                "SELECT * FROM questions WHERE kp_id=? ORDER BY difficulty, id",
                (it.kp_id,)).fetchall()
            if qs:
                story.append(Paragraph("练习：", s["answer"]))
                for i, q in enumerate(qs, 1):
                    story.extend(_render_question(i, q, s, with_answer=False))
                    answers.append("%s %d.%s　%s" % (
                        it.name, i, esc(q["answer"]), esc(q["analysis"] or "")))
            story.append(Spacer(1, 2.5 * mm))
        if answers:
            story.append(HRFlowable(width="100%", thickness=0.5,
                                    color=colors.HexColor("#bbbbbb"),
                                    spaceBefore=2 * mm, spaceAfter=1.5 * mm))
            story.append(Paragraph("当日答案（做完再看）", s["answer"]))
            for a in answers:
                story.append(Paragraph(a, s["analysis"]))

    name = "每日学习单_%s起%d天.pdf" % (start.strftime("%m%d"), len(plans))
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "每日学习单 · 起始 %s" % start.isoformat(),
                  "先学后练 · 每天各科")


# ----------------------------------------------------------------------
# 背诵手册（语文名句 + 英语词汇 + 作文模板，可打印随身背）
# ----------------------------------------------------------------------
def build_dictation_pdf(conn, out_dir: str | None = None) -> str:
    """《背诵手册》——语文名句名篇完整原文 + 英语核心词汇 + 作文模板，宽松排版。

    打印后可随身携带，利用碎片时间反复背诵。内容来自 core/content_*.py。
    排版专门优化：大行距、段间距、篇目分隔，方便阅读和标记。
    """
    from core import content as content_mod
    s = _styles()
    # 背诵专用宽松样式
    dict_body = ParagraphStyle("dict_body", parent=s["body"],
                               fontName=REG, fontSize=11, leading=22,
                               spaceAfter=5, firstLineIndent=0)
    dict_title = ParagraphStyle("dict_title", parent=s["h2"],
                                fontName=BOLD, fontSize=13, leading=20,
                                spaceBefore=10, spaceAfter=6,
                                textColor=colors.HexColor("#1a3a5c"))
    dict_subtitle = ParagraphStyle("dict_subtitle", parent=s["h3"],
                                   fontName=BOLD, fontSize=11.5, leading=18,
                                   spaceBefore=8, spaceAfter=4,
                                   textColor=colors.HexColor("#2c5f8a"))
    story: list = []
    story.append(Paragraph("高考背诵手册", s["title"]))
    story.append(Paragraph(
        "语文完整原文 · 英语核心词汇 · 作文模板｜宽松排版，方便朗读和标记",
        s["subtitle"]))
    story.append(Spacer(1, 2 * mm))
    story.append(HRFlowable(width="100%", thickness=0.8,
                            color=colors.HexColor("#999999"), spaceAfter=3 * mm))

    # 语文：名句名篇完整原文
    story.append(PageBreak())
    story.append(Paragraph("【语文】名句名篇完整原文", dict_title))
    story.append(Spacer(1, 3 * mm))
    pts = content_mod.get_content("chn_dictation")
    if pts:
        for p in pts:
            # 以「原文·」开头的是完整原文，用宽松样式；其他是方法指导用普通样式
            if p.startswith("原文·"):
                # 提取篇名作为小标题
                title_end = p.find("：", 3)
                if title_end > 0:
                    piece_title = p[3:title_end]
                    story.append(Paragraph("📜 " + piece_title, dict_subtitle))
                    body_text = p[title_end + 1:]
                else:
                    body_text = p
                story.append(Paragraph(esc(body_text), dict_body))
                story.append(Spacer(1, 2 * mm))
            else:
                story.append(Paragraph("· " + esc(p), s["body"]))
    else:
        story.append(Paragraph("（内容整理中）", s["small"]))

    # 语文：文言文实词
    story.append(PageBreak())
    story.append(Paragraph("【语文】文言文 120 实词速记", dict_title))
    story.append(Spacer(1, 3 * mm))
    pts = content_mod.get_content("chn_wenyan_word")
    if pts:
        for p in pts:
            story.append(Paragraph("· " + esc(p), dict_body))
    else:
        story.append(Paragraph("（内容整理中）", s["small"]))

    # 英语：核心词汇
    story.append(PageBreak())
    story.append(Paragraph("【英语】高考核心词汇", dict_title))
    story.append(Spacer(1, 3 * mm))
    pts = content_mod.get_content("eng_vocab")
    if pts:
        for p in pts:
            story.append(Paragraph("· " + esc(p), dict_body))
    else:
        story.append(Paragraph("（内容整理中）", s["small"]))

    # 英语：作文模板
    story.append(PageBreak())
    story.append(Paragraph("【英语】作文万能模板", dict_title))
    story.append(Spacer(1, 3 * mm))
    pts = content_mod.get_content("eng_write_apply")
    if pts:
        for p in pts:
            story.append(Paragraph("· " + esc(p), dict_body))
    else:
        story.append(Paragraph("（内容整理中）", s["small"]))

    name = "高考背诵手册_%s.pdf" % date.today().strftime("%Y%m%d")
    return _write(os.path.join(out_dir or OUTPUT_DIR, name), story,
                  "高考背诵手册", "完整原文 · 词汇 · 模板")
