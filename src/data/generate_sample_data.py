"""
生成示例数据
"""

import numpy as np
import pandas as pd


from src.config import (
    RAW_CSV_PATH,
    RAW_DATA_DIR,
    RAW_EXCEL_PATH,
    RANDOM_SEED,
    SAMPLE_SIZE,
)
from src.utils.logging import logger
from src.utils.file_utils import ensure_dirs

def generate_sample_data():
    """
    生成示例数据
    """
    # 确保数据目录存在
    ensure_dirs(RAW_DATA_DIR)

    # 设置随机种子
    np.random.seed(RANDOM_SEED)

    # 生成示例数据
    data = {
        'user_id': np.random.randint(1000, 9999, size=SAMPLE_SIZE), # 用户ID
        'timestamp': pd.date_range(start='2023-01-01', periods=SAMPLE_SIZE, freq='h'), # 时间戳
        'value': np.random.normal(100, 15, size=SAMPLE_SIZE), # 值
        'category': np.random.choice(['A', 'B', 'C', 'D'], size=SAMPLE_SIZE), # 类别
        'is_active': np.random.choice([True, False], size=SAMPLE_SIZE,p=[0.8, 0.2]), # 是否活跃
    }

    # 将数据转换为DataFrame
    df = pd.DataFrame(data)

    # 保存为CSV文件
    df.to_csv(RAW_CSV_PATH, index=False)
    logger.info(f"CSV文件已保存到: {RAW_CSV_PATH}")

    # 保存为Excel文件
    df.to_excel(RAW_EXCEL_PATH, index=False)
    logger.info(f"Excel文件已保存到: {RAW_EXCEL_PATH}")

    logger.success("示例数据生成完成")

if __name__ == "__main__":
    generate_sample_data()
