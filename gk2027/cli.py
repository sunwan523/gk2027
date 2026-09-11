# -*- coding: utf-8 -*-
"""命令行入口。

开店场景下，打开浏览器登录 Web 界面的心理门槛太高（方案 2.3）。
CLI 提供最快的日常操作路径：

    python cli.py init                初始化数据库与依赖图
    python cli.py today               今天该干什么（最常用）
    python cli.py pack A              生成今日碎片记忆包并打印
    python cli.py pack D              生成错题重做包
    python cli.py pack C 化学 化学平衡  生成某知识点专项包
    python cli.py pack E 物理         生成物理限时套卷
    python cli.py addq                交互式录入题目
    python cli.py wrong 12 计算失误    标记题目 12 答错及归因
    python cli.py right 12            标记题目 12 答对
    python cli.py diag                录入诊断成绩并自动定基础期天数
    python cli.py doctor              体检：依赖图环检测、题库重复、字体、来源合规
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from typing import Sequence

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import (EXAM_DATE, OUTPUT_DIR, SUBJECTS, TARGET_SCORES,
                    days_to_exam, today)
from core import db, graph, pdf, plan, srs


def _conn():
    return db.init_db()


def _bar(text: str = "", width: int = 62) -> str:
    return text.center(width, "─") if text else "─" * width


# ----------------------------------------------------------------------
def cmd_init(args) -> int:
    conn = _conn()
    res = graph.seed_graph(conn, reset=args.reset_edges)
    cycles = graph.detect_cycles(conn)
    print("依赖图已写入：新增 %d 节点，更新 %d 节点，%d 条依赖边"
          % (res["inserted"], res["updated"], res["edges"]))
    cross = graph.cross_subject_dependencies(conn)
    print("跨学科依赖 %d 条（这张图最重要的部分）：" % len(cross))
    for c in cross[:12]:
        print("   %s·%s  ←  %s·%s" % (c["ksub"], c["kname"], c["rsub"], c["rname"]))
    if len(cross) > 12:
        print("   … 其余 %d 条见 Web 界面" % (len(cross) - 12))
    if cycles:
        print("\n⚠ 依赖图存在环，会导致永久阻塞：")
        for c in cycles:
            print("   ", c)
        return 1
    print("\n环检测：通过（无循环依赖）")
    fd, reason = plan.auto_set_foundation_from_diagnosis(conn)
    print("基础期：%d 天 — %s" % (fd, reason))
    conn.close()
    return 0


def cmd_today(args) -> int:
    conn = _conn()
    t = plan.today_tasks(conn)
    sch = t["schedule"]

    print(_bar())
    print("  2027 高考复习 · %s 星期%s" % (sch.today.isoformat(), 
                                          "一二三四五六日"[sch.today.weekday()]))
    print("  距考试 %d 天｜第 %d 天｜%s" % (sch.days_left, sch.day_index, sch.phase))
    if sch.round_name:
        print("  练习轮次：%s — %s" % (sch.round_name, sch.round_hint))
    print(_bar())

    for d in t["行政提醒"]:
        flag = "🔴" if d["days"] <= 7 or d["state"] == "已过期" else "🟡"
        print("  %s %s  %s（%s）" % (flag, d["date"], d["text"], d["state"]))
    if t["行政提醒"]:
        print(_bar())

    print("  碎片时段（看店间隙，只做记忆，不做演算）")
    print("    今日轮换：%s" % t["碎片记忆轮换"])
    q = t["今日队列"]
    print("    A 类记忆卡到期：%d 张" % q["碎片时段"]["A类记忆包"])
    print("    D 类错题速览：%d 张" % q["碎片时段"]["D类错题速览"])
    print()
    print("  整块时段（打烊后，做理解与演算）")
    print("    今日合计：整块 %.2f h + 碎片 %.2f h"
          % (t["整块总学时"], t["碎片总学时"]))
    for row in t["学时分配"]:
        print("      %-4s 整块 %.2fh  碎片 %.2fh  占比 %s"
              % (row["科目"], row["整块学时"], row["碎片学时"], row["周占比"]))
    print()
    avail = q["整块时段"]["可学知识点"]
    if avail:
        print("  现在可以学（前置已满足）：")
        for n in avail[:8]:
            print("    %-4s %-6s %s  [%s｜%.1fh]"
                  % (n["subject"], n["tier"], n["name"], n["weight"], n["hours"]))
        if len(avail) > 8:
            print("    … 共 %d 个，Web 界面看全部" % len(avail))
    else:
        print("  ⚠ 没有可学知识点。请先录入题目或检查依赖图。")

    attr = q["错题归因分布"]
    if attr:
        print()
        print("  未解决错题归因分布：")
        for k, v in sorted(attr.items(), key=lambda x: -x[1]):
            print("    %-8s %3d 题 → %s" % (k, v, srs.INTERVENTIONS.get(k, {}).get("action", "")))
        dg = srs.diagnose(conn)
        print()
        print("  结论：%s" % dg["verdict"])

    cs = q["card_stats"]
    print()
    print("  卡片：今日到期 %d｜未到期 %d｜已出库 %d｜总 %d"
          % (cs["今日到期"], cs["未到期"], cs["已出库"], cs["卡片总数"]))
    print(_bar())
    conn.close()
    return 0


def cmd_pack(args) -> int:
    conn = _conn()
    kind = args.kind.upper()
    out = None
    try:
        if kind == "A":
            from core import srs as _s
            cards = _s.due_cards(conn, subject=args.subject, limit=args.limit)
            if not cards:
                print("今日无到期卡片。先用 `cli.py seed-cards` 生成，或检查是否已全部复习完。")
                return 0
            out = pdf.build_pack_A(conn, cards, subject=args.subject)
        elif kind == "D":
            out = pdf.build_pack_D(conn, limit=args.limit)
            if not out:
                print("暂无到期错题。做错题后系统会自动生成卡片。")
                return 0
        elif kind in ("B", "C"):
            kp_id = _resolve_kp(conn, args.subject, args.kp, force=args.force)
            if not kp_id:
                return 1
            out = (pdf.build_pack_B(conn, kp_id, limit=args.limit) if kind == "B"
                   else pdf.build_pack_C(conn, kp_id, limit=args.limit))
            if not out:
                print("该知识点下没有匹配难度的题目。请先录入题目（cli.py addq）。")
                return 0
        elif kind == "E":
            if not args.subject:
                print("E 类套卷需指定科目，例如：cli.py pack E 物理")
                return 1
            qs = db.list_questions(conn, subject=args.subject, limit=args.limit or 20)
            if not qs:
                print("%s 题库为空，无法生成套卷。" % args.subject)
                return 1
            out = pdf.build_pack_E(conn, args.subject, qs)
        elif kind == "F":
            if not args.subject:
                print("F 类表述规范包需指定科目（化学或生物）")
                return 1
            qs = conn.execute(
                "SELECT * FROM questions WHERE subject=? AND qtype IN ('解答题','实验题') "
                "ORDER BY RANDOM() LIMIT ?", (args.subject, args.limit or 8)).fetchall()
            if not qs:
                print("%s 无主观题。F 类包针对赋分科目表述失分，需要解答题/实验题。" % args.subject)
                return 1
            out = pdf.build_pack_F(conn, qs, args.subject)
        elif kind == "CALC":
            if not args.subject:
                print("限时计算训练需指定科目")
                return 1
            out = pdf.build_calc_pack(conn, args.subject, limit=args.limit or 12)
            if not out:
                print("%s 无可用于计算训练的题目。" % args.subject)
                return 1
        else:
            print("未知包类型：%s（可用 A/B/C/D/E/F/CALC）" % kind)
            return 1
    finally:
        conn.close()

    if out:
        conn = _conn()
        conn.execute("INSERT INTO packs(kind, subject, title, path) VALUES(?,?,?,?)",
                     (kind, args.subject, os.path.basename(out), out))
        conn.commit(); conn.close()
        size = os.path.getsize(out) / 1024.0
        print("已生成：%s（%.1f KB）" % (out, size))
        if args.print:
            _send_to_printer(out)
    return 0


def _resolve_kp(conn, subject: str | None, name: str | None, force: bool = False) -> str | None:
    if not name:
        print("需指定知识点名称，例如：cli.py pack C 化学 化学平衡")
        return None
    sql = "SELECT id, subject, name, tier, status FROM knowledge_points WHERE name LIKE ?"
    args = ["%" + name + "%"]
    if subject:
        sql += " AND subject=?"
        args.append(subject)
    rows = conn.execute(sql, args).fetchall()
    if not rows:
        print("找不到知识点「%s」。用 `cli.py kp` 查看全部。" % name)
        return None
    if len(rows) > 1:
        print("匹配到多个知识点，请指定学科：")
        for r in rows:
            print("   %s｜%s｜%s（%s）" % (r["subject"], r["tier"], r["name"], r["status"]))
        return None
    r = rows[0]
    if r["status"] == "未解锁":
        missing = conn.execute(
            "SELECT k.subject, k.name, k.mastery FROM kp_requires e "
            "JOIN knowledge_points k ON k.id=e.requires_id WHERE e.kp_id=?",
            (r["id"],)).fetchall()
        print("⚠「%s」尚未解锁，缺失前置：" % r["name"])
        for m in missing:
            print("     %s·%s（掌握度 %.0f%%）" % (m["subject"], m["name"], (m["mastery"] or 0) * 100))
        print("   依赖图的作用就是防止在前置未就绪时学上层内容——效率极低且容易挫败。")
        if force:
            print("   已指定 --force，强行生成。")
            return r["id"]
        print("   如确要强行生成，加 --force。")
        return None
    return r["id"]


def _send_to_printer(path: str) -> None:
    if sys.platform != "win32":
        print("非 Windows 环境，跳过打印。")
        return
    try:
        os.startfile(path, "print")  # noqa: S606 — 用户明确要求打印自己的训练包
        print("已发送到默认打印机。")
    except Exception as e:
        print("自动打印失败（%s），请手动打印该文件。" % e)


def cmd_addq(args) -> int:
    conn = _conn()
    print(_bar("录入题目"))
    print("留空即用默认值。Ctrl+C 退出。")
    try:
        subject = _ask("学科 [%s]" % "/".join(SUBJECTS), "数学")
        if subject not in SUBJECTS:
            print("学科必须是：%s" % "/".join(SUBJECTS)); return 1
        src = _ask("来源类型 [真题/教辅录入/自主命题练习/AI生成]", "教辅录入")
        year = paper = qno = ref = None
        if src == "真题":
            year = _ask_int("年份（真题必填）")
            paper = _ask("卷别（如 云南省选考化学卷）")
            qno = _ask("题号")
            ref = _ask("出处 source_ref（真题必填：链接或书名页码）")
            if not ref:
                print("真题必须有可核查出处，否则不得入库。"); return 1
        stem = _ask("题干（必填）")
        if not stem:
            print("题干不能为空"); return 1
        opt_raw = _ask("选项（用 | 分隔，非选择题留空）")
        options = [o.strip() for o in opt_raw.split("|") if o.strip()] if opt_raw else []
        answer = _ask("答案（必填）")
        if not answer:
            print("答案不能为空"); return 1
        analysis = _ask("解析")
        qtype = _ask("题型 [选择题/填空题/解答题/实验题/作文/默写]",
                     "选择题" if options else "解答题")
        diff = _ask_int("难度 1-5", 3)
        kp = _ask("知识点名称（留空则不关联）")
        kp_id = None
        if kp:
            kp_id = _resolve_kp(conn, subject, kp)
        img = _ask("图片路径（几何图/电路图/结构图，留空跳过）")
        qid = db.add_question(conn, source_type=src, year=year, paper=paper,
                              question_no=qno, source_ref=ref, subject=subject,
                              kp_id=kp_id, difficulty=diff, qtype=qtype, stem=stem,
                              options=options, answer=answer, analysis=analysis,
                              image_path=img or None)
        print("\n✓ 已录入，id=%d" % qid)
        if _ask("同时生成一张复习卡片？[Y/n]", "Y").lower().startswith("y"):
            front = stem if not options else stem
            back = "答案：%s\n%s" % (answer, analysis or "")
            cid = srs.add_card(conn, "知识卡", subject, front, back,
                               kp_id=kp_id, question_id=qid)
            print("✓ 卡片 id=%d" % cid)
    except (KeyboardInterrupt, EOFError):
        print("\n已取消。"); return 1
    finally:
        conn.close()
    return 0


def _ask(prompt: str, default: str = "") -> str:
    tip = "%s%s: " % (prompt, "" if not default else "（默认 %s）" % default)
    val = input(tip).strip()
    return val or default


def _ask_int(prompt: str, default: int | None = None) -> int | None:
    val = _ask(prompt, str(default) if default is not None else "")
    if not val:
        return default
    try:
        return int(val)
    except ValueError:
        print("需要数字，已跳过。")
        return default


def cmd_wrong(args) -> int:
    conn = _conn()
    try:
        db.record_attempt(conn, args.qid, False, attribution=args.attr)
        q = conn.execute("SELECT subject, stem, kp_id FROM questions WHERE id=?",
                         (args.qid,)).fetchone()
        if q:
            cid = srs.card_from_wrong_question(conn, args.qid, args.attr)
            conn.execute("UPDATE cards SET due_at=datetime('now','localtime') WHERE id=?", (cid,))
            conn.commit()
            from core import graph as g
            if q["kp_id"]:
                g.update_mastery(conn, q["kp_id"])
                g.refresh_unlock(conn)
            print("✓ 已记为错题，归因=%s，卡片 id=%d" % (args.attr, cid))
            print("  干预措施：%s" % srs.INTERVENTIONS[args.attr]["action"])
            print("  理由：%s" % srs.INTERVENTIONS[args.attr]["why"])
        else:
            print("题目 %d 不存在" % args.qid); return 1
    finally:
        conn.close()
    return 0


def cmd_right(args) -> int:
    conn = _conn()
    try:
        q = conn.execute("SELECT kp_id FROM questions WHERE id=?", (args.qid,)).fetchone()
        if not q:
            print("题目 %d 不存在" % args.qid); return 1
        db.record_attempt(conn, args.qid, True)
        row = conn.execute("SELECT streak, resolved FROM wrong_questions WHERE question_id=?",
                           (args.qid,)).fetchone()
        if row:
            print("✓ 答对。连续正确 %d/3%s"
                  % (row["streak"], "，已出库" if row["resolved"] else ""))
        else:
            print("✓ 答对。")
        if q["kp_id"]:
            m = graph.update_mastery(conn, q["kp_id"])
            newly = graph.refresh_unlock(conn)
            kp = conn.execute("SELECT name, tier, status FROM knowledge_points WHERE id=?",
                              (q["kp_id"],)).fetchone()
            print("  「%s」掌握度 %.0f%%（%s，放行线 %.0f%%）"
                  % (kp["name"], m * 100, kp["status"],
                     (0.75 if kp["tier"] == "初中" else 0.60) * 100))
            if newly:
                print("  🔓 新解锁 %d 个知识点" % newly)
    finally:
        conn.close()
    return 0


def cmd_diag(args) -> int:
    conn = _conn()
    try:
        print(_bar("录入诊断成绩"))
        print("诊断结果决定基础期长度，不能用期望代替实测（方案 2.1）。")
        print("判据（2026 云南选考物理真题，限时 75 分钟）：")
        print("   ≥50 分 → 90 天    35—49 分 → 110 天    <35 分 → 140 天")
        print()
        for s in SUBJECTS:
            sc = _ask_float("%s 诊断分（满分 %d，留空跳过）" % (s, _full(s)))
            if sc is None:
                continue
            conn.execute(
                "INSERT INTO exam_records(kind, subject, score, full_mark, duration_min, detail)"
                " VALUES('诊断',?,?,?,?,?)",
                (s, sc, _full(s), 75 if s in ("物理", "化学", "生物") else 120, args.note or ""))
            print("   已记录 %s = %s" % (s, sc))
        conn.commit()
        days, reason = plan.auto_set_foundation_from_diagnosis(conn)
        print("\n" + _bar())
        print("基础期设定为 %d 天" % days)
        print("依据：%s" % reason)
        if days != 90:
            print("\n说明：主动延长基础期不是退让。160 天练习仍充裕，")
            print("      但基础不牢的 180 天练习是无效劳动（方案 风险 1）。")
        sch = plan.compute_schedule(conn)
        print("\n日程：备考第 1 天 %s → 基础期结束 %s → 考试 %s"
              % (sch.start_date, sch.foundation_end, sch.exam_date))
    finally:
        conn.close()
    return 0


def _full(subject: str) -> int:
    from config import EXAM_FULL_MARK
    return EXAM_FULL_MARK.get(subject, 100)


def _ask_float(prompt: str) -> float | None:
    val = input(prompt + ": ").strip()
    if not val:
        return None
    try:
        return float(val)
    except ValueError:
        print("   需要数字，已跳过。")
        return None


def cmd_doctor(args) -> int:
    """体检。逐项检查系统能否真正跑起来。"""
    conn = _conn()
    ok = True
    print(_bar("系统体检"))

    print("\n[1] PDF 字体（方案标记的最大单点风险）")
    try:
        reg, bold = pdf.ensure_fonts()
        print("    ✓ %s / %s 注册成功" % (reg, bold))
        # 用 charToGlyph 权威判定，不用 stringWidth：
        # 缺失字形 stringWidth 仍返回默认宽度，是假阳性（上一会话踩过）。
        from reportlab.pdfbase.ttfonts import TTFont
        main = TTFont("msyh_probe", r"C:\Windows\Fonts\msyh.ttc",
                      subfontIndex=0).face.charToGlyph
        sym = TTFont("seguisym", r"C:\Windows\Fonts\seguisym.ttf").face.charToGlyph

        def covered(ch: str) -> bool:
            o = ord(ch)
            return (o in main and main[o] != 0) or (o in sym and sym[o] != 0)

        bad = [ch for ch in "√²₂₃⇌→Δ⊗♀♂⁻⁺≤±°×÷α≈₀₁" if not covered(ch)]
        if bad:
            ok = False
            print("    ✗ 以下符号 msyh 与 seguisym 均无字形，会印成空白：%s" % "".join(bad))
        else:
            print("    ✓ 特殊符号全部可渲染（msyh + seguisym 回退，含 ⇌ ₂ ₃ ⁻ ⊗）")
        print("    ⚠ 勿改用宋体：实测宋体与雅黑均缺 ⇌ ₂ ₃ ⁻ ⊗，靠 seguisym 回退补齐")
    except Exception as e:
        ok = False
        print("    ✗ 字体加载失败：%s" % e)

    print("\n[2] 依赖图")
    cycles = graph.detect_cycles(conn)
    if cycles:
        ok = False
        print("    ✗ 存在循环依赖，会导致永久阻塞：")
        for c in cycles:
            print("       ", c)
    else:
        print("    ✓ 无循环依赖")
    n = conn.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
    e = graph.count_edges(conn)
    print("    节点 %d 个，依赖边 %d 条，跨学科依赖 %d 条"
          % (n, e, len(graph.cross_subject_dependencies(conn))))
    if n == 0:
        ok = False
        print("    ✗ 依赖图为空，请先运行 cli.py init")
    avail = graph.available_nodes(conn)
    blocked = graph.blocked_nodes(conn)
    print("    可学 %d 个，被阻塞 %d 个" % (len(avail), len(blocked)))
    if n and not avail:
        print("    ⚠ 无任何可学节点，检查起点节点是否有前置依赖")

    print("\n[3] 题库防注水约束")
    try:
        db.add_question(conn, source_type="教辅录入", subject="数学",
                        stem="__doctor_probe__ 唯一性探针", answer="x")
        qid = conn.execute("SELECT id FROM questions WHERE stem LIKE '__doctor_probe__%'").fetchone()["id"]
        try:
            db.add_question(conn, source_type="教辅录入", subject="数学",
                            stem="__doctor_probe__ 唯一性探针", answer="x")
            ok = False
            print("    ✗ UNIQUE(stem) 未生效——重复题干可入库（旧项目因此注水 3003 条）")
        except (db.DuplicateStem, Exception):
            print("    ✓ UNIQUE(stem) 生效：重复题干被拒绝")
    finally:
        conn.execute("DELETE FROM questions WHERE stem LIKE '__doctor_probe__%'")
        conn.commit()

    print("\n[4] 来源合规约束（禁止假真题）")
    try:
        db.add_question(conn, source_type="AI生成", subject="生物", year=2009,
                        paper="天津卷", stem="__doctor_probe_ai__ 假出处探针", answer="A")
        conn.execute("DELETE FROM questions WHERE stem LIKE '__doctor_probe_ai__%'")
        conn.commit()
        ok = False
        print("    ✗ 触发器未生效：AI 生成题竟可带年份卷别（旧项目最严重的错误）")
    except Exception as ex:
        conn.rollback()
        print("    ✓ AI 生成题带 year/paper 被拒绝：%s" % str(ex)[:56])
    try:
        db.add_question(conn, source_type="真题", subject="生物", year=2026,
                        paper="云南卷", stem="__doctor_probe_ref__ 无出处探针", answer="A")
        conn.execute("DELETE FROM questions WHERE stem LIKE '__doctor_probe_ref__%'")
        conn.commit()
        ok = False
        print("    ✗ 真题缺少 source_ref 竟然入库了")
    except Exception as ex:
        conn.rollback()
        print("    ✓ 真题缺 source_ref 被拒绝：%s" % str(ex)[:56])

    print("\n[5] 归因强制约束")
    probe = conn.execute("SELECT id FROM questions LIMIT 1").fetchone()
    if probe:
        try:
            db.record_attempt(conn, probe["id"], False, attribution=None)
            ok = False
            print("    ✗ 无归因的错题被接受了")
        except ValueError:
            print("    ✓ 错题必须选归因，不可跳过")
        try:
            db.record_attempt(conn, probe["id"], False, attribution="随便写的")
            ok = False
            print("    ✗ 非法归因类型被接受")
        except ValueError:
            print("    ✓ 归因限定六类")
    else:
        print("    ⚠ 题库为空，跳过（录入题目后重试）")

    print("\n[6] 数据现状")
    st = db.stats(conn)
    for k, v in st.items():
        print("    %-12s %d" % (k, v))
    if st["题目总数"] == 0:
        print("    ⚠ 题库为空。系统可运行，但训练包需要题目。")
        print("      云南选考真题只有约 70 题，主力练习量需靠全国卷理综、")
        print("      外省选考卷与教辅录入（方案 6.2）。")

    print("\n[7] 日程")
    sch = plan.compute_schedule(conn)
    print("    基础期 %d 天 + 练习期 %d 天 = %d 天"
          % (sch.foundation_days, sch.practice_days, sch.foundation_days + sch.practice_days))
    print("    起点 %s，考试 %s，今天第 %d 天，剩 %d 天"
          % (sch.start_date, sch.exam_date, sch.day_index, sch.days_left))
    if sch.day_index <= 0:
        print("    ⚠ 今天早于计划起点。检查 foundation_days 是否设置过大。")

    print("\n" + _bar())
    print("体检结论：%s" % ("全部通过" if ok else "存在失败项，见上方 ✗"))
    conn.close()
    return 0 if ok else 1


def cmd_kp(args) -> int:
    conn = _conn()
    print(_bar("知识点依赖图"))
    for row in graph.graph_summary(conn):
        print("  %-4s %-8s 节点 %3d｜已掌握 %3d｜可学 %3d｜平均掌握度 %.0f%%｜预计 %.0f h"
              % (row["subject"], row["tier"], row["n"], row["mastered"], row["available"],
                 (row["avg_mastery"] or 0) * 100, row["hours"] or 0))
    if args.subject:
        print()
        for r in graph.topological_order(conn, args.subject):
            mark = {"已掌握": "✓", "学习中": "◐", "需复习": "↻",
                    "可学": "→", "未解锁": "·"}.get(r["status"], "?")
            print("  %s %-6s %-28s 掌握度 %3.0f%%  %s"
                  % (mark, r["tier"], r["name"], (r["mastery"] or 0) * 100, r["weight"]))
    conn.close()
    return 0


def cmd_stats(args) -> int:
    conn = _conn()
    print(_bar("进度看板"))
    pp = plan.phase_progress(conn)
    for k, v in pp.items():
        print("  %-14s %s" % (k, v))
    print()
    tt = plan.target_table(conn)
    print("  %-4s %-6s %-6s %-8s %-6s" % ("科目", "计分", "目标", "最近实测", "差距"))
    for r in tt["rows"]:
        act = "—" if r["最近实测"] is None else "%.0f" % r["最近实测"]
        gap = "—" if r["差距"] is None else "%+.1f" % (-r["差距"])
        print("  %-4s %-6s %-6d %-8s %-6s" % (r["科目"], r["计分"], r["目标"], act, gap))
    print("  %s" % ("─" * 40))
    print("  目标总分 %d（对外目标 600 / 内部瞄准 615）" % tt["目标总分"])
    if tt["实测总分"] is not None:
        print("  实测总分 %.1f" % tt["实测总分"])
    print()
    dg = srs.diagnose(conn)
    print("  归因诊断：%s" % dg["verdict"])
    for d in dg["distribution"]:
        print("    %-8s %3d 题（%.0f%%）→ %s"
              % (d["attribution"], d["n"], d["percent"], d.get("action", "")))
    print()
    for m in plan.milestone_status(conn):
        tgt = "" if not m["targets"] else " 目标 " + str(m["targets"])
        print("  [%s] %s %s%s" % (m["state"], m["date"], m["label"], tgt))
        if m["remedy"]:
            print("        → %s" % m["remedy"])
    conn.close()
    return 0


def cmd_seed_cards(args) -> int:
    """生成语文默写、英语词汇、化学生物概念等 A 类记忆卡。

    A 级门槛不在难题，而在基础题一分不丢（方案 3.4），
    而基础题精确度恰好靠碎片时间反复过记忆型内容。
    """
    conn = _conn()
    seeds = _memory_seeds()
    n = 0
    for kind, subject, front, back, kp in seeds:
        try:
            srs.add_card(conn, kind, subject, front, back, kp_id=kp)
            n += 1
        except Exception:
            pass
    graph.refresh_unlock(conn)
    print("已生成 %d 张记忆卡（%s）" % (n, "、".join(sorted({s[1] for s in seeds}))))
    print("这些卡片每天进入 A 类碎片记忆包，270 天累计 270—400 小时纯记忆训练。")
    conn.close()
    return 0


def _memory_seeds() -> list[tuple]:
    """首批记忆卡种子。内容取高考必背项，作为系统启动的最小可用集。"""
    out: list[tuple] = []
    # 语文默写（高频 6 分题，纯记忆，投入产出比最稳定）
    dictation = [
        ("《劝学》：故木受绳则直，＿＿＿＿＿＿", "金就砺则利，君子博学而日参省乎己，则知明而行无过矣"),
        ("《劝学》：积土成山，风雨兴焉；＿＿＿＿＿＿，＿＿＿＿＿＿", "积水成渊，蛟龙生焉；积善成德，而神明自得，圣心备焉"),
        ("《师说》：是故弟子不必不如师，＿＿＿＿＿＿", "师不必贤于弟子，闻道有先后，术业有专攻，如是而已"),
        ("《赤壁赋》：寄蜉蝣于天地，＿＿＿＿＿＿", "渺沧海之一粟。哀吾生之须臾，羡长江之无穷"),
        ("《阿房宫赋》：秦人不暇自哀，而后人哀之；＿＿＿＿＿＿，＿＿＿＿＿＿", "后人哀之而不鉴之，亦使后人而复哀后人也"),
        ("《岳阳楼记》：先天下之忧而忧，＿＿＿＿＿＿", "后天下之乐而乐"),
        ("《离骚》：长太息以掩涕兮，＿＿＿＿＿＿", "哀民生之多艰"),
        ("《琵琶行》：别有幽愁暗恨生，＿＿＿＿＿＿", "此时无声胜有声"),
    ]
    for f, b in dictation:
        out.append(("默写", "语文", f, b, "chn_dictation"))
    # 英语高频词（词汇退化最彻底且无法压缩，方案 风险 6）
    vocab = [
        ("abandon", "v. 放弃，抛弃"), ("abstract", "adj. 抽象的 n. 摘要"),
        ("acquire", "v. 获得，习得"), ("adapt", "v. 适应；改编"),
        ("adequate", "adj. 充足的，胜任的"), ("advocate", "v. 提倡 n. 拥护者"),
        ("ambitious", "adj. 有雄心的"), ("anticipate", "v. 预期，预料"),
        ("appreciate", "v. 感激；欣赏"), ("appropriate", "adj. 适当的"),
        ("assumption", "n. 假设，假定"), ("attribute", "v. 归因于 n. 属性"),
        ("available", "adj. 可获得的，有空的"), ("beneficial", "adj. 有益的"),
        ("capacity", "n. 能力，容量"), ("circumstance", "n. 环境，情况"),
    ]
    for f, b in vocab:
        out.append(("词汇", "英语", "%s 的中文释义与词性" % f, b, "eng_vocab"))
    # 化学方程式（碎片时间反复过，A 级要求条件反射）
    chem = [
        ("写出：实验室用高锰酸钾制氧气的化学方程式",
         "2KMnO₄ →(Δ) K₂MnO₄ + MnO₂ + O₂↑"),
        ("写出：铁与水蒸气高温反应的化学方程式", "3Fe + 4H₂O(g) →(高温) Fe₃O₄ + 4H₂"),
        ("写出：氯气与氢氧化钠溶液反应的离子方程式", "Cl₂ + 2OH⁻ → Cl⁻ + ClO⁻ + H₂O"),
        ("写出：碳酸氢钠受热分解的化学方程式", "2NaHCO₃ →(Δ) Na₂CO₃ + H₂O + CO₂↑"),
        ("写出：铝与氢氧化钠溶液反应的离子方程式",
         "2Al + 2OH⁻ + 2H₂O → 2AlO₂⁻ + 3H₂↑"),
        ("写出：工业合成氨的化学方程式（含条件）",
         "N₂ + 3H₂ ⇌(高温高压、催化剂) 2NH₃"),
        ("写出：铜与浓硫酸加热反应的化学方程式",
         "Cu + 2H₂SO₄(浓) →(Δ) CuSO₄ + SO₂↑ + 2H₂O"),
        ("判断：Fe³⁺ 与 SCN⁻ 的现象与方程式",
         "溶液变血红色；Fe³⁺ + 3SCN⁻ ⇌ Fe(SCN)₃"),
    ]
    for f, b in chem:
        out.append(("公式", "化学", f, b, "che_jr_equation"))
    # 生物概念（A 级要求表述与教材原文一致，方案 风险 3）
    bio = [
        ("细胞膜的结构特点与功能特性分别是什么？",
         "结构特点：具有一定的流动性；功能特性：选择透过性"),
        ("酶的特性有哪三点？", "高效性、专一性、作用条件较温和（需适宜温度和 pH）"),
        ("光合作用光反应的场所与产物？",
         "场所：类囊体薄膜；产物：O₂、[H]（NADPH）、ATP"),
        ("有氧呼吸三个阶段的场所？",
         "第一阶段：细胞质基质；第二、三阶段：线粒体（基质与内膜）"),
        ("基因分离定律的实质？",
         "在杂合子的细胞中，位于一对同源染色体上的等位基因，具有一定的独立性；"
         "在减数分裂形成配子时，等位基因随同源染色体的分开而分离，"
         "分别进入两个配子中，独立地随配子遗传给后代"),
        ("内环境的三个主要组成？", "血浆、组织液、淋巴（液）"),
        ("生态系统的四大成分？", "非生物的物质和能量、生产者、消费者、分解者"),
        ("神经调节的基本方式与结构基础？", "基本方式：反射；结构基础：反射弧"),
    ]
    for f, b in bio:
        out.append(("概念", "生物", f, b, "bio_jr_cell"))
    # 物理公式
    phy = [
        ("匀变速直线运动三个基本公式",
         "v = v₀ + at；x = v₀t + ½at²；v² − v₀² = 2ax"),
        ("牛顿第二定律表达式及方向关系",
         "F⃗合 = ma⃗；加速度方向与合外力方向相同"),
        ("动能定理表达式", "W合 = ΔEk = ½mv² − ½mv₀²"),
        ("动量守恒定律成立条件与表达式",
         "系统不受外力或所受合外力为零；m₁v₁ + m₂v₂ = m₁v₁′ + m₂v₂′"),
        ("电场强度定义式与点电荷场强公式", "E = F/q（定义式）；E = kQ/r²（点电荷）"),
        ("法拉第电磁感应定律", "ε = nΔΦ/Δt；导体切割：ε = BLv"),
    ]
    for f, b in phy:
        out.append(("公式", "物理", f, b, "phy_kinematics"))
    # 数学公式定理
    mat = [
        ("等差数列通项与前 n 项和", "aₙ = a₁ + (n−1)d；Sₙ = n(a₁+aₙ)/2 = na₁ + n(n−1)d/2"),
        ("等比数列通项与前 n 项和",
         "aₙ = a₁q^(n−1)；q≠1 时 Sₙ = a₁(1−qⁿ)/(1−q)"),
        ("正弦定理与余弦定理",
         "a/sinA = b/sinB = c/sinC = 2R；a² = b² + c² − 2bc·cosA"),
        ("向量数量积定义与坐标公式",
         "a⃗·b⃗ = |a⃗||b⃗|cosθ；坐标：x₁x₂ + y₁y₂"),
        ("导数四则运算法则（乘积与商）",
         "(uv)′ = u′v + uv′；(u/v)′ = (u′v − uv′)/v²  (v≠0)"),
        ("二项式定理通项公式", "T(r+1) = C(n,r)·a^(n−r)·b^r"),
    ]
    for f, b in mat:
        out.append(("公式", "数学", f, b, "mat_func"))
    return out


def cmd_plan90(args) -> int:
    """生成《90 天基础知识总梳理 · 一轮总表》PDF（排程 + 每日自检练习）。"""
    from core import scheduler as sc
    from core import seed_quiz

    conn = _conn()
    fdays = plan.get_foundation_days(conn)
    days = args.days or fdays
    factor = args.factor or 0.55
    start = args.start or today()

    # 自检题入库（幂等）
    stats = seed_quiz.seed_self_quiz(conn)
    print("自检题：新增 %d，重复跳过 %d" % (stats["inserted"], stats["duplicate"]))

    plans = sc.plan_round_one(conn, start, days=days, factor=factor)
    sc.save_plan(conn, plans, start=start, days=days, factor=factor)
    out = pdf.build_round_plan_pdf(conn, plans, start=start, days=days, factor=factor)
    conn.close()
    print("已生成：%s（%.0f KB）" % (out, os.path.getsize(out) / 1024.0))
    print("起始 %s｜%d 天｜factor=%.2f。打印后按表推进即可。" % (start.isoformat(), days, factor))
    if args.print:
        _send_to_printer(out)
    return 0


def cmd_daily(args) -> int:
    """生成《每日学习单》PDF：按当前进度排 N 天，每天各科都有、先学后练。"""
    from core import daily as dy
    from core import seed_quiz, content as content_mod

    conn = _conn()
    stats = seed_quiz.seed_self_quiz(conn)
    if stats["inserted"]:
        print("自检题：新增 %d" % stats["inserted"])
    start = args.start or today()
    factor = args.factor or 0.55
    plans = dy.build_daily_plan(conn, start, days=args.days, factor=factor)
    if not plans:
        print("没有待学内容（全部已掌握？）。")
        conn.close()
        return 0
    out = pdf.build_daily_plan_pdf(conn, plans, start=start)
    cov = content_mod.coverage()
    miss = sum(1 for s, (g, t) in cov["by_subject"].items() if g < t)
    conn.close()
    print("已生成：%s（%.0f KB）" % (out, os.path.getsize(out) / 1024.0))
    print("共 %d 天｜起始 %s｜factor=%.2f。每天各科都有，先读讲解再做练习。"
          % (len(plans), start.isoformat(), factor))
    if miss:
        print("提示：%d 个科目的知识点详解仍在整理中，PDF 里会显示占位说明。" % miss)
    if args.print:
        _send_to_printer(out)
    return 0


def cmd_book(args) -> int:
    """生成《高考总复习 · 知识点详解》PDF：按科目分章，讲解+自检题。"""
    from core import content as content_mod
    conn = _conn()
    out = pdf.build_review_book_pdf(conn)
    cov = content_mod.coverage()
    conn.close()
    print("已生成：%s（%.0f KB）" % (out, os.path.getsize(out) / 1024.0))
    for s, (g, t) in cov["by_subject"].items():
        print("  %s 详解 %d/%d" % (s, g, t))
    if args.print:
        _send_to_printer(out)
    return 0


def cmd_user(args) -> int:
    """用户管理：list / add <名字> / remove <名字> / migrate <名字>（迁移旧单人库进度）。"""
    from core import users as us

    act = args.action
    if act == "list":
        for u in us.list_users():
            p = us.db_path(u["id"])
            size = "%.0f KB" % (os.path.getsize(p) / 1024.0) if os.path.exists(p) else "空"
            print("  %-12s %s  %s  建档 %s" % (u["name"], u["id"], size, u["created"]))
        if not us.list_users():
            print("  （还没有用户。add 一个：python cli.py user add 小明）")
        return 0
    if not args.name:
        print("需要名字：python cli.py user %s <名字>" % act)
        return 2
    if act == "add":
        u = us.add_user(args.name)
        db.init_db(us.db_path(u["id"]), seed=True).close()
        print("已创建用户：%s（%s）" % (u["name"], u["id"]))
        return 0
    if act == "remove":
        u = us.find_by_name(args.name)
        if not u:
            print("找不到用户：%s" % args.name)
            return 1
        us.remove_user(u["id"])
        print("已删除用户：%s（旧库改名为 .deleted 保留）" % args.name)
        return 0
    if act == "migrate":
        # 把旧的单人主库（data/gk2027.db）整体复制给该用户
        u = us.find_by_name(args.name) or us.add_user(args.name)
        src, dst = db.DB_PATH, us.db_path(u["id"])
        if not os.path.exists(src):
            print("主库不存在，无需迁移：%s" % src)
            return 1
        if os.path.exists(dst):
            print("目标用户已有库，不覆盖：%s" % dst)
            return 1
        import shutil
        shutil.copy2(src, dst)
        db.init_db(dst).close()
        print("已将旧进度迁移给用户：%s（%s）" % (args.name, dst))
        return 0
    print("未知操作：%s（list/add/remove/migrate）" % act)
    return 2


def main(argv: Sequence[str] | None = None) -> int:
    global args_global
    p = argparse.ArgumentParser(
        prog="cli.py",
        description="2027 高考复习系统 · 命令行入口（软件排程，纸上学习）")
    sub = p.add_subparsers(dest="cmd")

    sp = sub.add_parser("init", help="初始化数据库与依赖图")
    sp.add_argument("--reset-edges", action="store_true", help="清空依赖边后重建")
    sp.set_defaults(func=cmd_init)

    sp = sub.add_parser("today", help="今天该干什么（最常用）")
    sp.set_defaults(func=cmd_today)

    sp = sub.add_parser("pack", help="生成训练包 PDF")
    sp.add_argument("kind", help="A/B/C/D/E/F/CALC")
    sp.add_argument("subject", nargs="?", help="学科")
    sp.add_argument("kp", nargs="?", help="知识点名称（B/C 类必填）")
    sp.add_argument("--limit", type=int, default=None)
    sp.add_argument("--print", action="store_true", help="生成后送默认打印机")
    sp.add_argument("--force", action="store_true", help="忽略未解锁警告")
    sp.set_defaults(func=cmd_pack)

    sp = sub.add_parser("addq", help="交互式录入题目")
    sp.set_defaults(func=cmd_addq)

    sp = sub.add_parser("wrong", help="标记答错（必须给归因）")
    sp.add_argument("qid", type=int)
    sp.add_argument("attr", choices=list(srs.INTERVENTIONS.keys()))
    sp.set_defaults(func=cmd_wrong)

    sp = sub.add_parser("right", help="标记答对")
    sp.add_argument("qid", type=int)
    sp.set_defaults(func=cmd_right)

    sp = sub.add_parser("diag", help="录入诊断成绩并自动定基础期天数")
    sp.add_argument("--note", default="")
    sp.set_defaults(func=cmd_diag)

    sp = sub.add_parser("doctor", help="系统体检")
    sp.set_defaults(func=cmd_doctor)

    sp = sub.add_parser("kp", help="查看知识点依赖图")
    sp.add_argument("subject", nargs="?")
    sp.set_defaults(func=cmd_kp)

    sp = sub.add_parser("stats", help="进度看板")
    sp.set_defaults(func=cmd_stats)

    sp = sub.add_parser("seed-cards", help="生成首批记忆卡")
    sp.set_defaults(func=cmd_seed_cards)

    sp = sub.add_parser("plan90", help="生成《90 天基础知识总梳理·一轮总表》PDF（排程+每日自检练习）")
    sp.add_argument("--days", type=int, default=None, help="排程天数，默认取基础期天数（90）")
    sp.add_argument("--factor", type=float, default=None, help="唤醒系数，默认 0.55")
    sp.add_argument("--start", type=lambda x: datetime.strptime(x, "%Y-%m-%d").date(),
                    default=None, help="起始日期 YYYY-MM-DD，默认按考试日反推")
    sp.add_argument("--print", action="store_true", help="生成后送默认打印机")
    sp.set_defaults(func=cmd_plan90)

    sp = sub.add_parser("daily", help="生成《每日学习单》PDF（按进度排N天，先学后练，每天各科）")
    sp.add_argument("--days", type=int, default=30, help="排程天数，默认 30")
    sp.add_argument("--factor", type=float, default=None, help="唤醒系数，默认 0.55")
    sp.add_argument("--start", type=lambda x: datetime.strptime(x, "%Y-%m-%d").date(),
                    default=None, help="起始日期 YYYY-MM-DD，默认今天")
    sp.add_argument("--print", action="store_true", help="生成后送默认打印机")
    sp.set_defaults(func=cmd_daily)

    sp = sub.add_parser("book", help="生成《高考总复习·知识点详解》PDF（按科目分章，讲解+练习）")
    sp.add_argument("--print", action="store_true", help="生成后送默认打印机")
    sp.set_defaults(func=cmd_book)

    sp = sub.add_parser("user", help="用户管理（多用户：各自独立进度/错题/复习）")
    sp.add_argument("action", choices=["list", "add", "remove", "migrate"])
    sp.add_argument("name", nargs="?", default=None, help="用户名")
    sp.set_defaults(func=cmd_user)

    args = p.parse_args(argv)
    args_global = args
    if not getattr(args, "func", None):
        p.print_help()
        print("\n最常用：python cli.py init && python cli.py doctor && python cli.py today")
        return 0
    return args.func(args)


args_global = None

if __name__ == "__main__":
    raise SystemExit(main())
