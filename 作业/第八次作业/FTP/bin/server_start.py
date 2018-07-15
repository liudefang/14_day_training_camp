# -*- encoding: utf-8 -*-
# @Time    : 18-6-11 上午11:02
# @Author  : mike.liu
# @File    : server_start.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from FTP.ftpserver.conf import settings
from FTP.ftpserver.modules.sokect_server import Myserver
from FTP.ftpserver.core.ftpserver import create_db, create_dir

# 创建用户数据库文件和宿主目录


if __name__ == "__main__":
    # 创建用户数据库文件和宿主目录
    create_db()
    create_dir()

    # 启动服务端
    server = Myserver(settings.IP_PORT)
    server.server_link()
    server.close()
