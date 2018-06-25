# -*- encoding: utf-8 -*-
# @Time    : 18-6-25 下午8:25
# @Author  : mike.liu
# @File    : client.py

import socket


IP = '127.0.0.1'
PORT = 8090

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.connect((IP, PORT))

while True:
    cmd = input("输入命令:").strip()
    if not cmd:
        continue

    socket_server.connect(cmd.encode('utf-8'))

    # 拿到命令结果并打印
    data = socket_server.recv(1024)
    print(data.decode('utf-8'))

socket_server.close()