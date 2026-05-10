@echo off
echo 正在设置开机自动启动...

set shortcut="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\高考冲刺学习系统.lnk"
set target="d:\codex\gaokao\start_server.vbs"

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $shortcut = $WshShell.CreateShortcut('%shortcut%'); $shortcut.TargetPath = '%target%'; $shortcut.WorkingDirectory = 'd:\codex\gaokao'; $shortcut.Save()"

echo 已设置开机自动启动！
echo 启动项已添加到: %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\
pause
