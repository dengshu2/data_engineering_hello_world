# 使用 Python 3.10 作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖和 Poetry
# curl: 用于下载 Poetry 安装脚本
# build-essential: 用于编译 Python 扩展模块
# 安装后清理 apt 缓存以减小镜像大小
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 -

# 将 Poetry 添加到 PATH
ENV PATH="/root/.local/bin:$PATH"

# 复制项目文件
COPY pyproject.toml .
COPY src/ ./src/
COPY scripts/ ./scripts/

# 安装依赖
RUN poetry install --no-dev --no-interaction

# 创建必要的目录结构
RUN mkdir -p data/raw data/processed data/final logs

# 设置环境变量
ENV PYTHONPATH=/app
ENV PROJECT_ROOT=/app

# 设置入口点
ENTRYPOINT ["poetry", "run", "python", "-m", "src.pipeline.main"]

