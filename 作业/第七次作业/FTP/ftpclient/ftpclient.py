# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 上午10:17
# @Author  : mike.liu
# @File    : ftpclient.py

import os
import sys
import socket
from 第七次作业.FTP.ftpserver.core.Log import *


class Myclient():
    '''ftp客户端'''

    def __init__(self, ip_port):
        self.ip_port = ip_port

    def connect(self):
        '''连接服务器'''
        self.client = socket.socket()
        self.client.connect(self.ip_port)
        logging.info("连接服务器成功!")

    def start(self):
        '''程序开始'''
        self.connect()
        count = 0
        while count < 3:
            print("开始进行用户登录".center(20, '-'))
            username = input("请输入用户名:").strip()
            password = input("请输入密码：").strip()
            login_info = ("%s:%s" % (username, password))
            self.client.sendall(login_info.encode())    # 发送用户密码信息
            status_code = self.client.recv(1024).decode()   # 返回状态
            if status_code == "400":
                logging.info("[%s]用户名或密码错误" % status_code)
                count += 1
            else:
                logging.info("[%s]用户认证成功!" % status_code)
                self.interactive()
        else:
            logging.info("输错次数太多,请稍后再试!")

    def interactive(self):
        '''开始进行操作'''
        logging.info("进行相应的操作")
        while True:
            command = input("->>").strip()
            if not command:
                continue
            command_str = command.split()[0]
            if hasattr(self, command_str):      # 执行命令
                func = getattr(self, command_str)
                func(command)
            else:
                logging.info("[%s]命令不存在" % command)


    def pwd(self, command):
        '''查看当前用户路径'''
        self.__universal_method_data(command)
        pass

    def mkdir(self, command):
        '''创建目录'''
        self.__universal_method_none(command)
        pass



    def __universal_method_none(self, command):
        '''通用方法，无data输出'''
        self.client.sendall(command.encode())       # 发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":    # 命令可执行
            self.client.sendall("000".encode())     # 建立系统连接
            # logging.info("建立和服务器的连接!")

        else:
            logging.info("[%s]错误" % status_code)

    def __universal_method_data(self, command):
        '''通用方法，有data输出'''
        self.client.sendall(command.encode())     # 发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":    # 命令可执行
            self.client.sendall("000".encode())     # 系统交互
            data = self.client.recv(1024).decode()
            logging.info(data)
        else:
            logging.info("[%s]错误" % status_code)