#!/bin/bash

# 运行数据管道的脚本
# 使用彩色输出

# 定义颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}开始运行数据处理管道...$(date)${NC}"

# 使用 poetry 运行数据处理管道
poetry run python -m src.pipeline.main

# 检查管道是否成功运行
if [ $? -eq 0 ]; then
    echo -e "${GREEN}数据处理管道运行成功$(date)${NC}"
else
    echo -e "${RED}数据处理管道运行失败$(date)${NC}"
    exit 1
fi

# 显示处理结果摘要
echo -e "${GREEN}数据结果摘要:$(date)${NC}"
poetry run python -c "
import os
print(f'原始数据文件数：{len(os.listdir(\"data/raw\")) - 1}')
print(f'处理后数据文件数：{len(os.listdir(\"data/processed\")) - 1}')
print(f'最终数据文件数：{len(os.listdir(\"data/final\")) - 1}')
"