# -*- coding: utf-8 -*-
"""Streamlit 本地界面（方案 5.7）。

⚠️ 这不是刷题软件。软件只做四件事（方案 5.1）：
   排程（今天练什么）→ 生成（印出来）→ 归因（错在哪一类）→ 看板。
   学习发生在纸上。这里绝不放"屏幕上点选项做题"的界面——介质错误是旧项目
   失败根因之一（方案 1.3 / 2.3）。

运行：
    streamlit run app.py
"""
from __future__ import annotations

import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import SUBJECTS, SOURCE_TYPES, ATTRIBUTIONS

BASE = os.path.dirname(os.path.abspath(__file__))
from core import db, graph, pdf, plan, srs

st.set_page_config(page_title="2027 高考复习系统", page_icon="📐", layout="wide")


# ----------------------------------------------------------------------
# 连接（每个 session 复用一个只读连接；写操作后立即重开）
# ----------------------------------------------------------------------
@st.cache_resource
def _conn():
    return db.init_db()


def conn():
    return _conn()


def _refresh():
    st.cache_resource.clear()


# ----------------------------------------------------------------------
# 侧边栏
# ----------------------------------------------------------------------
def sidebar() -> str:
    st.sidebar.title("📐 gk2027")
    c = conn()
    sch = plan.compute_schedule(c)
    st.sidebar.caption("距考试 **%d** 天｜备考第 %d 天" % (sch.days_left, sch.day_index))
    st.sidebar.progress(
        min(1.0, max(0.0, sch.day_index / max(1, sch.foundation_days + sch.practice_days))))
    st.sidebar.caption("%s%s" % (sch.phase, ("｜" + sch.round_name) if sch.round_name else ""))
    page = st.sidebar.radio(
        "导航",
        ["今天该干什么", "生成训练包", "知识点依赖图", "题库与录入", "归因诊断", "进度看板", "系统体检"],
        label_visibility="collapsed")
    st.sidebar.divider()
    st.sidebar.caption("软件排程，纸上学习。\n打印用自有复印机，成本为零。")
    return page


# ----------------------------------------------------------------------
# 今天
# ----------------------------------------------------------------------
def page_today():
    st.header("今天该干什么")
    c = conn()
    t = plan.today_tasks(c)
    sch = t["schedule"]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("距考试", "%d 天" % sch.days_left)
    col2.metric("备考", "第 %d 天" % sch.day_index)
    col3.metric("阶段", sch.phase.replace("第一阶段·", "").replace("第二阶段·", ""))
    cs = srs.card_stats(c)
    col4.metric("今日到期卡", cs["今日到期"])

    if t["行政提醒"]:
        st.subheader("⚠ 行政事项（比任何代码都紧急）")
        for d in t["行政提醒"]:
            flag = "🔴" if d["days"] <= 7 or d["state"] == "已过期" else "🟡"
            st.markdown("%s **%s** — %s（%s）" % (flag, d["date"], d["text"], d["state"]))

    st.subheader("碎片时段（看店间隙，只做记忆不做演算）")
    q = t["今日队列"]
    f1, f2, f3 = st.columns(3)
    f1.metric("今日轮换", t["碎片记忆轮换"])
    f2.metric("A 类记忆卡", q["碎片时段"]["A类记忆包"])
    f3.metric("D 类错题速览", q["碎片时段"]["D类错题速览"])

    st.subheader("整块时段（打烊后，做理解与演算）")
    st.markdown("今日合计：整块 **%.2f h** ＋ 碎片 **%.2f h**" % (t["整块总学时"], t["碎片总学时"]))
    st.dataframe(t["学时分配"], width="stretch", hide_index=True)

    avail = q["整块时段"]["可学知识点"]
    st.subheader("现在可以学（前置已满足）")
    if avail:
        st.dataframe(
            [{"科目": n["subject"], "层级": n["tier"], "知识点": n["name"],
              "权重": n["weight"], "预计学时": n["hours"]} for n in avail],
            width="stretch", hide_index=True)
    else:
        st.warning("没有可学知识点。请先录入题目或检查依赖图。")

    attr = q["错题归因分布"]
    if attr:
        st.subheader("未解决错题归因分布")
        dg = srs.diagnose(c)
        st.info("结论：%s" % dg["verdict"])
        st.dataframe(
            [{"归因": k, "题数": v, "干预措施": srs.INTERVENTIONS.get(k, {}).get("action", "")}
             for k, v in sorted(attr.items(), key=lambda x: -x[1])],
            width="stretch", hide_index=True)


