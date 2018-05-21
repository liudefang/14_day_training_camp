# -*- encoding: utf-8 -*-
# @Author  : mike.liu
# @File    : admincenter.py

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
__db_users_dict = BASE_DIR + r"\database\users_dict"
__db_creditcard_dict = BASE_DIR + r"\database\creditcard_dict"

'''创建用户'''


def User_create(address="None", locked=0, creditcard=0):
    while True:
        print("开始创建用户".center(50, "-"))
        with open(__db_users_dict, "r+", encoding='utf-8') as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                print("系统已有用户 [%s]" % key)
            if_create = input("\n\033[34;0m是否创建新的用户 确定[y]/返回[b]\033[0m:")
            if if_create == "y":
                username = input("\033[34;0m输入要添加账户的用户名：\033[0m")
                password = input("\033[34;0m输入添加账户的密码：\033[0m")
                if username not in users_dict.keys():
                    if len(username.strip()) > 0:
                        if len(password.strip()) > 0:
                            users_dict[username] = {"username": username, "password": password, "creditcard": creditcard,
                                                    "address": address, "locked": locked}
                            dict = json.dumps(users_dict)
                            f_users_dict.seek(0)
                            f_users_dict.truncate(0)
                            f_users_dict.write(dict)
                            print("\033[31;1m创建用户 %s 成功\033[0m\n" % username)
                        else:
                            print("\033[31;0m输入的密码为空\033[0m\n")
                    else:
                        print("\033[31;0m输入的用户名为空\033[0m\n")
                else:
                    print("\033[31;0m用户名 %s 已经存在\033[0m\n" % username)
            if if_create == "b":
                break


'''锁定用户'''


def Lock_user():
    while True:
        print("\033[32;0m锁定用户\033[0m".center(50, "-"))
        with open(__db_users_dict, "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                if users_dict[key]["locked"] == 0:
                    print("系统用户 【%s】\t\t锁定状态：【未锁定】" % key)
                else:
                    print("系统用户 【%s】\t\t锁定状态：\033[7m【已锁定】\033[0m" % key)
            if_lock = input("\n\033[34;0m是否进行用户锁定 确定【y】/返回【b】\033[0m:")
            if if_lock == "y":
                lock_user = input("\033[34;0m输入要锁定的用户名\033[0m:")
                if lock_user in users_dict.keys():
                    if users_dict[lock_user]["locked"] == 0:
                        users_dict[lock_user]["locked"] = 1
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\033[31;1m用户 %s 锁定成功\033[0m\n" % lock_user)
                    else:
                        print("\033[31;0m用户 %s 锁定失败 之前已经被锁定\033[0m\n" % lock_user)
                else:
                    print("\033[31;0m用户 %s 不存在\033[0m\n" % lock_user)
            if if_lock == "b":
                break


'''解锁用户'''


def Unlock_user():
    while True:
        print("\033[32;0m解锁用户\033[0m".center(50, "-"))
        with open(__db_users_dict, "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                if users_dict[key]["locked"] == 0:
                    print("系统用户 【%s】\t\t锁定状态：【未锁定】" % key)
                else:
                    print("系统用户 【%s】\t\t锁定状态：\033[7m【已锁定】\033[0m" % key)
            if_lock = input("\n\033[34;0m是否进行用户解锁 确定【y】/返回【b】\033[0m:")
            if if_lock == "y":
                unlock_user = input("\033[34;0m输入要解锁的用户名\033[0m:")
                if unlock_user in users_dict.keys():
                    if users_dict[unlock_user]["locked"] == 1:
                        users_dict[unlock_user]["locked"] = 0
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\033[31;1m用户 %s 解锁成功\033[0m\n" % unlock_user)
                    else:
                        print("\033[31;0m用户 %s 解锁失败 用户未被锁定\033[0m\n" % unlock_user)
                else:
                    print("\033[31;0m用户 %s 不存在\033[0m\n" % unlock_user)
            if if_lock == "b":
                break


'''修改信用卡额度'''


def Updata_limit():
    while True:
        print("\033[32;0m修改信用卡额度\033[0m".center(60, "-"))
        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                    limitcash = creditcard_dict[key]["limitcash"]
                    print("信用卡 【%s】\t目前可用额度：【￥%s】\t取现额度：【￥%s】" %
                          (key, creditcard_dict[key]["limit"], limitcash))
            if_Updata = input("\n\033[34;0m是否进行信用卡额度调整 确定【y】/返回【b】\033[0m:")
            if if_Updata == "y":
                creditcard = input("\033[34;0m输入要修改额度的信用卡卡号\033[0m:")
                if creditcard in creditcard_dict.keys():
                    limit = input("\033[34;0m输入额度修改后的金额(至少￥5000)\033[0m:")
                    if limit.isdigit():
                        limit_default = creditcard_dict[creditcard]["deflimit"]
                        limit = int(limit)
                        if limit >= 5000:
                            updata = limit - limit_default
                            creditcard_dict[creditcard]["limit"] += updata
                            creditcard_dict[creditcard]["limitcash"] += updata//2
                            creditcard_dict[creditcard]["deflimit"] = limit
                            dict = json.dumps(creditcard_dict)
                            f_creditcard_dict.seek(0)
                            f_creditcard_dict.truncate(0)
                            f_creditcard_dict.write(dict)
                            print("\033[31;1m信用卡 %s 额度修改成功 额度 %s \033[0m\n" % (creditcard, limit))
                        else:
                            print("\033[31;0m输入金额 ￥%s 小于￥5000\033[0m\n" % limit)
                    else:
                        print("\033[31;0m输入金额 ￥%s 格式错误\033[0m\n" % limit)
                else:
                    print("\033[31;0m信用卡 【%s】 不存在\033[0m\n" % creditcard)
            if if_Updata == "b":
                break