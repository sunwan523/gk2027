@echo off
cls
echo ================================
echo Uninstall Gaokao Service
echo ================================

set SERVICE=GaokaoStudyService

sc query %SERVICE% >nul 2>&1
if errorlevel 1 (
    echo Service does not exist.
    pause
    exit /b 0
)

echo Stopping service...
sc stop %SERVICE%
timeout /t 3 /nobreak >nul

echo Deleting service...
sc delete %SERVICE%

if errorlevel 1 (
    echo ERROR: Run as Administrator.
    pause
    exit /b 1
)

echo ================================
echo Service uninstalled successfully!
echo ================================
pause