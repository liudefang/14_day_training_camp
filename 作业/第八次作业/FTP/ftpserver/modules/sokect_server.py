# -*- encoding: utf-8 -*-
# @Time    : 18-6-11 下午1:48
# @Author  : mike.liu
# @File    : sokect_server.py
import hashlib
import json
import os
import time
import socket
import struct
from os.path import getsize, join
import queue
from threading import Thread
import subprocess
from FTP.ftpserver.core.Log import *
from FTP.ftpserver.modules import auth_user


class Myserver():

    '''ftp服务端'''
    logging.info("ftp服务器已经启动")

    def __init__(self, server_address, bind_and_listen=True):
        self.server_address = server_address
        self.socket = socket.socket(settings.address_family, settings.socket_type)
        self.q = queue.Queue(settings.MAX_CONCURRENT_COUNT)
        if bind_and_listen:
            try:
                self.server_bind()
                self.server_listen()
            except Exception as e:
                print(e)
                self.server_close()

    def server_bind(self):
        allow_reuse_address = False
        if allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

    def server_listen(self):
        self.socket.listen(settings.listen_count)

    def server_close(self):
        self.socket.close()

    def server_accept(self):
        return self.socket.accept()

    def conn_close(self, conn):
        conn.close()

    def server_link(self):
        time.sleep(1)
        print("\033[32;1m 等待客户端接入\033[0m")
        while True:     # 链接循环
            conn, self.client_addr = self.server_accept()
            print("客户端地址：", self.client_addr)
            try:
                t = Thread(target=self.handle, args=(conn,))
                self.q.put(t)
                t.start()
            except Exception as e:
                print(e)
                self.conn_close(conn)
                self.q.get()

    def handle(self, conn):
        try:

            while True:
                login_info = conn.recv(1024).decode()      # 接收客户端发的账号密码信息
                result = self.authenticat(login_info)
                status_code = result[0]
                conn.sendall(status_code.encode())
                if status_code == "400":
                    logging.info("用户认证失败!")
                    continue

                else:
                    self.user_db = result[1]

                    self.current_path = settings.BASE_DIR + r"\%s" % self.user_db["homepath"]    # 用户当前目录
                    self.home_path = settings.BASE_DIR + r"\%s" % self.user_db["homepath"]   # 用户宿主目录

                while True:
                    command = conn.recv(1024)

                    self.cmds = command.decode('utf-8').split()

                    if hasattr(self, self.cmds[0]):
                        func = getattr(self, self.cmds[0])
                        func(conn)
                    else:
                        conn.sendall("401".encode())
        except ConnectionAbortedError as e:
            self.conn_close(conn)
            self.get()
            print(e)

    def authenticat(self, login_info):
        '''认证用户'''
        auth = auth_user.User_operation()   # 创建认证实例
        result = auth.authentication(login_info)    # 认证用户
        if result:
            return "200", result
        else:
            return "400", result

    def pwd(self, conn):
        '''查看当前用户路径'''
        if len(self.cmds) == 1:
            conn.sendall("201".encode())
            conn.recv(1024)
            res = subprocess.Popen(self.cmds[0],
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            err = res.stderr.read()
            print(err)
            if err:
                back_msg = err
            else:
                back_msg = res.stdout.read()

            headers = {
                'data_size': len(back_msg)
            }
            head_json = json.dumps(headers)
            head_json_bytes = bytes(head_json, encoding='utf-8')

            conn.send(struct.pack('i', len(head_json_bytes)))
            conn.send(head_json_bytes)
            conn.sendall(back_msg)
        else:
            conn.sendall("401".encode())

    def mkdir(self, conn):
        '''创建目录'''
        if len(self.cmds) > 1:
            dir_name = self.cmds[1]   # 目录名
            dir_path = self.current_path + r"\%s" % dir_name        # 目录路径

            if os.path.isdir(dir_path):  # 目录存在
                conn.sendall("403".encode())
            else:
                conn.sendall("201".encode())
                os.makedirs(dir_path)
                logging.info("创建目录[%s]成功" % dir_name)

        else:
            conn.sendall("401".encode())

    def cd(self, conn):
        '''目录切换'''
        if len(self.cmds) > 1:
            dir_name = self.cmds[1]       # 目录名
            dir_path = self.current_path + r"\%s" % dir_name    # 目录路径
            user_home_path = settings.HOME_PATH + r"\%s" % self.user_db["username"]     # 宿主目录

            if dir_name == ".." and len(self.current_path) > len(user_home_path):
                conn.sendall("201".encode())
                conn.recv(1024)
                self.current_path = os.path.dirname(self.current_path)      # 返回上一级目录
                logging.info("返回上一级目录:%s 成功" % self.current_path)
            elif os.path.isdir(dir_path):
                conn.sendall("201".encode())
                conn.recv(1024)
                if dir_name != "." and dir_name != "..":
                    self.current_path += r"\%s" % dir_name      # 切换目录
                    logging.info("切换到目录【%s】成功" % dir_name)

            else:
                conn.sendall("402".encode())
        else:
            conn.sendall("401".encode())

    def dir(self, conn):
        '''查看当前目录下的文件'''
        if len(self.cmds) == 1:
            conn.sendall("201".encode())
            conn.recv(1024)

            res = subprocess.Popen("%s %s" % (self.cmds[0], self.current_path),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            err = res.stderr.read()
            print(err)
            if err:
                back_msg = err
            else:
                back_msg = res.stdout.read()

            headers = {
                'data_size': len(back_msg)
            }
            head_json = json.dumps(headers)
            head_json_bytes = bytes(head_json, encoding='utf-8')

            conn.send(struct.pack('i', len(head_json_bytes)))
            conn.send(head_json_bytes)
            conn.sendall(back_msg)
        else:
            conn.sendall("401".encode())

    def put(self, conn):
        '''上传文件'''

        filename = self.cmds[1]
        file_path = self.current_path + r"\%s" % filename
        conn.sendall("000".encode())       # 发送确认
        file_size = conn.recv(1024).decode()   # 文件大小
        file_size = int(file_size)
        limit_size = self.user_db["limitsize"]  # 磁盘额度
        used_size = self.__getdirsize(self.home_path)   # 已用空间大小
        if not os.path.isfile(file_path):   # 判断文件是否存在
            if limit_size > file_size + used_size:
                conn.sendall("202".encode())
                with open(file_path, "wb") as file:
                    revice_size = 0
                    m = hashlib.md5()
                    while revice_size < file_size:
                        minus_size = file_size - revice_size
                        if minus_size > 1024:
                            size = 1024
                        else:
                            size = minus_size
                        data = conn.recv(size)
                        revice_size += len(data)
                        file.write(data)
                        m.update(data)
                    new_file_md5 = m.hexdigest()    # 生成新文件的md5值
                    server_file_md5 = conn.recv(1024).decode()
                    if new_file_md5 == server_file_md5:     # md5值一致
                        conn.sendall("203".encode())
            else:
                conn.sendall("404".encode())
        else:
            conn.sendall("403".encode())

    def get(self, conn):
        '''下载文件'''
        if len(self.cmds) > 1:
            filename = self.cmds[1]
            file_path = self.current_path + r"/%s" % filename
            if os.path.isfile(file_path):        # 文件是否存在
                conn.sendall("201".encode())   # 命令可执行
                file_size = os.stat(file_path).st_size   # 文件总大小
                status_code = conn.recv(1024).decode()

                # 客户端存在次文件
                if status_code == "403":
                    conn.sendall("000".encode())   # 系统交互
                    has_send_size = conn.recv(1024).decode()
                    has_send_size = int(has_send_size)
                    # 客户端文件不完整可以续传
                    if has_send_size < file_size:
                        conn.sendall("205".encode())
                        file_size -= has_send_size  # 续传文件大小
                        conn.recv(1024)

                    # 客户端文件完整不可续传，不提供下载
                    else:
                        conn.sendall("405".encode())
                        return
                elif status_code == "402":
                    has_send_size = 0

                with open(file_path, "rb") as file:
                    conn.sendall(str(file_size).encode())      # 发送文件大小
                    conn.recv(1024)
                    file.seek(has_send_size)
                    m = hashlib.md5()
                    for line in file:
                        m.update(line)
                        conn.sendall(line)
                conn.sendall(m.hexdigest().encode())       # 发送文件md5值
            else:
                conn.sendall("402".encode())
        else:
            conn.sendall("401".encode())

    def __getdirsize(self, home_path):
        '''统计目录空间大小'''
        size = 0
        for root, dirs, files in os.walk(home_path):
            size += sum([getsize(join(root, name)) for name in files])
        return size
