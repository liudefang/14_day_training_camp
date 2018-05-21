# -*- encoding: utf-8 -*-
# @Author  : mike.liu
# @File    : main.py
import os
import sys
from modules import authentication, creditcard, shopping, admincenter

# 程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_DIR)

while True:
    print("\033[32;1m欢迎进入ATM + 购物商城:\033[0m".center(50, '-'),
          "\n1: 购物中心\n"
          "2: 信用卡中心\n"
          "3: 后台管理\n"
          "q: 退出系统\n")
    choice = input("\033[34;0m请选择要进入的模块ID:\033[0m")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            res = authentication.user_auth()
            if res != None:
                if res[0] == "True":
                    current_user = res[1]
                    shopping.Empty_shopping_car()
                    while True:
                        print("\033[36;1m欢迎进入购物中心\033[0m".center(50, '-'),
                              "\n1:购物商城\n"
                              "2:查看购物车\n"
                              "3:购物结算\n"
                              "4:个人中心\n"
                              "b: 返回\n")
                        choice = input("\033[34;0m请选择要进入的模块ID:\033[0m")
                        if choice.isdigit():
                            choice = int(choice)

                            if choice == 1:
                                shopping.Shopping_mall()
                            elif choice == 2:
                                shopping.Shopping_car()
                            elif choice == 3:
                                shopping.Pay_shopping(current_user)
                            elif choice == 4:
                                while True:
                                    print("\033\33;0m个人中心\033[0m".center(50, '-'),
                                          "\n1:购物历史记录\n"
                                          "2:修改登录密码\n"
                                          "3:修改个人信息\n"
                                          "4:修改信用卡绑定\n"
                                          "b: 返回")
                                    choice = input("\033[34;0m请选择要进入的模块ID:\033[0m")
                                    if choice.isdigit():
                                        choice = int(choice)
                                        if choice == 1:
                                            shopping.Catcar_record(current_user)
                                        elif choice == 2:
                                            shopping.Updata_password(current_user)
                                        elif choice == 3:
                                            shopping.Updata_address(current_user)
                                        elif choice == 4:
                                            shopping.Link_creditcard(current_user)
                                    elif choice == "b":
                                        break
                                    else:
                                        print("\033[31;0m输入的模块ID无效,请重新输入!\033[0m")
                        elif choice == "b":
                            break
                        else:
                            print("\033[31;0m输入的模块ID无效,请重新输入!\033[0m")
        elif choice == 2:
            res = authentication.creditcard_auth()
            if res != None:
                if res[0] == 'True':
                    current_creditcard = res[1]
                    while True:
                        print("\033[36;1m欢迎进入信用卡中心\033[0m".center(50, '-'),
                              "\n1:我的信用卡\n"
                              "2:提现\n"
                              "3:转账\n"
                              "4:还款\n"
                              "5:流水记录\n"
                              "b: 返回\n")
                        choice = input("\033[34;0m请选择要进入的模块ID:\033[0m")
                        if choice.isdigit():
                            choice = int(choice)
                            if choice == 1:
                                creditcard.My_creditcard(current_creditcard)
                            elif choice == 2:
                                creditcard.Cash_advance(current_creditcard)
                            elif choice == 3:
                                creditcard.Transfer(current_creditcard)
                            elif choice == 4:
                                creditcard.Repayment(current_creditcard)
                            elif choice == 5:
                                creditcard.Catcard_record(current_creditcard)
                        elif choice == 'b':
                            break
                        else:
                            print("\033[31;0m输入的模块ID无效,请重新输入!\033[0m")
        elif choice == 3:
            res = authentication.admincenter_auth()
            if res != None:
                while True:
                    print("\033[36;1m欢迎进入管理中心\033[0m".center(50, '-'),
                          "\n1:创建账号\n"
                          "2:锁定账号\n"
                          "3:解锁账号\n"
                          "4:提升信用卡额度\n"
                          "b: 返回\n")
                    choice = input("\033[34;0m请选择要进入的模块ID:\033[0m")
                    if choice.isdigit():
                        choice = int(choice)
                        if choice == 1:
                            admincenter.User_create()
                        elif choice == 2:
                            admincenter.Lock_user()
                        elif choice == 3:
                            admincenter.Unlock_user()
                        elif choice == 4:
                            admincenter.Updata_limit()
                    elif choice == 'b':
                        break
                    else:
                        print("\033[31;0m输入的模块ID无效,请重新输入!\033[0m")
    elif choice == 'q':
        exit('退出系统')
    else:
        print("\033\31;0m输入的模块ID无效,请重新输入!\033[0m")






