# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 上午11:33
# @Author  : mike.liu
# @File    : start.py

import os
import sys

from 第七次作业.FTP.ftpserver.conf.settings import IP_PORT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from 第七次作业.FTP.ftpclient.ftpclient import Myclient


if __name__ == '__main__':
    ip_port = IP_PORT   # 服务端ip，端口
    client = Myclient(ip_port)
    client.start()
