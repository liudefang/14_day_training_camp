# -*- encoding: utf-8 -*-
# @Time    : 18-6-22 上午10:40
# @Author  : mike.liu
# @File    : 练习题.py

# 练习题
# 什么是C/S架构？
"""
C指client(客户端软件)，S指的是Server(服务端软件)
"""
#
# 互联网协议是什么？分别介绍五层协议中每一层的功能？
"""
互联网协议：就是计算机之间的通信有一套统一的标准
TCP/IP五层协议：
物理层：主要是基于电器特性发送高低信号的，比如高电压对应数字1，低电压对应数字0
数据链路层：定义了电信号的分组方式
网络层：引入一套新的地址用来区分不同的广播域/子网，这套地址即王李地址
"""
# 基于tcp协议通信，为何建立链接需要三次握手，而断开链接却需要四次挥手
"""
传输控制协议（Transmission Control Protocol, TCP）是一种面向连接的、可靠的、基于字节流的运输层（Transport layer）通信协议。

三次握手：
客户端发送请求，服务端接收请求，并做出响应，客户端收到请求
第一次握手：建立连接时，客户端发送syn包(syn=j)到服务器，并进入SYN_SEND状态，等待服务器确认；
第二次握手：服务器收到syn包，必须确认客户的syn（ack=j+1），同时自己也发送一个SYN包（syn=k），即SYN+ACK包，此时服务器进入SYN_RECV状态；
第三次握手：客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=k+1)，此包发送完毕，客户端和服务器进入ESTABLISHED状态，完成三次握手。


因为当Server端收到Client端的SYN连接请求报文后，可以直接发送SYN+ACK报文。其中ACK报文是用来应答的，SYN报文是用来同步的。
但是关闭连接时，当Server端收到FIN报文时，很可能并不会立即关闭SOCKET，所以只能先回复一个ACK报文，告诉Client端，"你发的FIN报文我收到了"。
只有等到我Server端所有的报文都发送完了，我才能发送FIN报文，因此不能一起发送。故需要四步握手。
四次握手：

"""
# 为何基于tcp协议的通信比基于udp协议的通信更可靠？
"""
tcp:是面向连接的，可靠的，接收信息需要确认
udp：接收信息不需要确认，客户端只管发就可以了
"""
# ‍流式协议指的是什么协议，数据报协议指的是什么协议？
"""
流式协议：tcp协议
数据报协议：udp协议
"""
# 什么是socket？简述基于tcp协议的套接字通信流程
"""
socket:是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口

"""
# 什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？
"""
粘包：就是指两次结果粘到一起了
原因：是因为socket缓冲器导致的
"""
# 基于socket开发一个聊天程序，实现两端互相发送和接收消息
# server
import socket

HOST = '127.0.01'
PORT = 8081

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # 建立TCP连接
sock_server.bind((HOST, PORT))    # 绑定IP地址和端口

sock_server.listen(1)       # 开始监听

conn, addr = sock_server.accept()   # 阻塞直到有连接为止

with conn:
    print("连接信息:", addr)
    while True:
        data = conn.recv(1024)
        print("接收到的信息:", conn.getpeername(), data.decode())
        if not data:
            break

        response = input("服务器输入的信息:").strip()
        conn.send(response.encode('utf-8'))

        print("服务器发出的信息:", response)

# client
while True:
    msg = input("请输入信息:").strip()
    if
    sock_server.sendall(msg.encode('utf-8'))



# 基于tcp socket，开发简单的远程命令执行程序，允许用户执行命令，并返回结果
#
# 基于tcp协议编写简单FTP程序，实现上传、下载文件功能，并解决粘包问题
#
# 基于udp协议编写程序，实现功能
#
# 执行指定的命令，让客户端可以查看服务端的时间
#
# 执行指定的命令，让客户端可以与服务的的时间同步

