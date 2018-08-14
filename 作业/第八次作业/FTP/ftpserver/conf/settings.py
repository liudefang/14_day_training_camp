# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 上午11:12
# @Author  : mike.liu
# @File    : settings.py

import os
import sys
import socket

# 主程序目录文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.insert(0, BASE_DIR)

# 数据库目录
DATABASE = os.path.join(BASE_DIR, "database")

# 用户宿主目录
HOME_PATH = os.path.join(BASE_DIR, "home")

# 用户字典
USERS_PWD = {"mike": "123", "tom": "123", "jack": "123"}

# 磁盘配额 10m
LIMIT_SIZE = 10240000

address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

# ftp服务端口
IP_PORT = ("127.0.0.1", 8888)

# 监听的数目
listen_count = 5

# 允许配置最大并发数
MAX_CONCURRENT_COUNT = 5

# 日志路径
LOG_PATH = os.path.join(BASE_DIR, "conf")
