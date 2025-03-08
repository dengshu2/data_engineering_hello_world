"""
配置模块：定义项目中使用的所有路径和配置参数
集中管理配置，方便维护和修改
"""

import os
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(os.getenv('PROJECT_ROOT', os.path.dirname(os.path.dirname(__file__))))

# 数据目录
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
FINAL_DATA_DIR = DATA_DIR / 'final'

# 日志目录
LOG_DIR = PROJECT_ROOT / 'logs'

# 数据文件路径
RAW_CSV_PATH = RAW_DATA_DIR / 'sample_data.csv'
RAW_EXCEL_PATH = RAW_DATA_DIR / 'sample_data.xlsx'
PROCESSED_PARQUET_PATH = PROCESSED_DATA_DIR / 'sample_data.parquet'
EXCEL_PARQUET_PATH = PROCESSED_DATA_DIR / 'sample_data_from_excel.parquet'
TRANSFORMED_DATA_PATH = PROCESSED_DATA_DIR / 'transformed_data.parquet'
POLARS_OUTPUT_PATH = FINAL_DATA_DIR / 'polars_processed.parquet'
DAFT_OUTPUT_PATH = FINAL_DATA_DIR / 'daft_processed.parquet'

# 数据生成配置
SAMPLE_SIZE = 1000
RANDOM_SEED = 42

