# gk2027 部署与 HTTPS 运维手册

> 最后更新：2026-09-20（HTTPS 正式证书上线）
> 覆盖：架构地址、HTTPS 全流程（自签 → Let's Encrypt）、防锁屏朗读、镜像构建与 88 部署、密钥管理

---

## 一、架构与访问地址

| 入口 | 地址 | 说明 |
|---|---|---|
| 外网（主用） | **https://p.mhtc.top:8443** | 正式证书，地址栏小锁，防锁屏生效 |
| 旧入口（兼容） | http://p.mhtc.top:8577 | 无防锁屏 |
| 88 内网 | https://192.168.100.88:8443 | 自签（IP 无法签正式证书），仅备用 |
| 本机 | http://192.168.100.200:8577 / https://192.168.100.200:8443 | Windows 本机，8443 为自签 |

网络链路：
- 域名 `p.mhtc.top` 托管在 **Cloudflare**（父域 mhtc.top），解析到公网 IP 106.57.7.228
- 公网流量由**爱快主路由**端口转发 8577 / 8443 → 内网 `192.168.100.88`
- `192.168.100.88` 为 iStoreOS（OpenWrt 系）软路由旁路由，Docker 容器 `gk2027-mobile` 长期运行
- 本机 Windows（192.168.100.200）跑同一套服务，用于日常开发

---

## 二、HTTPS 部署详细记录

### 2.1 为什么需要 HTTPS

学习页朗读依赖 **Wake Lock API**（`navigator.wakeLock.request("screen")`）保持手机屏幕常亮、锁屏不断读。该 API **只允许安全域**（HTTPS 或 localhost）调用。原站点全部是 http，手机一锁屏朗读即断，故引入 HTTPS。

### 2.2 证书方案演进

1. **自签证书**（openssl，RSA 2048，10 年）——首版可用，但浏览器一直提示"连接不安全"，需手动放行
2. **Let's Encrypt 正式证书**（EC-256，90 天自动续期）——最终方案。利用域名在 Cloudflare 托管，走 **DNS-01 验证**（无需开放 80 端口、不碰软路由 LuCI 的 80/443、不碰上级路由 HTTP 转发），风险最小

### 2.3 本机 Windows（svc.py 双实例）

`svc.py` 启动时同时拉起两个 uvicorn 进程：
- 8577（HTTP，兼容旧入口）
- 8443（HTTPS，自签证书 `data/certs/cert.pem` + `key.pem`）

证书生成（Git 自带 openssl）：
```
"C:\Program Files\Git\usr\bin\openssl.exe" req -x509 -newkey rsa:2048 \
  -keyout data\certs\key.pem -out data\certs\cert.pem -days 3650 -nodes \
  -subj "/CN=192.168.100.200" \
  -addext "subjectAltName=IP:192.168.100.200,IP:127.0.0.1,DNS:localhost,DNS:p.mhtc.top"
```
相关代码：`svc.py` 的 `HTTPS_PORT=8443` / `CERT_FILE` / `KEY_FILE` / `cmd_start`。

### 2.4 容器（88 Docker）双实例

- `Dockerfile`：`EXPOSE 8577 8443`；`apt-get install openssl`；`CMD ["/app/entrypoint.sh"]`
- `entrypoint.sh`（容器入口）：
  - 检查数据卷证书 `/app/data/certs/cert.pem` 是否存在——存在则复用（正式证书即放这里），不存在则生成自签
  - 后台起 8443（HTTPS）+ 前台 8577（HTTP）
- 容器端口映射：`-p 8577:8577 -p 8443:8443 -v /root/gk2027-data:/app/data`
- 证书持久化在宿主 `/root/gk2027-data/certs/`，重建容器不丢

### 2.5 正式证书（acme.sh + Cloudflare DNS-01）★核心

前置：域名在 Cloudflare 解析；Cloudflare API Token（权限：Zone → DNS → Edit，区域 mhtc.top）。

步骤（全部在 88 上执行）：

```bash
# 1. 安装 acme.sh（装到 /root/.acme.sh，自带续期 cron）
curl -sL https://get.acme.sh | sh

# 2. 指定 Let's Encrypt，注入 Cloudflare Token 并签发（DNS-01 验证）
export CF_Token='<你的 Cloudflare API Token>'
/root/.acme.sh/acme.sh --set-default-ca --server letsencrypt
/root/.acme.sh/acme.sh --issue --dns dns_cf -d p.mhtc.top --keylength ec-256

# 3. 安装证书到容器数据卷（容器入口检测到即复用），并设续期后自动重启容器
/root/.acme.sh/acme.sh --install-cert -d p.mhtc.top --ecc \
  --key-file /root/gk2027-data/certs/key.pem \
  --fullchain-file /root/gk2027-data/certs/cert.pem \
  --reloadcmd 'docker restart gk2027-mobile'

# 4. 验证线上证书
echo | openssl s_client -connect p.mhtc.top:8443 -servername p.mhtc.top 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates
# 期望：subject=CN = p.mhtc.top；issuer=... Let's Encrypt ...
```

续期机制：acme.sh 安装时自动写入 cron，每 60 天检查续期；续期成功自动执行 `docker restart gk2027-mobile` 使 uvicorn 加载新证书。**无需人工干预**。

