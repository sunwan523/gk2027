# 高考冲刺 · 智能复习系统

一个基于 Streamlit 的高考智能复习系统，包含语文、数学、英语、物理、化学、生物六门学科的知识点学习、题目练习、真题演练等功能。

## 功能特性

- 📚 分科目知识点学习
- 📝 针对性题目练习
- 📋 24天冲刺学习计划
- 🔄 知识复盘功能
- ❌ 错题本系统
- 🎯 历年真题练习
- 🔊 语音朗读支持

## 本地运行

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
streamlit run app.py
```

## 部署到 Streamlit Community Cloud

### 1. 创建 GitHub 仓库

1. 在 GitHub 上创建一个新的仓库
2. 将本项目推送到 GitHub

### 2. 部署到 Streamlit

1. 访问 [share.streamlit.io](https://share.streamlit.io)
2. 点击 "New app"
3. 连接你的 GitHub 账号
4. 选择你的仓库和分支
5. 主文件路径设置为：`app.py`
6. 点击 "Deploy!"

## 技术栈

- Streamlit 1.32.0
- Pandas 2.2.1
- NumPy 1.26.4

## 项目结构

```
.
├── app.py                 # 主应用文件
├── requirements.txt       # 依赖列表
├── config.py             # 配置文件
├── data/                 # 数据模块
│   ├── knowledge/        # 知识点数据
│   ├── questions/        # 练习题数据
│   ├── real_exam/        # 真题数据
│   ├── knowledge_loader.py
│   ├── questions_loader.py
│   ├── real_exam_loader.py
│   ├── progress.py       # 进度管理
│   ├── study_plan.py     # 学习计划
│   └── subjects.py       # 科目配置
└── README.md
```
