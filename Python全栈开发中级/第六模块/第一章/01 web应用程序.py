# -*- encoding: utf-8 -*-
# @Time    : 2018-09-02 14:46
# @Author  : mike.liu
# @File    : 01 web应用程序.py

import socket

def handle_request(cliect):

    request_data = cliect.recv(1024)
    print("request_data:", request_data)
    cliect.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf-8"))
    cliect.send("<h1 style='color:red'>Hello word! </h1>".encode("utf-8"))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)

    while True:
        print("the server is waiting for client-connection...")
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()