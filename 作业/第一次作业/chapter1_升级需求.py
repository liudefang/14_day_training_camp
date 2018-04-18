#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/11 9:39
# @Author  : mike.liu
# @File    : chapter1_升级需求.py
# 升级需求：
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
import time

'''user_name_list = ['mike','tom','jack']

for count in range(3):
    username = input("请输入你的姓名：")
    password = input("请输入你的密码：")
    if username in user_name_list:
        if username in user_name_list and password == '123':
          print("恭喜你,登录成功！")
          break
        else:
          print("输入的用户名或密码错误，请重新输入！")
    else:
        print("用户名不存在！")
    count += 1'''


# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

#定义一个用户字典
user_dict = {}
#定义一个用户列表
user_list = []

f = open("user.txt",'r')
#帐号的锁定信息：0表示正常，1表示锁定
for line in f.readlines():
    print("line:", line)
    useriterm = line.strip()

    value_interm = useriterm.split(',')
    value_username = value_interm[0]
    value_password = value_interm[1]
    value_lock = value_interm[2]
    user_dict[value_username] = {
        "name":value_username,
        "password":value_password,
        "lock":value_lock
    }
f.close()

#定义count_num计算用户输入错误用户的次数
count_num =0
#用于跳出多层循环
flag = True
while flag:
    if count_num == 3:
        print("登录失败3次，请1分钟之后再试")
        time.sleep(600)
    user_name = input("请输入你的姓名：")
    if user_name in user_dict.keys():
        #判断用户是否被锁定
        if int(user_dict[user_name]["lock"]) == 0:
            for i in range(3):
                password = input("请输入你的密码：")
                #判断密码是否正确
                if password == user_dict[user_name]["password"]:
                    print("登录成功！")
                    flag = False
                    break
                else:
                    print("密码输入错误！")
            else:
                #用户输入密码错误三次后锁定
                user_dict[user_name]["lock"] ="1"
                f = open("user.txt","w+")
                #将字典转换成列表，将改变的信息写入到文件中
                for value in user_dict.values():
                    user_list = [value["name"],value["password"],value["lock"]]
                    user_list = ",".join(user_list)
                    f.write(user_list+"\n")
                print("你输入的密码错误了三次，用户已经被锁定!")
                break
        else:
            print("用户已经被锁定!")
    else:
        print("用户不存在!")
        count_num +=1


