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

# 发送数据
client.sendall(b'Hello, world')

# 接收数据
data = client.recv(1024)

print('Received', data)