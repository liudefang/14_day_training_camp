# -*- encoding: utf-8 -*-
# @Time    : 18-6-20 下午7:10
# @Author  : mike.liu
# @File    : udp_server.py

import socket
import subprocess

ip_port = ('127.0.0.1', 8080)
bufsize = 1024

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    # 收消息
    cmd, addr = udp_server.recvfrom(bufsize)
    print('用户命令————>', cmd, addr)

    # 逻辑处理
    res = subprocess.Popen(cmd.decode('utf-8'), shell=True, stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    stderr = res.stderr.read()
    stdout = res.stdout.read()

    # 发消息
    udp_server.sendto(stdout + stderr, addr)

udp_server.close()