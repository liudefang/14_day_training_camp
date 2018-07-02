# -*- encoding: utf-8 -*-
# @Time    : 2018-07-01 11:03
# @Author  : mike.liu
# @File    : client.py

import socket

ip_port = ('127.0.0.1', 8081)

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.connect(ip_port)

cmd = input('发送数据:').strip()

socket_server.send(cmd.encode('utf-8'))
recv_data = socket_server.recv(1024)
print("客户端收到的数据:", recv_data)
socket_server.close()