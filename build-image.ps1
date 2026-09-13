# ============================================================
# build-image.ps1 — 构建 gk2027-mobile 多架构镜像并推送到 ghcr
# 供软路由（iStoreOS/爱快）Docker 拉取使用；登录信息复用 iptv 的
# sunwan523@ghcr.io（Docker Desktop 凭据管理器已存）
#
# 前置条件：本机已安装 Docker Desktop（含 buildx）
# 用法：powershell -ExecutionPolicy Bypass -File build-image.ps1
# ============================================================

$ErrorActionPreference = 'Stop'

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "未检测到 docker 命令，请先安装 Docker Desktop。" -ForegroundColor Red
    exit 1
}

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$fonts = Join-Path $root 'fonts'
New-Item -ItemType Directory -Force -Path $fonts | Out-Null

# PDF 生成依赖的中文字体（微软雅黑 + Segoe UI Symbol），拷贝进构建上下文
$fontFiles = @{
    'C:\Windows\Fonts\msyh.ttc'      = 'msyh.ttc'
    'C:\Windows\Fonts\msyhbd.ttc'    = 'msyhbd.ttc'
    'C:\Windows\Fonts\seguisym.ttf'  = 'seguisym.ttf'
}
foreach ($src in $fontFiles.Keys) {
    if (-not (Test-Path $src)) { Write-Host "缺少字体：$src" -ForegroundColor Red; exit 1 }
    Copy-Item $src (Join-Path $fonts $fontFiles[$src]) -Force
}
Write-Host ">>> 字体已就绪：$fonts"

Write-Host ">>> 构建并推送 ghcr.io/sunwan523/gk2027-mobile:latest (amd64+arm64) ..."
docker buildx build --platform linux/amd64,linux/arm64 `
    -t ghcr.io/sunwan523/gk2027-mobile:latest --push .

if ($LASTEXITCODE -ne 0) { Write-Host "构建/推送失败" -ForegroundColor Red; exit $LASTEXITCODE }
Write-Host ""
Write-Host "完成！镜像已推送 ghcr.io/sunwan523/gk2027-mobile:latest" -ForegroundColor Green
Write-Host "部署点更新："
Write-Host "  - 软路由 iStoreOS:  ssh root@192.168.100.88 (docker pull + 重建容器)"
Write-Host "  - 爱快:             Docker → 镜像管理拉取 latest 后重启容器"
