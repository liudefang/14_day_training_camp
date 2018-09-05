# -*- encoding: utf-8 -*-
# @Time    : 18-9-5 上午8:38
# @Author  : mike.liu
# @File    : wsgiref_server.py

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, Web!</h1>']


httpd = make_server('127.0.0.1', 8080, application)

print('Servering HTTP on port 8080...')
# 开始监听HTTP请求
httpd.serve_forever()