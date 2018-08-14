# -*- encoding: utf-8 -*-
# @Time    : 18-5-16 下午4:41
# @Author  : mike.liu
# @File    : 函数进阶练习题.py
import time

# 一：编写3个函数，每个函数执行的时间是不一样的
# def time1(func):
#
#     func()
#     start = time.time()
#     return start
#
# def test1():
#     time.sleep(2)
#     print('test1')
#
# def test2():
#     time.sleep(3)
#     print('test2')
#
# @time1
# def test3():
#     #time.sleep(5)
#     print('test3')
#
#
#
#
#
# test1()
#
# test2()
# test3()


# 二：编写装饰器，为每个函数加上统计运行时间的功能

# def 第九次作业(func):
#     def inner():
#         start = time.time()
#         print('hello,第九次作业')
#
#         end = time.time() - start
#         print('花的时间:', end )
#
#         func()
#
#     return inner
#
# @第九次作业
# def test1():
#     print('执行时间')
#
# #test1 = 第九次作业(test1)
# test1()

# 三：编写装饰器，为函数加上认证的功能，即要求认证成功后才能执行函数
# def login(func):
#     def inner(*args, **kwargs):
#         _username = 'mike'
#         _password = '123'
#         username = input('请输入用户名:').strip()
#         password = input('请输入密码:').strip()
#         if username == _username and password == _password:
#             print('欢迎登录, %s' % username)
#         else:
#             print('用户名或密码错误！')
#
#         func(*args, **kwargs)
#
#     return inner
#
# @login
# def user_info(style):
#     print('登录到个人信息页面')
#
#
# user_info('个人信息')

# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
user_status = False
def login(func):
    def inner(*args, **kwargs):

        user_list = 'user_file.txt'
        f = open(user_list, 'r', encoding='utf-8')
        user_data1 = {}
        user_data = f.readlines()
        user_data1 = eval(str(user_data))
        print(user_data1)

        _username = user_data1[0]['name']
        _password = user_data1['password']
        global user_status

        if user_status == False:
            username = input('请输入用户名:').strip()
            password = input('请输入密码:').strip()
            if username == _username and password == _password:
                print('欢迎登录, %s' % username)
                user_status = True
            else:
                print('用户名或密码错误！')

        if user_status == True:

            return func(*args, **kwargs)

    return inner

@login
def user_info(style):
    print('登录到个人信息页面')

@login
def user_home():
    print('登录到用户首页')


user_info('个人信息')
user_home()