# ----------------------------------------------------------------------
# 生成训练包
# ----------------------------------------------------------------------
def page_pack():
    st.header("生成训练包（A4 PDF → 复印机）")
    c = conn()
    kind = st.selectbox(
        "包类型",
        ["A 碎片记忆包", "D 错题重做包", "B 唤醒包", "C 专项包", "E 限时套卷",
         "F 表述规范包", "CALC 限时计算训练"])
    key = kind.split()[0]

    limit = st.slider("题目/卡片数量上限", 5, 60, 20, step=5)
    subject = st.selectbox("科目（部分包类型需要）", ["（不指定）"] + SUBJECTS)
    subj = None if subject == "（不指定）" else subject

    kp_options = []
    if key in ("B", "C"):
        rows = graph.available_nodes(c, subject=subj)
        kp_options = [r["name"] for r in rows]
        if not kp_options:
            st.warning("该科目暂无可学知识点。B/C 包需要指定一个已解锁知识点。")

    kp_name = st.selectbox("知识点", kp_options) if kp_options else None

    out = None
    if st.button("生成 PDF", type="primary"):
        try:
            if key == "A":
                cards = srs.due_cards(c, subject=subj, limit=limit)
                out = pdf.build_pack_A(c, cards, subject=subj) if cards else None
                if not cards:
                    st.info("今日无到期卡片。")
            elif key == "D":
                out = pdf.build_pack_D(c, limit=limit)
            elif key in ("B", "C"):
                kp = next((r for r in graph.available_nodes(c, subject=subj)
                           if r["name"] == kp_name), None)
                if not kp:
                    st.error("请先选择知识点。")
                    return
                out = (pdf.build_pack_B(c, kp["id"], limit=limit) if key == "B"
                       else pdf.build_pack_C(c, kp["id"], limit=limit))
            elif key == "E":
                if not subj:
                    st.error("E 类套卷需指定科目。")
                    return
                qs = db.list_questions(c, subject=subj, limit=limit)
                out = pdf.build_pack_E(c, subj, qs) if qs else None
                if not qs:
                    st.info("%s 题库为空，无法生成套卷。请先录入题目。" % subj)
            elif key == "F":
                if not subj:
                    st.error("F 类需指定科目（化学或生物）。")
                    return
                qs = c.execute(
                    "SELECT * FROM questions WHERE subject=? AND qtype IN ('解答题','实验题') "
                    "ORDER BY RANDOM() LIMIT ?", (subj, limit)).fetchall()
                out = pdf.build_pack_F(c, qs, subj) if qs else None
                if not qs:
                    st.info("%s 无主观题（解答题/实验题）。" % subj)
            elif key == "CALC":
                if not subj:
                    st.error("限时计算训练需指定科目。")
                    return
                out = pdf.build_calc_pack(c, subj, limit=limit)
        except Exception as e:
            st.error("生成失败：%s" % e)

        if out:
            c.execute(
                "INSERT INTO packs(kind, subject, title, path) VALUES(?,?,?,?)",
                (key, subj, os.path.basename(out), out))
            c.commit()
            st.success("已生成：%s（%.1f KB）" % (out, os.path.getsize(out) / 1024))
            with open(out, "rb") as f:
                st.download_button("⬇ 下载 PDF 去打印", f.read(),
                                   file_name=os.path.basename(out), mime="application/pdf")
        elif out is None:
            st.warning("没有可打印内容。")


# ----------------------------------------------------------------------
# 依赖图
# ----------------------------------------------------------------------
def page_graph():
    st.header("知识点依赖图")
    st.caption("跨学科依赖是这张图最重要的部分（方案 5.4）。90 天一轮没有回头路，顺序错了漏洞会固化。")
    c = conn()

    st.dataframe(graph.graph_summary(c), width="stretch", hide_index=True)

    subj = st.selectbox("选择科目查看拓扑顺序", SUBJECTS)
    rows = graph.topological_order(c, subj)
    mark = {"已掌握": "✅", "学习中": "🔶", "需复习": "🔁", "可学": "▶️", "未解锁": "🔒"}
    st.dataframe(
        [{"顺序": mark.get(r["status"], ""), "层级": r["tier"], "知识点": r["name"],
          "状态": r["status"], "掌握度": "%.0f%%" % ((r["mastery"] or 0) * 100),
          "权重": r["weight"]} for r in rows],
        width="stretch", hide_index=True)

    with st.expander("跨学科依赖（%d 条）" % len(graph.cross_subject_dependencies(c))):
        st.dataframe(
            [{"需要": "%s·%s" % (x["ksub"], x["kname"]),
              "依赖": "%s·%s" % (x["rsub"], x["rname"])}
             for x in graph.cross_subject_dependencies(c)],
            width="stretch", hide_index=True)

    with st.expander("被阻塞的节点及缺失前置（自查依赖图是否合理）"):
        blocked = graph.blocked_nodes(c, subject=subj)
        if not blocked:
            st.success("%s 无被阻塞节点。" % subj)
        for b in blocked[:40]:
            miss = "、".join("%s·%s(%.0f%%)" % (m["subject"], m["name"], (m["mastery"] or 0) * 100)
                             for m in b["missing"])
            st.markdown("🔒 **%s** ← 缺：%s" % (b["node"]["name"], miss))


