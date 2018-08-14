# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 下午5:37
# @Author  : mike.liu
# @File    : server.py

import socket
ip_port = ('127.0.0.1', 9002)
BUFSIZE = 1024

udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # udp类型

udp_server_client.bind(ip_port)

while True:
    msg, addr=udp_server_client.recvfrom(BUFSIZE)
    print("recv", msg, addr)

    udp_server_client.sendto(msg.upper(), addr)