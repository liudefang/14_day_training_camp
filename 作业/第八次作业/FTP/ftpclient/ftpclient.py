# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 上午10:17
# @Author  : mike.liu
# @File    : ftpclient.py
import hashlib
import json
import os
import struct
import sys
import socket
import time
from FTP.ftpserver.core.Log import *


class Myclient():
    '''ftp客户端'''

    def __init__(self, server_address, connect = True):
        self.server_address = server_address
        self.client = socket.socket(settings.address_family, settings.socket_type)
        if connect:
            try:
                self.client_connect()
            except Exception as e:
                self.client_close()
                print(e)

    def client_connect(self):
        '''连接服务器'''

        self.client.connect(self.server_address)
        logging.info("连接服务器成功!")

    def client_close(self):
        self.client.close()

    def start(self):
        '''程序开始'''
        count = 0
        while count < 3:
            time.sleep(1)
            logging.info("开始进行用户登录".center(20, '-'))
            time.sleep(1)

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
        time.sleep(1)
        logging.info("进行相应的操作")

        while True:
            time.sleep(1)
            command = input("请输入相应的命令:").strip()
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

    def cd(self, command):
        '''目录切换'''
        self.__universal_method_none(command)
        pass

    def dir(self, command):
        '''查看当前目录下的文件'''
        self.__universal_method_data(command)
        pass

    def put(self, command):
        '''上传文件'''
        if len(command.split()) > 1:
            filename = command.split()[1]
            file_path = settings.DATABASE + r"\%s" % filename
            print(file_path)
            if os.path.isfile(file_path):     # 文件是否存在
                self.client.sendall(command.encode())   # 发送要执行的命令
                self.client.recv(1024)

                file_size = os.stat(file_path).st_size   # 文件大小
                self.client.sendall(str(file_size).encode())    # 发送文件大小
                status_code = self.client.recv(1024).decode()   # 等待响应，返回状态码
                if status_code == "202":
                    with open(file_path, "rb") as file:
                        m = hashlib.md5()
                        for line in file:
                            m.update(line)
                            send_size = file.tell()
                            self.client.sendall(line)
                            self.__progress(send_size, file_size, "上传中")    # 进度条
                    self.client.sendall(m.hexdigest().encode())     # 发送md5值
                    status_code = self.client.recv(1024).decode()   # 返回状态码
                    if status_code == "203":
                        logging.info("\n文件具有一致性")
                else:
                    logging.info("[%s]错误" % status_code)
            else:
                logging.info("[402]文件不存在!")
        else:
            logging.info("[401]命令不正确!")

    def get(self, command):
        '''下载文件'''
        self.client.sendall(command.encode())       # 发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":    # 命令可执行
            filename = command.split()[1]

            # 文件名存在，判断是否续传
            if os.path.isfile(filename):
                revice_size = os.stat(filename).st_size     # 文件已接收大小
                self.client.sendall("403".encode())
                self.client.recv(1024)
                self.client.sendall(str(revice_size).encode())  # 发送已接收文件大小
                status_code = self.client.recv(1024).decode()

                # 文件大小不一致，续传
                if status_code == "205":
                    logging.info("继续上次上传位置进行续传")
                    self.client.sendall("000".encode())

                # 文件大小一直，不续传，不下载
                elif status_code == "405":
                    logging.info("文件已经存在，大小一致")
                    return

            # 文件不存在
            else:
                self.client.sendall("402".encode())
                revice_size = 0

            file_size = self.client.recv(1024).decode()     # 文件大小
            file_size = int(file_size)
            self.client.sendall("000".encode())

            with open(filename, "ab") as file:  # 开始接收
                # file_size 为文件总大小
                file_size += revice_size
                m = hashlib.md5()
                while revice_size < file_size:
                    minus_size = file_size - revice_size
                    if minus_size > 1024:
                        size = 1024
                    else:
                        size = minus_size
                    data = self.client.recv(size)
                    revice_size += len(data)
                    file.write(data)
                    m.update(data)
                    self.__progress(revice_size, file_size, "下载中")      # 进度条
                new_file_md5 = m.hexdigest()    # 生成新文件的md5值
                server_file_md5 = self.client.recv(1024).decode()
                if new_file_md5 == server_file_md5:     # md5值一致
                    logging.info("\n文件具有一致性")
        else:
            logging.info("[%s] 错误" % status_code)

    def __progress(self, trans_size, file_size, mode):
        '''
        显示进度条
        :param trans_size: 已经传输的数据大小
        :param file_size: 文件总大小
        :param mode: 模式
        :return:
        '''
        bar_length = 100    # 进度条长度
        percent = float(trans_size) / float(file_size)
        hashes = '=' * int(percent * bar_length)       # 进度条显示的数量长度百分比
        spaces = ' ' * (bar_length - len(hashes))       # 定义空格的数量=总长度-显示长度
        sys.stdout.write(r"%s:%.2fM/%.2fM %d%% [%s]"
                         % (mode, trans_size/1048576, file_size/1048576, percent*100, hashes + spaces))

    def __universal_method_none(self, command):
        '''通用方法，无data输出'''
        self.client.sendall(command.encode())       # 发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":    # 命令可执行
            self.client.sendall("000".encode())     # 建立系统连接
            logging.info("操作成功!")

        else:
            logging.info("[%s]错误" % status_code)

    def __universal_method_data(self, command):
        '''通用方法，有data输出'''
        self.client.send(bytes(command.encode('utf-8')))     # 发送要执行的命令
        status_code = self.client.recv(1024).decode()
        if status_code == "201":    # 命令可执行
            self.client.sendall("000".encode())     # 系统交互
            # data = self.client.recv(1024).decode()
            head = self.client.recv(4)
            head_json_len = struct.unpack('i', head)[0]
            head_json = json.loads(self.client.recv(head_json_len).decode('utf-8'))
            data_len = head_json['data_size']

            # 开始收数据
            recv_size = 0
            recv_data = b''
            while recv_size < data_len:
                recv_data += self.client.recv(1024)
                recv_size += len(recv_data)
            logging.info(recv_data.decode('gbk'))
            logging.info("操作成功!")
        else:
            logging.info("[%s]错误" % status_code)
