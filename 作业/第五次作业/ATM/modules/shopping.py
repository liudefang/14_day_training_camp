# -*- encoding: utf-8 -*-
# @Author  : mike.liu
# @File    : shopping.py

import json
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
__db_product = BASE_DIR + r"\db\product_list"
__db_shoping_car = BASE_DIR + r"\db\shopping_car"
__db_users_dict = BASE_DIR + r"\db\users_dict"
__db_creditcard_dict = BASE_DIR + r"\db\creditcard_dict"
__db_shopping_record = BASE_DIR + r"\db\shopping_record"
__db_creditcard_record = BASE_DIR + r"\db\creditcard_record"


'''购物商城'''


def Shopping_mall():
    shopping_list, pro_list = [], []
    with open(__db_product, "r", encoding="utf-8") as f_product:
        for item in f_product:
            pro_list.append(item.strip("\n").split())

    def pro_inf():
        print("编号\t商品\t\t价格")
        for index, item in enumerate(pro_list):
            print("%s\t\t%s\t\t%s" % (index, item[0], item[1]))
    while True:
            print("\033[32;0m目前商城在售的商品信息\033[0m").center(50, "-")
            pro_inf()
            choice_id = input("\n\033[34;0m选择要购买的商品编号 【购买 ID】/【返回 b】\033[0m：")
            if choice_id.isdigit():
                choice_id = int(choice_id)
                if 0 <= choice_id < len(pro_list):
                    pro_item = pro_list[choice_id]
                    print("\033[31;0m商品%s加入购物车 价格%s\033[0m" %(pro_item[0], pro_item[1]))
                    shopping_list.append(pro_item)

                else:
                    print("\033[31;0m错误：没有相应的编号 请重新输入:\033[0m\n")
            elif  choice_id == "b":
                with open(__db_shoping_car, "r+") as f_shopping_car:
                    list = json.loads(f_shopping_car.read())
                    list.extend(shopping_list)
                    f_shopping_car.seek(0)
                    f_shopping_car.truncate(0)
                    list = json.dumps(list)
                    f_shopping_car.write(list)
                break
            else:
                 print("\033[31;0m错误：没有相应的编号 请重新输入:\033[0m\n")


'''清空购物车'''


def Empty_shopping_car():
    with open(__db_shoping_car, "w") as f_shopping_car:
        list = json.dumps([])
        f_shopping_car.write(list)


'''购物车'''


def Shopping_car():
    while True:
        with open(__db_shoping_car, "r+") as f_shopping_car:
            list = json.loads(f_shopping_car.read())
            sum = 0
            print("\033[32;0m购物车信息清单\033[0m".center(40, "-"))
            for index, item in enumerate(list):
                print(index, item[0], item[1])
                sum += int(item[1])
            print("\033[31;1m商品总额共计： %s\033[0m" % sum)
        if_buy = input("\n\033[34;0m选择要进行的操作 返回【b】/清空【f】\033[0m:")
        if if_buy == "b":
            break
        if if_buy == "f":
            Empty_shopping_car()


'''购物记录'''
def Shoppingcar_record(current_user,value):
    with open(__db_shopping_record, "r+") as f_shoppingcar_record:
        record_dict = json.loads(f_shoppingcar_record.read())
        month = time.strftime('%Y-%m-%d', time.localtime())
        times = time.strftime("%H:%M:%S")
        if str(current_user) not in record_dict.keys():
            record_dict[current_user]={month:{times:value}}
        else:
            if month not in record_dict[current_user].keys():
                record_dict[current_user][month] = {times: value}
            else:
                record_dict[current_user][month][times] = value
        dict = json.dumps(record_dict)
        f_shoppingcar_record.seek(0)
        f_shoppingcar_record.truncate(0)
        f_shoppingcar_record.write(dict)


'''查看购物记录'''


def Catcar_record(current_user):
    while True:
        print("\033[32;0m用户 %s 购物记录\033[0m".center(40, "-") % current_user)
        with open(__db_shopping_record, "r+") as f_shoppingcar_record:
            record_dict = json.loads(f_shoppingcar_record.read())
            if current_user not in record_dict.keys():
                print("\033[31;0m用户 %s 还没有进行过消费\033[0m\n" % current_user)
            else:
                data = sorted(record_dict[current_user])
                for d in data:
                    times = sorted(record_dict[current_user][d])
                    for t in times:
                        print("\033[31;0m【时间】 %s %s\033[0m" % (d, t))
                        items =record_dict[current_user][d][t]
                        print("\033[31;0m【商品】 【价格】\033[0m")
                        for v in items:
                            print("\033[31;0m %s\t\t%s\033[0m" % (v[0], v[1]))
            if_back = input("\n\033[34;0m是否返回 返回【b】\033[0m:")
            if if_back == "b":
                break


def Creditcard_record(creditcard,value):
    with open(__db_creditcard_record, "r+", encoding='utf-8') as f_creditcard_record:
        record_dict = json.loads(f_creditcard_record.read())
        month = time.strftime('%Y-%m-%d', time.localtime())
        times = time.strftime("%H:%M:%S")
        if str(creditcard) not in record_dict.keys():
            record_dict[creditcard] = {month: {times: value}}
        else:
            if month not in record_dict[creditcard].keys():
                record_dict[creditcard][month] = {times: value}
            else:
                record_dict[creditcard][month][times] = value
        dict = json.dumps(record_dict)
        f_creditcard_record.seek(0)
        f_creditcard_record.truncate(0)
        f_creditcard_record.write(dict)


'''信用卡密码认证'''


