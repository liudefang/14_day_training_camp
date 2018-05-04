#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/5/3 9:45
# @Author  : mike.liu
# @File    : 函数参数.py

# 默认参数
# def stu_register(name, age, course, country = "CN" ):
#     print("注册学生信息".center(20, '-'))
#     print("姓名", name)
#     print("age", age)
#     print("国籍", country)
#     print("课程", course)
#
# stu_register("张三", 22,  "python")
# stu_register("王五", 23,  "linux")
# stu_register("李四", 25,  "Java")

# 关键参数


# def stu_register(name, age, course='py', country="CN"):
#     print("注册学生信息".center(20, '-'))
#     print("姓名", name)
#     print("age", age)
#     print("国籍", country)
#     print("课程", course)
#
# stu_register("张三", course='py', age=22, country="CN")

# 非固定参数
# def stu_register(name, age, *args, **kwargs):   # *args 会把多传入的参数变成一个元组形式  *kwargs会把多传入的参数变成一个dict形式
#     print(name, age, args, kwargs)
#
# stu_register("张三", 22, "CN", "python", sex="M", province="湖南")

# 返回值
# def stu_register(name, age, course='py', country="CN"):
#     print("注册学生信息".center(20, '-'))
#     print("姓名", name)
#     print("age", age)
#     print("国籍", country)
#     print("课程", course)
#     if age > 22:
#         return False
#     else:
#         return True
#
# registration_status = stu_register("张三", 22, course="python全栈开发", country="CN")
#
# if registration_status:
#     print("注册成功!")
# else:
#     print("注册信息有误!")

# 全局和局部变量
# name = "张三"
#
# def change_name():
#     global name
#
#     name = "张三买了一辆特斯拉"
#     print("修改后的姓名:", name)
#
# change_name()
# print("在外面看看name改了吗？", name)

# 嵌套函数
# name = "张三"
#
# def change_name():
#     name = "张三丰"
#
#     def change_name2():
#         name = "张山峰"
#         print("张山峰打印:", name)
#
#     change_name2()    # 调用内层函数
#     print("第二层打印:", name)
#
#
# change_name()
# print("最外层打印:", name)

# 匿名函数
# calc = lambda x,y:x**y
# print(calc(2, 5))
#
# res = map(lambda x:x**2, (1, 5, 7, 4, 8))
# for i in res:
#     print(i)

# 高阶函数
# def add(x, y, f):
#     return f(x) + f(y)
#
# res = add(3, -6, abs)
# print(res)

# 递归函数
# def calc(n):
#     print(n)
#     if int(n/2) == 0:
#         return n
#     return calc(int(n/2))
#
# calc(10)

# 练习题
#
# 修改个人信息程序
#
# 在一个文件里存多个人的个人信息，如以下
#
# username password  age position department
# alex     abc123    24   Engineer   IT
# rain     df2@432    25   Teacher   Teching
# ....
# 1.输入用户名密码，正确后登录系统 ，打印
#
# 1. 修改个人信息
# 2. 打印个人信息
# 3. 修改密码
# 2.每个选项写一个方法
#
# 3.登录时输错3次退出程序

user_file = "user_list"
f = open(user_file, 'r+', encoding='utf-8')
raw_data = f.readlines()
users = {}
# 把账户数据从文件里读出来，变成dict
for line in raw_data:
    line = line.strip()
    if not line.startswith('#'):
        item = line.split(',')
        users[item[0]] = item
        print(item)

menu = '''
1.打印个人信息
2.修改个人信息
3.修改密码
'''

count = 0
while count < 3:
    username = input("请输入用户名:").strip()
    password = input("请输入密码:").strip()
    if username in users:
        if password == users[username][1]:
            print(users[username])
            print("欢迎登录成功 %s".center(20, '-') % username)
        else:
            print("用户名或密码输入错误，请重新输入!")
    else:
        print("用户名不存在!")
