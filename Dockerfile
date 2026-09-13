# gk2027 高考复习系统 容器镜像
# 构建（Windows 本机）：powershell -ExecutionPolicy Bypass -File build-image.ps1
# 依赖中文字体（微软雅黑 + Segoe UI Symbol），由 build-image.ps1 从 Windows 字体目录拷贝到 fonts/
FROM python:3.13-slim

WORKDIR /app

# 项目代码（运行态目录由 .dockerignore 排除）
COPY . /app

# 中文字体目录（PDF 生成依赖，见 config.py 的 GK_FONT_DIR）
COPY fonts/ /app/fonts/
ENV GK_FONT_DIR=/app/fonts

# 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行态目录（容器内 data/output/logs 挂载或新建）
RUN mkdir -p /app/data /app/output /app/logs

EXPOSE 8577

# 手机端入口；电脑端（app.py）可另行指定入口
CMD ["streamlit", "run", "mobile.py", \
     "--server.address=0.0.0.0", "--server.port=8577", \
     "--server.headless=true", "--browser.gatherUsageStats=false"]
