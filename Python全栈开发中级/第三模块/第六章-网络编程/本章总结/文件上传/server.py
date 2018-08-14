# -*- encoding: utf-8 -*-
# @Time    : 2018-06-25 23:03
# @Author  : mike.liu
# @File    : server.py
import socket
import subprocess
import struct
import os
import json

share_dir = r'D:\Python\14_day_training_camp\Python全栈开发中级\第三模块\第六章-网络编程\本章总结\文件上传\share'

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('127.0.0.1', 8092))

socket_server.listen(5)

print("服务器启动")
while True: # 连接循环
    conn, addr = socket_server.accept()
    print(addr)

    while True:     # 通信循环
        try:
            # 1.收命令
            res = conn.recv(1024)
            if not res:
                break

            # 2、解析命令，提取相应命令参数
            cmds = res.decode('utf-8').split()
            filname = cmds[1]

            # 3、以读的方式打开文件，读取文件内容发送给客户端
            # 第一步：制作固定长度的报头
            header_dic = {
                'filename': filname,
                'md5': 'xxdxxx',
                'file_size': os.path.getsize(r'%s/%s' %(share_dir, filname))

            }

            header_json = json.dumps(header_dic)

            header_bytes = header_json.encode('utf-8')

            # 第二步：先发送报头的长度
            conn.send(struct.pack('i', len(header_bytes)))

            # 第三步：再发报头
            conn.send(header_bytes)


            # 第四步：再发送真实的数据
            with open('%s/%s' %(share_dir, filname), 'rb') as f:
                for line in f:
                    conn.send(line)
        except ConnectionResetError:
            break
    conn.close()
socket_server.close()





