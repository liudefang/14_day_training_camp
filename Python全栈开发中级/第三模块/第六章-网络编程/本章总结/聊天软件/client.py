# -*- encoding: utf-8 -*-
# @Time    : 18-6-25 下午7:56
# @Author  : mike.liu
# @File    : client.py

import socket

HOST = '127.0.0.1'
PORT = 8081

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))    # 连接服务器

while True:
    msg = input("输入信息:").strip()
    if len(msg) == 0:
        continue

    client.sendall(msg.encode())    # 发送用户输入的数据，必须是bytes模式

    data = client.recv(1024)

    print('服务器返回的信息:', data.decode())   # 收到服务器的响应后，decode一下