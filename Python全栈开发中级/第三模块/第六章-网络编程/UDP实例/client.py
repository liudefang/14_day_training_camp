# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 下午5:40
# @Author  : mike.liu
# @File    : client.py

import socket
ip_port = ('127.0.0.1', 9002)
BUFSIZE = 1024

udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("请输入信息:").strip()
    if not msg:
        continue

    udp_server_client.sendto(msg.encode('utf-8'), ip_port)

    back_msg, addr = udp_server_client.recvfrom(BUFSIZE)
    print(back_msg.decode('utf-8'), addr)