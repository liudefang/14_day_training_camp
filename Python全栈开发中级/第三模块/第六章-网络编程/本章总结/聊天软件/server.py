# -*- encoding: utf-8 -*-
# @Time    : 18-6-25 下午7:25
# @Author  : mike.liu
# @File    : server.py

import socket

HOST = '127.0.01'
PORT = 8081

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # 建立TCP连接
sock_server.bind((HOST, PORT))    # 绑定IP地址和端口

sock_server.listen(1)       # 开始监听

conn, addr = sock_server.accept()   # 阻塞直到有连接为止


with conn:
    print("连接信息:", addr)
    while True:
        data = conn.recv(1024)  # 接收数据
        print("recv from mike:", conn.getpeername(), data.decode())
        if not data:
            break   # 收不到数据就break

        response = input("输入数据:").strip()
        conn.send(response.encode())
        print("发送数据给服务端:", response)