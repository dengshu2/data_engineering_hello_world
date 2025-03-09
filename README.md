# Data Engineering Hello World

一个简单但完整的数据工程 Hello World 项目，展示如何使用现代工具构建数据处理管道。

## 项目概述

本项目在一台全新的 VPS 上搭建一套现代数据工程开发环境，并实现一个简单但完整的数据处理管道。项目采用渐进式开发方法，每完成一个阶段就进行测试，确保每一步都正确无误。

## 技术栈

- **Python 3.10**：编程语言
- **Docker & Docker Compose**：容器化和服务编排
- **Poetry**：依赖管理
- **Pandas**：数据处理和分析
- **Polars**：高性能数据处理
- **DuckDB**：嵌入式分析型数据库
- **Daft**：分布式数据处理框架
- **Loguru**：日志记录
- **Makefile**：自动化任务

## 项目结构

```
data_engineering_hello_world/
├── data/
│   ├── raw/           # 原始数据
│   ├── processed/     # 处理后的中间数据
│   └── final/         # 最终输出数据
├── src/
│   ├── config.py      # 配置参数
│   ├── data/
│   │   ├── generate_sample_data.py  # 数据生成
│   │   └── transformers.py          # 数据转换
│   ├── pipeline/
│   │   └── main.py                  # 管道主模块
│   └── utils/
│       ├── file_utils.py            # 文件工具
│       └── logging.py               # 日志配置
├── scripts/
│   └── run_pipeline.sh              # 运行脚本
├── logs/               # 日志文件
├── Dockerfile          # Docker 配置
├── docker compose.yml  # Docker Compose 配置
├── pyproject.toml      # 项目依赖配置
├── Makefile            # 自动化任务
└── .gitignore          # Git 忽略文件
```

## 使用指南

### 前提条件

- Docker 和 Docker Compose
- Make（可选，用于运行自动化任务）

### 快速开始

1. 克隆仓库：

```bash
git clone https://github.com/dengshu2/data_engineering_hello_world.git
cd data_engineering_hello_world
```

2. 设置环境：

```bash
make setup
```

3. 生成示例数据：

```bash
make generate-data
```

4. 运行数据管道：

```bash
make run-pipeline
```

### 其他命令

- 清理生成的数据和日志：

```bash
make clean
```

## 数据处理流程

1. **数据生成**：
   - 生成包含用户ID、时间戳、数值、类别和活跃状态的随机数据
   - 保存为CSV和Excel格式

2. **格式转换**：
   - 使用Polars将CSV转换为Parquet格式
   - 使用Pandas和Daft将Excel转换为Parquet格式

3. **数据处理**：
   - 使用DuckDB执行SQL转换，添加value_category分类
   - 使用Polars过滤活跃用户，增加value值，并排序
   - 使用Daft过滤特定类别，计算优先级分数

4. **结果存储**：
   - 将处理结果保存至`data/final`目录的Parquet文件

## 许可证

MIT