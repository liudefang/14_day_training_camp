# -*- encoding: utf-8 -*-
# @Author  : mike.liu
# @File    : authentication.py
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
__db_user_dict = BASE_DIR + r"/db/users_dict"       # 读取用户信息
__db_creditcard_dict = BASE_DIR + r"/db/creditcard_dict"        # 读取信用卡信息

'''认证装饰器'''


def auth(auth_type):
    def outer_wrapper(func):
        if auth_type == "user_auth":
            def wrapper():
                res = func()
                username = input("\033[34;0m请输入用户名:\033[0m").strip()
                password = input("\033[34;0m请输入密码:\033[0m").strip()
                with open(__db_user_dict, 'r+', encoding='utf-8') as f_users_dict:
                    users_dict = json.loads(f_users_dict.read())
                    if username in users_dict.keys():
                        if password == users_dict[username]['password']:
                            if users_dict[username]['locked'] == 0:
                                print('\033[31;0m用户 %s 登录成功\033[0m' % username)
                                return res, username
                            else:
                                print('\033[31;0m用户 %s 已经被锁定，登录失败!\033[0m')
                        else:
                            print('\033[31;0m输入的用户名或密码错误,请重新输入!\033[0m')
                    else:
                        print('\033[31;0m输入的用户名不存在!\033[0m')
            return wrapper

        if auth_type == "creditcard_auth":
            def wrapper():
                res = func()
                creditcard = input("\033[34;0m请输入信用卡卡号:\033[0m").strip()
                password = input("\033[34;0m请输入信用卡密码:\033[0m").strip()
                with open(__db_creditcard_dict, 'r+', encoding='utf-8') as f_creditcard_dict:
                    creditcard_dict = json.loads(f_creditcard_dict.read())
                    if creditcard in creditcard_dict.keys():
                        if password == creditcard_dict[creditcard]['password']:
                            if creditcard_dict[creditcard]['locked'] == 0:
                                print("\033[31;0m信用卡 %s 登录成功\033[0m" % creditcard)
                                return res, creditcard
                            else:
                                print("\033[31;0m信用卡 %s 已被锁定,登录失败!\033[0m")
                        else:
                            print("\033[31;0m输入的信用卡卡号或密码错误!\033[0m")
                    else:
                        print("\033[31;0m输入的信用卡卡号不存在!\033[0m")
            return wrapper

        if auth_type == "admincenter_auth":
            def wrapper():
                res = func()
                admincenter_dict = {"admin": "admin"}
                username = input("\033[34;0m请输入管理用户名：\033[0m")
                password = input("\033[34;0m请输入管理密码：\033[0m")
                if len(username.strip()) > 0:
                    if username in admincenter_dict.keys():
                        if password == admincenter_dict[username]:
                            print("\033[31;0m管理用户 %s 认证成功\033[0m" % username)
                            return res, username
                        else:
                            print("\033[31;0m输入的密码不匹配 认证失败\033[0m")
                    else:
                        print("\033[31;0m输入的用户名不存在 认证失败\033[0m")
                else:
                    print("\033[31;0m输入的用户名为空 认证失败\033[0m")

            return wrapper
    return outer_wrapper


'''用户登录认证'''


@auth(auth_type="user_auth")
def user_auth():
    print("\33[32;0m用户登录认证\33[0m".center(50, "-"))
    return "True"


'''信用卡认证'''


@auth(auth_type="creditcard_auth")
def creditcard_auth():
    print("\33[32;0m信用卡登录认证\33[0m".center(50, "-"))
    return "True"


'''后台管理认证'''


@auth(auth_type="admincenter_auth")
def admincenter_auth():
    print("\33[32;0m后台管理登录认证\33[0m".center(50, "-"))
    return "True"
