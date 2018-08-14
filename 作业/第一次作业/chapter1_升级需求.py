#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/11 9:39
# @Author  : mike.liu
# @File    : chapter1_升级需求.py
# 升级需求：
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
'''
user_name_list = {'mike': '123', 'tom': '456', 'jack': '789'}


def user_login():
    count = 0
    while count < 3:
        username = input("请输入你的用户名:").strip()
        password = input("请输入你的密码:").strip()
        if username in user_name_list:
            if password == user_name_list[username]:
                print("欢迎登录", username)
                break
            else:
                print("密码错误,请重新输入!")
        else:
            print("用户名不存在!")
        count += 1


if __name__ == '__main__':
    user_login()
'''


# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

# 定义一个用户字典
user_dict = {}
f = open('account_db', 'r', encoding='utf-8')
for line in f:
    u, p = line.split(',')
    user_dict[u] = p.strip()
f.close()
print(user_dict)

# 加载锁定的用户
lock_file = open('lock_file', 'r', encoding='utf-8')
lock_user = []
for line in lock_file:
    lock_user.append(line.strip())

lock_file.close()
count = 0
fist_input_val = None  # 空，占位符 ，为了生成一个变量
same_to_first_input = True   # 存储每次输入的用户名是否一致的状态
username = None
while count < 3:
    username = input("请输入你的用户名:").strip()
    password = input("请输入你的密码:").strip()
    # 判断用户是否被锁定
    if username in lock_user:
        print("该用户已经被锁定,请联系管理员!")
        exit()
    # 第一次循环
    if count == 0:
        fist_input_val = username
    # 第二次循环
    if fist_input_val != username:   # 表示第一次输入的用户名和第二次输入的用户名不一致
        # 记下对比的状态
        same_to_first_input = False
        print('开始登录'.center(20, '-'))
    if username in user_dict:
        if password == user_dict[username]:
            print("登录成功", username)
            break
        else:
            print("用户名或密码错误,请重新输入!")
    else:
        print("用户名不存在")
    count += 1
else:
    print("输入错误信息太多,请稍后再试!")

    if same_to_first_input:
        # 输入错误次数为三次了，要锁定该用户
        print("开始写入文件".center(20, '-'))
        f = open('lock_file', 'a', encoding='utf-8')
        f.write("%s\n" % username)
        f.close()
        print("该用户的密码输入错误3次，用户已经被锁定!")

