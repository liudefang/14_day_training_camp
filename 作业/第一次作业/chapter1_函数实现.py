# -*- encoding: utf-8 -*-
# @Time    : 2018-04-23 21:19
# @Author  : mike.liu
# @File    : chapter1_函数实现.py
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
