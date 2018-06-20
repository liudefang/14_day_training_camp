# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 下午7:14
# @Author  : mike.liu
# @File    : udp_client.py

from socket import *
import time

ip_port = ('127.0.0.1', 8080)
bufsize = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("请输入信息:").strip()
    if len(msg) == 0:
        continue

    udp_client.sendto(msg.encode('utf-8'), ip_port)
    data, addr = udp_client.recvfrom(bufsize)
    print(data.decode('utf-8'), end='')