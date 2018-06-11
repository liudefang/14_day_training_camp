# -*- encoding: utf-8 -*-
# @Time    : 18-6-11 下午1:48
# @Author  : mike.liu
# @File    : sokect_server.py
import socketserver
from 第七次作业.FTP.ftpserver.core.Log import *
from 第七次作业.FTP.ftpserver.modules import auth_user


class Myserver(socketserver.BaseRequestHandler):
    '''ftp服务端'''
    logging.info("ftp服务器已经启动")

    def handle(self):
        try:
            self.conn = self.request
            while True:
                login_info = self.conn.recv(1024).decode()      # 接收客户端发的账号密码信息
                result = self.authenticat(login_info)
                status_code = result[0]
                self.conn.sendall(status_code.encode())
                if status_code == "400":
                    logging.info("用户认证失败!")
                    continue
                else:
                    self.user_db = result[1]
                    self.current_path = self.user_db["homepath"]    # 用户当前目录
                    self.home_path = self.user_db["homepath"]   # 用户宿主目录

                while True:
                    command = self.conn.recv(1024).decode()
                    command_str = command.split()[0]
                    if hasattr(self, command_str):
                        func = getattr(self, command_str)
                        func(command)
                    else:
                        self.conn.sendall("401".encode())
        except ConnectionAbortedError as e:
            self.conn.close()
            print(e)

    def authenticat(self, login_info):
        '''认证用户'''
        auth = auth_user.User_operation()   # 创建认证实例
        result = auth.authentication(login_info)    # 认证用户
        if result:
            return "200", result
        else:
            return "400", result
