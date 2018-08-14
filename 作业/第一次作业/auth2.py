#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/13 10:56
# @Author  : mike.liu
# @File    : auth2.py
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)

f = open("account_db", "r")
accounts = {}
for line in f:   #循环文件内容
    u,p = line.split(',')
    accounts[u] = p.strip()
print(accounts)

count = 0
while count < 3:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username in accounts:   #判断用户是否在字典中存在
        if password == accounts[username]:    # 判断用户名对应的密码是否正确
            print("欢迎你", username)
            break
        else:
            print("输入用户名或密码错误")

    else:
        print("用户名不存在!")
    count += 1
else:
    print("输入错误信息太多，请稍后再试!")

