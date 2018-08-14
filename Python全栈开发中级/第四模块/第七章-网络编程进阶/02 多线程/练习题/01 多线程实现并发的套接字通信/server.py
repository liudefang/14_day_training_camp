# -*- encoding: utf-8 -*-
# @Time    : 2018-07-08 12:57
# @Author  : mike.liu
# @File    : server.py

from socket import *
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


# def talk(conn):
#     while True:
#         try:
#             data = conn.recv(1204)
#             if not data:
#                 break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#     conn.close()
#
#
# def server(ip, port):
#
#     server_socket = socket(AF_INET, SOCK_STREAM)
#
#     server_socket.bind((ip, port))
#     server_socket.listen(1)
#
#     while True:
#         conn, addr = server_socket.accept()
#         p = Thread(target=talk, args=(conn,))
#         p.start()
#     conn.close()
#
#
# if __name__ == '__main__':
#     server('127.0.0.1', 8081)

# 基于线程池实现
def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except ConnectionResetError:
            break
def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(ip, port)
    server.listen(5)

    while True:
        conn, addr = server.accept()
        pool.submit(communicate, conn)

    server.close()


if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    server('127.0.0.1', 8081)