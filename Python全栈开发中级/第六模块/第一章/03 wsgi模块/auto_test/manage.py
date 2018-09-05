# -*- encoding: utf-8 -*-
# @Time    : 18-9-5 下午7:20
# @Author  : mike.liu
# @File    : manage.py

# from wsgiref.simple_server import make_server
#
# from app01.views import *
# import urls
#
# def routers():
#
#     URLpattern = urls.URLpattern
#     return URLpattern
#
#
# def applications(environ, start_response):
#
#     path = environ.get("PATH_INFO")
#     print(path)
#     start_response('200 OK', [('Content-Type', 'text/html'), ('Charset', 'utf8')])
#     urlpattern = routers()
#     func = None
#     for item in urlpattern:
#         if path == item[0]:
#             func = item[1]
#             break
#
#     if func:
#         return [func(environ)]
#     else:
#         return [b"<h1>404!<h1>"]
#
#
# if __name__ == '__main__':
#     server = make_server("127.0.0.1", 8889, applications)
#     print("服务器开始启动")
#     server.serve_forever()


from wsgiref.simple_server import make_server

from app01.views import *
import urls


def routers():

    URLpattern=urls.URLpattern
    return URLpattern


def applications(environ,start_response):

    path=environ.get("PATH_INFO")
    print("path:", path)
    start_response('200 OK', [('Content-Type', 'text/html'),('Charset', 'utf8')])
    urlpattern=routers()
    func=None
    for item in urlpattern:
        if path==item[0]:
            func=item[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b"<h1>404!<h1>"]

if __name__ == '__main__':

    server=make_server("",8889,applications)
    print("server is working...")
    server.serve_forever()
