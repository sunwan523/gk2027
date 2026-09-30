# 微信小程序接入方案

> 状态：**规划稿，尚未动工**。本文只做设计，未修改任何现有代码。
> 目标：在现有 `server.py` + `web/` 之外，再加一个微信小程序前端，**全量照搬 web 端功能**。

---

## 一、现状盘点（改造的事实基础）

| 层 | 现状 | 对小程序的影响 |
|---|---|---|
| 后端 | `server.py`（FastAPI），**40+ 个 REST 接口** | ✅ 接口可完全复用，无需重写业务 |
| 业务逻辑 | 全在 `core/`（题库/知识点/判分/AI 出题/SRS/PDF/日记） | ✅ 零改动 |
| 前端 | `web/` 单页应用（原生 JS，无框架） | 小程序端另起一套 UI，接口层对齐 |
| 鉴权 | Cookie `gk_uid`（httponly），`/api/login` 传用户名即建号，**无密码** | ⚠️ 小程序无 Cookie 自动管理，需加 token 通道 |
| 多用户 | `data/users.json` 注册表 + 每用户独立 SQLite（`data/users/<id>.db`） | ✅ 直接沿用 |
| 部署 | 域名 `p.mhtc.top`（已备案，Cloudflare 托管）→ 公网 `106.57.7.228` → 爱快转发 `8577/8443` → `192.168.100.88` | ⚠️ 小程序强制 https + **443 端口**，当前 8443 不合规 |
| 前端地址 | `web/app.js` **无任何硬编码域名/端口**（全相对路径） | ✅ 换域名对 web 端透明 |
| 图片 | `app.mount("/photos", ...)` 静态目录；头像/照片上传走 **JSON base64**（非 multipart） | ✅ 小程序可用 `chooseMedia` + base64 复用，不需配置 uploadFile 域名 |

---

## 二、三个前置条件（阻塞项，必须先落地）

### 1. 小程序账号：AppID + AppSecret
- 微信公众平台注册小程序（个人主体即可，免费）→ 拿到 **AppID / AppSecret**。
- 开发阶段可先用**测试号**跑通流程，但最终发布需要正式 AppID。
- AppSecret 属敏感信息：走**环境变量**注入容器（`WX_APPID` / `WX_SECRET`），绝不入库、不写进代码。

### 2. 443 入口：Cloudflare Tunnel（已选方案）

小程序 `request` 合法域名必须是 **https + 端口 443**，且需工信部备案。当前 `https://p.mhtc.top:8443` 端口不合规。

Cloudflare Tunnel 让公网 443 由 Cloudflare 终止，再转发到内网 `8577`，**不用开端口、不用管证书（CF 免费签发）、不碰软路由被占用的 443**。

软路由侧配置（`config.yml` 示意）：

```yaml
tunnel: <tunnel-id>
credentials-file: /root/.cloudflared/<tunnel-id>.json
ingress:
  - hostname: mp.mhtc.top          # 建议：小程序专用子域
    service: http://192.168.100.88:8577
  - service: http_status:404
```

```bash
cloudflared tunnel login
cloudflared tunnel create gk2027
cloudflared tunnel route dns gk2027 mp.mhtc.top   # CF 自动建 CNAME
cloudflared tunnel run gk2027                      # 建议 docker 容器常驻
```

**⚠️ 关键决策：域名要不要分开？** 一旦某域名开启 CF 代理（橙色云），外网就只能走 80/443，原来的 `:8443/:8577` 直连会失效。两种选择：

- **方案 A（推荐先这样）**：新开子域 `mp.mhtc.top` 走 Tunnel 给小程序用；`p.mhtc.top` 保持现状给 web 端。两者互不影响，切换零风险。
- **方案 B（更干净，后做）**：`p.mhtc.top` 整体走 Tunnel，web 和小程序统一用 `https://p.mhtc.top`。需同步改 `config.py` 的 `PUBLIC_URL` 和 README，且旧入口失效。

