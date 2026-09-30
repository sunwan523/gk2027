# gk2027 高考复习系统

> 口号没变：**排程 → 生成 → 归因 → 看板**。学习发生在纸上，系统只管调度和统计。

## 架构与主入口

| 入口 | 文件 | 技术栈 | 当前角色 |
|------|------|--------|----------|
| **主应用（生产）** | `server.py` + `web/` | FastAPI + 原生 JS 单页应用 | ✅ **实际部署的就是它**。HTTP 8577 / HTTPS 8443 |
| 命令行工具 | `cli.py` | 无框架 | ✅ 日常最快路径（`plan90.bat` / `today.bat` 在用） |
| 本地服务管理 | `svc.py` | uvicorn 子进程 | ✅ Windows 后台服务（`svc_start.bat` 等） |
| 旧手机端界面 | `mobile.py` | Streamlit | ⚠️ 历史版本，已被 `server.py` 取代（`mobile.bat` 仍能启） |
| 旧看板界面 | `app.py` | Streamlit | ⚠️ 历史版本（`start_app.bat`，8501 端口） |

- 业务逻辑全在 `core/`（题库、知识点、作答判分、AI 出题、SRS、PDF 生成等），三种入口共用。
- 容器入口 `entrypoint.sh`：先确保自签证书，再起 8443（HTTPS，手机防锁屏）+ 8577（HTTP，兼容旧入口）。

## 部署总览

| 部署点 | 访问地址 | 方式 | 状态 |
|--------|----------|------|------|
| 外网（主用） | **`https://p.mhtc.top:8443`**（正式证书，防锁屏） | 88 软路由 Docker 容器 `gk2027-mobile` | 运行中（末次更新 2026-09-23 20:45） |
| 旧入口（兼容） | `http://p.mhtc.top:8577` | 同容器 8577 端口 | 运行中 |
| 软路由 iStoreOS（88） | `http://192.168.100.88:8577` / `https://192.168.100.88:8443`（自签备用） | Docker 容器 `gk2027-mobile`（`--restart always`） | 运行中 |
| 本地 Windows | `http://192.168.100.200:8577` / `https://192.168.100.200:8443` | `python svc.py start`（开发用） | **当前未运行**（pid 文件已过期） |

镜像：`ghcr.io/sunwan523/gk2027-mobile:latest`（amd64 + arm64 多架构）

> 📖 **HTTPS 部署、正式证书（Let's Encrypt + Cloudflare DNS-01）、密钥管理、防锁屏朗读、容器运维**详见 [docs/DEPLOY.md](docs/DEPLOY.md)。

## Git 与自动部署（git commit 即部署）

> ⚠️ **重要**：git 仓库根目录是 **`D:\codex\gaokao`（父目录）**，不是本目录，`gk2027/` 只是它跟踪的子目录。

- 仓库根：`D:\codex\gaokao`
- 活动分支：**`master`**（不是 `main`；远程上那个 `main` 分支是 2026-09-13 前的旧版本，已废弃）
- 远程：`gk2027` → `https://github.com/sunwan523/gk2027.git`
- `post-commit` hook 位于 `D:\codex\gaokao\.git\hooks\post-commit`，提交后自动在后台跑 `tools\deploy.ps1`：
  1. `git -C D:\codex\gaokao push gk2027 master` → GitHub
  2. 构建并推送多架构镜像到 ghcr（`build-image.ps1`）
  3. SSH 免密登录软路由 `192.168.100.88` 拉取最新镜像并重建容器

在本目录里直接敲 git 命令即可（会自动上溯到 `D:\codex\gaokao`）。部署日志：`logs\deploy.log`。

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
>
> 注：爱快 Web 上保存的 YML 若还是旧版（镜像 `ghcr.nju.edu.cn/...`），仍可正常运行（南大镜像已拉到本地）；若南大加速拉取失败，需把爱快 YML 的镜像行改成 `ghcr.io/sunwan523/gk2027-mobile:latest`。

## 爱快手动更新步骤（每次改代码后）

> 镜像从 `ghcr.io` 或 `ghcr.nju.edu.cn` 拉取均可，**镜像名必须与爱快上 YML 里写的 image 一致**（当前为 `ghcr.nju.edu.cn/sunwan523/gk2027-mobile`）。

