# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 下午7:31
# @Author  : mike.liu
# @File    : client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(('127.0.0.1', 8081))

while True:
    msg = input('请输入信息:').strip()
    if len(msg) == 0:
        continue
    if msg == 'quit':
        break

    s.send(msg.encode('utf-8'))
    length = int(s.recv(1024).decode('utf-8'))
    s.send('recv_ready'.encode('utf-8'))

    send_size = 0
    recv_size = 0
    data = b''
    while recv_size < length:
        data += s.recv(1024)
        recv_size += len(data)  # 为什么不直接写1024？

    print(data.decode())