# -*- encoding: utf-8 -*-
# @Time    : 18-6-21 上午9:01
# @Author  : mike.liu
# @File    : server.py

import socket
import json
import subprocess

ip_port = ('127.0.0.1', 8080)

tcp_socke_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socke_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcp_socke_server.bind(ip_port)

tcp_socke_server.listen(5)

def pack_msg_header(header, size):
    bytes_header = bytes(json.dumps(header), encoding='utf-8')
    fill_up_size = size - len(bytes_header)
    print('need to fill up', fill_up_size)

    header['fill'] = header['fill'].zfill(fill_up_size)
    print('new header', header)
    bytes_new_header = bytes(bytes(json.dumps(header), encoding='utf-8'))
    return bytes_new_header

while True:
    conn, addr = tcp_socke_server.accept()
    print('客户端', addr)

    while True:
        cmd = conn.recv(1024)
        if len(cmd) == 0:
            break
        print('recv cmd', cmd)
        res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stderr = res.stderr.read()
        stdout = res.stdout.read()
        print('res length', len(stdout))

        msg_header = {
            'length': len(stdout + stderr),
            'fill': ''

        }
        packed_header = pack_msg_header(msg_header, 100)
        print('packed header size', packed_header, len(packed_header))
        conn.send(packed_header)
        conn.send(stdout + stderr)