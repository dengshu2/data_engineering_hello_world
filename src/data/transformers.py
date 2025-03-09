"""
数据模块：提供各种数据格式转换和处理函数
"""

import pandas as pd
import polars as pl
import duckdb
import daft

from src.config import (
    DAFT_OUTPUT_PATH,
    EXCEL_PARQUET_PATH,
    POLARS_OUTPUT_PATH,
    PROCESSED_PARQUET_PATH,
    RAW_CSV_PATH,
    RAW_EXCEL_PATH,
    TRANSFORMED_DATA_PATH,
)
from src.utils.logging import logger

def csv_to_parquet():
    """
    将CSV文件转换为Parquet文件
    """
    # 使用polars读取csv文件
    df = pl.read_csv(RAW_CSV_PATH)
    # 使用polars写入parquet文件
    df.write_parquet(PROCESSED_PARQUET_PATH)
    logger.info(f"{RAW_CSV_PATH}共计({len(df)})条数据已转换为Parquet文件: {PROCESSED_PARQUET_PATH}")
    return df

def excel_to_parquet():
    """
    将Excel文件转换为Parquet文件
    """
    # 使用pandas读取excel文件
    pandas_df = pd.read_excel(RAW_EXCEL_PATH)
    # 使用daft写入parquet文件
    daft_df = daft.from_pandas(pandas_df)
    daft_df.write_parquet(EXCEL_PARQUET_PATH)
    logger.info(f"{RAW_EXCEL_PATH}共计({len(daft_df)})条数据已转换为Parquet文件: {EXCEL_PARQUET_PATH}")
    return daft_df

def duckdb_transform():
    """
    使用duckdb进行数据转换
    """
    # 创建内存数据库链接
    conn = duckdb.connect(database=':memory:')
    # 从 Parquet 文件读取数据
    df = conn.execute("CREATE TABLE sample_data AS SELECT * FROM read_parquet(?)", [str(PROCESSED_PARQUET_PATH)])

    # 执行 SQL 转换：添加value_category列，根据value 值分类
    conn.execute("""
        CREATE TABLE transformed_data AS 
        SELECT 
        user_id
        ,timestamp
        ,value
        ,category
        ,is_active
        ,CASE WHEN value > 100 THEN 'high'
             WHEN value < 90 THEN 'low'
             ELSE 'medium'
        END AS value_category
        FROM sample_data
        """)
    # 将结果保存为 Parquet 文件
    conn.execute(f"COPY (SELECT * FROM transformed_data) TO '{TRANSFORMED_DATA_PATH}' (FORMAT PARQUET)")
    row_count = conn.execute("SELECT COUNT(*) FROM transformed_data").fetchone()[0]
    logger.info(f"duckdb转换结果,处理了{row_count}条数据,已保存为Parquet文件: {TRANSFORMED_DATA_PATH}")

def polars_processing():
    """
    使用polars进行数据处理
    """
    # 从 Parquet 文件读取数据
    df = pl.read_parquet(TRANSFORMED_DATA_PATH)

    result_df = df.filter(pl.col("is_active") == True) \
        .with_columns(pl.col("value") * 1.1) \
        .sort("value",descending=True) \
    
    # 保存处理结果
    result_df.write_parquet(POLARS_OUTPUT_PATH)
    logger.info(f"polars转换结果,处理了{len(df)}条数据,已保存为Parquet文件: {POLARS_OUTPUT_PATH}")
    return result_df

def daft_processing():
    """
    使用daft进行数据处理
    """
    # 从 Parquet 文件读取数据
    df = daft.read_parquet(str(TRANSFORMED_DATA_PATH))
    
    # 数据处理：
    # 1. 过滤类别为‘A’的记录
    # 2. 添加优先级分数列
    result_df = df.filter(df["category"] == "A") \
        .with_column("priority_score", df["value"] / 100 * 5)

    # 保存处理结果
    result_df.write_parquet(DAFT_OUTPUT_PATH)
    logger.info(f"daft转换结果,处理了{df.count_rows()}条数据,已保存为Parquet文件: {DAFT_OUTPUT_PATH}")
    return result_df
