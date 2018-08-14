# -*- encoding: utf-8 -*-
# @Time    : 2018-07-14 12:42
# @Author  : mike.liu
# @File    : server.py

import socketserver
from threading import Thread
class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    break
                print('client data:', data.decode())
                self.request.send(data.upper())
            except Exception as e:
                print(e)
                break


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), Handler)
    t = Thread(target=server.serve_forever())
    t.start()
