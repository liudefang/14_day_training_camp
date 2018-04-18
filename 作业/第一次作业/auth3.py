#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/13 12:09
# @Author  : mike.liu
# @File    : auth3.py

# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

f = open("account_db", "r")
accounts = {}
for line in f:   # 循环文件内容
    u,p = line.split(',')
    accounts[u] = p.strip()

print(accounts)
# 加载锁定的用户列表
lock_file = open("lock_file", "r")
lock_users = []
for line in lock_file:
    lock_users.append(line.strip())

count = 0
fist_input_val = None  # 空，占位符 ，为了生成一个变量

same_to_first_input = True   # 存储每次输入的用户名是否一致的状态

while count < 3:
    username = input("请输入用户名:").strip()
    password = input("请输入密码:").strip()
    #判断用户是否被锁定
    if username in lock_users:
        print("该用户已锁定,请联系管理员")
        exit()

    if count == 0 :  # 第一次循环
        fist_input_val = username

    # 第二次循环
    if fist_input_val != username: # 代表第一次和第二次输入的用户名不一样
        #记下对比的状态
        same_to_first_input = False
        print("-----------------")
    if username in accounts:  # 判断用户是否在字典中存在
        if password == accounts[username]:  # 判断用户名对应的密码是否正确
            print("欢迎你", username)
            break
        else:
            print("输入用户名或密码错误")

    else:
        print("用户名不存在!")
    count += 1
else:
    print("输入错误信息太多，请稍后重试!")

    if same_to_first_input:  # 代表三次输入的用户名一致
        #要锁定这个用户
        f = open("lock_file", 'a')
        f.write("%s\n" % username)
        f.close()
        print("该用户的密码输入错误3次，用户已经被锁定!")
