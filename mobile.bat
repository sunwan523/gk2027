@echo off
rem gk2027 mobile learning server (Duolingo-style).
rem Phone on SAME wifi opens the LAN url printed below.
rem Close this window to stop the service (nothing runs in background).
cd /d D:\codex\gaokao\gk2027
echo ============================================
echo  gk2027 phone study  -  LAN access
echo ============================================
echo.
echo  PC LAN IP (wifi):
ipconfig | findstr /i "IPv4"
echo.
echo  Open on your phone browser:
echo      http://192.168.100.200:8577
echo  (make sure phone is on the SAME wifi)
echo.
echo  Close this window to stop.
echo.
C:\Python314\python.exe -m streamlit run mobile.py --server.address 0.0.0.0 --server.port 8577 --server.headless true
