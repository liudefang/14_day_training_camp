# -*- encoding: utf-8 -*-
# @Time    : 2018-07-12 22:46
# @Author  : mike.liu
# @File    : 客户端.py

from socket import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('127.0.0.1', 8080))

while True:
    msg = input("请输入信息:").strip()
    if not msg:
        continue
    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode('utf-8'))

c.close()