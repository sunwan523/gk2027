# gk2027 高考复习系统

高考复习系统：`mobile.py`（手机端，Streamlit，端口 **8577**）、`app.py`（电脑端）。

## 部署总览

| 部署点 | 访问地址 | 方式 | 状态 |
|--------|----------|------|------|
| 本地 Windows | `http://p.mhtc.top:8577`（DDNS + 端口映射） | 系统服务 `svc.py` | 运行中 |
| 软路由 iStoreOS | `http://192.168.100.88:8577` | Docker 容器 `gk2027-mobile`（`--restart always`） | 运行中 |
| 爱快软路由 | `http://192.168.100.1:8577` | Docker Compose（Web 编排） | 运行中 |

代码仓库：`https://github.com/sunwan523/gk2027`（main 分支）
镜像：`ghcr.io/sunwan523/gk2027-mobile:latest`（amd64 + arm64 多架构）

## 自动部署（git commit 即部署）

项目 `.git` 为 gitdir 指针（实体仓库在 `C:\Users\sunwa\AppData\Local\Temp\gk2027-git\.git`），
并安装了 `post-commit` hook：**每次 `git commit` 后自动在后台执行** `tools\deploy.ps1`：

1. `git push` → GitHub
2. 本地 Windows 服务重启（`svc.py restart`）
3. 构建并推送多架构镜像到 ghcr（`build-image.ps1`）
4. SSH 免密登录软路由 `192.168.100.88` 拉取最新镜像并重建容器

爱快无法命令行代做：每次提交后需在爱快 Web 手动「镜像管理拉取 latest → 重启容器」。
部署日志：`logs\deploy.log`。
### 手动部署

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File D:\codex\gaokao\gk2027\tools\deploy.ps1
```

## 软路由（iStoreOS 192.168.100.88）部署细节

- 容器：`gk2027-mobile`，`--restart always`，端口 `8577:8577`，数据目录 `/root/gk2027-data:/app/data`
- SSH 免密：本机密钥 `C:\Users\sunwa\.ssh\id_ed25519_gk2027`，公钥已写入软路由
  `/etc/dropbear/authorized_keys`（OpenWrt dropbear 的全局公钥路径，注意不是 `~/.ssh/`）
- 首次部署命令：

```bash
ssh -i C:\Users\sunwa\.ssh\id_ed25519_gk2027 -o BatchMode=yes root@192.168.100.88 \
  "mkdir -p /root/gk2027-data && docker pull ghcr.io/sunwan523/gk2027-mobile:latest && \
   docker rm -f gk2027-mobile; \
   docker run -d --name gk2027-mobile --restart always -p 8577:8577 \
     -v /root/gk2027-data:/app/data ghcr.io/sunwan523/gk2027-mobile:latest"
```

## 爱快（192.168.100.1）部署步骤

参照 `docker-compose.yml`（已按爱快实测约束编写：镜像 `ghcr.io` 直连——南大加速 `ghcr.nju.edu.cn` 在爱快拉取超时、ghcr.io 直连成功；挂载为相对路径）：

1. 爱快 Web → Docker → 编排 → 新建，粘贴 `docker-compose.yml` 内容
2. 保存后爱快落盘到 `/docker/Compose/doc_gk2027/gk2027.yaml`
3. 爱快文件管理 → 进入该目录 → **手动新建 `data` 文件夹**（爱快不会自动建）
4. Docker → 编排 → 点开启（镜像从 `ghcr.io` 直连拉取，约 200MB 需等待）
5. 访问 `http://192.168.100.1:8577`

> 已部署完成（2026-09-13）：gk2027-mobile 容器运行中，`http://192.168.100.1:8577` 可访问。

## 镜像构建与推送（本机）

```powershell
# 自动拷贝 Windows 中文字体并 buildx 多架构推送 ghcr
powershell -NoProfile -ExecutionPolicy Bypass -File D:\codex\gaokao\gk2027\build-image.ps1
```

- 构建环境：Docker Desktop + buildx，平台 `linux/amd64,linux/arm64`
- 字体：容器内 `GK_FONT_DIR=/app/fonts`（msyh/msyhbd/seguisym 已随镜像打包）
- pip 依赖走清华镜像源（`requirements.txt`：streamlit==1.62.0、reportlab==5.0.1）

## 本机 Windows

- 服务：`C:\Python314\pythonw.exe D:\codex\gaokao\gk2027\svc.py _autorun`
- 开机自启：计划任务 `GK2027MobileAutoStart`（登录触发）+ 启动文件夹快捷方式兜底

## 常见问题

- **git push 走代理**：仓库配置了 `http.proxy=http://192.168.100.88:7890`（软路由代理）
- **爱快拉取镜像**：爱快实测南大加速 `ghcr.nju.edu.cn` 拉取超时（compose 报 `failed to wait for process: timeout`），改用 **`ghcr.io` 直连**成功；镜像公开后直连即可匿名拉取
- **容器内 PDF 字体**：依赖 `/app/fonts` 下的 msyh.ttc/msyhbd.ttc/seguisym.ttf，缺失时 PDF 中文会乱码
