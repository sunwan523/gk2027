import streamlit as st
from datetime import datetime
import json
import random

st.set_page_config(
    page_title="高考冲刺 · 智能复习系统",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

from data.subjects import get_subjects, get_subject_color, get_subject_total_kps
from data.progress import init_progress, get_progress, update_progress, get_last_kp_index, set_current_kp_index, get_total_progress
from data.knowledge_loader import load_knowledge
from data.questions_loader import load_questions
from data.study_plan import load_plan_progress, get_current_day, mark_task_completed, get_plan_summary, get_day_plan
from data.real_exam_loader import (
    load_real_exam_questions, get_real_exam_count, get_uncompleted_questions,
    add_completed_question, get_completed_questions
)

init_progress()

def get_days_left():
    exam_date = datetime(2026, 6, 7)
    today = datetime.now()
    return max(0, (exam_date - today).days)

# ============================================================
# HTML/CSS 组件
# ============================================================

def load_css():
    """加载全局样式"""
    return st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');

    * { font-family: 'Noto Sans SC', sans-serif; }

    .main .block-container { padding: 0.8rem 1.5rem; max-width: 100%; }

    /* 整体背景渐变 */
    .stApp {
        background: linear-gradient(135deg, #f0f4ff 0%, #faf5ff 50%, #fef2f2 100%);
    }

    /* 玻璃卡片效果 */
    .glass-card {
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 1rem;
        padding: 1.2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border: 1px solid rgba(255,255,255,0.7);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    .glass-card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        transform: translateY(-1px);
    }

    /* 科目卡片 */
    .subject-card-modern {
        border-radius: 1rem;
        padding: 1.2rem;
        color: white;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .subject-card-modern::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 100%;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        transform: rotate(30deg);
    }
    .subject-card-modern:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.2);
    }

    /* 喇叭按钮 */
    .speaker-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: none;
        background: #6366f1;
        color: white;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(99,102,241,0.3);
    }
    .speaker-btn:hover {
        background: #4f46e5;
        transform: scale(1.1);
        box-shadow: 0 4px 15px rgba(99,102,241,0.4);
    }
    .speaker-btn.speaking {
        background: #10b981;
        animation: pulse 1.5s infinite;
    }
    .speaker-btn.stopped {
        background: #ef4444;
    }
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(16,185,129,0.4); }
        50% { box-shadow: 0 0 0 12px rgba(16,185,129,0); }
    }

    /* 进度条 */
    .progress-modern {
        height: 8px;
        border-radius: 4px;
        background: #e2e8f0;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    .progress-modern .fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.8s ease;
        background: linear-gradient(90deg, #6366f1, #a78bfa);
    }

    /* 知识点标签 */
    .kp-badge {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 0.5rem;
        font-size: 12px;
        font-weight: 500;
        margin: 0.15rem;
        cursor: pointer;
        transition: all 0.2s;
    }
    .kp-badge:hover { opacity: 0.8; transform: scale(1.05); }
    .kp-badge.completed { opacity: 0.6; text-decoration: line-through; }

    /* 学习板块标签 */
    .section-tab {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.4rem 1rem;
        border-radius: 2rem;
        font-size: 13px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
        border: 1px solid transparent;
    }
    .section-tab:hover { opacity: 0.85; }
    .section-tab.active {
        background: white;
        border-color: #6366f1;
        color: #4338ca;
        box-shadow: 0 2px 8px rgba(99,102,241,0.15);
    }

    /* 按钮 */
    .stButton>button {
        border-radius: 0.75rem;
        border: none;
        transition: all 0.25s ease;
        font-weight: 500;
        height: 2.5rem;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    }

    /* 侧边栏 */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8faff 0%, #f0f0ff 100%);
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 0.5rem;
    }

    /* 知识板块内容卡片 */
    .content-section {
        border-radius: 0.75rem;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        border-left: 4px solid;
        transition: all 0.3s;
    }
    .content-section:hover {
        transform: translateX(3px);
    }
    .content-section .title {
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .content-section .body {
        font-size: 14px;
        line-height: 1.8;
        color: #334155;
    }

    /* 统计数字 */
    .stat-number {
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* 复盘知识点卡片 */
    .review-card {
        padding: 0.8rem 1rem;
        border-radius: 0.75rem;
        background: white;
        border: 1px solid #e2e8f0;
        margin-bottom: 0.5rem;
        transition: all 0.2s;
        cursor: pointer;
    }
    .review-card:hover {
        border-color: #a5b4fc;
        box-shadow: 0 2px 12px rgba(99,102,241,0.1);
    }
    .review-card .emoji { font-size: 1.2rem; margin-right: 0.5rem; }

    /* 3D翻页效果按钮 */
    .flip-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 2rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
    }
    .flip-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102,126,234,0.4);
    }

    /* 移动端适配 */
    @media (max-width: 768px) {
        .main .block-container { padding: 0.5rem; }
        .subject-card-modern { padding: 0.8rem; }
    }
    </style>
    """, unsafe_allow_html=True)


def tts_script():
    """注入 TTS JavaScript"""
    return st.markdown("""
    <script>
    // TTS 朗读功能
    let ttsUtterance = null;
    let ttsPlaying = false;

    function speakText(text, btnId) {
        if (!window.speechSynthesis) {
            alert('您的浏览器不支持语音朗读功能，请使用Chrome浏览器');
            return;
        }

        if (ttsPlaying) {
            window.speechSynthesis.cancel();
            ttsPlaying = false;
            const btn = document.getElementById(btnId);
            if (btn) {
                btn.innerHTML = '🔊';
                btn.className = 'speaker-btn';
            }
            return;
        }

        window.speechSynthesis.cancel();

        ttsUtterance = new SpeechSynthesisUtterance(text);
        ttsUtterance.lang = 'zh-CN';
        ttsUtterance.rate = 1.0;
        ttsUtterance.pitch = 1.0;
        ttsUtterance.volume = 1.0;

        // 尝试选择中文语音
        const voices = window.speechSynthesis.getVoices();
        const zhVoice = voices.find(v => v.lang.startsWith('zh'));
        if (zhVoice) ttsUtterance.voice = zhVoice;

        ttsUtterance.onstart = function() {
            ttsPlaying = true;
            const btn = document.getElementById(btnId);
            if (btn) {
                btn.innerHTML = '⏹';
                btn.className = 'speaker-btn speaking';
            }
        };

        ttsUtterance.onend = function() {
            ttsPlaying = false;
            const btn = document.getElementById(btnId);
            if (btn) {
                btn.innerHTML = '🔊';
                btn.className = 'speaker-btn';
            }
        };

        ttsUtterance.onerror = function() {
            ttsPlaying = false;
            const btn = document.getElementById(btnId);
            if (btn) {
                btn.innerHTML = '🔊';
                btn.className = 'speaker-btn';
            }
        };

        window.speechSynthesis.speak(ttsUtterance);
        const btn = document.getElementById(btnId);
        if (btn) {
            btn.innerHTML = '🔊';
            btn.className = 'speaker-btn';
        }
    }

    // 监听来自Streamlit的TTS请求
    document.addEventListener('click', function(e) {
        if (e.target && e.target.classList.contains('speaker-btn')) {
            const textId = e.target.getAttribute('data-text-id');
            if (textId) {
                const textEl = document.getElementById(textId);
                if (textEl) {
                    speakText(textEl.textContent, e.target.id);
                }
            }
        }
    });
    </script>
    """, unsafe_allow_html=True)


def get_kp_emoji(kp_name):
    """根据知识点名称返回对应表情"""
    emoji_map = {
        '文言文': '📜',
        '诗词': '📝',
        '作文': '✏️',
        '阅读': '📖',
        '语言': '💬',
        '字音': '🔤',
        '词语': '📚',
        '病句': '🔍',
        '函数': '📈',
        '方程': '⚖️',
        '不等式': '⚖️',
        '数列': '🔢',
        '三角': '📐',
        '几何': '📐',
        '向量': '➡️',
        '导数': '📊',
        '积分': '∫',
        '概率': '🎲',
        '统计': '📊',
        '复数': '🔢',
        '集合': '📋',
        '圆': '⭕',
        '椭圆': '🔵',
        '双曲线': '〰️',
        '抛物线': '↗️',
        '名词': '🏷️',
        '代词': '👤',
        '动词': '🏃',
        '时态': '⏰',
        '从句': '🔗',
        '语法': '📝',
        '阅读': '📖',
        '写作': '✍️',
        '物理': '⚛️',
        '运动': '🏃',
        '力': '💪',
        '牛顿': '🍎',
        '功': '⚡',
        '能': '⚡',
        '动量': '🏓',
        '电场': '⚡',
        '磁场': '🧲',
        '电磁': '🧲',
        '电路': '🔌',
        '光': '💡',
        '振动': '〰️',
        '波': '🌊',
        '热': '🔥',
        '化学': '🧪',
        '原子': '⚛️',
        '分子': '🧬',
        '离子': '⚡',
        '氧化': '🔥',
        '还原': '⬇️',
        '酸碱': '🧪',
        '盐': '🧂',
        '金属': '🔩',
        '有机': '🧬',
        '反应': '⚗️',
        '生物': '🧬',
        '细胞': '🔬',
        'DNA': '🧬',
        '基因': '🧬',
        '遗传': '🧬',
        '变异': '🔄',
        '进化': '🌿',
        '生态': '🌍',
        '光合': '☀️',
        '呼吸': '🫁',
        '神经': '🧠',
        '免疫': '🛡️',
        '激素': '🧪',
    }
    for key, emoji in emoji_map.items():
        if key in kp_name:
            return emoji
    return '📚'


def main():
    load_css()

    with st.sidebar:
        show_sidebar()

    if st.session_state.view_mode == "subject":
        show_subject_select()
    elif st.session_state.view_mode == "study":
        show_study_view()
    elif st.session_state.view_mode == "practice":
        show_practice_view()
    elif st.session_state.view_mode == "wrong":
        show_wrong_view()
    elif st.session_state.view_mode == "plan":
        show_plan_view()
    elif st.session_state.view_mode == "real_exam":
        show_real_exam_view()
    elif st.session_state.view_mode == "real_exam_practice":
        show_real_exam_practice_view()
    elif st.session_state.view_mode == "wrong_real_exam":
        show_wrong_real_exam_view()
    elif st.session_state.view_mode == "review":
        show_review_view()


# ============================================================
# 侧边栏
# ============================================================

def show_sidebar():
    days_left = get_days_left()
    st.markdown(f"""
    <div style="text-align:center;padding:0.8rem 0 1.2rem;">
        <div style="font-size:26px;font-weight:900;background:linear-gradient(135deg,#6366f1,#a78bfa,#f472b6);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
                    margin-bottom:0.3rem;">🎯 高考冲刺</div>
        <div style="font-size:13px;color:#64748b;">
            距离高考还有 <span style="color:#ef4444;font-weight:700;font-size:18px;">{days_left}</span> 天
        </div>
        <div style="font-size:11px;color:#94a3b8;margin-top:0.2rem;">2026年6月7日</div>
    </div>
    """, unsafe_allow_html=True)

    progress_total, kps_total = get_total_progress()
    progress_percent = (progress_total / kps_total) * 100 if kps_total > 0 else 0

    st.markdown(f"""
    <div class="glass-card" style="padding:0.8rem 1rem;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.3rem;">
            <span style="font-size:13px;color:#64748b;">总进度</span>
            <span style="font-size:13px;font-weight:700;color:#6366f1;">{progress_total}/{kps_total}</span>
        </div>
        <div class="progress-modern">
            <div class="fill" style="width:{progress_percent}%;"></div>
        </div>
        <div style="font-size:11px;color:#94a3b8;text-align:right;margin-top:0.2rem;">
            {progress_percent:.1f}%
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav_items = [
        ("📖 科目学习", "subject"),
        ("📋 每日计划", "plan"),
        ("🔄 知识复盘", "review"),
        ("📝 真题练习", "real_exam"),
        ("❌ 错题本", "wrong"),
    ]

    for label, mode in nav_items:
        is_active = st.session_state.view_mode == mode
        cols = st.columns([1, 20])
        with cols[0]:
            st.markdown(
                f'<div style="text-align:center;font-size:18px;padding:0.4rem 0;">'
                f'{"👉" if is_active else ""}</div>',
                unsafe_allow_html=True
            )
        with cols[1]:
            if st.button(
                label,
                key=f"nav_{mode}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.view_mode = mode
                st.rerun()

    st.markdown("""
    <div style="margin-top:1.5rem;padding-top:0.8rem;border-top:1px solid #e2e8f0;
                font-size:11px;color:#94a3b8;text-align:center;">
        🎯 智能复习系统 v2.0
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 科目选择页
# ============================================================

def show_subject_select():
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <h2 style="font-size:24px;font-weight:800;color:#1e293b;margin:0;">
            📚 选择科目
        </h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.2rem;">
            点击卡片继续学习，系统会自动记住你的进度
        </p>
    </div>
    """, unsafe_allow_html=True)

    subjects = get_subjects()
    cols = st.columns(3)

    for i, subject in enumerate(subjects):
        with cols[i % 3]:
            progress = get_progress(subject)
            total = get_subject_total_kps(subject)
            percent = (progress / total) * 100 if total > 0 else 0
            color = get_subject_color(subject)
            last_kp = get_last_kp_index(subject)

            st.markdown(f"""
            <div class="subject-card-modern" style="background:linear-gradient(135deg,{color},{color}dd);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div>
                        <div style="font-weight:800;font-size:22px;margin-bottom:0.2rem;">{subject}</div>
                        <div style="font-size:12px;opacity:0.85;">
                            {f'已学 {last_kp}/{total}' if last_kp > 0 else '尚未开始'}
                        </div>
                    </div>
                    <div style="font-size:32px;font-weight:900;opacity:0.9;">
                        {progress}
                    </div>
                </div>
                <div class="progress-modern" style="background:rgba(255,255,255,0.25);margin:0.6rem 0;">
                    <div class="fill" style="width:{percent}%;background:white;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button(f"📖 学习", key=f"learn_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.current_kp_index = get_last_kp_index(subject)
                    st.session_state.view_mode = "study"
                    st.rerun()
            with col_b:
                if st.button(f"📝 刷题", key=f"practice_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.view_mode = "practice"
                    st.rerun()
            with col_c:
                if st.button(f"🔄 复盘", key=f"review_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.view_mode = "review"
                    st.rerun()

    st.divider()
    if st.button("🎯 真题练习", key="real_exam_btn_2", use_container_width=True, type="primary"):
        st.session_state.view_mode = "real_exam"
        st.rerun()


# ============================================================
# 学习视图（含TTS喇叭按钮）
# ============================================================

def show_study_view():
    current_subject = st.session_state.current_subject
    current_index = st.session_state.current_kp_index

    kp_dict, kp_names = load_knowledge(current_subject)
    total_kps = len(kp_names)

    # 页面标题栏
    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem;">
        <div>
            <span style="font-size:14px;color:#64748b;">{current_subject}</span>
            <h2 style="font-size:20px;font-weight:700;color:#1e293b;margin:0;">知识点学习</h2>
        </div>
        <div style="display:flex;align-items:center;gap:0.8rem;">
            <span style="font-size:13px;color:#94a3b8;">{current_index+1}/{total_kps}</span>
            <div class="progress-modern" style="width:120px;height:6px;">
                <div class="fill" style="width:{(current_index+1)/total_kps*100}%;"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if current_index < total_kps:
        current_kp_name = kp_names[current_index]
        kp_data = kp_dict[current_kp_name]

        # 知识点标题 + TTS按钮
        emoji = get_kp_emoji(current_kp_name)
        # 准备朗读文本
        tts_text = f"{current_kp_name}。{kp_data['核心概念']}。{kp_data['高频考法']}。{kp_data['易错点']}。{kp_data['例题']}"

        speaker_html = f"""
        <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1rem;">
            <h3 style="font-size:22px;font-weight:800;color:#1e293b;margin:0;">
                {emoji} {current_kp_name}
            </h3>
            <button id="tts-btn-{current_index}" class="speaker-btn" data-text-id="tts-text-{current_index}"
                    onclick="if(window.speakText){{}}"
                    title="朗读本节内容">
                🔊
            </button>
            <span style="font-size:11px;color:#94a3b8;">点击朗读</span>
        </div>
        <div id="tts-text-{current_index}" style="display:none;">{tts_text}</div>
        """
        st.markdown(speaker_html, unsafe_allow_html=True)

        # 注入TTS脚本（仅一次）
        if 'tts_injected' not in st.session_state:
            tts_script()
            st.session_state.tts_injected = True

        # 使用JS方式触发TTS
        st.markdown(f"""
        <script>
        (function() {{
            var btn = document.getElementById('tts-btn-{current_index}');
            if (btn) {{
                btn.onclick = function() {{
                    var textEl = document.getElementById('tts-text-{current_index}');
                    if (textEl && window.speakText) {{
                        window.speakText(textEl.textContent, 'tts-btn-{current_index}');
                    }}
                }};
            }}
        }})();
        </script>
        """, unsafe_allow_html=True)

        # 知识点内容（四个板块）
        sections = [
            ("🌱 核心概念", kp_data['核心概念'], "#16a34a", "#f0fdf4"),
            ("🔥 高频考法", kp_data['高频考法'], "#d97706", "#fffbeb"),
            ("⚠️ 易错点", kp_data['易错点'], "#dc2626", "#fef2f2"),
            ("📝 例题", kp_data['例题'], "#2563eb", "#eff6ff"),
        ]

        for emoji_label, content, border_color, bg_color in sections:
            st.markdown(f"""
            <div class="content-section" style="background:{bg_color};border-color:{border_color};">
                <div class="title" style="color:{border_color};">{emoji_label}</div>
                <div class="body">{content}</div>
            </div>
            """, unsafe_allow_html=True)

        # 导航按钮
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if current_index > 0:
                if st.button("⬅️ 上一个", key="prev_kp", use_container_width=True):
                    st.session_state.current_kp_index -= 1
                    st.rerun()
        with col2:
            if st.button("🔙 返回", key="back_kp", use_container_width=True):
                st.session_state.view_mode = "subject"
                st.rerun()
        with col3:
            if current_index < total_kps - 1:
                if st.button("下一个 ➡️", key="next_kp", use_container_width=True):
                    update_progress(current_subject)
                    st.session_state.current_kp_index += 1
                    st.rerun()
            else:
                if st.button("🎉 完成！", key="finish_kp", use_container_width=True):
                    update_progress(current_subject)
                    from_plan = st.session_state.get('from_plan', False)
                    if from_plan:
                        plan = load_plan_progress()
                        current_day = get_current_day(plan)
                        mark_task_completed(plan, current_day, current_subject)
                        st.session_state.from_plan = False
                        st.session_state.view_mode = "plan"
                    else:
                        st.session_state.view_mode = "subject"
                    st.rerun()

        # 知识点快速跳转（底部）
        st.markdown("""
        <div style="margin-top:1.5rem;">
            <div style="font-size:13px;font-weight:600;color:#64748b;margin-bottom:0.5rem;">📌 快速跳转</div>
        """, unsafe_allow_html=True)

        kp_chunks = [kp_names[i:i+6] for i in range(0, len(kp_names), 6)]
        for chunk in kp_chunks:
            cols = st.columns(len(chunk))
            for j, kp in enumerate(chunk):
                kp_idx = kp_names.index(kp)
                is_current = kp_idx == current_index
                is_done = kp_idx < current_index
                with cols[j]:
                    bg = "#6366f1" if is_current else ("#dcfce7" if is_done else "#f1f5f9")
                    text_color = "white" if is_current else ("#16a34a" if is_done else "#94a3b8")
                    if st.button(f"{'📍' if is_current else '✅' if is_done else '○'}", key=f"jump_{kp_idx}",
                                help=kp, use_container_width=True):
                        st.session_state.current_kp_index = kp_idx
                        st.rerun()
                    st.markdown(f"""
                    <div style="text-align:center;font-size:10px;color:{text_color};
                                white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
                        {kp[:8]}{'…' if len(kp)>8 else ''}
                    </div>
                    """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div class="glass-card" style="text-align:center;padding:2.5rem;">
            <div style="font-size:56px;margin-bottom:1rem;">🎉</div>
            <h3 style="font-size:22px;color:#1e293b;margin-bottom:0.5rem;">
                {current_subject} 全部学完！
            </h3>
            <p style="color:#64748b;margin-bottom:1.5rem;">
                太棒了！你已经完成了所有知识点的学习 🚀
            </p>
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔙 返回首页", use_container_width=True):
                st.session_state.view_mode = "subject"
                st.rerun()
        with col2:
            if st.button("🔄 进入复盘", use_container_width=True):
                st.session_state.view_mode = "review"
                st.rerun()


# ============================================================
# 知识复盘（复习）视图
# ============================================================

def show_review_view():
    current_subject = st.session_state.get('current_subject', '语文')
    kp_dict, kp_names = load_knowledge(current_subject)
    total_kps = len(kp_names)

    st.markdown(f"""
    <div style="margin-bottom:1.2rem;">
        <div style="display:flex;align-items:center;justify-content:space-between;">
            <div>
                <h2 style="font-size:22px;font-weight:800;color:#1e293b;margin:0;">
                    🔄 知识复盘
                </h2>
                <p style="font-size:14px;color:#64748b;margin-top:0.2rem;">
                    快速浏览 {current_subject} 所有知识点，查漏补缺
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 科目切换
    subjects = get_subjects()
    subj_cols = st.columns(len(subjects))
    for i, subj in enumerate(subjects):
        with subj_cols[i]:
            is_active = subj == current_subject
            if st.button(
                f"{subj}",
                key=f"review_subj_{subj}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.current_subject = subj
                st.rerun()

    st.markdown("""
    <div style="margin:0.5rem 0 1rem;font-size:12px;color:#94a3b8;">
        💡 点击知识点可展开详情，逐一复盘不遗漏
    </div>
    """, unsafe_allow_html=True)

    # 进度统计
    progress = get_progress(current_subject)
    st.markdown(f"""
    <div class="glass-card" style="padding:0.8rem 1rem;margin-bottom:1rem;">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="display:flex;align-items:center;gap:0.5rem;">
                <span style="font-size:13px;color:#64748b;">已学</span>
                <span class="stat-number">{progress}</span>
                <span style="font-size:13px;color:#94a3b8;">/ {total_kps} 个知识点</span>
            </div>
            <div style="font-size:13px;color:#6366f1;font-weight:600;">
                完成度 {(progress/total_kps)*100:.0f}%
            </div>
        </div>
        <div class="progress-modern">
            <div class="fill" style="width:{(progress/total_kps)*100}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 知识点列表 - 按科目分组
    first_group, rest_groups = [], []

    # 按主题域分组
    domain_map = {}
    for name in kp_names:
        domain = name.split('·')[0] if '·' in name else name.split('．')[0] if '．' in name else name
        if domain not in domain_map:
            domain_map[domain] = []
        domain_map[domain].append(name)

    # 显示每个域
    for domain, kps in domain_map.items():
        st.markdown(f"""
        <div style="font-size:15px;font-weight:700;color:#1e293b;margin:0.8rem 0 0.5rem;
                    padding-left:0.5rem;border-left:3px solid #6366f1;">
            {get_kp_emoji(domain)} {domain}
        </div>
        """, unsafe_allow_html=True)

        for name in kps:
            idx = kp_names.index(name)
            is_done = idx < progress
            kp_data = kp_dict[name]

            expander_key = f"review_exp_{current_subject}_{idx}"
            with st.expander(
                f"{'✅' if is_done else '🔄'} {get_kp_emoji(name)} {name}",
                expanded=not is_done
            ):
                cols = st.columns([3, 1])
                with cols[0]:
                    st.markdown(f"""
                    <div style="font-size:13px;color:#334155;line-height:1.7;">
                        <b>📖 核心概念：</b>{kp_data['核心概念'][:150]}{'……' if len(kp_data['核心概念'])>150 else ''}
                    </div>
                    <div style="font-size:13px;color:#334155;line-height:1.7;margin-top:0.5rem;">
                        <b>⚠️ 易错点：</b>{kp_data['易错点'][:100]}{'……' if len(kp_data['易错点'])>100 else ''}
                    </div>
                    """, unsafe_allow_html=True)
                with cols[1]:
                    if not is_done:
                        if st.button("📖 去学习", key=f"review_go_{idx}", use_container_width=True):
                            st.session_state.current_subject = current_subject
                            st.session_state.current_kp_index = idx
                            st.session_state.view_mode = "study"
                            st.rerun()
                    else:
                        st.markdown("""
                        <div style="text-align:center;padding:0.3rem;color:#16a34a;font-size:13px;">
                            ✅ 已掌握
                        </div>
                        """, unsafe_allow_html=True)


# ============================================================
# 刷题视图
# ============================================================

def show_practice_view():
    current_subject = st.session_state.current_subject

    questions_dict, kp_names = load_questions(current_subject)

    if 'practice_kp_index' not in st.session_state:
        st.session_state.practice_kp_index = 0
    if 'practice_q_index' not in st.session_state:
        st.session_state.practice_q_index = 0
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

    current_kp_index = st.session_state.practice_kp_index
    current_q_index = st.session_state.practice_q_index

    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem;">
        <div>
            <span style="font-size:14px;color:#64748b;">{current_subject}</span>
            <h2 style="font-size:20px;font-weight:700;color:#1e293b;margin:0;">📝 刷题练习</h2>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
            <span style="font-size:12px;color:#94a3b8;">
                {kp_names[current_kp_index] if current_kp_index < len(kp_names) else ''}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if current_kp_index < len(kp_names):
        current_kp_name = kp_names[current_kp_index]
        questions = questions_dict.get(current_kp_name, [])

        if current_q_index < len(questions):
            current_q = questions[current_q_index]

            st.markdown(f"""
            <div class="glass-card">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;">
                    <span style="font-size:12px;color:#94a3b8;background:#f1f5f9;padding:0.2rem 0.6rem;border-radius:0.5rem;">
                        {current_kp_name}
                    </span>
                    <span style="font-size:12px;color:#6366f1;font-weight:600;">
                        第 {current_q_index+1}/{len(questions)} 题
                    </span>
                </div>
                <div style="padding:1rem;background:#f8fafc;border-radius:0.75rem;margin-bottom:1rem;
                            border:1px solid #e2e8f0;">
                    <div style="font-size:16px;color:#1e293b;font-weight:500;">{current_q['question']}</div>
                </div>
            """, unsafe_allow_html=True)

            for idx, option in enumerate(current_q['options']):
                option_letter = chr(65 + idx)
                btn_key = f"opt_{current_kp_index}_{current_q_index}_{idx}"
                if st.button(f"{option_letter}. {option}", key=btn_key, use_container_width=True,
                           type="primary" if st.session_state.get('user_answer') == idx else "secondary"):
                    st.session_state.user_answer = idx
                    st.session_state.show_answer = True
                    st.session_state.is_correct = (idx == current_q['answer'])
                    st.rerun()

            if st.session_state.get('show_answer', False):
                user_ans = st.session_state.get('user_answer', -1)
                correct_ans = current_q['answer']

                if st.session_state.get('is_correct', False):
                    st.markdown("""
                    <div style="padding:0.5rem 1rem;background:#dcfce7;border-radius:0.5rem;color:#16a34a;font-weight:600;">
                        ✅ 回答正确！太棒了！
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="padding:0.5rem 1rem;background:#fee2e2;border-radius:0.5rem;color:#dc2626;font-weight:600;">
                        ❌ 回答错误！正确答案是：{chr(65 + correct_ans)}. {current_q['options'][correct_ans]}
                    </div>
                    """, unsafe_allow_html=True)
                    wrong_questions = st.session_state.get('wrong_questions', {})
                    if current_subject not in wrong_questions:
                        wrong_questions[current_subject] = []
                    wrong_questions[current_subject].append({
                        "question": current_q['question'],
                        "options": current_q['options'],
                        "user_answer": chr(65 + user_ans) if user_ans >= 0 else '未作答',
                        "correct_answer": chr(65 + correct_ans),
                        "analysis": current_q['解析'],
                        "knowledge_point": current_kp_name,
                        "type": "practice"
                    })
                    st.session_state['wrong_questions'] = wrong_questions

                st.markdown(f"""
                <div style="margin-top:0.8rem;padding:0.8rem 1rem;background:#eff6ff;border-radius:0.5rem;
                            border-left:4px solid #2563eb;">
                    <div style="font-weight:700;color:#2563eb;font-size:13px;margin-bottom:0.3rem;">📝 解析</div>
                    <div style="font-size:14px;color:#334155;">{current_q['解析']}</div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("下一题 ➡️", key="next_q_btn", use_container_width=True):
                    if current_q_index < len(questions) - 1:
                        st.session_state.practice_q_index += 1
                    else:
                        st.session_state.practice_kp_index += 1
                        st.session_state.practice_q_index = 0
                    st.session_state.show_answer = False
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="glass-card" style="text-align:center;padding:2rem;">
                <div style="font-size:36px;margin-bottom:0.5rem;">✅</div>
                <h3 style="font-size:18px;color:#1e293b;">{current_kp_name} 已完成！</h3>
            </div>
            """, unsafe_allow_html=True)
            if st.button("下一知识点 ➡️", key="next_kp_q", use_container_width=True):
                st.session_state.practice_kp_index += 1
                st.session_state.practice_q_index = 0
                st.session_state.show_answer = False
                st.rerun()
    else:
        st.markdown(f"""
        <div class="glass-card" style="text-align:center;padding:2.5rem;">
            <div style="font-size:56px;margin-bottom:1rem;">🎉</div>
            <h3 style="font-size:22px;color:#1e293b;">全部题目已完成！</h3>
            <p style="color:#64748b;margin-bottom:1rem;">你已经完成了所有练习题</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🔙 返回主页", key="back_home_practice", use_container_width=True):
        st.session_state.view_mode = "subject"
        st.session_state.show_answer = False
        st.rerun()


# ============================================================
# 错题本
# ============================================================

def show_wrong_view():
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <h2 style="font-size:22px;font-weight:800;color:#1e293b;margin:0;">❌ 错题本</h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.2rem;">
            复习错题，巩固薄弱知识点，避免重复犯错
        </p>
    </div>
    """, unsafe_allow_html=True)

    wrong_list = st.session_state.get('wrong_questions', {})
    real_exam_wrong = st.session_state.get('real_exam_wrong', {})

    has_wrong = False

    # 练习题错题
    if wrong_list and any(len(items) > 0 for items in wrong_list.values()):
        has_wrong = True
        st.markdown("""
        <div style="margin-bottom:0.8rem;">
            <h3 style="font-size:16px;font-weight:700;color:#6366f1;">📚 练习题错题</h3>
        </div>
        """, unsafe_allow_html=True)

        for subject, questions in wrong_list.items():
            if questions:
                color = get_subject_color(subject)
                st.markdown(f"""
                <div style="margin-bottom:0.5rem;">
                    <h4 style="font-size:14px;font-weight:600;color:{color};">{subject}（{len(questions)}题）</h4>
                </div>
                """, unsafe_allow_html=True)

                for i, q in enumerate(questions):
                    st.markdown(f"""
                    <div class="glass-card" style="border-left:4px solid #ef4444;">
                        <div style="font-weight:600;color:#1e293b;margin-bottom:0.5rem;">{q['question']}</div>
                        <div style="display:flex;gap:1rem;font-size:13px;margin-bottom:0.5rem;">
                            <span style="color:#dc2626;">✘ 你的答案: {q.get('user_answer', '未作答')}</span>
                            <span style="color:#16a34a;">✔ 正确答案: {q['correct_answer']}</span>
                        </div>
                        <div style="padding:0.6rem;background:#f8fafc;border-radius:0.5rem;">
                            <div style="font-weight:600;color:#64748b;font-size:12px;margin-bottom:0.2rem;">💡 解析</div>
                            <div style="font-size:13px;color:#475569;">{q['analysis']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    # 真题错题
    if real_exam_wrong and any(len(items) > 0 for items in real_exam_wrong.values()):
        has_wrong = True
        st.markdown("""
        <div style="margin-bottom:0.8rem;margin-top:1.5rem;">
            <h3 style="font-size:16px;font-weight:700;color:#f59e0b;">📝 真题错题</h3>
        </div>
        """, unsafe_allow_html=True)

        for subject, questions in real_exam_wrong.items():
            if questions:
                color = get_subject_color(subject)
                st.markdown(f"""
                <div style="margin-bottom:0.5rem;">
                    <h4 style="font-size:14px;font-weight:600;color:{color};">{subject}（{len(questions)}题）</h4>
                </div>
                """, unsafe_allow_html=True)

                for i, q in enumerate(questions):
                    st.markdown(f"""
                    <div class="glass-card" style="border-left:4px solid #f59e0b;">
                        <div style="font-size:12px;color:#94a3b8;margin-bottom:0.2rem;">
                            {q['year']}年 {q['province']} | {q['question_type']}
                        </div>
                        <div style="font-weight:600;color:#1e293b;margin-bottom:0.5rem;">{q['question']}</div>
                        <div style="display:flex;gap:1rem;font-size:13px;margin-bottom:0.5rem;">
                            <span style="color:#dc2626;">✘ 你的答案: {q.get('user_answer', '未作答')}</span>
                            <span style="color:#16a34a;">✔ 正确答案: {q['answer']}</span>
                        </div>
                        <div style="padding:0.6rem;background:#f8fafc;border-radius:0.5rem;">
                            <div style="font-weight:600;color:#64748b;font-size:12px;margin-bottom:0.2rem;">💡 解析</div>
                            <div style="font-size:13px;color:#475569;">{q['analysis']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    if not has_wrong:
        st.markdown("""
        <div class="glass-card" style="text-align:center;padding:2.5rem;">
            <div style="font-size:56px;margin-bottom:1rem;">🎉</div>
            <h3 style="font-size:20px;color:#1e293b;">暂无错题记录</h3>
            <p style="color:#64748b;margin:0.5rem 0 1rem;">继续保持！你做得很好！</p>
        </div>
        """, unsafe_allow_html=True)

    if real_exam_wrong and any(len(items) > 0 for items in real_exam_wrong.values()):
        st.divider()
        if st.button("🔄 重新练习真题错题", key="practice_real_exam_wrong", use_container_width=True, type="primary"):
            st.session_state.view_mode = "wrong_real_exam"
            st.rerun()


# ============================================================
# 学习计划视图
# ============================================================

def show_plan_view():
    plan = load_plan_progress()
    current_day_num = get_current_day(plan)
    summary = get_plan_summary(plan)

    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <h2 style="font-size:22px;font-weight:800;color:#1e293b;margin:0;">📋 24天冲刺计划</h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.2rem;">动态调整，高效冲刺每一天</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass-card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;">
            <div>
                <div style="font-size:13px;color:#64748b;">学习进度</div>
                <div style="font-size:24px;font-weight:800;color:#1e293b;">
                    {summary['completed_days']} / {summary['total_days']} 天
                </div>
            </div>
            <div style="text-align:right;">
                <div class="stat-number">{int(summary['progress_percent'])}%</div>
                <div style="font-size:11px;color:#94a3b8;">完成度</div>
            </div>
        </div>
        <div class="progress-modern">
            <div class="fill" style="width:{summary['progress_percent']}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    current_plan = get_day_plan(plan, current_day_num)
    if current_plan:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;">
                <div>
                    <div style="font-size:13px;color:#64748b;">今日任务</div>
                    <div style="font-size:18px;font-weight:700;color:#1e293b;">
                        第 {current_day_num} 天 · {current_plan['date']}
                    </div>
                </div>
                <div style="padding:0.4rem 1rem;border-radius:2rem;background:{
                    '#dcfce7' if current_plan['completed'] else '#fef3c7'
                };">
                    <span style="font-size:13px;font-weight:600;color:{
                        '#16a34a' if current_plan['completed'] else '#d97706'
                    };">
                        {'✅ 已完成' if current_plan['completed'] else '📝 进行中'}
                    </span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        task_cols = st.columns(3)
        task_index = 0
        for subject, task in current_plan['tasks'].items():
            with task_cols[task_index % 3]:
                bg_color = '#f0fdf4' if task['completed'] else 'white'
                border_color = '#bbf7d0' if task['completed'] else '#e2e8f0'
                st.markdown(f"""
                <div style="padding:0.8rem;border-radius:0.75rem;background:{bg_color};
                            border:1px solid {border_color};margin-bottom:0.8rem;">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.3rem;">
                        <span style="font-weight:700;color:{get_subject_color(subject)};font-size:14px;">
                            {get_kp_emoji(subject)} {subject}
                        </span>
                        <span style="font-size:11px;color:#94a3b8;">{task['questions_count']}题</span>
                    </div>
                    <div style="font-size:12px;color:#64748b;margin-bottom:0.5rem;">
                        {task['knowledge_point']}
                    </div>
                    {'<div style="color:#16a34a;font-size:13px;">✅ 已完成</div>' if task['completed'] else ''}
                </div>
                """, unsafe_allow_html=True)

                if not task['completed']:
                    if st.button(f"📖 去学习", key=f"plan_study_{subject}", use_container_width=True):
                        st.session_state.current_subject = subject
                        st.session_state.current_kp_index = get_last_kp_index(subject)
                        st.session_state.view_mode = "study"
                        st.session_state.from_plan = True
                        st.rerun()

            task_index += 1

        st.markdown("</div>", unsafe_allow_html=True)

    # 未来任务预览
    st.markdown("""
    <div style="margin-top:1.2rem;">
        <h3 style="font-size:16px;font-weight:700;color:#1e293b;margin-bottom:0.8rem;">📋 未来任务</h3>
    </div>
    """, unsafe_allow_html=True)

    future_days = []
    for i in range(current_day_num, min(current_day_num + 3, len(plan) + 1)):
        if i <= len(plan):
            future_days.append(get_day_plan(plan, i))

    for day_plan in future_days:
        completed_count = sum(1 for t in day_plan["tasks"].values() if t["completed"])
        total_tasks = len(day_plan["tasks"])
        st.markdown(f"""
        <div class="glass-card" style="display:flex;justify-content:space-between;align-items:center;padding:0.8rem 1rem;">
            <div>
                <div style="font-weight:600;color:#1e293b;font-size:14px;">第 {day_plan['day']} 天</div>
                <div style="font-size:12px;color:#94a3b8;">{day_plan['date']} {day_plan['weekday']}</div>
            </div>
            <div style="text-align:right;">
                <div style="font-size:13px;color:#64748b;">{completed_count}/{total_tasks}</div>
                <div class="progress-modern" style="width:100px;height:5px;">
                    <div class="fill" style="width:{(completed_count/total_tasks)*100 if total_tasks > 0 else 0}%;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# 真题练习视图
# ============================================================

def show_real_exam_view():
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <h2 style="font-size:22px;font-weight:800;color:#1e293b;margin:0;">📝 真题练习</h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.2rem;">选择科目开始练习，随机抽取5道未做过的真题</p>
    </div>
    """, unsafe_allow_html=True)

    subjects = get_subjects()
    cols = st.columns(3)

    for i, subject in enumerate(subjects):
        with cols[i % 3]:
            total_count = get_real_exam_count(subject)
            uncompleted_count = len(get_uncompleted_questions(subject))
            completed_count = total_count - uncompleted_count
            color = get_subject_color(subject)

            st.markdown(f"""
            <div class="subject-card-modern" style="background:linear-gradient(135deg,{color},{color}dd);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div style="font-weight:800;font-size:22px;">{subject}</div>
                    <div style="font-size:13px;opacity:0.9;">
                        {completed_count}/{total_count}
                    </div>
                </div>
                <div class="progress-modern" style="background:rgba(255,255,255,0.25);margin:0.5rem 0;">
                    <div class="fill" style="width:{(completed_count/total_count)*100 if total_count > 0 else 0}%;background:white;"></div>
                </div>
                <div style="font-size:12px;opacity:0.85;">
                    剩余 {uncompleted_count} 道
                </div>
            </div>
            """, unsafe_allow_html=True)

            if uncompleted_count > 0:
                if st.button(f"🚀 开始练习", key=f"real_exam_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.view_mode = "real_exam_practice"
                    st.rerun()
            else:
                st.markdown("""
                <div style="text-align:center;padding:0.4rem;color:#16a34a;font-size:13px;font-weight:500;">
                    ✅ 已全部完成
                </div>
                """, unsafe_allow_html=True)

    if st.button("🔙 返回首页", key="back_to_main_real", use_container_width=True):
        st.session_state.view_mode = "subject"
        st.rerun()


def show_real_exam_practice_view():
    current_subject = st.session_state.current_subject

    if 'real_exam_questions' not in st.session_state:
        uncompleted = get_uncompleted_questions(current_subject)
        sample_size = min(5, len(uncompleted))
        st.session_state.real_exam_questions = random.sample(uncompleted, sample_size)
        st.session_state.real_exam_current = 0
        st.session_state.real_exam_show_answer = False
        st.session_state.real_exam_user_answer = None
        st.session_state.real_exam_results = []

    questions = st.session_state.real_exam_questions
    current_idx = st.session_state.real_exam_current

    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem;">
        <div>
            <span style="font-size:14px;color:#64748b;">{current_subject}</span>
            <h2 style="font-size:20px;font-weight:700;color:#1e293b;margin:0;">📝 真题练习</h2>
        </div>
        <span style="font-size:13px;color:#6366f1;font-weight:600;">{current_idx+1}/{len(questions)}</span>
    </div>
    """, unsafe_allow_html=True)

    if current_idx < len(questions):
        current_q = questions[current_idx]

        st.markdown(f"""
        <div class="glass-card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;">
                <span style="font-size:12px;color:#94a3b8;background:#f1f5f9;padding:0.2rem 0.6rem;border-radius:0.5rem;">
                    {current_q['year']}年 {current_q['province']}
                </span>
                <span style="font-size:12px;color:#f59e0b;font-weight:600;">
                    {current_q['question_type']}
                </span>
            </div>
            <div style="padding:1rem;background:#f8fafc;border-radius:0.75rem;margin-bottom:1rem;
                        border:1px solid #e2e8f0;">
                <div style="font-size:16px;color:#1e293b;font-weight:500;">{current_q['question']}</div>
            </div>
        """, unsafe_allow_html=True)

        if current_q['options']:
            for idx, option in enumerate(current_q['options']):
                option_letter = chr(65 + idx)
                btn_key = f"real_exam_opt_{current_idx}_{idx}"
                is_selected = st.session_state.real_exam_user_answer == idx

                if not st.session_state.real_exam_show_answer:
                    if st.button(f"{option_letter}. {option}", key=btn_key, use_container_width=True,
                               type="primary" if is_selected else "secondary"):
                        st.session_state.real_exam_user_answer = idx
                        st.session_state.real_exam_show_answer = True
                        st.rerun()
                else:
                    is_correct = option_letter == current_q['answer']
                    bg_color = '#dcfce7' if is_correct else ''
                    if is_selected and not is_correct:
                        bg_color = '#fee2e2'
                    st.markdown(f"""
                    <div style="padding:0.6rem 0.8rem;border-radius:0.5rem;margin-bottom:0.4rem;
                                {'background:'+bg_color+';' if bg_color else ''}
                                {'font-weight:600;' if is_selected or is_correct else ''}">
                        <span style="font-weight:bold;">{option_letter}.</span> {option}
                        {' ✅' if is_correct else ''}{' ❌' if is_selected and not is_correct else ''}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            user_answer = st.text_input("请输入你的答案：", key=f"real_exam_text_{current_idx}")
            if st.button("提交答案", key=f"submit_{current_idx}", use_container_width=True):
                st.session_state.real_exam_user_answer = user_answer
                st.session_state.real_exam_show_answer = True
                st.rerun()

        if st.session_state.real_exam_show_answer:
            user_ans = st.session_state.real_exam_user_answer
            correct_ans = current_q['answer']

            is_correct = False
            if current_q['options']:
                is_correct = chr(65 + user_ans) == correct_ans if user_ans is not None else False
            else:
                is_correct = user_ans == correct_ans if user_ans else False

            if is_correct:
                st.markdown("""
                <div style="padding:0.5rem 1rem;background:#dcfce7;border-radius:0.5rem;color:#16a34a;font-weight:600;">
                    ✅ 回答正确！
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="padding:0.5rem 1rem;background:#fee2e2;border-radius:0.5rem;color:#dc2626;font-weight:600;">
                    ❌ 回答错误！正确答案是：{correct_ans}
                </div>
                """, unsafe_allow_html=True)

                real_exam_wrong = st.session_state.get('real_exam_wrong', {})
                if current_subject not in real_exam_wrong:
                    real_exam_wrong[current_subject] = []
                real_exam_wrong[current_subject].append({
                    "year": current_q['year'],
                    "province": current_q['province'],
                    "question_type": current_q['question_type'],
                    "question": current_q['question'],
                    "options": current_q['options'],
                    "answer": current_q['answer'],
                    "analysis": current_q['analysis'],
                    "user_answer": chr(65 + user_ans) if user_ans is not None and current_q['options'] else (user_ans or '未作答')
                })
                st.session_state['real_exam_wrong'] = real_exam_wrong

            st.session_state.real_exam_results.append({
                "question": current_q['question'],
                "user_answer": chr(65 + user_ans) if user_ans is not None and current_q['options'] else (user_ans or '未作答'),
                "correct_answer": correct_ans,
                "is_correct": is_correct
            })

            st.markdown(f"""
            <div style="margin-top:0.8rem;padding:0.8rem 1rem;background:#eff6ff;border-radius:0.5rem;
                        border-left:4px solid #2563eb;">
                <div style="font-weight:700;color:#2563eb;font-size:13px;margin-bottom:0.3rem;">📝 解析</div>
                <div style="font-size:14px;color:#334155;">{current_q['analysis']}</div>
            </div>
            """, unsafe_allow_html=True)

            add_completed_question(current_subject, current_q['id'])

            if st.button("下一题 ➡️", key="real_exam_next_q", use_container_width=True):
                st.session_state.real_exam_current += 1
                st.session_state.real_exam_show_answer = False
                st.session_state.real_exam_user_answer = None
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
    else:
        correct_count = sum(1 for r in st.session_state.real_exam_results if r['is_correct'])
        total_count = len(st.session_state.real_exam_results)

        st.markdown(f"""
        <div class="glass-card" style="text-align:center;padding:2.5rem;">
            <div style="font-size:56px;margin-bottom:1rem;">{'🎉' if correct_count == total_count else '💪'}</div>
            <h3 style="font-size:22px;color:#1e293b;">本轮完成！</h3>
            <p style="color:#64748b;margin:0.5rem 0 1rem;">
                答对 <span style="color:#16a34a;font-weight:800;font-size:24px;">{correct_count}</span>
                / {total_count} 道题
            </p>
            {'<p style="color:#f59e0b;">继续加油！错题已记录到错题本 📝</p>' if correct_count < total_count else '<p style="color:#16a34a;">满分！太厉害了！</p>'}
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔙 返回真题练习", key="back_to_real_exam_done", use_container_width=True):
            st.session_state.view_mode = "real_exam"
            st.session_state.pop('real_exam_questions', None)
            st.session_state.pop('real_exam_current', None)
            st.session_state.pop('real_exam_show_answer', None)
            st.session_state.pop('real_exam_user_answer', None)
            st.session_state.pop('real_exam_results', None)
            st.rerun()


def show_wrong_real_exam_view():
    current_subject = st.session_state.get('current_subject')
    real_exam_wrong = st.session_state.get('real_exam_wrong', {})

    if not current_subject:
        st.markdown("""
        <div style="margin-bottom:1.2rem;">
            <h2 style="font-size:22px;font-weight:800;color:#1e293b;margin:0;">🔄 真题错题练习</h2>
            <p style="font-size:14px;color:#64748b;margin-top:0.2rem;">选择科目重新练习错题</p>
        </div>
        """, unsafe_allow_html=True)

        subjects_with_wrong = [s for s in get_subjects() if s in real_exam_wrong and len(real_exam_wrong[s]) > 0]

        if not subjects_with_wrong:
            st.markdown("""
            <div class="glass-card" style="text-align:center;padding:2.5rem;">
                <div style="font-size:56px;margin-bottom:1rem;">🎉</div>
                <p style="color:#64748b;">暂无真题错题记录</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            cols = st.columns(3)
            for i, subject in enumerate(subjects_with_wrong):
                with cols[i % 3]:
                    color = get_subject_color(subject)
                    count = len(real_exam_wrong[subject])
                    st.markdown(f"""
                    <div class="subject-card-modern" style="background:linear-gradient(135deg,{color},{color}dd);">
                        <div style="font-weight:800;font-size:22px;">{subject}</div>
                        <div style="font-size:14px;opacity:0.9;">{count} 道错题待复习</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"🚀 练习错题", key=f"wrong_real_exam_{subject}", use_container_width=True):
                        st.session_state.current_subject = subject
                        st.session_state.view_mode = "wrong_real_exam"
                        st.rerun()
    else:
        if 'wrong_exam_questions' not in st.session_state:
            wrong_list = real_exam_wrong.get(current_subject, [])
            sample_size = min(5, len(wrong_list))
            st.session_state.wrong_exam_questions = random.sample(wrong_list, sample_size) if wrong_list else []
            st.session_state.wrong_exam_current = 0
            st.session_state.wrong_exam_show_answer = False
            st.session_state.wrong_exam_user_answer = None

        questions = st.session_state.wrong_exam_questions
        current_idx = st.session_state.wrong_exam_current

        st.markdown(f"""
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem;">
            <div>
                <span style="font-size:14px;color:#64748b;">{current_subject}</span>
                <h2 style="font-size:20px;font-weight:700;color:#1e293b;margin:0;">🔄 真题错题巩固</h2>
            </div>
            <span style="font-size:13px;color:#6366f1;font-weight:600;">{current_idx+1}/{len(questions)}</span>
        </div>
        """, unsafe_allow_html=True)

        if not questions:
            st.markdown("""
            <div class="glass-card" style="text-align:center;padding:2rem;">
                <div style="font-size:48px;margin-bottom:0.5rem;">🎉</div>
                <p style="color:#64748b;">该科目暂无错题记录</p>
            </div>
            """, unsafe_allow_html=True)
        elif current_idx < len(questions):
            current_q = questions[current_idx]

            st.markdown(f"""
            <div class="glass-card">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;">
                    <span style="font-size:12px;color:#94a3b8;">
                        {current_q['year']}年 {current_q['province']}
                    </span>
                    <span style="font-size:12px;color:#f59e0b;font-weight:600;">
                        {current_q['question_type']}
                    </span>
                </div>
                <div style="padding:1rem;background:#fef3c7;border-radius:0.75rem;margin-bottom:1rem;
                            border:1px solid #fde68a;">
                    <div style="font-size:16px;color:#1e293b;font-weight:500;">{current_q['question']}</div>
                </div>
            """, unsafe_allow_html=True)

            if current_q['options']:
                for idx, option in enumerate(current_q['options']):
                    option_letter = chr(65 + idx)
                    btn_key = f"wrong_exam_opt_{current_idx}_{idx}"
                    is_selected = st.session_state.wrong_exam_user_answer == idx

                    if not st.session_state.wrong_exam_show_answer:
                        if st.button(f"{option_letter}. {option}", key=btn_key, use_container_width=True,
                                   type="primary" if is_selected else "secondary"):
                            st.session_state.wrong_exam_user_answer = idx
                            st.session_state.wrong_exam_show_answer = True
                            st.rerun()
                    else:
                        is_correct = option_letter == current_q['answer']
                        bg_color = '#dcfce7' if is_correct else ''
                        if is_selected and not is_correct:
                            bg_color = '#fee2e2'
                        st.markdown(f"""
                        <div style="padding:0.6rem 0.8rem;border-radius:0.5rem;margin-bottom:0.4rem;
                                    {'background:'+bg_color+';' if bg_color else ''}
                                    {'font-weight:600;' if is_selected or is_correct else ''}">
                            <span style="font-weight:bold;">{option_letter}.</span> {option}
                            {' ✅' if is_correct else ''}{' ❌' if is_selected and not is_correct else ''}
                        </div>
                        """, unsafe_allow_html=True)

            if st.session_state.wrong_exam_show_answer:
                user_ans = st.session_state.wrong_exam_user_answer
                correct_ans = current_q['answer']

                is_correct = chr(65 + user_ans) == correct_ans if user_ans is not None else False

                if is_correct:
                    st.markdown("""
                    <div style="padding:0.5rem 1rem;background:#dcfce7;border-radius:0.5rem;color:#16a34a;font-weight:600;">
                        ✅ 这次答对了！错题已从记录中移除
                    </div>
                    """, unsafe_allow_html=True)
                    real_exam_wrong[current_subject] = [q for q in real_exam_wrong[current_subject] if q['question'] != current_q['question']]
                    st.session_state['real_exam_wrong'] = real_exam_wrong
                else:
                    st.markdown(f"""
                    <div style="padding:0.5rem 1rem;background:#fee2e2;border-radius:0.5rem;color:#dc2626;font-weight:600;">
                        ❌ 回答错误！正确答案是：{correct_ans}
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                <div style="margin-top:0.8rem;padding:0.8rem 1rem;background:#eff6ff;border-radius:0.5rem;
                            border-left:4px solid #2563eb;">
                    <div style="font-weight:700;color:#2563eb;font-size:13px;margin-bottom:0.3rem;">📝 解析</div>
                    <div style="font-size:14px;color:#334155;">{current_q['analysis']}</div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("下一题 ➡️", key="wrong_exam_next_q", use_container_width=True):
                    st.session_state.wrong_exam_current += 1
                    st.session_state.wrong_exam_show_answer = False
                    st.session_state.wrong_exam_user_answer = None
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="glass-card" style="text-align:center;padding:2rem;">
                <div style="font-size:56px;margin-bottom:1rem;">🎉</div>
                <h3 style="font-size:20px;color:#1e293b;">错题巩固完成！</h3>
                <p style="color:#64748b;">所有错题已重新练习</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🔙 返回错题本", key="back_to_wrong_done", use_container_width=True):
                st.session_state.view_mode = "wrong"
                st.session_state.pop('wrong_exam_questions', None)
                st.session_state.pop('wrong_exam_current', None)
                st.session_state.pop('wrong_exam_show_answer', None)
                st.session_state.pop('wrong_exam_user_answer', None)
                st.rerun()


if __name__ == "__main__":
    if 'view_mode' not in st.session_state:
        st.session_state.view_mode = "subject"
    main()