# ----------------------------------------------------------------------
# 题库与录入
# ----------------------------------------------------------------------
def page_bank():
    st.header("题库与录入")
    c = conn()
    st.dataframe(db.question_stats_by_subject(c), width="stretch", hide_index=True)

    tab_add, tab_list, tab_result = st.tabs(["录入题目", "浏览题库", "回填作答结果"])

    with tab_add:
        st.caption("硬约束（方案 5.3）：题干重复直接拒绝；AI 生成题永不带年份卷别；真题必须有可核查出处。")
        with st.form("addq", clear_on_submit=True):
            subj = st.selectbox("学科", SUBJECTS)
            src = st.selectbox("来源类型", list(__import__("config").SOURCE_TYPES))
            year = paper = qno = ref = None
            if src == "真题":
                year = st.number_input("年份", 2000, 2030, 2026)
                paper = st.text_input("卷别（如 云南省选考化学卷）")
                qno = st.text_input("题号")
                ref = st.text_input("出处 source_ref（真题必填）")
            stem = st.text_area("题干（必填）", height=100)
            opts = st.text_input("选项（用 | 分隔，非选择题留空）")
            ans = st.text_input("答案（必填）")
            ana = st.text_area("解析", height=80)
            qtype = st.selectbox("题型", ["选择题", "填空题", "解答题", "实验题", "作文", "默写"])
            diff = st.slider("难度", 1, 5, 3)
            kp = st.text_input("知识点名称（留空不关联）")
            img = st.text_input("图片路径（几何图/电路图，留空跳过）")
            submitted = st.form_submit_button("入库", type="primary")

        if submitted:
            if not stem.strip() or not ans.strip():
                st.error("题干与答案不能为空。")
            else:
                kp_id = None
                if kp:
                    r = c.execute("SELECT id FROM knowledge_points WHERE name LIKE ? AND subject=?",
                                  ("%" + kp + "%", subj)).fetchone()
                    kp_id = r["id"] if r else None
                try:
                    qid = db.add_question(
                        c, source_type=src, year=year if src == "真题" else None,
                        paper=paper or None, question_no=qno or None, source_ref=ref or None,
                        subject=subj, kp_id=kp_id, difficulty=diff, qtype=qtype, stem=stem,
                        options=[o.strip() for o in opts.split("|") if o.strip()],
                        answer=ans, analysis=ana, image_path=img or None)
                    st.success("✓ 已录入 id=%d" % qid)
                except db.DuplicateStem as e:
                    st.error("重复题干：%s" % e)
                except Exception as e:
                    st.error("入库被拒：%s" % e)

    with tab_list:
        fs = st.selectbox("筛选学科", ["全部"] + SUBJECTS)
        rows = db.list_questions(c, subject=None if fs == "全部" else fs, limit=200)
        st.dataframe(
            [{"id": r["id"], "学科": r["subject"], "来源": r["source_type"],
              "年份": r["year"], "难度": r["difficulty"], "题型": r["qtype"],
              "题干": r["stem"][:60], "答案": r["answer"][:30]} for r in rows],
            width="stretch", hide_index=True)

    with tab_result:
        st.caption("做完纸质卷子后回填。错题必须选归因（六选一，不能跳过——方案 4.3）。")
        qid = st.number_input("题目 id", min_value=1, step=1)
        res = st.radio("结果", ["答对", "答错"])
        attr = st.selectbox("归因（答错必填）", ["（答对无需选）"] + list(ATTRIBUTIONS))
        if st.button("记录"):
            try:
                if res == "答对":
                    db.record_attempt(c, int(qid), True)
                    row = c.execute("SELECT streak, resolved FROM wrong_questions WHERE question_id=?",
                                    (int(qid),)).fetchone()
                    st.success("✓ 答对。连续正确 %d/3%s" % (
                        (row["streak"] if row else 0), "，已出库" if row and row["resolved"] else ""))
                else:
                    if attr == "（答对无需选）":
                        st.error("错题必须选择归因类型。")
                    else:
                        db.record_attempt(c, int(qid), False, attribution=attr)
                        srs.card_from_wrong_question(c, int(qid), attr)
                        st.success("✓ 已记错题，归因=%s。干预：%s" % (
                            attr, srs.INTERVENTIONS[attr]["action"]))
                # 刷新掌握度与解锁
                q = c.execute("SELECT kp_id FROM questions WHERE id=?", (int(qid),)).fetchone()
                if q and q["kp_id"]:
                    graph.update_mastery(c, q["kp_id"])
                    graph.refresh_unlock(c)
            except Exception as e:
                st.error("记录失败：%s" % e)


