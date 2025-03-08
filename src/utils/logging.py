"""
日志模块：配置项目的日志记录记录功能
使用 loguru 库进行日志记录
"""

import sys
from datetime import datetime
from pathlib import Path

from loguru import logger

from src.config import LOG_DIR


def setup_logger():
    """
    配置日志记录器

    设置两个日志接收器：
    1. 控制台输出 - 显示所有 INFO 及以上级别的日志
    2. 文件输出 - 将 DEBUG 及以上级别的日志保存到日志文件中

    返回：
        配置好的 logger 实例
    """
    # 确保日志目录存在
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

    # 生成带时间戳的日志文件名
    log_file = LOG_DIR / f'pipeline_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

    # 移除默认的日志记录器
    logger.remove()

    # 添加新的日志记录器
    logger.add( 
        sys.stdout,
        format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>',
        level='INFO'
    )
    logger.add(
        log_file,
        level='DEBUG',
        format='{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}',
        rotation='10 MB',
        retention='7 days'
    )

    return logger
    
# 创建全局 logger 实例
logger = setup_logger()



