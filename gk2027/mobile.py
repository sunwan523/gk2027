# -*- coding: utf-8 -*-
"""手机端学习界面（多邻国式）。

运行（电脑）：
    streamlit run mobile.py --server.address=0.0.0.0 --server.port=8577
手机连同一 WiFi 打开  http://<电脑IP>:8577  即可。

设计：
  - 不预排日历。每天打开 = 实时队列（前置已解锁的知识点课程）。
  - 学 = 一节课（知识点自检题，选择/填空自动判分，解答类看答案自评）。
  - 复习 = 间隔重复到期卡片（含错题卡）。
  - 少学的自动滚到明天（状态没变就还在队列）；有空就多做（队列不封顶）。
  - XP / 每日目标 / 连胜：纯激励，答对 +5，通关一节课 +20。
"""
from __future__ import annotations

import os
import sys
from datetime import date, timedelta

import streamlit as st
import streamlit.components.v1 as components

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import SUBJECTS, ATTRIBUTIONS
from core import db, graph, queue, seed_quiz, content, users

st.set_page_config(page_title="高考复习", page_icon="🔥", layout="centered",
                   initial_sidebar_state="collapsed")
st.markdown("""
<style>
/* 手机浏览器顶栏会盖住 Streamlit 自带 header，内容再往上叠一层。
   直接隐藏自带 header（菜单无用），并把内容区下移，确保我们的状态条完整可见。 */
header[data-testid="stHeader"] {display: none; height: 0;}
div.block-container {padding-top: 1.6rem; padding-bottom: 3rem; max-width: 720px;}
h1 {font-size: 1.5rem;}
button[data-testid="stButton"] > p {font-size: 1.05rem;}
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def _user_conn(uid: str):
    """每个用户一个独立库（进度/错题/卡片全隔离），首次使用自动灌种子。"""
    return db.init_db(users.db_path(uid), seed=True)


def conn():
    return _user_conn(st.session_state.uid)


# ----------------------------------------------------------------------
# 登录 / 用户切换
# 登录态存在浏览器会话（st.session_state）里，不是服务器全局——
# 两个人用不同手机同时打开，各自是各自的账号，互不顶替。
# ----------------------------------------------------------------------
def login_page():
    st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
    st.subheader("👋 你是谁？")
    existing = users.list_users()
    for u in existing:
        if st.button("🧑 %s" % u["name"], use_container_width=True,
                     key="login_%s" % u["id"]):
            st.session_state.uid = u["id"]
            st.rerun()
    if existing:
        st.caption("—— 或新同学 ——")
    name = st.text_input("输入名字，建立你的学习档案", key="new_name",
                         label_visibility="collapsed",
                         placeholder="名字（如：小明）")
    if st.button("✨ 开始使用", type="primary", use_container_width=True,
                 disabled=not name.strip()):
        try:
            u = users.ensure_user(name)
            st.session_state.uid = u["id"]
            st.rerun()
        except ValueError as e:
            st.error(str(e))
    st.caption("每个人的进度、错题、复习卡片独立保存，互不影响。")
    st.stop()


def _current_user() -> dict | None:
    uid = st.session_state.get("uid")
    if not uid:
        return None
    u = next((x for x in users.list_users() if x["id"] == uid), None)
    if u is None:
        st.session_state.pop("uid", None)   # 账号已被删除
    return u


# ----------------------------------------------------------------------
# 顶栏：连胜 / 今日 XP / 掌握进度
# ----------------------------------------------------------------------
def header_bar():
    c = conn()
    stt = queue.today_state(c)
    mastered, total = c.execute(
        "SELECT SUM(status='已掌握'), COUNT(*) FROM knowledge_points"
        " WHERE id NOT IN ('eng_vocab','chn_dictation')").fetchone()
    ratio = min(100, round(stt["xp_today"] / stt["xp_goal"] * 100))
    goal = "✅" if stt["goal_done"] else ""
    uname = (_current_user() or {}).get("name", "")
    # 单行 HTML：手机上列布局会把 #### 标题裁切，固定高度的 flex 行不受影响
    st.markdown(
        """
<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;
            background:#fff;border:1px solid #e5e5e5;border-radius:12px;
            padding:10px 14px;margin-top:10px;margin-bottom:8px;">
  <span style="font-size:1.05rem;font-weight:700;white-space:nowrap;">🧑 %s</span>
  <span style="font-size:1.15rem;font-weight:700;white-space:nowrap;">🔥 %d 天</span>
  <span style="font-size:1.15rem;font-weight:700;white-space:nowrap;">🏆 %d/%d</span>
  <span style="flex:1;min-width:140px;">
    <span style="font-size:.85rem;font-weight:600;">今日 XP %d/%d %s</span>
    <div style="background:#eee;border-radius:6px;height:10px;margin-top:3px;">
      <div style="background:#1fd16f;border-radius:6px;height:10px;width:%d%%;"></div>
    </div>
  </span>
</div>
""" % (uname, stt["streak"], mastered or 0, total,
       stt["xp_today"], stt["xp_goal"], goal, ratio),
        unsafe_allow_html=True)


# ----------------------------------------------------------------------
# 朗读：浏览器 Web Speech API（中文 TTS，无需联网、无需 API Key）
# ----------------------------------------------------------------------
def _render_tts_controls(pts: list[str]):
    """知识点要点朗读条：逐条/全部朗读、暂停继续、上下条、语速/音调/语音选择。"""
    import json
    js_pts = json.dumps(pts, ensure_ascii=False)
    html = """
<div style="background:#f0f7ff;border:1px solid #cfe2ff;border-radius:10px;padding:8px 12px;margin-bottom:8px;">
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;">
    <button onclick="prevPt()" style="border:1px solid #cfe2ff;background:#fff;border-radius:6px;padding:4px 8px;cursor:pointer;font-size:14px;">⏮</button>
    <button onclick="togglePlay()" id="ttsPlay" style="border:1px solid #4a90d9;background:#4a90d9;color:#fff;border-radius:6px;padding:4px 12px;cursor:pointer;font-size:13px;font-weight:600;">▶️ 朗读</button>
    <button onclick="nextPt()" style="border:1px solid #cfe2ff;background:#fff;border-radius:6px;padding:4px 8px;cursor:pointer;font-size:14px;">⏭</button>
    <button onclick="stopTts()" style="border:1px solid #f5c2c7;background:#fff;border-radius:6px;padding:4px 8px;cursor:pointer;font-size:14px;">⏹</button>
    <span style="font-size:11px;color:#666;">语速</span>
    <input type="range" id="ttsRate" min="0.5" max="1.8" step="0.1" value="1" oninput="setRate(this.value)" style="width:60px;vertical-align:middle;">
    <span style="font-size:11px;color:#666;">音调</span>
    <input type="range" id="ttsPitch" min="0.5" max="1.5" step="0.1" value="1" oninput="setPitch(this.value)" style="width:50px;vertical-align:middle;">
    <select id="ttsVoice" onchange="setVoice(this.value)" style="font-size:11px;padding:2px;border:1px solid #cfe2ff;border-radius:4px;max-width:140px;">
      <option value="">加载语音…</option>
    </select>
    <span id="ttsStat" style="font-size:11px;color:#888;margin-left:auto;">共 %d 条</span>
  </div>
</div>
<script>
var pts=%s,idx=0,playing=false,rate=1.0,pitch=1.0,utter=null,voices=[],curVoice=null;
function loadVoices(){voices=window.speechSynthesis.getVoices().filter(function(v){return v.lang&&v.lang.toLowerCase().indexOf('zh')>=0});
  var sel=document.getElementById('ttsVoice');if(!sel)return;
  sel.innerHTML='';var saved=localStorage.getItem('tts_voice');var found=false;
  if(voices.length===0){sel.innerHTML='<option value="">系统无中文语音</option>';return}
  voices.forEach(function(v,i){var o=document.createElement('option');o.value=i;o.text=v.name+(v.default?' (默认)':'');sel.appendChild(o);if(saved&&v.name===saved){sel.value=i;found=true;curVoice=v}});
  if(!found){curVoice=voices[0];sel.value=0}}
if(window.speechSynthesis.onvoiceschanged!==undefined){window.speechSynthesis.onvoiceschanged=loadVoices}
loadVoices();
function setVoice(i){curVoice=voices[parseInt(i)];localStorage.setItem('tts_voice',curVoice?curVoice.name:'');if(playing)speak(idx)}
function setRate(r){rate=parseFloat(r);localStorage.setItem('tts_rate',r);if(playing)speak(idx)}
function setPitch(p){pitch=parseFloat(p);localStorage.setItem('tts_pitch',p);if(playing)speak(idx)}
// 恢复保存的设置
try{var sr=localStorage.getItem('tts_rate');if(sr){rate=parseFloat(sr);document.getElementById('ttsRate').value=sr}
var sp=localStorage.getItem('tts_pitch');if(sp){pitch=parseFloat(sp);document.getElementById('ttsPitch').value=sp}}catch(e){}
function speak(i){if(i<0||i>=pts.length)return;idx=i;window.speechSynthesis.cancel();
utter=new SpeechSynthesisUtterance(pts[i]);utter.lang='zh-CN';utter.rate=rate;utter.pitch=pitch;if(curVoice)utter.voice=curVoice;
utter.onend=function(){if(idx<pts.length-1){speak(idx+1)}else{playing=false;document.getElementById('ttsPlay').textContent='▶️ 朗读';document.getElementById('ttsStat').textContent='朗读完成'}};
utter.onerror=function(){playing=false;document.getElementById('ttsPlay').textContent='▶️ 朗读'};
window.speechSynthesis.speak(utter);playing=true;
document.getElementById('ttsPlay').textContent='⏸ 暂停';
document.getElementById('ttsStat').textContent='第 '+(idx+1)+'/'+pts.length+' 条'}
function togglePlay(){if(playing){window.speechSynthesis.pause();playing=false;document.getElementById('ttsPlay').textContent='▶️ 继续'}
else if(window.speechSynthesis.paused){window.speechSynthesis.resume();playing=true;document.getElementById('ttsPlay').textContent='⏸ 暂停'}
else{speak(idx)}}
function stopTts(){window.speechSynthesis.cancel();playing=false;document.getElementById('ttsPlay').textContent='▶️ 朗读';document.getElementById('ttsStat').textContent='已停止'}
function prevPt(){if(idx>0)speak(idx-1)}
function nextPt(){if(idx<pts.length-1)speak(idx+1)}
</script>
""" % (len(pts), js_pts)
    components.html(html, height=56, scrolling=False)


# ----------------------------------------------------------------------
# 学：课程队列 + 答题流水线
# ----------------------------------------------------------------------
def render_lesson():
    c = conn()
    L = st.session_state.lesson
    qs = L["qs"]

    if L["phase"] == "done":
        st.balloons()
        st.subheader("🎉 通关：%s" % L["name"])
        if not L.get("rewarded"):
            L["rewarded"] = True
            L["reward"] = queue.finish_lesson(c, L["kp_id"], all(L["results"]))
        r = L["reward"]
        st.success("+%d XP（全对奖励 %s）" % (r["bonus"], "已含" if all(L["results"]) else "未含"))
        row = c.execute("SELECT mastery,status FROM knowledge_points WHERE id=?",
                        (L["kp_id"],)).fetchone()
        st.markdown("掌握度 **%d%%**（%s）" % (round(row["mastery"] * 100), row["status"]))
        if r["newly_unlocked"]:
            st.info("🔓 解锁了 %d 节新课" % r["newly_unlocked"])
        # AI出题测试
        if st.button("🤖 AI出题测试（再练5题）", use_container_width=True):
            L["phase"] = "ai_loading"
            st.rerun()
        if st.button("返回课程列表", type="primary"):
            st.session_state.lesson = None
            st.rerun()
        return

    # AI出题加载
    if L["phase"] == "ai_loading":
        from core import ai_quiz
        st.subheader("🤖 AI出题中…")
        st.caption("正在根据「%s」的知识点内容生成测试题" % L["name"])
        with st.spinner("DeepSeek 正在出题，请稍候…"):
            try:
                # 获取科目
                kp_row = c.execute("SELECT subject FROM knowledge_points WHERE id=?",
                                  (L["kp_id"],)).fetchone()
                subject = kp_row["subject"] if kp_row else "数学"
                ai_qs = ai_quiz.generate_quiz(
                    subject, L["name"], L.get("points", []), count=5)
                L["ai_qs"] = ai_qs
                L["ai_idx"] = 0
                L["ai_results"] = []
                L["phase"] = "ai_q"
                st.rerun()
            except Exception as e:
                st.error("AI出题失败：%s" % str(e)[:200])
                if st.button("返回"):
                    L["phase"] = "done"
                    st.rerun()
                return

    # AI出题答题
    if L["phase"] in ("ai_q", "ai_fb"):
        ai_qs = L.get("ai_qs", [])
        ai_idx = L.get("ai_idx", 0)
        if ai_idx >= len(ai_qs):
            # AI测试完成
            st.balloons()
            st.subheader("🤖 AI测试完成")
            correct = sum(L.get("ai_results", []))
            total = len(ai_qs)
            st.markdown("答对 **%d / %d** 题" % (correct, total))
            if correct == total:
                st.success("全对！掌握得很扎实 🔥")
            elif correct >= total * 0.6:
                st.info("不错，再复习一下错题就更好了")
            else:
                st.warning("建议回到知识点卡片再复习一遍")
            if st.button("返回课程列表", type="primary"):
                st.session_state.lesson = None
                st.rerun()
            return

        q = ai_qs[ai_idx]
        st.progress(ai_idx / max(1, len(ai_qs)))
        st.caption("🤖 AI出题 · 第 %d/%d 题 · %s" % (ai_idx + 1, len(ai_qs), q["qtype"]))
        st.markdown("##### %s" % q["stem"])

        key = "ai_ans_%d" % ai_idx
        if L["phase"] == "ai_q":
            if q["qtype"] == "选择题":
                labels = q["options"] or ["（无选项）"]
                st.radio("选择答案", labels, key=key, label_visibility="collapsed")
                if st.button("提交答案", type="primary", use_container_width=True):
                    pick = st.session_state.get(key, "")
                    letter = ""
                    for o in q["options"]:
                        if o == pick:
                            letter = queue._letter_of(o)
                    ok = queue.grade_choice(letter, q["answer"]) if q["options"] else False
                    L["ai_results"].append(ok)
                    L["phase"] = "ai_fb"
                    L["ai_last"] = ok
                    st.rerun()
            else:
                st.text_input("你的答案", key=key, placeholder="输入答案")
                if st.button("提交答案", type="primary", use_container_width=True):
                    ok = queue.grade_fill(st.session_state.get(key, ""), q["answer"])
                    L["ai_results"].append(ok)
                    L["phase"] = "ai_fb"
                    L["ai_last"] = ok
                    st.rerun()

        if L["phase"] == "ai_fb":
            if L.get("ai_last"):
                st.success("✅ 答对了")
            else:
                st.error("❌ 答错了")
            st.markdown("**答案：** %s" % q["answer"])
            if q["analysis"]:
                st.markdown("解析：%s" % q["analysis"])
            if st.button("下一题 →", type="primary", use_container_width=True):
                L["ai_idx"] = ai_idx + 1
                L["phase"] = "ai_q"
                st.rerun()
        return

    if L["phase"] == "learn":
        st.subheader("📖 %s" % L["name"])
        pts = L.get("points") or []
        if not pts:
            st.info("该知识点暂无详细讲解，可直接进入练习。")
        else:
            # 卡片式翻页学习
            card_idx = L.get("card_idx", 0)
            total = len(pts)

            # 朗读控制条
            _render_tts_controls(pts)

            # 卡片进度
            st.progress(card_idx / max(1, total - 1))
            st.caption("卡片 %d / %d" % (card_idx + 1, total))

            # 当前卡片
            with st.container(border=True):
                st.markdown(
                    """
                    <div style="padding:20px 16px;min-height:180px;
                                display:flex;align-items:center;justify-content:center;
                                background:linear-gradient(135deg,#f8f9ff,#eef2ff);
                                border-radius:12px;margin:8px 0;">
                      <div style="font-size:15px;line-height:1.8;color:#1a1b1c;text-align:left;width:100%;">
                        %s
                      </div>
                    </div>
                    """.replace("                    ", "") % pts[card_idx],
                    unsafe_allow_html=True)

            # 翻页按钮
            col_p, col_n = st.columns(2)
            if col_p.button("⬅️ 上一张", disabled=(card_idx == 0),
                           use_container_width=True):
                L["card_idx"] = card_idx - 1
                st.rerun()
            if col_n.button("下一张 ➡️", disabled=(card_idx >= total - 1),
                           use_container_width=True):
                L["card_idx"] = card_idx + 1
                st.rerun()

            # 快速跳选
            with st.expander("跳转到指定卡片"):
                jump = st.slider("卡片", 1, total, card_idx + 1,
                                 key="card_jump")
                if st.button("跳转", use_container_width=True):
                    L["card_idx"] = jump - 1
                    st.rerun()

        st.divider()
        b1, b2 = st.columns([3, 1])
        if b1.button("我学完了，开始练习 ✏️", type="primary",
                     use_container_width=True):
            L["phase"] = "q"
            st.rerun()
        if b2.button("跳过", use_container_width=True):
            L["phase"] = "q"
            st.rerun()
        return

    q = qs[L["idx"]]
    st.progress(L["idx"] / max(1, len(qs)))
    st.caption("%s · 第 %d/%d 题 · %s" % (L["name"], L["idx"] + 1, len(qs), q["qtype"]))
    st.markdown("##### %s" % q["stem"])

    key = "ans_%d" % q["qid"]

    if L["phase"] == "q":
        if q["qtype"] == "选择题":
            labels = q["options"] or ["（无选项，看答案自评）"]
            st.radio("选择答案", labels, key=key, label_visibility="collapsed")
            if st.button("提交答案", type="primary", use_container_width=True):
                pick = st.session_state.get(key, "")
                letter = ""
                for o in q["options"]:
                    if o == pick:
                        letter = queue._letter_of(o)
                ok = queue.grade_choice(letter, q["answer"]) if q["options"] else False
                _after_answer(c, L, q, ok)
        elif q["qtype"] == "填空题":
            st.text_input("你的答案", key=key, placeholder="多空用 ; 分隔")
            if st.button("提交答案", type="primary", use_container_width=True):
                ok = queue.grade_fill(st.session_state.get(key, ""), q["answer"])
                _after_answer(c, L, q, ok)
        else:
            st.caption("先在纸上/脑中作答，再看答案诚实自评")
            if st.button("看答案", use_container_width=True):
                L["phase"] = "peek"
                st.rerun()

    if L["phase"] == "peek":
        st.info("**答案：** %s" % q["answer"])
        if q["analysis"]:
            st.markdown("解析：%s" % q["analysis"])
        c1, c2 = st.columns(2)
        if c1.button("✅ 我答对了", use_container_width=True):
            _after_answer(c, L, q, True, show_feedback=False)
            _advance(L)
            st.rerun()
        if c2.button("❌ 答错了", use_container_width=True):
            _after_answer(c, L, q, False)

    if L["phase"] == "fb":
        if L["last_correct"]:
            st.success("✅ 答对了  +%d XP" % queue.XP_PER_CORRECT)
        else:
            st.error("❌ 答错了，已进错题本（稍后会自动复习）")
        st.markdown("**答案：** %s" % q["answer"])
        if q["analysis"]:
            st.markdown("解析：%s" % q["analysis"])
        if not L["last_correct"]:
            attr = st.selectbox("错在哪一类？（决定下一步怎么练）",
                                ["（默认：概念不清）"] + list(ATTRIBUTIONS), key="attr_%d" % q["qid"])
            if attr != "（默认：概念不清）":
                queue.set_wrong_attribution(c, q["qid"], attr)
        label = "完成本节 🎉" if L["idx"] + 1 >= len(qs) else "下一题 →"
        if st.button(label, type="primary", use_container_width=True):
            _advance(L)
            st.rerun()


def _after_answer(c, L, q, ok, show_feedback=True):
    queue.submit_answer(c, q["qid"], ok, kp_id=L["kp_id"])
    L["results"].append(ok)
    L["last_correct"] = ok
    L["phase"] = "fb" if show_feedback else "q"


def _advance(L):
    L["idx"] += 1
    L["phase"] = "q"
    if L["idx"] >= len(L["qs"]):
        L["phase"] = "done"


def open_lesson(kp_id: str, name: str):
    c = conn()
    qs = queue.start_lesson(c, kp_id)
    if not qs:
        st.warning("该知识点暂无自检题。")
        return
    pts = content.get_content(kp_id)
    st.session_state.lesson = {"kp_id": kp_id, "name": name, "qs": qs,
                               "idx": 0, "phase": "learn", "results": [],
                               "last_correct": False, "points": pts,
                               "card_idx": 0}


ICON = {"可学": "▶️", "学习中": "🔶", "需复习": "🔁", "已掌握": "✅", "未解锁": "🔒"}


def page_learn():
    c = conn()
    if st.session_state.get("lesson"):
        render_lesson()
        return
    subj = st.radio("科目", ["全部"] + SUBJECTS, horizontal=True,
                    label_visibility="collapsed")
    s = None if subj == "全部" else subj
    lessons = queue.available_lessons(c, subject=s)
    if not lessons:
        # 区分三种空队列情况，避免误报"通关"
        if s:
            total = c.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE subject=? AND id NOT IN ('eng_vocab','chn_dictation')",
                (s,)).fetchone()[0]
            mastered = c.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE subject=? AND status='已掌握' AND id NOT IN ('eng_vocab','chn_dictation')",
                (s,)).fetchone()[0]
            locked = c.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE subject=? AND status='未解锁' AND id NOT IN ('eng_vocab','chn_dictation')",
                (s,)).fetchone()[0]
            no_quiz = c.execute(
                "SELECT COUNT(*) FROM knowledge_points k WHERE subject=? AND id NOT IN ('eng_vocab','chn_dictation') AND id NOT IN (SELECT DISTINCT kp_id FROM questions WHERE kp_id IS NOT NULL)",
                (s,)).fetchone()[0]
            if mastered >= total and total > 0:
                st.success("该科目已全部通关 🎉 去复习页巩固或换个科目。")
            elif locked > 0 and mastered == 0:
                st.info("该科目高中课程尚未解锁（%d 节），先完成初中诊断课程即可解锁。" % locked)
            elif no_quiz > 0:
                st.warning("该科目有 %d 节课程暂无自检题，内容可在「导出」页生成 PDF 学习。" % no_quiz)
            else:
                st.success("该科目已解锁课程全部通关 🎉 换个科目或去复习页。")
        else:
            st.success("所有已解锁课程全部通关 🎉 去复习页巩固吧。")
        return
    st.caption("共 %d 节可学（做完的会自动滚出队列，没做的明天还在）" % len(lessons))
    for i, ls in enumerate(lessons[:40]):
        with st.container(border=True):
            c1, c2 = st.columns([5, 1.6])
            c1.markdown("%s **%s·%s**" % (ICON.get(ls["status"], ""), ls["subject"], ls["name"]))
            c1.caption("掌握度 %d%%｜自检题 %d/%d｜约 %d 分钟" % (
                ls["mastery"], ls["q_done"], ls["q_total"], ls["minutes"]))
            if c2.button("开始", key="go_%s" % ls["kp_id"], type="primary"):
                open_lesson(ls["kp_id"], ls["name"])
                st.rerun()


# ----------------------------------------------------------------------
# 复习：到期卡片
# ----------------------------------------------------------------------
def page_review():
    c = conn()
    cards = queue.due_reviews(c)
    if not cards:
        st.success("🎉 今日没有到期的复习卡片。")
        return
    idx = st.session_state.get("review_idx", 0)
    if idx >= len(cards):
        st.balloons()
        st.success("本轮复习完成！共复习 %d 张卡。" % idx)
        if st.button("再来一轮检查", key="re_review"):
            st.session_state.review_idx = 0
            st.rerun()
        return
    card = cards[idx]
    st.progress(idx / len(cards))
    st.caption("复习 %d/%d · %s · %s" % (idx + 1, len(cards), card["subject"], card["kind"]))
    st.markdown("##### %s" % card["front"])
    if st.button("显示答案", key="peek_card", use_container_width=True):
        st.session_state.card_peek = card["card_id"]
    if st.session_state.get("card_peek") == card["card_id"]:
        st.info(card["back"] or "（无背面内容）")
        c1, c2 = st.columns(2)
        if c1.button("😅 忘了", key="forgot", use_container_width=True):
            queue.review_result(c, card["card_id"], False)
            st.session_state.card_peek = None
            st.session_state.review_idx = idx + 1
            st.rerun()
        if c2.button("🙂 记得", key="remembered", type="primary", use_container_width=True):
            queue.review_result(c, card["card_id"], True)
            st.session_state.card_peek = None
            st.session_state.review_idx = idx + 1
            st.rerun()


# ----------------------------------------------------------------------
# 进度
# ----------------------------------------------------------------------
def page_progress():
    c = conn()
    tree = queue.lesson_tree(c)
    total_m = sum(t["mastered"] for t in tree)
    total_n = sum(t["total"] for t in tree)
    st.progress(total_m / max(1, total_n))
    st.caption("一轮总进度 %d / %d 知识点已掌握" % (total_m, total_n))
    for t in tree:
        with st.expander("%s %d/%d" % (t["subject"], t["mastered"], t["total"]),
                         expanded=False):
            for it in t["items"]:
                if it["status"] == "已掌握":
                    mark = "✅"
                elif it["status"] == "未解锁":
                    mark = "🔒"
                else:
                    mark = "🔶" if it["status"] in ("学习中", "需复习") else "▶️"
                extra = "" if it["has_quiz"] else "（自检题待补）"
                st.markdown("%s %s %d%%%s" % (mark, it["name"], it["mastery"], extra))

    st.divider()
    st.subheader("近 14 天 XP")
    log = db.get_setting(c, "xp_log", {}) or {}
    days = [(date.today() - timedelta(days=k)).isoformat() for k in range(13, -1, -1)]
    st.bar_chart({d[5:]: log.get(d, 0) for d in days})

    st.divider()
    if st.button("🔄 切换用户 / 退出", use_container_width=True):
        st.session_state.pop("uid", None)
        st.session_state.lesson = None
        st.rerun()


# ----------------------------------------------------------------------
# 导出：每日学习单 / 总复习文档 PDF（手机生成→发送到电脑/手机直接打印）
# ----------------------------------------------------------------------
def page_export():
    import io
    from datetime import date as _date
    from core import daily as dy, pdf, content as content_mod
    c = conn()
    content_mod.reload_content()   # 内容文件有更新时立即生效
    st.caption("生成的 PDF 可发送到电脑打印，或手机连打印机直接打。"
               "每日学习单＝按你当前进度排（已掌握的自动跳过，不重复）；"
               "总复习文档＝全部知识点讲解+练习，按科目分章。")
    days = st.slider("每日学习单排多少天", 7, 90, 30, step=1, key="exp_days")
    if st.button("📄 生成《每日学习单》PDF", type="primary", use_container_width=True):
        with st.spinner("排程并生成中…"):
            plans = dy.build_daily_plan(c, _date.today(), days=days)
            if not plans:
                st.warning("没有待学内容（都已掌握？）。")
                return
            path = pdf.build_daily_plan_pdf(c, plans, start=_date.today())
        data = io.BytesIO(open(path, "rb").read())
        st.download_button("⬇️ 下载每日学习单（%d 天）" % len(plans), data,
                           file_name=os.path.basename(path),
                           mime="application/pdf", use_container_width=True)
    if st.button("📚 生成《高考总复习·知识点详解》PDF", use_container_width=True):
        with st.spinner("全书生成中，需要一点时间…"):
            path = pdf.build_review_book_pdf(c)
        data = io.BytesIO(open(path, "rb").read())
        st.download_button("⬇️ 下载总复习文档", data,
                           file_name=os.path.basename(path),
                           mime="application/pdf", use_container_width=True)
    if st.button("📖 生成《背诵手册》PDF（语文名句+英语词汇+作文模板）", use_container_width=True):
        with st.spinner("背诵手册生成中…"):
            path = pdf.build_dictation_pdf(c)
        data = io.BytesIO(open(path, "rb").read())
        st.download_button("⬇️ 下载背诵手册", data,
                           file_name=os.path.basename(path),
                           mime="application/pdf", use_container_width=True)
    cov = content_mod.coverage()
    st.caption("详解进度：" + "｜".join(
        "%s %d/%d" % (s, g, t) for s, (g, t) in cov["by_subject"].items()))


# ----------------------------------------------------------------------
# 背诵页：语文/英语分类背诵 + 逐条朗读 + 全部连播 + 已背标记
# ----------------------------------------------------------------------
RECITE_CATALOG = {
    "语文": [
        ("chn_dictation", "名句名篇默写"),
        ("chn_wenyan_word", "文言文120实词"),
        ("chn_essay_material", "作文素材库"),
        ("chn_read_argue", "现代文答题模板"),
    ],
    "英语": [
        ("eng_vocab", "核心词汇3500"),
        ("eng_write_apply", "作文万能模板"),
        ("eng_grammar_fill", "语法填空高频考点"),
    ],
}


def page_recite():
    c = conn()
    from core import content as content_mod
    content_mod.reload_content()

    st.subheader("📖 背诵听读")
    st.caption("出门随身背：选科目→选分类→逐条听读，已背的打勾，进度自动保存。")

    col_s, col_c = st.columns([1, 2])
    subject = col_s.radio("科目", list(RECITE_CATALOG.keys()), horizontal=True,
                          label_visibility="collapsed")
    cats = RECITE_CATALOG[subject]
    cat_names = [c[1] for c in cats]
    cat_idx = col_c.radio("分类", cat_names, horizontal=True, label_visibility="collapsed")
    kp_id = cats[cat_names.index(cat_idx)][0]

    pts = content_mod.get_content(kp_id) or []
    if not pts:
        st.info("该分类内容整理中，先看看其他分类。")
        return

    # 搜索过滤
    kw = st.text_input("🔍 搜索关键词（留空显示全部）", "", key="recite_search")
    if kw.strip():
        filtered = [p for p in pts if kw.lower() in p.lower()]
    else:
        filtered = pts

    st.caption("共 %d 条%s" % (len(filtered), "（搜索结果）" if kw.strip() else ""))

    # 朗读控制条（全部连播）
    _render_tts_controls(filtered)

    # 已背统计
    recite_key = "recite_done_%s" % kp_id
    done_set = set(st.session_state.get(recite_key, set()))

    # 内容列表 + 逐条朗读 + 已背标记（大HTML组件）
    import json
    items_json = json.dumps(filtered, ensure_ascii=False)
    done_json = json.dumps(sorted(done_set), ensure_ascii=False)
    html = """
<div id="reciteList" style="margin-top:6px;">
<script>
var items=%s, doneSet=new Set(%s), kpId='%s';
var reciteVoices=[],reciteVoice=null,reciteRate=1.0,recitePitch=1.0;
function reciteLoadVoices(){reciteVoices=window.speechSynthesis.getVoices().filter(function(v){return v.lang&&v.lang.toLowerCase().indexOf('zh')>=0});
  var saved=localStorage.getItem('tts_voice');reciteVoice=reciteVoices.find(function(v){return v.name===saved})||reciteVoices[0]||null;
  var sr=localStorage.getItem('tts_rate');if(sr)reciteRate=parseFloat(sr);
  var sp=localStorage.getItem('tts_pitch');if(sp)recitePitch=parseFloat(sp);}
if(window.speechSynthesis.onvoiceschanged!==undefined){window.speechSynthesis.onvoiceschanged=reciteLoadVoices}
reciteLoadVoices();
function speakOne(i){window.speechSynthesis.cancel();reciteLoadVoices();
  var u=new SpeechSynthesisUtterance(items[i]);u.lang='zh-CN';u.rate=reciteRate;u.pitch=recitePitch;if(reciteVoice)u.voice=reciteVoice;
  window.speechSynthesis.speak(u);}
function toggleDone(i){var cb=document.getElementById('done_'+i);
  if(cb.checked){doneSet.add(i)}else{doneSet.delete(i)}
  var arr=Array.from(doneSet).sort(function(a,b){return a-b});
  var xhr=new XMLHttpRequest();
  // 用 localStorage 持久化已背标记
  localStorage.setItem('recite_'+kpId, JSON.stringify(arr));
  document.getElementById('doneCount').textContent=arr.length+'/'+items.length;}
// 从 localStorage 恢复
try{var saved=JSON.parse(localStorage.getItem('recite_'+kpId)||'[]');saved.forEach(function(i){doneSet.add(i);});}catch(e){}
document.write('<div style=\"font-size:12px;color:#888;margin-bottom:8px;\">已背 <span id=\"doneCount\">'+doneSet.size+'/'+items.length+'</span></div>');
for(var i=0;i<items.length;i++){
  var isDone=doneSet.has(i);
  document.write('<div style=\"background:'+(isDone?'#f0fff0':'#fff')+';border:1px solid #e5e5e5;border-radius:8px;padding:8px 10px;margin-bottom:6px;\">');
  document.write('<div style=\"display:flex;align-items:flex-start;gap:8px;\">');
  document.write('<input type=\"checkbox\" id=\"done_'+i+'\" '+(isDone?'checked':'')+' onchange=\"toggleDone('+i+')\" style=\"margin-top:3px;flex-shrink:0;\">');
  document.write('<div style=\"flex:1;font-size:13px;line-height:1.6;color:'+(isDone?'#999':'#1A1B1C')+';\">'+items[i].replace(/</g,'&lt;').replace(/>/g,'&gt;')+'</div>');
  document.write('<button onclick=\"speakOne('+i+')\" style=\"border:1px solid #cfe2ff;background:#f0f7ff;border-radius:6px;padding:2px 8px;cursor:pointer;font-size:12px;flex-shrink:0;\">🔊</button>');
  document.write('</div></div>');
}
</script>
</div>
""" % (items_json, done_json, kp_id)
    components.html(html, height=min(600, max(200, len(filtered) * 55)), scrolling=True)


# ----------------------------------------------------------------------
# 主入口：未登录先出登录页
# ----------------------------------------------------------------------
if _current_user() is None:
    login_page()

header_bar()
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 学", "🔁 复习", "📈 进度", "📄 导出", "📖 背诵"])
with tab1:
    page_learn()
with tab2:
    page_review()
with tab3:
    page_progress()
with tab4:
    page_export()
with tab5:
    page_recite()