1. **拉取最新镜像**：
   - 爱快 Web → 高级服务 → Docker → **本地镜像** → 右上角**下载镜像**
   - 镜像名填 `ghcr.nju.edu.cn/sunwan523/gk2027-mobile`（或 ghcr.io 版），标签留 `latest` → 点**下载**
   - ⚠️ 爱快下载**没有进度条**，界面可能一直显示"下载中(0)"：等 1~3 分钟后重新进本地镜像页，看该镜像的"下载时间/大小"是否变化（变了即成功）
2. **重启容器**：
   - 切到 **Compose** 页 → 找到 **gk2027** → 点右侧**电源图标**（停止）→ 等状态变化
   - 再点**电源图标**（开启）→ 等状态变为"**正在运行**"（约 1~2 分钟，期间别刷新）
3. **验证**：浏览器打开 `http://192.168.100.1:8577`，能出页面即成功

**南大加速拉不动时**：镜像名改用 `ghcr.io/sunwan523/gk2027-mobile` 下载，并同步把爱快 YML 的 image 行改成 ghcr.io 地址（改完再执行第 2 步）。

## 镜像构建与推送（本机）

```powershell
# 自动拷贝 Windows 中文字体并 buildx 多架构推送 ghcr
powershell -NoProfile -ExecutionPolicy Bypass -File D:\codex\gaokao\gk2027\build-image.ps1
```

- 构建环境：Docker Desktop + buildx，平台 `linux/amd64,linux/arm64`
- 字体：容器内 `GK_FONT_DIR=/app/fonts`（msyh/msyhbd/seguisym 已随镜像打包）
- 生产依赖（`requirements.txt`，容器用清华源安装）：`fastapi`、`uvicorn`、`pydantic`、`cryptography`、`reportlab`、`edge-tts`
  - ⚠️ **依赖里没有 streamlit**：`mobile.py` / `app.py` 这两个旧 Streamlit 界面只在本机跑，本机 Python 需自行安装 streamlit

## 本机 Windows

- 服务：`python svc.py start`（隐藏窗口后台运行，日志 `logs/mobile.log`，进程 pid 在 `data/mobile*.pid`）
- 开机自启：计划任务 `GK2027MobileAutoStart`（登录触发）+ 启动文件夹快捷方式兜底

## 常见问题

- **git push 走代理**：仓库配置了 `http.proxy=http://192.168.100.88:7890`（软路由代理）
- **在本目录敲 git 报 "not a git repository"**：历史上的 `.git` 指针文件已失效并移走，现在会自动上溯到 `D:\codex\gaokao`；若仍报错，检查本目录是否又冒出了 `.git` 文件
- **爱快拉取镜像**：爱快实测南大加速 `ghcr.nju.edu.cn` 拉取超时（compose 报 `failed to wait for process: timeout`），改用 **`ghcr.io` 直连**成功；镜像公开后直连即可匿名拉取
- **容器内 PDF 字体**：依赖 `/app/fonts` 下的 msyh.ttc/msyhbd.ttc/seguisym.ttf，缺失时 PDF 中文会乱码
- **日志里的 `ConnectionResetError 10054`**：手机/浏览器断开连接的噪音，可忽略

## 目录说明

```
core/        业务逻辑（题库/知识点/判分/AI出题/SRS/PDF）
web/         前端单页应用（index.html / app.js / style.css）
data/        运行态数据（SQLite 库、证书、照片、pid）
output/      生成的 PDF
logs/        服务与部署日志
tools/       deploy.ps1 部署脚本
_vendor/     本机 Windows 本地依赖副本（fastapi/uvicorn，勿删）
_trash_20260924/  2026-09-24 大扫除回收区，确认无影响后可整目录删除
```

> `_trash_20260924/` 里是迁移过来的历史残留：失效的 `.git` 指针、一次性补丁脚本（`_patch_*.py` 等）、空壳 `.git_old/`、空文件 `x`。它们原本就已 gitignore、未被任何代码引用；观察几天没问题直接删掉即可，需要恢复也能从这个目录捞回来。
