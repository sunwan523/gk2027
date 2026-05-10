import json
import os
import streamlit as st
from data.subjects import get_subjects, get_subject_total_kps

PROGRESS_FILE = "data/progress.json"

def load_progress_file():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_progress_file(data):
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def init_progress():
    saved_data = load_progress_file()
    
    if 'study_progress' not in st.session_state:
        st.session_state.study_progress = saved_data.get('study_progress', {})
    
    if 'wrong_questions' not in st.session_state:
        st.session_state.wrong_questions = saved_data.get('wrong_questions', {})
    
    if 'current_subject' not in st.session_state:
        st.session_state.current_subject = saved_data.get('current_subject', "语文")
    
    if 'current_kp_index' not in st.session_state:
        st.session_state.current_kp_index = saved_data.get('current_kp_index', 0)
    
    # 首次打开始终显示首页
    if 'view_mode' not in st.session_state:
        st.session_state.view_mode = "subject"
    
    if 'subject_kp_indexes' not in st.session_state:
        st.session_state.subject_kp_indexes = saved_data.get('subject_kp_indexes', {})
    
    if 'last_study_time' not in st.session_state:
        st.session_state.last_study_time = saved_data.get('last_study_time', {})

def save_progress():
    data = {
        'study_progress': st.session_state.study_progress,
        'wrong_questions': st.session_state.wrong_questions,
        'current_subject': st.session_state.current_subject,
        'subject_kp_indexes': st.session_state.subject_kp_indexes,
        'last_study_time': st.session_state.last_study_time
    }
    save_progress_file(data)

def get_progress(subject):
    if subject not in st.session_state.study_progress:
        st.session_state.study_progress[subject] = 0
    return st.session_state.study_progress[subject]

def update_progress(subject):
    current = get_progress(subject)
    total = get_subject_total_kps(subject)
    if current < total:
        st.session_state.study_progress[subject] = current + 1
        st.session_state.subject_kp_indexes[subject] = current + 1
        st.session_state.last_study_time[subject] = {
            'timestamp': str(st.session_state.get('current_kp_index', 0)),
            'kp_index': st.session_state.get('current_kp_index', 0)
        }
        save_progress()

def get_wrong_questions(subject=None):
    if subject is None:
        return st.session_state.wrong_questions
    return st.session_state.wrong_questions.get(subject, [])

def add_wrong_question(subject, kp_name, question_data):
    if subject not in st.session_state.wrong_questions:
        st.session_state.wrong_questions[subject] = []
    st.session_state.wrong_questions[subject].append({
        "kp": kp_name,
        "question": question_data["question"],
        "options": question_data["options"],
        "user_answer": None,
        "correct_answer": question_data["answer"],
        "analysis": question_data["解析"]
    })
    save_progress()

def remove_wrong_question(subject, index):
    if subject in st.session_state.wrong_questions:
        if 0 <= index < len(st.session_state.wrong_questions[subject]):
            st.session_state.wrong_questions[subject].pop(index)
            save_progress()

def clear_wrong_questions(subject):
    if subject in st.session_state.wrong_questions:
        st.session_state.wrong_questions[subject] = []
        save_progress()

def get_last_kp_index(subject):
    return st.session_state.subject_kp_indexes.get(subject, 0)

def set_current_kp_index(subject, index):
    st.session_state.subject_kp_indexes[subject] = index
    st.session_state.current_kp_index = index
    save_progress()

def get_total_progress():
    subjects = get_subjects()
    total_progress = 0
    total_kps = 0
    for subject in subjects:
        total_progress += get_progress(subject)
        total_kps += get_subject_total_kps(subject)
    return total_progress, total_kps