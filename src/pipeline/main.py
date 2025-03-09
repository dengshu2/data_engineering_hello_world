"""
数据处理管道主文件:协调数据处理流程
"""

from src.config import (
    FINAL_DATA_DIR,
    LOGS_DIR,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
)
from src.data.transformers import (
    csv_to_parquet,
    excel_to_parquet,
    duckdb_transform,
    polars_processing,
    daft_processing,
)
from src.utils.file_utils import ensure_dirs
from src.utils.logging import logger


def setup_environment():
    """
    设置项目环境
    """
    ensure_dirs(RAW_DATA_DIR, PROCESSED_DATA_DIR, FINAL_DATA_DIR, LOGS_DIR)
    logger.info("项目环境设置完成")


def run_pipeline():
    """
    运行数据处理管道
    1. 设置项目环境
    2. 处理CSV数据
    3. 处理Excel数据
    4. 处理DuckDB数据
    5. 处理Polars数据
    6. 处理Daft数据
    7. 保存处理后的数据
    """
    logger.info("开始运行数据处理管道")
    # 1. 设置项目环境
    setup_environment()

    # 2. 处理CSV数据
    csv_to_parquet()

    # 3. 处理Excel数据
    excel_to_parquet()

    # 4. 处理DuckDB数据
    duckdb_transform()

    # 5. 处理Polars数据
    polars_processing()

    # 6. 处理Daft数据
    daft_processing()

    # 7. 保存处理后的数据
    logger.info("数据处理管道运行完成")


if __name__ == "__main__":
    run_pipeline()


