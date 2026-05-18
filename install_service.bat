@echo off
cls
echo ================================
echo Install Gaokao Service
echo ================================

set SERVICE=GaokaoStudyService
set PYTHON=python
set SCRIPT=d:\codex\gaokao\run_server.py

sc query %SERVICE% >nul 2>&1
if not errorlevel 1 (
    echo Service exists, stopping and removing...
    sc stop %SERVICE%
    timeout /t 3 /nobreak >nul
    sc delete %SERVICE%
)

echo Creating service...
sc create %SERVICE% binPath= "%PYTHON% %SCRIPT%" start= auto obj= LocalSystem DisplayName= "Gaokao Study Service"

if errorlevel 1 (
    echo ERROR: Failed to create service. Run as Administrator.
    pause
    exit /b 1
)

echo Service created successfully.
echo Starting service...
sc start %SERVICE%

if errorlevel 1 (
    echo ERROR: Failed to start service.
    pause
    exit /b 1
)

echo ================================
echo Service installed successfully!
echo Access: http://localhost:7777
echo ================================
pause