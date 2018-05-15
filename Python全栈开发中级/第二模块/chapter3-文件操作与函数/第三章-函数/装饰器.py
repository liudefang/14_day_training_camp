# -*- encoding: utf-8 -*-
# @Time    : 18-5-15 下午5:53
# @Author  : mike.liu
# @File    : 装饰器.py

user_status = False    # 用户登录了就把这个改成True


def login(func):
    _username = 'mike'
    _password = '123'
    global user_status
    if user_status == False:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        if username == _username and password == _password:
            print('欢迎光临,%s' % username)
            user_status = True
        else:
            print('用户名或密码错误，请重新输入!')

    if user_status == True:
        func()   # 看这里看这里，只要验证通过了，就调用相应功能
    # else:
    #     print('用户已登录，验证通过!')


def home():
    print('首页'.center(20, '-'))


def america():
    # login()   # 执行前加上验证
    print('欧美专区'.center(20, '-'))


def japan():
    print('日韩专区'.center(20, '-'))


def henan():
    # login()   # 执行前加上验证
    print('河南专区'.center(20, '-'))


home()
login(america)    # 需要验证就调用login，把需要验证的功能，当做一个参数传给login
# america()
# henan()
login(henan)