def Auth_creditcard(creditcard):
    with open(__db_creditcard_dict, "r+", encoding='utf-8') as f_creditcard_dict:
        creditcard_dict = json.loads(f_creditcard_dict.read())
        passwd = input("\033[34;0m当前信用卡【%s】 请输入支付密码：\033[0m:"%(creditcard))
        if passwd == creditcard_dict[creditcard]["password"]:
            return True
        else:
            print("\033[31;0m密码输入错误，支付失败\033[0m")


'''购物结算'''


def Pay_shopping(current_user):
    while True:
        sum = 0
        print("\033[32;0m购物结算\033[0m".center(40, "-"))
        with open(__db_shoping_car, "r+", encoding='utf-8') as f_shopping_car:
            list = json.loads(f_shopping_car.read())
            for item in list:
                sum += int(item[1])
            if_pay = input("\n\n\033[34;0m当前商品总额：%s 是否进行支付 确定【y】/返回【b】\033[0m:" % sum)
            if if_pay == "y":
                with open(__db_users_dict, "r+") as f_users_dict:
                    users_dict = json.loads(f_users_dict.read())
                    creditcard=users_dict[current_user]["creditcard"]
                    if creditcard == 0:
                        print("\033[31;0m账号 %s未绑定信用卡，请到个人中心里修改信用卡绑定\033[0m\n" % current_user)
                    else:
                        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
                            creditcard_dict = json.loads(f_creditcard_dict.read())
                            limit = creditcard_dict[creditcard]["limit"]
                            limit_new = limit - sum
                            if limit_new >=0:
                                res = Auth_creditcard(creditcard)
                                if res == True:
                                    creditcard_dict[creditcard]["limit"] = limit_new
                                    dict = json.dumps(creditcard_dict)
                                    f_creditcard_dict.seek(0)
                                    f_creditcard_dict.truncate(0)
                                    f_creditcard_dict.write(dict)
                                    value = "购物支付 %s" % sum
                                    print("\033[31;1m支付成功，当前余额 %s元\033[0m\n" % limit_new)
                                    Shoppingcar_record(current_user, list)
                                    Creditcard_record(creditcard, value)
                                    Empty_shopping_car()
                            else:
                                print("\033[31;0m当前信用卡额度 %s元 不足矣支付购物款 可绑定其他信用卡支付\033[0m\n" % limit)
            if if_pay == "b":
                break


'''信用卡绑定'''
def Link_creditcard(current_user):
    while True:
        print("\033[32;0m修改信用卡绑定\033[0m".center(50, "-"))
        with open(__db_users_dict, "r+", encoding='utf-8') as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            creditcard = users_dict[current_user]["creditcard"]
            if creditcard == 0:
                print("当前账号： \t%s" % current_user)
                print("信用卡绑定：\033[31;0m未绑定\033[0m\n")
            else:
                print("当前账号： \t%s" % current_user)
                print("绑定的信用卡： %s\n" % creditcard)
            if_updata = input("\033[34;0m是否要修改信用卡绑定 确定【y】/返回【b】\033[0m:")
            if if_updata == "y":
                creditcard_new = input("\033[34;0m输入新的信用卡卡号(6位数字)\033[0m:")
                if creditcard_new.isdigit() and len(creditcard_new) == 6:
                    with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
                        creditcard_dict = json.loads(f_creditcard_dict.read())
                        if creditcard_new in creditcard_dict.keys():
                            users_dict[current_user]["creditcard"] = creditcard_new
                            dict = json.dumps(users_dict)
                            f_users_dict.seek(0)
                            f_users_dict.truncate(0)
                            f_users_dict.write(dict)
                            print("\033[31;1m信用卡绑定成功\033[0m\n")
                        else:
                            print("\033[31;0m输入信用卡卡号不存在(未发行)\033[0m\n")
                else:
                    print("\033[31;0m输入信用卡格式错误\033[0m\n")
            if if_updata == "b":
                break


'''修改登录密码'''


def Updata_password(current_user):
    while True:
        print("\033[32;0m修改登录密码\033[0m".center(40, "-"))
        print("当前账号：\t%s\n当前密码：\t**\n" % current_user)
        if_updata = input("\033[34;0m是否要修改 % s登录密码 确定【y】/返回【b】\033[0m:" % current_user)
        if if_updata == "y":
            with open(__db_users_dict, "r+", encoding='utf-8') as f_users_dict:
                users_dict = json.loads(f_users_dict.read())
                password = users_dict[current_user]["password"]
                old_pwd = input("\033[34;0m输入原来的密码\033[0m:")
                if old_pwd == password:
                    new_pwd = input("\033[34;0m输入新的密码\033[0m:")
                    agin_pwd = input("\033[34;0m再输入新的密码\033[0m:")
                    if new_pwd == agin_pwd:
                        users_dict[current_user]["password"] = new_pwd
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\033[31;1m密码修改成功\033[0m\n")
                    else:
                        print("\033[31;0m两次密码不一致\033[0m\n")
                else:
                    print("\033[31;0m密码不正确\033[0m\n")
        if if_updata == "b":
            break


'''修改个人资料'''


def Updata_address(current_user):
    while True:
        print("\033[32;0m修改个人资料\033[0m".center(50, "-"))
        with open(__db_users_dict, "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            address = users_dict[current_user]["address"]
            print("当前账号：\t%s\n当前收货地址：\t%s\n" % (current_user, address))
            if_updata = input("\033[34;0m是否要修改 % s登录密码 确定【y】/返回【b】\033[0m:" % current_user)
            if if_updata == "y":
                new_address = input("\033[34;0m输入新的收货地址\033[0m:")
                users_dict[current_user]["address"] = new_address
                dict = json.dumps(users_dict)
                f_users_dict.seek(0)
                f_users_dict.truncate(0)
                f_users_dict.write(dict)
                print("\033[31;1m收货地址修改成功\033[0m\n")
            if if_updata == "b":
                break
