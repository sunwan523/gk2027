@echo off
echo ==============================================
echo 安装高考智能复习系统开机自启动服务
echo ==============================================

set "SERVICE_NAME=GaokaoStudyService"
set "PYTHON_PATH=python"
set "SCRIPT_PATH=d:\codex\gaokao\run_server.py"
set "WORKING_DIR=d:\codex\gaokao"

sc query %SERVICE_NAME% >nul 2>&1
if %errorlevel% equ 0 (
    echo 服务已存在，先停止并删除...
    sc stop %SERVICE_NAME%
    sc delete %SERVICE_NAME%
    timeout /t 3 /nobreak >nul
)

echo 创建服务...
sc create %SERVICE_NAME% binPath= "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" start= auto obj= LocalSystem DisplayName= "高考智能复习系统"

if %errorlevel% equ 0 (
    echo 服务创建成功!
    echo 启动服务...
    sc start %SERVICE_NAME%
    
    if %errorlevel% equ 0 (
        echo ==============================================
        echo 服务安装完成!
        echo 访问地址: http://localhost:7777
        echo ==============================================
    ) else (
        echo 服务启动失败，请检查配置
        pause
    )
) else (
    echo 服务创建失败，请以管理员身份运行此脚本
    pause
)