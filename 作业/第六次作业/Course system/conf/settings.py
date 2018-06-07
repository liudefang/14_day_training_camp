# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 21:45
# @Author  : mike.liu
# @File    : settings.py

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DATABASE = {
    'engine': 'file_storage',  # 文件存储，这里可扩展成数据库形式
    'name': 'accounts',         # db下的文件名称
    'path': '%s/db' % BASE_DIR
}

LOGIN_LEVEL = logging.INFO      # 初始化日志记录级别为info，info以上的可以直接打印
# 日志类型
LOGIN_TYPE = {
    'system': 'system.log',
}
