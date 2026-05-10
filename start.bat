@echo off
cd /d "d:\codex\gaokao"
streamlit run app.py --server.port 9999 --server.address 0.0.0.0
