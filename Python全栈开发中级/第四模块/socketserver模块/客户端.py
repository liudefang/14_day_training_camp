# -*- encoding: utf-8 -*-
# @Time    : 18-7-25 下午5:59
# @Author  : mike.liu
# @File    : 客户端.py

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while True:
    msg = input('请输入信息：').strip()
    if not msg:
        break
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))