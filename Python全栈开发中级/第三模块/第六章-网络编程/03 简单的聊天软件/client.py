# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 上午9:32
# @Author  : mike.liu
# @File    : client1.py

import socket

HOST = '127.0.0.1'
PORT = 50007

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # socket.SOCK_STREAM,for tcp

# 连接服务端
client.connect((HOST, PORT))

while True:
    msg = input("请输入数据：").strip()
    if len(msg) == 0:
        continue

    client.sendall(msg.encode())    # 发送用户输入的数据，必须是bytes模式

    data = client.recv(1024)

    print('Received:', data.decode())    # 收到服务器的响应后，decode一下