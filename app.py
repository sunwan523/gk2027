import streamlit as st
from datetime import datetime
import json
import random

st.set_page_config(
    page_title="高考冲刺",
    page_icon="📚",
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

def main():
    st.markdown("""
    <style>
    :root {
        --primary-color: #6366f1;
        --success-color: #10b981;
        --warning-color: #f59e0b;
        --danger-color: #ef4444;
        --bg-color: #f8fafc;
        --card-bg: #ffffff;
    }
    .main .block-container {
        padding: 1rem 1.5rem;
        max-width: 100%;
    }
    .sidebar .block-container {
        padding: 1rem;
    }
    .stButton>button {
        border-radius: 0.5rem;
        border: none;
        transition: all 0.2s ease;
        font-weight: 500;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .progress-bar {
        height: 8px;
        border-radius: 4px;
        background: #e2e8f0;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.5s ease;
    }
    .card {
        background: white;
        border-radius: 0.75rem;
        padding: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .subject-card {
        border-radius: 0.75rem;
        padding: 1rem;
        color: white;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .subject-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

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

def show_sidebar():
    st.markdown(f"""
    <div style="text-align:center;padding:1rem 0 1.5rem;">
        <div style="font-size:24px;font-weight:bold;color:#333;margin-bottom:0.5rem;">📚 高考冲刺</div>
        <div style="font-size:14px;color:#666;">距离高考还有 <span style="color:#ef4444;font-weight:bold;">{get_days_left()}</span> 天</div>
    </div>
    """, unsafe_allow_html=True)

    progress_total, kps_total = get_total_progress()
    progress_percent = (progress_total / kps_total) * 100 if kps_total > 0 else 0
    
    st.markdown(f"""
    <div class="card">
        <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem;">
            <span style="font-size:14px;color:#666;">总体进度</span>
            <span style="font-size:14px;font-weight:bold;color:#333;">{progress_total}/{kps_total}</span>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" style="width:{progress_percent}%;background:linear-gradient(90deg, #6366f1, #8b5cf6);"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav_items = [
        ("📖 科目选择", "subject"),
        ("📅 学习计划", "plan"),
        ("📝 真题练习", "real_exam"),
        ("❌ 错题本", "wrong")
    ]
    
    for label, mode in nav_items:
        if st.button(label, key=f"nav_{mode}", use_container_width=True, 
                    type="primary" if st.session_state.view_mode == mode else "secondary"):
            st.session_state.view_mode = mode
            st.experimental_rerun()

    st.markdown("""
    <div style="margin-top:2rem;padding-top:1rem;border-top:1px solid #e2e8f0;">
        <div style="font-size:12px;color:#9ca3af;">上次学习: 刚刚</div>
    </div>
    """, unsafe_allow_html=True)

def show_subject_select():
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <h2 style="font-size:20px;font-weight:bold;color:#1e293b;margin:0;">🎯 选择科目继续学习</h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.25rem;">点击卡片即可继续上次的学习进度</p>
    </div>
    """, unsafe_allow_html=True)

    subjects = get_subjects()
    cols = st.columns(2)
    
    for i, subject in enumerate(subjects):
        with cols[i % 2]:
            progress = get_progress(subject)
            total = get_subject_total_kps(subject)
            percent = (progress / total) * 100
            color = get_subject_color(subject)
            last_kp = get_last_kp_index(subject)
            
            st.markdown(f"""
            <div class="subject-card" style="background:{color};">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
                    <div style="font-weight:bold;font-size:20px;">{subject}</div>
                    <div style="font-size:12px;opacity:0.9;">{progress}/{total}</div>
                </div>
                <div class="progress-bar" style="background:rgba(255,255,255,0.3);">
                    <div class="progress-fill" style="width:{percent}%;background:white;"></div>
                </div>
                <div style="font-size:12px;opacity:0.8;margin-top:0.5rem;">
                    {f"已学习到第 {last_kp} 个知识点" if last_kp > 0 else "尚未开始"}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"📖 学习", key=f"learn_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.current_kp_index = get_last_kp_index(subject)
                    st.session_state.view_mode = "study"
                    st.experimental_rerun()
            with col2:
                if st.button(f"📝 刷题", key=f"practice_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.view_mode = "practice"
                    st.experimental_rerun()

    st.markdown("""
    <div style="margin-top:2rem;">
    """, unsafe_allow_html=True)
    
    if st.button("🎯 真题练习", key="real_exam_btn", use_container_width=True, type="primary"):
        st.session_state.view_mode = "real_exam"
        st.experimental_rerun()

def show_study_view():
    current_subject = st.session_state.current_subject
    current_index = st.session_state.current_kp_index
    
    kp_dict, kp_names = load_knowledge(current_subject)
    total_kps = len(kp_names)

    if current_index < total_kps:
        current_kp_name = kp_names[current_index]
        kp_data = kp_dict[current_kp_name]

        st.markdown(f"""
        <div style="margin-bottom:1rem;">
            <div style="display:flex;align-items:center;gap:1rem;">
                <button onclick="window.history.back()" style="padding:0.5rem 1rem;border-radius:0.5rem;border:none;background:#f1f5f9;cursor:pointer;">
                    ← 返回
                </button>
                <div style="flex:1;text-align:center;">
                    <div style="font-size:14px;color:#64748b;">{current_subject}</div>
                    <div style="font-size:12px;color:#9ca3af;">{current_index+1}/{total_kps}</div>
                </div>
                <div style="width:60px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.container():
            st.subheader(f"🎯 {current_kp_name}")
            
            st.markdown("""
            <div style="margin-bottom:1rem;padding:1rem;background:#f0fdf4;border-radius:0.5rem;">
                <div style="font-weight:bold;color:#16a34a;font-size:14px;margin-bottom:0.5rem;">🌱 核心概念</div>
            </div>
            """, unsafe_allow_html=True)
            st.write(kp_data['核心概念'])
            
            st.markdown("""
            <div style="margin-bottom:1rem;padding:1rem;background:#fffbeb;border-radius:0.5rem;">
                <div style="font-weight:bold;color:#d97706;font-size:14px;margin-bottom:0.5rem;">🔥 高频考法</div>
            </div>
            """, unsafe_allow_html=True)
            st.write(kp_data['高频考法'])
            
            st.markdown("""
            <div style="margin-bottom:1rem;padding:1rem;background:#fef2f2;border-radius:0.5rem;">
                <div style="font-weight:bold;color:#dc2626;font-size:14px;margin-bottom:0.5rem;">⚠️ 易错点</div>
            </div>
            """, unsafe_allow_html=True)
            st.write(kp_data['易错点'])
            
            st.markdown("""
            <div style="padding:1rem;background:#eff6ff;border-radius:0.5rem;">
                <div style="font-weight:bold;color:#2563eb;font-size:14px;margin-bottom:0.5rem;">📝 例题</div>
            </div>
            """, unsafe_allow_html=True)
            st.write(kp_data['例题'])

        col1, col2, col3 = st.columns(3)
        with col1:
            if current_index > 0:
                if st.button("⬅️ 上一个", key="prev", use_container_width=True):
                    st.session_state.current_kp_index -= 1
                    st.experimental_rerun()
        with col2:
            if st.button("🔙 返回", key="back", use_container_width=True):
                st.session_state.view_mode = "subject"
                st.experimental_rerun()
        with col3:
            if current_index < total_kps - 1:
                if st.button("下一个 ➡️", key="next", use_container_width=True):
                    update_progress(current_subject)
                    st.session_state.current_kp_index += 1
                    st.experimental_rerun()
            else:
                if st.button("🎉 完成", key="finish", use_container_width=True):
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
                    st.experimental_rerun()
    else:
        st.markdown(f"""
        <div class="card" style="text-align:center;padding:2rem;">
            <div style="font-size:48px;margin-bottom:1rem;">🎉</div>
            <h3 style="font-size:20px;color:#1e293b;">{current_subject} 学习完成！</h3>
            <p style="color:#64748b;margin:1rem 0;">你已经学完了所有知识点</p>
            {st.button("🔙 返回主页", key="back_to_subject", use_container_width=True)}
        </div>
        """, unsafe_allow_html=True)
        if st.session_state.get('back_to_subject'):
            st.session_state.view_mode = "subject"
            st.experimental_rerun()

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
    <div style="margin-bottom:1rem;">
        <div style="display:flex;align-items:center;gap:1rem;">
            <button onclick="window.history.back()" style="padding:0.5rem 1rem;border-radius:0.5rem;border:none;background:#f1f5f9;cursor:pointer;">
                ← 返回
            </button>
            <div style="flex:1;text-align:center;">
                <div style="font-size:14px;color:#64748b;">{current_subject}</div>
            </div>
            <div style="width:60px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if current_kp_index < len(kp_names):
        current_kp_name = kp_names[current_kp_index]
        questions = questions_dict.get(current_kp_name, [])
        
        if current_q_index < len(questions):
            current_q = questions[current_q_index]
            
            st.markdown(f"""
            <div class="card">
                <div style="text-align:center;margin-bottom:1rem;">
                    <div style="font-size:12px;color:#9ca3af;">{current_kp_name}</div>
                    <div style="font-size:14px;font-weight:bold;color:#64748b;">{current_q_index+1}/{len(questions)}</div>
                </div>
                
                <div style="padding:1rem;background:#f8fafc;border-radius:0.5rem;margin-bottom:1rem;">
                    <div style="font-size:16px;color:#1e293b;">{current_q['question']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            for idx, option in enumerate(current_q['options']):
                option_letter = chr(65 + idx)
                btn_key = f"opt_{idx}"
                if st.button(f"{option_letter}. {option}", key=btn_key, use_container_width=True,
                           type="primary" if st.session_state.get('user_answer') == idx else "secondary"):
                    st.session_state.user_answer = idx
                    st.session_state.show_answer = True
                    st.session_state.is_correct = (idx == current_q['answer'])
                    st.experimental_rerun()
            
            if st.session_state.get('show_answer', False):
                user_ans = st.session_state.get('user_answer', -1)
                correct_ans = current_q['answer']
                
                if st.session_state.get('is_correct', False):
                    st.success("✅ 回答正确！")
                else:
                    st.error(f"❌ 回答错误！正确答案是：{chr(65 + correct_ans)}. {current_q['options'][correct_ans]}")
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
                <div style="margin-top:1rem;padding:1rem;background:#eff6ff;border-radius:0.5rem;">
                    <div style="font-weight:bold;color:#2563eb;font-size:14px;margin-bottom:0.5rem;">📝 解析</div>
                    <div style="font-size:14px;color:#334155;">{current_q['解析']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("下一题 ➡️", key="next_q", use_container_width=True):
                    if current_q_index < len(questions) - 1:
                        st.session_state.practice_q_index += 1
                    else:
                        st.session_state.practice_kp_index += 1
                        st.session_state.practice_q_index = 0
                    st.session_state.show_answer = False
                    st.experimental_rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card" style="text-align:center;padding:2rem;">
                <div style="font-size:32px;margin-bottom:1rem;">✅</div>
                <h3 style="font-size:18px;color:#1e293b;">{current_kp_name} 题目已完成！</h3>
                {st.button("下一知识点 ➡️", key="next_kp", use_container_width=True)}
            </div>
            """, unsafe_allow_html=True)
            if st.session_state.get('next_kp'):
                st.session_state.practice_kp_index += 1
                st.session_state.practice_q_index = 0
                st.session_state.show_answer = False
                st.experimental_rerun()
    else:
        st.markdown(f"""
        <div class="card" style="text-align:center;padding:2rem;">
            <div style="font-size:48px;margin-bottom:1rem;">🎉</div>
            <h3 style="font-size:20px;color:#1e293b;">{current_subject} 刷题完成！</h3>
            <p style="color:#64748b;margin:1rem 0;">你已经完成了所有练习题</p>
            {st.button("🔙 返回主页", key="back_home", use_container_width=True)}
        </div>
        """, unsafe_allow_html=True)
        if st.session_state.get('back_home'):
            st.session_state.view_mode = "subject"
            st.experimental_rerun()
    
    if st.button("🔙 返回", key="back_btn", use_container_width=True):
        st.session_state.view_mode = "subject"
        st.session_state.show_answer = False
        st.experimental_rerun()

def show_wrong_view():
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <h2 style="font-size:20px;font-weight:bold;color:#1e293b;margin:0;">❌ 错题本</h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.25rem;">复习错题，巩固薄弱知识点</p>
    </div>
    """, unsafe_allow_html=True)
    
    wrong_list = st.session_state.get('wrong_questions', {})
    real_exam_wrong = st.session_state.get('real_exam_wrong', {})
    
    has_wrong = False
    if wrong_list and any(len(items) > 0 for items in wrong_list.values()):
        has_wrong = True
        st.markdown("""
        <div style="margin-bottom:1.5rem;">
            <h3 style="font-size:16px;font-weight:bold;color:#6366f1;">📚 练习题错题</h3>
        </div>
        """, unsafe_allow_html=True)
        
        for subject, questions in wrong_list.items():
            if questions:
                st.markdown(f"""
                <div style="margin-bottom:1rem;">
                    <h4 style="font-size:14px;font-weight:bold;color:{get_subject_color(subject)};">{subject}</h4>
                </div>
                """, unsafe_allow_html=True)
                
                for i, q in enumerate(questions):
                    st.markdown(f"""
                    <div class="card" style="border-left:4px solid #ef4444;">
                        <div style="font-weight:bold;color:#1e293b;margin-bottom:0.5rem;">{q['question']}</div>
                        <div style="font-size:14px;color:#64748b;margin-bottom:0.25rem;">
                            你的答案: {q.get('user_answer', '未作答')}
                        </div>
                        <div style="font-size:14px;color:#10b981;margin-bottom:0.5rem;">
                            正确答案: {q['correct_answer']}
                        </div>
                        <div style="padding:0.75rem;background:#f8fafc;border-radius:0.25rem;">
                            <div style="font-weight:bold;color:#64748b;font-size:12px;margin-bottom:0.25rem;">💡 解析</div>
                            <div style="font-size:13px;color:#475569;">{q['analysis']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    if real_exam_wrong and any(len(items) > 0 for items in real_exam_wrong.values()):
        has_wrong = True
        st.markdown("""
        <div style="margin-bottom:1.5rem;">
            <h3 style="font-size:16px;font-weight:bold;color:#f59e0b;">📝 真题错题</h3>
        </div>
        """, unsafe_allow_html=True)
        
        for subject, questions in real_exam_wrong.items():
            if questions:
                st.markdown(f"""
                <div style="margin-bottom:1rem;">
                    <h4 style="font-size:14px;font-weight:bold;color:{get_subject_color(subject)};">{subject}</h4>
                </div>
                """, unsafe_allow_html=True)
                
                for i, q in enumerate(questions):
                    st.markdown(f"""
                    <div class="card" style="border-left:4px solid #f59e0b;">
                        <div style="font-size:12px;color:#9ca3af;margin-bottom:0.25rem;">
                            {q['year']}年 {q['province']} | {q['question_type']}
                        </div>
                        <div style="font-weight:bold;color:#1e293b;margin-bottom:0.5rem;">{q['question']}</div>
                        <div style="font-size:14px;color:#64748b;margin-bottom:0.25rem;">
                            你的答案: {q.get('user_answer', '未作答')}
                        </div>
                        <div style="font-size:14px;color:#10b981;margin-bottom:0.5rem;">
                            正确答案: {q['answer']}
                        </div>
                        <div style="padding:0.75rem;background:#f8fafc;border-radius:0.25rem;">
                            <div style="font-weight:bold;color:#64748b;font-size:12px;margin-bottom:0.25rem;">💡 解析</div>
                            <div style="font-size:13px;color:#475569;">{q['analysis']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    if not has_wrong:
        st.markdown("""
        <div class="card" style="text-align:center;padding:2rem;">
            <div style="font-size:48px;margin-bottom:1rem;">🎉</div>
            <p style="color:#64748b;">暂无错题记录，继续保持！</p>
        </div>
        """, unsafe_allow_html=True)
    
    if real_exam_wrong and any(len(items) > 0 for items in real_exam_wrong.values()):
        if st.button("🔄 重新练习真题错题", key="practice_real_exam_wrong", use_container_width=True):
            st.session_state.view_mode = "wrong_real_exam"
            st.experimental_rerun()

def show_plan_view():
    plan = load_plan_progress()
    current_day_num = get_current_day(plan)
    summary = get_plan_summary(plan)
    
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <h2 style="font-size:20px;font-weight:bold;color:#1e293b;margin:0;">📅 24天学习计划</h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.25rem;">动态调整，高效冲刺</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
            <div>
                <div style="font-size:14px;color:#64748b;">学习进度</div>
                <div style="font-size:24px;font-weight:bold;color:#1e293b;">
                    {summary['completed_days']} / {summary['total_days']} 天
                </div>
            </div>
            <div style="text-align:right;">
                <div style="font-size:36px;font-weight:bold;color:#6366f1;">
                    {int(summary['progress_percent'])}%
                </div>
                <div style="font-size:12px;color:#9ca3af;">完成度</div>
            </div>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" style="width:{summary['progress_percent']}%;background:linear-gradient(90deg, #6366f1, #8b5cf6);"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    current_plan = get_day_plan(plan, current_day_num)
    
    st.markdown(f"""
    <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
            <div>
                <div style="font-size:14px;color:#64748b;">今日任务</div>
                <div style="font-size:18px;font-weight:bold;color:#1e293b;">
                    第 {current_day_num} 天 ({current_plan['date']})
                </div>
            </div>
            <div style="padding:0.5rem 1rem;border-radius:0.5rem;background:{
                '#dcfce7' if current_plan['completed'] else '#fef3c7'
            };">
                <span style="font-size:14px;font-weight:bold;color:{
                    '#16a34a' if current_plan['completed'] else '#d97706'
                };">
                    {'✅ 已完成' if current_plan['completed'] else '📝 进行中'}
                </span>
            </div>
        </div>
        
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.75rem;">
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    task_index = 0
    for subject, task in current_plan['tasks'].items():
        with cols[task_index % 3]:
            bg_color = '#f0fdf4' if task['completed'] else '#f8fafc'
            border_color = '#bbf7d0' if task['completed'] else '#e2e8f0'
            
            st.markdown(f"""
            <div style="padding:1rem;border-radius:0.5rem;background:{bg_color};border:1px solid {border_color};margin-bottom:0.75rem;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
                    <span style="font-weight:bold;color:{get_subject_color(subject)};">{subject}</span>
                    <span style="font-size:12px;color:#9ca3af;">{task['questions_count']}题</span>
                </div>
                <div style="font-size:13px;color:#64748b;margin-bottom:0.75rem;">
                    {task['knowledge_point']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if task['completed']:
                st.success("✓ 已完成", icon="✅")
            else:
                if st.button(f"📖 去学习", key=f"study_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.current_kp_index = get_last_kp_index(subject)
                    st.session_state.view_mode = "study"
                    st.session_state.from_plan = True
                    st.experimental_rerun()
        
        task_index += 1
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:1.5rem;">
        <h3 style="font-size:16px;font-weight:bold;color:#1e293b;margin-bottom:1rem;">📋 未来任务预览</h3>
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
        <div class="card" style="display:flex;justify-content:space-between;align-items:center;">
            <div>
                <div style="font-weight:bold;color:#1e293b;">第 {day_plan['day']} 天</div>
                <div style="font-size:12px;color:#9ca3af;">{day_plan['date']} | {day_plan['weekday']}</div>
            </div>
            <div style="text-align:right;">
                <div style="font-size:14px;color:#64748b;">{completed_count}/{total_tasks} 任务</div>
                <div class="progress-bar" style="width:120px;">
                    <div class="progress-fill" style="width:{(completed_count/total_tasks)*100}%;background:#6366f1;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_real_exam_view():
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <h2 style="font-size:20px;font-weight:bold;color:#1e293b;margin:0;">📝 真题练习</h2>
        <p style="font-size:14px;color:#64748b;margin-top:0.25rem;">选择科目开始真题练习，随机抽取5道未做过的真题</p>
    </div>
    """, unsafe_allow_html=True)

    subjects = get_subjects()
    cols = st.columns(2)
    
    for i, subject in enumerate(subjects):
        with cols[i % 2]:
            total_count = get_real_exam_count(subject)
            uncompleted_count = len(get_uncompleted_questions(subject))
            completed_count = total_count - uncompleted_count
            color = get_subject_color(subject)
            
            st.markdown(f"""
            <div class="subject-card" style="background:{color};">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
                    <div style="font-weight:bold;font-size:20px;">{subject}</div>
                    <div style="font-size:12px;opacity:0.9;">{completed_count}/{total_count} 已练</div>
                </div>
                <div class="progress-bar" style="background:rgba(255,255,255,0.3);">
                    <div class="progress-fill" style="width:{(completed_count/total_count)*100 if total_count > 0 else 0}%;background:white;"></div>
                </div>
                <div style="font-size:12px;opacity:0.8;margin-top:0.5rem;">
                    剩余 {uncompleted_count} 道真题
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if uncompleted_count > 0:
                if st.button(f"🚀 开始练习", key=f"real_exam_{subject}", use_container_width=True):
                    st.session_state.current_subject = subject
                    st.session_state.view_mode = "real_exam_practice"
                    st.experimental_rerun()
            else:
                st.markdown("""
                <div style="text-align:center;padding:0.5rem;color:#10b981;font-size:14px;">
                    ✅ 该科目真题已全部完成
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top:2rem;">
    """, unsafe_allow_html=True)
    
    if st.button("🔙 返回主页", key="back_to_main", use_container_width=True):
        st.session_state.view_mode = "subject"
        st.experimental_rerun()

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
    <div style="margin-bottom:1rem;">
        <div style="display:flex;align-items:center;gap:1rem;">
            <button onclick="window.history.back()" style="padding:0.5rem 1rem;border-radius:0.5rem;border:none;background:#f1f5f9;cursor:pointer;">
                ← 返回
            </button>
            <div style="flex:1;text-align:center;">
                <div style="font-size:14px;color:#64748b;">{current_subject} - 真题练习</div>
                <div style="font-size:12px;color:#9ca3af;">{current_idx+1}/{len(questions)}</div>
            </div>
            <div style="width:60px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if current_idx < len(questions):
        current_q = questions[current_idx]
        
        st.markdown(f"""
        <div class="card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
                <div style="font-size:12px;color:#9ca3af;">
                    {current_q['year']}年 {current_q['province']}
                </div>
                <div style="font-size:12px;color:#f59e0b;font-weight:bold;">
                    {current_q['question_type']}
                </div>
            </div>
            
            <div style="padding:1rem;background:#f8fafc;border-radius:0.5rem;margin-bottom:1rem;">
                <div style="font-size:16px;color:#1e293b;">{current_q['question']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        if current_q['options']:
            for idx, option in enumerate(current_q['options']):
                option_letter = chr(65 + idx)
                btn_key = f"real_exam_opt_{idx}"
                is_selected = st.session_state.real_exam_user_answer == idx
                
                if not st.session_state.real_exam_show_answer:
                    if st.button(f"{option_letter}. {option}", key=btn_key, use_container_width=True,
                               type="primary" if is_selected else "secondary"):
                        st.session_state.real_exam_user_answer = idx
                        st.session_state.real_exam_show_answer = True
                        st.experimental_rerun()
                else:
                    is_correct = option_letter == current_q['answer']
                    bg_color = '#dcfce7' if is_correct else ''
                    if is_selected and not is_correct:
                        bg_color = '#fee2e2'
                    
                    st.markdown(f"""
                    <div style="padding:0.75rem;border-radius:0.5rem;margin-bottom:0.5rem;{f'background:{bg_color};' if bg_color else ''}">
                        <span style="font-weight:bold;">{option_letter}.</span> {option}
                        {' ✅' if is_correct else ''}{' ❌' if is_selected and not is_correct else ''}
                    </div>
                    """, unsafe_allow_html=True)
        
        else:
            user_answer = st.text_input("请输入你的答案：", key="real_exam_text_answer")
            if st.button("提交答案", key="submit_answer", use_container_width=True):
                st.session_state.real_exam_user_answer = user_answer
                st.session_state.real_exam_show_answer = True
                st.experimental_rerun()
        
        if st.session_state.real_exam_show_answer:
            user_ans = st.session_state.real_exam_user_answer
            correct_ans = current_q['answer']
            
            is_correct = False
            if current_q['options']:
                is_correct = chr(65 + user_ans) == correct_ans if user_ans is not None else False
            else:
                is_correct = user_ans == correct_ans if user_ans else False
            
            if is_correct:
                st.success("✅ 回答正确！")
            else:
                st.error(f"❌ 回答错误！正确答案是：{correct_ans}")
                
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
            <div style="margin-top:1rem;padding:1rem;background:#eff6ff;border-radius:0.5rem;">
                <div style="font-weight:bold;color:#2563eb;font-size:14px;margin-bottom:0.5rem;">📝 解析</div>
                <div style="font-size:14px;color:#334155;">{current_q['analysis']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            add_completed_question(current_subject, current_q['id'])
            
            if st.button("下一题 ➡️", key="real_exam_next", use_container_width=True):
                st.session_state.real_exam_current += 1
                st.session_state.real_exam_show_answer = False
                st.session_state.real_exam_user_answer = None
                st.experimental_rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        correct_count = sum(1 for r in st.session_state.real_exam_results if r['is_correct'])
        total_count = len(st.session_state.real_exam_results)
        
        st.markdown(f"""
        <div class="card" style="text-align:center;padding:2rem;">
            <div style="font-size:48px;margin-bottom:1rem;">{'🎉' if correct_count == total_count else '💪'}</div>
            <h3 style="font-size:20px;color:#1e293b;">本轮练习完成！</h3>
            <p style="color:#64748b;margin:1rem 0;">
                答对 <span style="color:#10b981;font-weight:bold;">{correct_count}</span> / {total_count} 道题
            </p>
            {st.button("🔙 返回真题练习首页", key="back_to_real_exam", use_container_width=True)}
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.get('back_to_real_exam'):
            st.session_state.view_mode = "real_exam"
            st.session_state.pop('real_exam_questions', None)
            st.session_state.pop('real_exam_current', None)
            st.session_state.pop('real_exam_show_answer', None)
            st.session_state.pop('real_exam_user_answer', None)
            st.session_state.pop('real_exam_results', None)
            st.experimental_rerun()

def show_wrong_real_exam_view():
    current_subject = st.session_state.get('current_subject')
    real_exam_wrong = st.session_state.get('real_exam_wrong', {})
    
    if not current_subject:
        st.markdown("""
        <div style="margin-bottom:1.5rem;">
            <h2 style="font-size:20px;font-weight:bold;color:#1e293b;margin:0;">🔄 真题错题练习</h2>
            <p style="font-size:14px;color:#64748b;margin-top:0.25rem;">选择科目开始错题练习</p>
        </div>
        """, unsafe_allow_html=True)
        
        subjects_with_wrong = [s for s in get_subjects() if s in real_exam_wrong and len(real_exam_wrong[s]) > 0]
        
        if not subjects_with_wrong:
            st.markdown("""
            <div class="card" style="text-align:center;padding:2rem;">
                <div style="font-size:48px;margin-bottom:1rem;">🎉</div>
                <p style="color:#64748b;">暂无真题错题记录</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            cols = st.columns(2)
            for i, subject in enumerate(subjects_with_wrong):
                with cols[i % 2]:
                    color = get_subject_color(subject)
                    count = len(real_exam_wrong[subject])
                    
                    st.markdown(f"""
                    <div class="subject-card" style="background:{color};">
                        <div style="font-weight:bold;font-size:20px;">{subject}</div>
                        <div style="font-size:14px;opacity:0.9;">{count} 道错题</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"🚀 练习错题", key=f"wrong_real_exam_{subject}", use_container_width=True):
                        st.session_state.current_subject = subject
                        st.session_state.view_mode = "wrong_real_exam"
                        st.experimental_rerun()
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
        <div style="margin-bottom:1rem;">
            <div style="display:flex;align-items:center;gap:1rem;">
                <button onclick="window.history.back()" style="padding:0.5rem 1rem;border-radius:0.5rem;border:none;background:#f1f5f9;cursor:pointer;">
                    ← 返回
                </button>
                <div style="flex:1;text-align:center;">
                    <div style="font-size:14px;color:#64748b;">{current_subject} - 真题错题练习</div>
                    <div style="font-size:12px;color:#9ca3af;">{current_idx+1}/{len(questions)}</div>
                </div>
                <div style="width:60px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if not questions:
            st.markdown("""
            <div class="card" style="text-align:center;padding:2rem;">
                <div style="font-size:48px;margin-bottom:1rem;">🎉</div>
                <p style="color:#64748b;">该科目暂无错题记录</p>
            </div>
            """, unsafe_allow_html=True)
        elif current_idx < len(questions):
            current_q = questions[current_idx]
            
            st.markdown(f"""
            <div class="card">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
                    <div style="font-size:12px;color:#9ca3af;">
                        {current_q['year']}年 {current_q['province']}
                    </div>
                    <div style="font-size:12px;color:#f59e0b;font-weight:bold;">
                        {current_q['question_type']}
                    </div>
                </div>
                
                <div style="padding:1rem;background:#fef3c7;border-radius:0.5rem;margin-bottom:1rem;">
                    <div style="font-size:16px;color:#1e293b;">{current_q['question']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            if current_q['options']:
                for idx, option in enumerate(current_q['options']):
                    option_letter = chr(65 + idx)
                    btn_key = f"wrong_exam_opt_{idx}"
                    is_selected = st.session_state.wrong_exam_user_answer == idx
                    
                    if not st.session_state.wrong_exam_show_answer:
                        if st.button(f"{option_letter}. {option}", key=btn_key, use_container_width=True,
                                   type="primary" if is_selected else "secondary"):
                            st.session_state.wrong_exam_user_answer = idx
                            st.session_state.wrong_exam_show_answer = True
                            st.experimental_rerun()
                    else:
                        is_correct = option_letter == current_q['answer']
                        bg_color = '#dcfce7' if is_correct else ''
                        if is_selected and not is_correct:
                            bg_color = '#fee2e2'
                        
                        st.markdown(f"""
                        <div style="padding:0.75rem;border-radius:0.5rem;margin-bottom:0.5rem;{f'background:{bg_color};' if bg_color else ''}">
                            <span style="font-weight:bold;">{option_letter}.</span> {option}
                            {' ✅' if is_correct else ''}{' ❌' if is_selected and not is_correct else ''}
                        </div>
                        """, unsafe_allow_html=True)
            
            if st.session_state.wrong_exam_show_answer:
                user_ans = st.session_state.wrong_exam_user_answer
                correct_ans = current_q['answer']
                
                is_correct = chr(65 + user_ans) == correct_ans if user_ans is not None else False
                
                if is_correct:
                    st.success("✅ 回答正确！")
                    real_exam_wrong[current_subject] = [q for q in real_exam_wrong[current_subject] if q['question'] != current_q['question']]
                    st.session_state['real_exam_wrong'] = real_exam_wrong
                else:
                    st.error(f"❌ 回答错误！正确答案是：{correct_ans}")
                
                st.markdown(f"""
                <div style="margin-top:1rem;padding:1rem;background:#eff6ff;border-radius:0.5rem;">
                    <div style="font-weight:bold;color:#2563eb;font-size:14px;margin-bottom:0.5rem;">📝 解析</div>
                    <div style="font-size:14px;color:#334155;">{current_q['analysis']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("下一题 ➡️", key="wrong_exam_next", use_container_width=True):
                    st.session_state.wrong_exam_current += 1
                    st.session_state.wrong_exam_show_answer = False
                    st.session_state.wrong_exam_user_answer = None
                    st.experimental_rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card" style="text-align:center;padding:2rem;">
                <div style="font-size:48px;margin-bottom:1rem;">🎉</div>
                <h3 style="font-size:20px;color:#1e293b;">错题练习完成！</h3>
                {st.button("🔙 返回错题本", key="back_to_wrong", use_container_width=True)}
            </div>
            """, unsafe_allow_html=True)
            
            if st.session_state.get('back_to_wrong'):
                st.session_state.view_mode = "wrong"
                st.session_state.pop('wrong_exam_questions', None)
                st.session_state.pop('wrong_exam_current', None)
                st.session_state.pop('wrong_exam_show_answer', None)
                st.session_state.pop('wrong_exam_user_answer', None)
                st.experimental_rerun()

if __name__ == "__main__":
    if 'view_mode' not in st.session_state:
        st.session_state.view_mode = "subject"
    main()