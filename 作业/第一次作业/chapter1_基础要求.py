#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/11 9:31
# @Author  : mike.liu
# @File    : chapter1_基础要求.py

# 基础需求：
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序

# while循环实现

'''count = 0
while count < 3:
    username = input("请输入你的姓名:").strip()
    password = input("请输入你的密码:").strip()
    if username == 'mike' and password == '123':
        print("恭喜你,登录成功！")
        break
    else:
        print("输入的用户名或密码错误，请重新输入！")
    count += 1'''

# for 循环实现
for count in range(3):
    username = input("请输入你的姓名:").strip()
    password = input("请输入你的密码:").strip()
    if username == 'mike':
        if username == 'mike' and password == '123':
            print("恭喜你,登录成功！")
            break

        else:
            print("输入的用户名或密码错误，请重新输入！")
    else:
        print("用户名不存在！")
    count += 1
