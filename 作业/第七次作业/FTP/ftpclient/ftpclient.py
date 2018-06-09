# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 上午10:17
# @Author  : mike.liu
# @File    : ftpclient.py

import os
import sys
import socket
import hashlib
from _tracemalloc import start


class Myclient():
    '''ftp客户端'''

    def __init__(self, ip_port):
        self.ip_port = ip_port

    def connect(self):
        '''连接服务器'''
        self.client = socket.socket()
        self.client.connect(self.ip_port)

    def start(self):
        '''程序开始'''
        # self.connect()
        while True:
            username = input("请输入用户名:").strip()
            password = input("请输入密码：").strip()
            login_info = ("%s:%s" % (username, password))
            self.client.sendall(login_info.encode())    # 发送用户密码信息
            status_code = self.client.recv(1024).decode()   # 返回状态
            if status_code == "400":
                print("[%s]用户名或密码错误" % status_code)
                continue
            else:
                print("[%s]用户认证成功!" % status_code)



