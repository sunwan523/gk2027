@echo off
rem gk2027 Streamlit dashboard - on-demand start.
rem Close this window to stop the service (nothing runs in background).
cd /d D:\codex\gaokao\gk2027
echo Starting gk2027 dashboard at http://localhost:8501 ...
echo Close this window to stop the service.
C:\Python314\python.exe -m streamlit run app.py
