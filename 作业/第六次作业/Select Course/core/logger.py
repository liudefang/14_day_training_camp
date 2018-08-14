# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 21:55
# @Author  : mike.liu
# @File    : logger.py

'''操作所有的日志工作'''
import logging
from conf import settings


def logger(log_type):

    # 创建日志
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOGIN_LEVEL)

    # 创建屏幕对象和设置等级INFO
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOGIN_LEVEL)

    # 创建文件对象，给文件对象设置等级
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOGIN_TYPE[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOGIN_LEVEL)
    # 设置输出日志格式
    formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # 把格式添加到配置中
    ch.setFormatter(formater)
    fh.setFormatter(formater)

    # 把日志打印到制定的handler
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
