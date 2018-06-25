# -*- encoding: utf-8 -*-
# @Time    : 2018-06-25 23:03
# @Author  : mike.liu
# @File    : client.py

import socket
import struct
import json

download_dir =r'D:\Python\14_day_training_camp\Python全栈开发中级\第三模块\第六章-网络编程\本章总结\文件上传\download'

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.connect(('127.0.0.1', 8092))

while True:
    # 1.发命令
    cmd = input("请输入命令:").strip()
    if not cmd:
        continue

    socket_server.send(cmd.encode('utf-8'))

    # 2.以写的方式打开一个新文件，接收服务端发来的文件的内容写入客户的新文件
    # 第一步：先收报头的长度
    obj = socket_server.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_bytes = socket_server.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)

    print(header_dic)
    total_size = header_dic['file_size']
    filename = header_dic['filename']

    # 第四步：接收真实数据
    with open('%s/%s' %(download_dir, filename), 'wb') as f:
        recv_size = 0

        while recv_size < total_size:
            line = socket_server.recv(1024)
            f.write(line)
            recv_size += len(line)
            percent = float(recv_size) / float(total_size)
            print('总大小:%s  已下载大小：%s %%[%s]' % (total_size, recv_size, percent*100))
socket_server.close()
