# -*- encoding: utf-8 -*-
# @Time    : 18-7-5 下午3:00
# @Author  : mike.liu
# @File    : client.py

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))


while True:
    msg = input('客户端输入数据:').strip()
    if not msg:
        continue

    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))