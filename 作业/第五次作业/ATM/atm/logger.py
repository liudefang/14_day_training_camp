# -*- encoding: utf-8 -*-
# @Time    : 2018-05-20 17:14
# @Author  : mike.liu
# @File    : logger.py
import logging
import os

from 作业.第五次作业.ATM.conf import settings


def logger(log_type):

    # 创建日志
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    log_file = os.path.join(settings.LOG_PATH, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    formatter = settings.LOG_FORMAT

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return  logger