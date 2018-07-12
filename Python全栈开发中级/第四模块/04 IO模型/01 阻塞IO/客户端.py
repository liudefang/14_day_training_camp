# -*- encoding: utf-8 -*-
# @Time    : 2018-07-12 22:13
# @Author  : mike.liu
# @File    : 客户端.py

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    msg = input("请输入数据：").strip()
    if not msg:
        continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()