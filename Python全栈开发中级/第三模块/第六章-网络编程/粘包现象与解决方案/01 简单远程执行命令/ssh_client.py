# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 下午6:40
# @Author  : mike.liu
# @File    : ssh_client.py

import socket


ip_port = ('127.0.0.1', 8081)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(ip_port)

while True:
    msg = input("请输入信息:").strip()
    if len(msg) == 0:
        continue
    if msg == 'quit':
        break

    s.send(msg.encode('utf-8'))
    act_res = s.recv(1024)
    print(act_res.decode('utf-8'), end='')