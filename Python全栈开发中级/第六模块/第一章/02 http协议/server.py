# -*- encoding: utf-8 -*-
# @Time    : 2018-09-02 20:30
# @Author  : mike.liu
# @File    : server.py

import socket

sock=socket.socket()
sock.bind(("127.0.0.1", 8080))
sock.listen(5)

while True:
    print("server waiting...")
    conn,addr=sock.accept()
    data=conn.recv(1024)
    print("data:", data)

    # 读取HTML文件
    with open("01-module.html", "rb") as f:
        data = f.read()

    conn.send(b"HTTP/1.1 200 OK\r\n\r\n%s" % data)
    conn.close()