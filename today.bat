@echo off
chcp 65001 >nul
rem Show today's tasks (no browser needed).
cd /d D:\codex\gaokao\gk2027
C:\Python314\python.exe cli.py today
echo.
pause