手动续期（如需）：`/root/.acme.sh/acme.sh --renew -d p.mhtc.top --ecc`

### 2.6 镜像构建与 88 部署

```powershell
# 本机构建并推送多架构镜像（amd64+arm64）到 ghcr.io/sunwan523/gk2027-mobile:latest
powershell -ExecutionPolicy Bypass -File build-image.ps1
```

```bash
# 88 上更新容器（数据卷保留，进度/用户/证书不丢）
docker pull ghcr.io/sunwan523/gk2027-mobile:latest
docker rm -f gk2027-mobile
docker run -d --name gk2027-mobile --restart always \
  -p 8577:8577 -p 8443:8443 \
  -v /root/gk2027-data:/app/data \
  ghcr.io/sunwan523/gk2027-mobile:latest
```

注意：`build-image.ps1` 已内置 `Set-Location $root`，可从任意目录调用；`.dockerignore` 排除 `_vendor/`（Windows 二进制不进镜像，依赖走 requirements.txt 装 Linux 版）。

### 2.7 常见排障

| 现象 | 处理 |
|---|---|
| 外网 https 打不开 | 检查爱快主路由端口转发：TCP 8443 → 192.168.100.88:8443 |
| 证书到期没自动续 | 88 上执行 `/root/.acme.sh/acme.sh --renew -d p.mhtc.top --ecc`，查 cron：`crontab -l` |
| 容器重建后变回自签 | 确认挂载 `-v /root/gk2027-data:/app/data`，证书在 `certs/` 下（entrypoint 检测到即复用） |
| 手机访问还是提示不安全 | 用 `https://p.mhtc.top:8443`（正式证书）；IP 直连（192.168.100.88:8443）是自签必然提示 |

---

## 三、密钥与凭据管理（重要）

> **原则：密钥不明文写入本仓库**（仓库推送到 GitHub 公网，明文即泄露）。以下只记录存放位置与更换方法。

| 凭据 | 用途 | 存放位置 | 更换方法 |
|---|---|---|---|
| Cloudflare API Token | acme.sh 签发/续期 DNS-01 | 88 上 `/root/.acme.sh/account.conf`（CF_Token，签发时环境变量注入） | Cloudflare 控制台 → My Profile → API Tokens 重建 → 更新 88 上 token 后重签 |
| DeepSeek API Key | AI 讲懂 / 出题 / 建议 | 仓库代码 `src/core/ai_quiz.py`（`_chat` 配置） | DeepSeek 开放平台重置 → 替换代码中常量 |
| SSH 密钥 | 本机 → 88 运维 | 本机 `~/.ssh/id_ed25519_gk2027`（root@192.168.100.88） | 重新生成后把公钥追加到 88 的 `~/.ssh/authorized_keys` |
| 数据库 | 用户/进度/空间数据 | 容器内 `/app/data`（挂载宿主 `/root/gk2027-data`）；本机 `data/` | 备份即复制该目录 |

如需在文档/交付物中引用密钥，一律用占位符（如 `<CF_TOKEN>`），真实值只存在于上述运行环境。

---

## 四、防锁屏朗读（Wake Lock）

- 位置：`web/app.js`，`lockScreen()` / `unlockScreen()`
- 逻辑：`ttsSpeak` 开始朗读 → 请求屏幕常亮；暂停/停止/队列读完 → 释放；页面重新可见且正在播放 → 自动重新请求
- 生效条件：仅 HTTPS（或 localhost）；手机 Chrome 上学习页点朗读即常亮，锁屏不再断读
- 已覆盖：播放/暂停/切换卡片/自动翻页/语速即时切换全链路

---

## 五、今日学习页 UI 改动速查（2026-09-20）

- 学习页顶栏压成一行（返回 ← + 标题 + 计数 + 🎓AI 博士帽按钮），全局顶栏隐藏
- 播放控制收进右下角白面板：播放键居中（▶/❚❚ 主题蓝，非 emoji）；左列 自动翻页🔁 / 语速▾ / 字号▾ 上下并列；右列 上一页 / 下一页 上下并列
- 语速三档 1x / 1.5x / 2x 点按弹出、播放中即时生效；字号四档 小16 / 中18 / 大20 / 特大22，全局记忆
- 音色多选（7 种在线 Edge 音色）按卡片轮换，系统音色后备；在线语音优先
- 内容框固定高度 + flex 布局自动填满视口、框底贴住右下播放面板（长屏手机不再悬空），长内容框内滚动
- "开始练习"浅蓝小按钮固定屏幕底部，与播放面板同层不重叠
- 卡片左右滑动切换 + 左右边缘 30% 热区点击翻页；朗读读完自动翻页续读

---

## 六、常用命令速查

```bash
# 本机
python svc.py restart        # 重启服务（8577 + 8443 双实例）
python svc.py status         # 查看状态/地址

# 构建推送镜像（本机）
powershell -ExecutionPolicy Bypass -File build-image.ps1

# 88 运维（本机执行，需 ssh 密钥）
ssh -i ~/.ssh/id_ed25519_gk2027 root@192.168.100.88

# 容器与证书
docker ps | grep gk2027
docker logs gk2027-mobile | grep entrypoint
echo | openssl s_client -connect p.mhtc.top:8443 -servername p.mhtc.top 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```
