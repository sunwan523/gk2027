@echo off
echo ==============================================
echo 卸载高考智能复习系统服务
echo ==============================================

set "SERVICE_NAME=GaokaoStudyService"

sc query %SERVICE_NAME% >nul 2>&1
if %errorlevel% equ 0 (
    echo 停止服务...
    sc stop %SERVICE_NAME%
    timeout /t 3 /nobreak >nul
    
    echo 删除服务...
    sc delete %SERVICE_NAME%
    
    if %errorlevel% equ 0 (
        echo ==============================================
        echo 服务卸载完成!
        echo ==============================================
    ) else (
        echo 服务删除失败，请以管理员身份运行此脚本
        pause
    )
) else (
    echo 服务不存在
    pause
)