> 备案：`mhtc.top` 已备案，子域通常随主域生效；若微信后台校验不通过，就改用备案信息里明确包含的那个域名。

### 3. 微信后台配置
- 小程序后台 → 开发管理 → 开发设置 → **服务器域名**：
  - `request 合法域名`：`https://mp.mhtc.top`
  - `uploadFile / downloadFile`：本方案不需要（图片走 JSON base64）
  - `socket`：暂不需要
- 开发期可在开发者工具勾选「不校验合法域名」先跑通，但**体验版和正式版会真校验**，所以 443 + 备案必须搞定。

---

## 三、后端改造清单

### 3.1 鉴权：Cookie + Token 双通道（核心改动）

小程序无法自动管理 Cookie，因此让 `_user_from()` 同时认两种凭证，**web 端行为完全不变**：

```
凭证优先级：Authorization: Bearer <token>  >  Cookie gk_uid
```

| 文件 | 改动 |
|---|---|
| `core/wx.py`（新增） | `code2session(code)` 换 openid/session_key（用标准库 `urllib.request`，**零新依赖**）；token 生成与校验 |
| `core/session.py`（新增，或并入 wx.py） | token 持久化：`data/sessions.db`（表 `sessions(token, uid, expire)`），避免容器重启后全体掉线 |
| `core/users.py` | user 对象加 `wx_openid` 字段；新增 `find_by_openid()` / `bind_wx()` |
| `server.py` | 改 `_user_from()` 支持 Bearer；新增 `/api/wx/login`、`/api/wx/refresh` |
| `config.py` | 新增 `WX_APPID` / `WX_SECRET`（读环境变量）；`PUBLIC_URL` 按接入域名更新 |
| `requirements.txt` | **无需新增依赖** |

新接口契约：

```
POST /api/wx/login   { code }  →  { ok, token, user:{id,name}, is_new }
POST /api/wx/refresh { token } →  { ok, token }        # 续期，避免用到期掉线
```

登录流程（对应用户选择的「微信 openid 独立账号」）：
1. 小程序 `wx.login()` 拿 code → 后端 `code2session` → openid
2. `find_by_openid(openid)` 命中 → 直接签发 token
3. 未命中 → `ensure_user("wx_" + openid[:6])` 自动建号 + seed 灌库 + 绑定 openid → 签发 token
4. 用户之后可在「我的」里改昵称（复用现有 `/api/profile/save`）

> token 有效期建议 30 天；所有接口 401 时小程序端自动重登。

### 3.2 其他需要适配的点

| 事项 | 处理方式 |
|---|---|
| **TTS 朗读** | 现有 `/api/tts` 直接返回音频二进制。小程序端用 `responseType: 'arraybuffer'` 拉取 → 写临时文件 → `InnerAudioContext` 播放。**后端零改动** |
| **图片/照片** | 展示需绝对地址：`https://mp.mhtc.top/photos/<path>`，小程序端统一拼 base URL；上传复用现有 JSON base64 接口 |
| **私密空间门禁（5235）** | 现有 `/api/diary/private/*` 接口直接复用；解锁状态建议存**服务端 session**（不要只存小程序本地，易被清且可伪造） |
| **并发** | `wx.request` 最大并发 10；答题提交串行即可，无需后端限流 |
| **CORS** | 小程序不受浏览器同源策略限制，**无需改** |
| **镜像体积** | `.dockerignore` 加 `miniprogram/`，小程序代码不进后端镜像 |

---

## 四、小程序端结构（新建 `miniprogram/`）

技术选型：**原生小程序**（与 `web/` 一致的无框架风格，无构建链、包体小、调试直连）。若要跨端复用可考虑 Taro/uni-app，但成本高、收益不明显。

