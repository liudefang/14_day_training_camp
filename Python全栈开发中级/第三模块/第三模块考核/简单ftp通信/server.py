# -*- encoding: utf-8 -*-
# @Time    : 2018-07-01 10:58
# @Author  : mike.liu
# @File    : server.py

import socket

ip_port = ('127.0.0.1', 8081)

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(ip_port)

socket_server.listen(1)

conn, addr = socket_server.accept()

print(addr)
data = conn.recv(1024)
print("收到的数据:%s" % data)
cmd = input("输入数据:").strip()
recv_data = conn.send(cmd.encode('utf-8'))
print("发出去的数据:", recv_data)
conn.close()
socket_server.close()