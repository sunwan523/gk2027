@echo off
cd /d D:\codex\gaokao\gk2027
C:\Python314\python.exe svc.py autostart
echo.
echo Autostart installed: service starts silently at login.
echo To remove: python svc.py autostop
pause
