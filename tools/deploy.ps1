# ============================================================
# deploy.ps1 — gk2027 一键部署（git commit 后自动调用）
# 流程：push GitHub → 本地服务重启 → 构建推送 ghcr 镜像 → 软路由更新
# 爱快需在 Web 上拉取 latest 并重启容器（见 deploy 输出提示）
# ============================================================

$ErrorActionPreference = 'Continue'
$root = 'D:\codex\gaokao\gk2027'
$logFile = Join-Path $root 'logs\deploy.log'
New-Item -ItemType Directory -Force -Path (Split-Path $logFile) | Out-Null
Start-Transcript -Path $logFile -Append -Force
$PY = 'C:\Python314\python.exe'
$SSHKEY = 'C:\Users\sunwa\.ssh\id_ed25519_gk2027'
$ROUTER = 'root@192.168.100.88'
$IMG = 'ghcr.io/sunwan523/gk2027-mobile:latest'

Write-Host "[1/4] git push GitHub ..."
git -C $root push 2>&1

Write-Host "[2/4] 本地服务重启（Windows 原生） ..."
& $PY (Join-Path $root 'svc.py') restart 2>&1

Write-Host "[3/4] 构建并推送 ghcr 镜像 ..."
& powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $root 'build-image.ps1') 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[3/4] 构建/推送失败，停止后续部署。" -ForegroundColor Red
    exit 1
}

Write-Host "[4/4] 软路由 192.168.100.88 更新容器 ..."
ssh -i $SSHKEY -o BatchMode=yes -o ConnectTimeout=8 $ROUTER "mkdir -p /root/gk2027-data && docker pull $IMG && docker rm -f gk2027-mobile && docker run -d --name gk2027-mobile --restart always -p 8577:8577 -v /root/gk2027-data:/app/data $IMG" 2>&1

Write-Host ""
Write-Host "部署完成。"
Write-Host "  - 本地:     http://p.mhtc.top:8577（DDNS 端口映射）"
Write-Host "  - 软路由:   http://192.168.100.88:8577"
Write-Host "  - 爱快:     请在爱快 Docker 界面拉取 latest 镜像后重启 gk2027-mobile 容器"
