# -*- encoding: utf-8 -*-
# @Time    : 18-6-21 上午9:30
# @Author  : mike.liu
# @File    : server.py

import socket
import struct
import json
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # 回收time_wait进程

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

while True:
    conn, addr = phone.accept()
    while True:
        cmd = conn.recv(1024)
        if not cmd:
            break
        print('cmd:%s' % cmd)

        res = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,  # shell命令，可以是字符串或者序列类型(如：list，元组)
                               stdout=subprocess.PIPE,  # 标准输出
                               stderr=subprocess.PIPE)  # 错误句柄

        err = res.stderr.read()
        print(err)
        if err:
            brack_msg = err
        else:
            back_msg = res.stdout.read()

        headers = {
            'data_size': len(back_msg)
        }
        head_json = json.dumps(headers)
        head_json_bytes = bytes(head_json, encoding='utf-8')

        conn.send(struct.pack('i', len(head_json_bytes)))   # 先发报头的长度
        conn.send(head_json_bytes)  # 再发报头
        conn.sendall(back_msg)  # 发送真实的内容

    conn.close()

