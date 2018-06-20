# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 上午9:38
# @Author  : mike.liu
# @File    : server.py

import socket

HOST = '127.0.0.1'
PORT = 50007

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口
sock_server.bind((HOST, PORT))

# 开始监听，1代表在允许有一个连接排队，更多的新连接连进来时就会被拒绝
sock_server.listen(1)

# 阻塞直到有连接为止，有了一个新连接进来后，就会为这个请求生成一个连接对象
conn, addr = sock_server.accept()

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)  # 接收1024个字节
        print("server recv:", conn.getpeername(), data.decode())

        if not data:
            break  # 接收不到数据，就break
        conn.sendall(data)      # 把接收到的数据再全部返回给客户端
