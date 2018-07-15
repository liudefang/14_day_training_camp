# -*- encoding: utf-8 -*-
# @Time    : 2018-07-14 12:46
# @Author  : mike.liu
# @File    : client.py
import socket
ip_port = ('127.0.0.1', 8080)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ip_port)

while True:
    msg = input("请输入信息:").strip()
    if not msg:
        continue

    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data)