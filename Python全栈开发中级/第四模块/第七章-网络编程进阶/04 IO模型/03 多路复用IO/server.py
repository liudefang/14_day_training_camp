# -*- encoding: utf-8 -*-
# @Time    : 2018-07-12 23:11
# @Author  : mike.liu
# @File    : server.py

from socket import *
import select

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8081))
server.listen(5)
server.setblocking(False)
print('starting')

rlist = [server,]
wlist = []
wdata = {}

while True:
    r1, w1, x1 = select.select(rlist, wlist, [], 0.5)
    print(w1)
    for sock in r1:
        if sock == server:
            conn, addr = sock.accept()
            rlist.append(conn)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                rlist.remove(sock)

    for sock in w1:
        sock.send(wdata[sock])
        wlist.remove(sock)
        wdata.pop(sock)
