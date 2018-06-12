# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 下午3:25
# @Author  : mike.liu
# @File    : Log.py

import logging.config

from 第七次作业.FTP.ftpserver.conf import settings

logging.config.fileConfig(settings.LOG_PATH + r"/Logger.conf")

# 选择一个日志格式

logger = logging.getLogger("example02")


def debug(message):
    # 定义debgug级别日志打印方法
    logger.debug(message)


def info(message):
    # 定义info级别日志打印方法
    logger.info(message)


def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)
