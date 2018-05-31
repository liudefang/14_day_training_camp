# -*- encoding: utf-8 -*-
# @Time    : 2018-05-31 21:38
# @Author  : mike.liu
# @File    : 1 面向过程编程.py
import re
import json


def interactive():
    username = input("请输入用户名:").strip()
    password = input("请输入密码:").strip()
    email = input("请输入邮箱地址:").strip()

    return {
        "username": username,
        "password": password,
        "email": email
    }


def check(user_info):
    is_valid = True

    if len(user_info["username"]) == 0:
        print("用户名不能为空!")
        is_valid = False

    if len(user_info["password"]) < 6:
        print("密码不能为空!")
        is_valid = False

    if not re.search(r'@.*?\.com$', user_info["email"]):
        print("邮件格式不合法!")
        is_valid = False

    return {
        "is_valid": is_valid,
        "user_info": user_info
    }


def register(check_info):
    if check_info["is_valid"]:
        with open("db.json", "w", encoding="utf-8") as f:
            json.dump(check_info["user_info"], f)



def main():
    user_info = interactive()

    check_info = check(user_info)

    register(check_info)


if __name__ == '__main__':
    main()
