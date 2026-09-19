# gk2027 高考复习系统 容器镜像
# 构建（Windows 本机）：powershell -ExecutionPolicy Bypass -File build-image.ps1
# 依赖中文字体（微软雅黑 + Segoe UI Symbol），由 build-image.ps1 从 Windows 字体目录拷贝到 fonts/
FROM python:3.13-slim

WORKDIR /app

# 项目代码（_vendor 里的 Windows 二进制由 .dockerignore 排除，依赖走 requirements.txt 装 Linux 版）
COPY . /app

# 中文字体目录（PDF 生成依赖，见 config.py 的 GK_FONT_DIR）
COPY fonts/ /app/fonts/
ENV GK_FONT_DIR=/app/fonts

# 依赖（国内网络用清华镜像源；构建成功后部署端只拉取成品镜像，无需 pip）
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 自签证书生成依赖 openssl
RUN apt-get update && apt-get install -y --no-install-recommends openssl \
    && rm -rf /var/lib/apt/lists/*

# 运行态目录（容器内 data/output/logs 挂载或新建）
RUN mkdir -p /app/data /app/output /app/logs

EXPOSE 8577 8443

# 入口脚本：先确保自签证书，再起 8443(HTTPS 防锁屏) + 8577(HTTP 兼容旧入口)
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