# ----------------------------------------------------------------------
# 归因诊断
# ----------------------------------------------------------------------
def page_attr():
    st.header("归因诊断（软件唯一无法被教辅替代的功能）")
    st.caption("教辅能给你题，但不能告诉你「你的失分 40% 来自计算失误，别再刷难题了」。")
    c = conn()
    subj = st.selectbox("科目（全部=六科合计）", ["全部"] + SUBJECTS)
    dg = srs.diagnose(c, None if subj == "全部" else subj)
    if dg["total"] == 0:
        st.info("暂无未解决错题。做错题并回填后这里会出现分析。")
        return
    st.metric("未解决错题", dg["total"])
    st.info("结论：%s" % dg["verdict"])
    st.dataframe(
        [{"归因": d["attribution"], "题数": d["n"], "占比": "%.0f%%" % d["percent"],
          "干预措施": d.get("action", ""), "理由": d.get("why", "")}
         for d in dg["distribution"]],
        width="stretch", hide_index=True)


# ----------------------------------------------------------------------
# 进度看板
# ----------------------------------------------------------------------
def page_stats():
    st.header("进度看板")
    c = conn()
    pp = plan.phase_progress(c)
    col1, col2, col3 = st.columns(3)
    col1.metric("整体进度", "%.1f%%" % pp["整体进度"], "%d/%d 知识点" % (pp["知识点已掌握"], pp["知识点总数"]))
    col2.metric("剩余天数", pp["剩余天数"])
    col3.metric("阶段", pp["阶段"])

    st.subheader("目标分解 vs 最近实测（方案 3.4 双 A 版）")
    tt = plan.target_table(c)
    st.dataframe(tt["rows"], width="stretch", hide_index=True)
    st.markdown("目标总分 **%d**（对外 600 / 内部瞄准 615）｜实测总分 %s" % (
        tt["目标总分"], tt["实测总分"] or "—"))

    st.subheader("里程碑（未达标 → 换方法/加资源，不降目标）")
    for m in plan.milestone_status(c):
        icon = "✅" if m["state"] == "已过期" else "⏳"
        tgt = "" if not m["targets"] else " 目标 " + str(m["targets"])
        st.markdown("%s **%s** %s%s" % (icon, m["date"], m["label"], tgt))
        if m["remedy"]:
            st.caption("　→ %s" % m["remedy"])

    st.subheader("模考与实测记录")
    recs = c.execute(
        "SELECT taken_at, kind, subject, score, full_mark FROM exam_records "
        "ORDER BY taken_at DESC LIMIT 50").fetchall()
    if recs:
        st.dataframe([dict(r) for r in recs], width="stretch", hide_index=True)
    else:
        st.caption("暂无记录。第 4—10 天做诊断测试后录入（cli.py diag）。")


# ----------------------------------------------------------------------
# 体检
# ----------------------------------------------------------------------
def page_doctor():
    st.header("系统体检")
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(BASE, "cli.py"), "doctor"],
                       capture_output=True, text=True, encoding="utf-8")
    st.code((r.stdout or "") + (r.stderr or ""), language="text")
    if r.returncode == 0:
        st.success("体检通过")
    else:
        st.error("体检存在失败项")


BASE = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------------------
PAGES = {
    "今天该干什么": page_today,
    "生成训练包": page_pack,
    "知识点依赖图": page_graph,
    "题库与录入": page_bank,
    "归因诊断": page_attr,
    "进度看板": page_stats,
    "系统体检": page_doctor,
}

PAGES[sidebar()]()
