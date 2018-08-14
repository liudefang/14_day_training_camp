# -*- encoding: utf-8 -*-
# @Time    : 18-7-25 下午5:51
# @Author  : mike.liu
# @File    : 服务端.py


import socketserver
class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print('connection:', self.client_address)
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
    server.serve_forever()