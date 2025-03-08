"""
文件操作工具模块：提供文件和目录操作的辅助函数
"""

import os
from pathlib import Path

from src.utils.logging import logger

def ensure_dirs(*dirs):
    """
    确保目录存在,如果目录不存在,则创建目录

    参数：
        *dirs: 需要确保存在的目录路径
    """
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        logger.info(f"确保目录存在: {dir_path}")

def check_file_exists(file_path):
    """
    检查文件是否存在

    参数：
        file_path: 文件路径

    返回：
        bool: 如果文件存在返回True,否则返回False
    """
    exists = Path(file_path).exists()
    if not exists:
        logger.warning(f"文件不存在: {file_path}")
        return False
    return exists

def get_file_size(file_path):
    """
    读取文件大小(以 MB 为单位)

    参数：
        file_path: 文件路径

    返回：
        文件大小(以 MB 为单位)
    """ 
    if check_file_exists(file_path):
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)
        return size_mb
    return 0

