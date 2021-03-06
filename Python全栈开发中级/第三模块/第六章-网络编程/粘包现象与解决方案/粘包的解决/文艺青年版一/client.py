# -*- encoding: utf-8 -*-
# @Time    : 18-6-21 上午9:10
# @Author  : mike.liu
# @File    : client.py

import socket
import json

ip_port = ('127.0.0.1', 8081)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(ip_port)

while True:
    msg = input("请输入命令:").strip()
    if len(msg) == 0:
        continue

    if msg == 'quit':
        break

    s.send(msg.encode('utf-8'))
    response_msg_header = s.recv(100).decode('utf-8')

    response_msg_header_data = json.loads(response_msg_header)
    msg_size = response_msg_header_data['length']

    res = s.recv(msg_size)
    print('received res size', len(res))
    print(res.decode('utf-8'), end='')