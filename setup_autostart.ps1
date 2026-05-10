$WshShell = New-Object -ComObject WScript.Shell
$shortcutPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\gaokao_study.lnk"
$shortcut = $WshShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = "d:\codex\gaokao\start_server.vbs"
$shortcut.WorkingDirectory = "d:\codex\gaokao"
$shortcut.Save()
Write-Host "Startup shortcut created successfully!"
Write-Host "Path: $shortcutPath"
