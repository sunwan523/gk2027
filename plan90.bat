@echo off
chcp 65001 >nul
cd /d D:\codex\gaokao\gk2027
C:\Python314\python.exe cli.py plan90
if %errorlevel% neq 0 goto fail
echo.
echo Opening newest plan PDF...
powershell -NoProfile -Command "Get-ChildItem 'D:\codex\gaokao\gk2027\output\90*.pdf' | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Invoke-Item"
timeout /t 5 >nul
exit /b 0
:fail
echo.
echo Generate FAILED. Check messages above.
pause
exit /b 1
