# -*- encoding: utf-8 -*-
# @Time    : 18-9-5 下午7:25
# @Author  : mike.liu
# @File    : views.py
import datetime

import pymysql

from urllib.parse import parse_qs


def login(environ):

    with open("templates/index.html", "rb") as f:
        data = f.read()
    return data

def index(environ):

    with open("templates/index.html", "rb") as f:
        data = f.read()
    return data

def fav(environ):

    with open("templates/favicon.ico", "rb") as f:
        data = f.read()
    return data

def reg(environ):

    with open("templates/reg.html", "rb") as f:
        data = f.read()
    return data

def timer(environ):
    now = datetime.datetime.now().strftime("%y-%m-%d %x")
    return now.encode("utf8")

def auth(request):
    try:
        request_body_size = int(request.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = request['wsgi.input'].read(request_body_size)
    data = parse_qs(request_body)

    user = data.get(b"user")[0].decode("utf-8")
    pwd = data.get(b"pwd")[0].decode("utf-8")

    # 连接数据库
    conn = pymysql.connect(host='10.1.2.71', port=3306, user='root', passwd='testjfz', db='blog')
    # 创建游标
    cur = conn.cursor()
    SQL="select * from userinfo where name='%s' and password='%s'" %(user,pwd)
    cur.execute(SQL)

    if cur.fetchone():

        f = open("templates/backend.html", "rb")
        data = f.read()
        data = data.decode("utf8")
        return data.encode("utf8")

    else:
        print("OK456")
        return b"user or pwd is wrong"



