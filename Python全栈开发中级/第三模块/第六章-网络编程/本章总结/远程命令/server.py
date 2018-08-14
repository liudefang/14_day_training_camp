# -*- encoding: utf-8 -*-
# @Time    : 18-6-25 下午8:08
# @Author  : mike.liu
# @File    : server.py

import socket
import subprocess

IP = '127.0.0.1'
PORT = 8090

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind((IP, PORT))

socket_server.listen(5)

print("服务器启动")

while True:     # 循环链接
    conn, client_addr = socket_server.accept()
    print(client_addr)

    while True: # 通信循环
        try:
            # 1、收命令
            cmd = conn.recv(1024)
            if not cmd:
                break

            # 执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 3、把命令的结果返回给客户端
            print(len(stdout) + len(stderr))
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:    # 适应于Windows操作系统
            break
    conn.close()
socket_server.close()