```
miniprogram/
├─ app.js / app.json / app.wxss / sitemap.json / project.config.json
├─ utils/
│   ├─ api.js        # 封装 wx.request：统一带 token、统一 401 重登、统一错误提示
│   └─ config.js     # BASE_URL（https://mp.mhtc.top）
├─ pages/            # 主包（tabBar）
│   ├─ index/        # 今日任务：顶栏（连续天数/XP/掌握度）+ 课程队列
│   ├─ lesson/       # 课程列表（按科目筛选，含已掌握 ✅）
│   ├─ quiz/         # 答题：题干/选项/提交/判分/解析/AI 讲解
│   ├─ review/       # 复习（SRS 队列 + 归因）
│   └─ mine/         # 我的：个人资料、统计、设置
├─ packageDiary/     # 分包：日记（月视图/日编辑/AI 整理）
├─ packageRecite/    # 分包：背诵（目录/卡片/已背进度）
├─ packagePrivate/   # 分包：私密空间（密码门禁 + 照片）
└─ components/       # 复用组件：顶栏、题目卡、底部 tab、空状态
```

**包体限制**：主包 ≤ 2MB、总包 ≤ 20MB → 日记/背诵/私密空间走**分包**按需加载。

---

## 五、实施里程碑

| 阶段 | 内容 | 产出 |
|---|---|---|
| **M0 前置** | 注册小程序拿 AppID/AppSecret；确定接入域名（建议 `mp.mhtc.top`）；确认备案可用 | 凭据 + 域名就绪 |
| **M1 网络打通** | 软路由跑 cloudflared Tunnel；浏览器验证 `https://mp.mhtc.top/api/me` 通 | 443 入口可用 |
| **M2 后端改造** | Cookie+Token 双通道、`/api/wx/login`、openid 绑定、sessions 持久化 | web 端不受影响，小程序可登录 |
| **M3 主流程闭环** | 小程序骨架：登录 → 今日任务 → 课程 → 答题 → 判分 → 归因 | 开发版跑通核心闭环 |
| **M4 补齐学习侧** | 复习(SRS)、统计看板、背诵、设置（音色/语速/字号） | 学习功能对齐 web |
| **M5 补齐生活侧** | 日记（含 AI 整理）、私密空间与照片、个人资料/体重 | 全量功能对齐 |
| **M6 上线** | 配置合法域名、加体验成员、真机验证；按需提交审核 | 可用（自用走体验版即可，无需提审） |

建议：**M1、M2 与 M3 前端骨架可以并行**——后端改造不依赖小程序代码。

---

## 六、风险与注意事项

1. **域名切换会打断旧入口**：某域名一旦开 CF 代理，外网 `:8443/:8577` 直连失效 → 用方案 A 的新子域规避。
2. **个人主体小程序类目受限**：教育类目可能要资质。自用**走体验版不提审**即可规避；若要发布，类目建议选「工具 → 效率」（以微信后台实际可选为准）。
3. **体验版也校验合法域名**：开发者工具可勾「不校验」，但体验版/正式版真校验 → 443 + 备案是硬门槛。
4. **AppSecret 泄露风险**：只放环境变量，别写进仓库；`data/` 已 gitignore，但 Tunnel 凭据在软路由上，同样别外泄。
5. **容器重启导致掉线**：token 必须持久化（SQLite），不能只放内存。
6. **`users.json` 并发写**：注册/绑定走「读-改-写」+ `os.replace` 原子替换，现有实现已是这个模式，新增绑定逻辑时保持一致。
7. **PDF 生成接口**（`/api/export/*`）：小程序端无法直接打印，建议首版只提供「预览」或暂不接入（待定）。

---

## 七、待你拍板的几个点

1. **接入域名**：`mp.mhtc.top`（新子域走 Tunnel，web 端不动）还是 `p.mhtc.top` 整体切换？
2. **AppID**：已有正式小程序账号，还是先用测试号开发？
3. **cloudflared 跑在哪**：软路由 docker 容器，还是本机 Windows（软路由更合适，7×24 在线）？
4. **PDF 导出**：小程序端是否需要？若要，走「预览」还是「转发文件」？
5. **是否提审发布**：自用走体验版（免审核），还是要正式发布上线？
