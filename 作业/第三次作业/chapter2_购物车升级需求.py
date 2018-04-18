#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/18 10:47
# @Author  : mike.liu
# @File    : chapter2_购物车升级需求.py

# 扩展需求：
#
# 1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
#
# 2、允许查询之前的消费记录

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    {"name": "飞机", "price": 9999}
]

#定义一个用户字典
user_dict = {}

# 定义购物车
shopping_cart = {}

# 加载购物车的用户列表
user_shop_cart = open("user_shop_cart", "r", encoding="utf-8")  # 读取购物车用户信息文件

for line in user_shop_cart.readlines():
    print("line:", line)
    useriterm = line.strip()

    value_interm = useriterm.split(',')
    value_username = value_interm[0]
    value_goodsname = value_interm[1]

    shopping_cart[value_username] = {
        "username": value_username,
        "goodsname": value_goodsname

    }
user_shop_cart.close()

# 加载用户列表信息
f = open("user_list", "r", encoding="utf-8")   # 读取用户列表信息

for line in f.readlines():
    print("line:", line)
    useriterm = line.strip()

    value_interm = useriterm.split(',')
    value_username = value_interm[0]
    value_password = value_interm[1]
    value_pay = value_interm[2]
    user_dict[value_username] = {
        "username": value_username,
        "password": value_password,
        "salary": value_pay
    }
f.close()

while True:
    username = input("请输入你的用户名:").strip()
    password = input("请输入你的密码:").strip()

    if username in user_dict:
        if username in shopping_cart:

            if user_dict[username]["password"] == password:  # 输入的密码和字典的密码是否一致
                salary = float(user_dict[username]["salary"])
                print("\033[32;1m登录成功:%s,您的余额为:%s\033[0m" %(username, salary))
                break
            else:

                print("用户名或密码错误，请重新输入!")

        else:
            print("欢迎第一次登录", username)
            break
    else:
        print("用户名不存在!")
while True:
    pay = input("请输入你的工资:")
    if pay.isdigit():
        pay = int(pay)
        break
    else:
        print("工资只能为数字!")
print("--------商品列表如下:-------")
for index, item in enumerate(goods):  # 从序号1打印商品列表信息
    print("%s. %s" % (index, item))

exit_flag = False
while not exit_flag:

    choice = input("请输入商品编号:")
    if choice.isdigit():  # 校验是否为整数
        choice = int(choice)
        if choice >= 0 and choice < len(goods):
            if goods[choice]['price'] <= pay:
                salary = pay - goods[choice]['price']
                #shopping_cart.append(goods[choice])

                f = open("user_shop_cart", 'a', encoding="utf-8")
                f.write("%s,%s\n" % (username, goods[choice]['name']))
                f.close()
                user_dict[username]["salary"] = salary
                f1 = open("user_list", "w+", encoding="utf-8")
                # 将字典转换成列表，将改变的信息写入到文件中
                for value in user_dict.values():
                    user = [value["username"], value["password"], str(value["salary"])]
                    user = ",".join(user)
                    f1.write(user + "\n")
                    f1.close()
                print("\033[31;1m添加商品'%s'到购物车成功\033[0m, \033[31;1m当前余额为%s\033[0m" % (goods[choice]['name'], salary))

            else:
                print("你的余额不足，不能购买该商品")
                continue
        else:
            print("该商品编号不存在！")

    elif choice == 'q':
        #if len(user_shop_cart) > 0:
        print("----您已经购买的商品如下----")

        for index,item in enumerate(shopping_cart):
            if shopping_cart[username]["username"] == username:
                print("商品名称:", shopping_cart[username]["goodsname"])
        index += 1


        print("----您所剩余额为----")
        print("余额:", pay)
        exit_flag = True



# name = input("输入姓名：")
# password = input("输入密码：")
# while True:
#     if name in data:            #用户在档案中
#         if password in data[name]:          #密码和用户名对应，校验正确，登录。
#             salary = float(data[name][password])
#             print('''\033[32;1m欢迎登录，当前余额为%s\033[0m'''%salary)
#             break
#         else:           #否则密码错误，请重新输入
#             password = input("密码错误，请重新输入：")
#             continue
#     else:           #否则判断为首次登录，将用户名，密码，工资存到用户信息文件中
#         password_salary = {}
#         salary_str = input("欢迎首次登录，请输入你的工资：")
#         salary = float(salary_str)
#         password_salary[password] = salary          #工资对应到密码
#         data[name] = password_salary            #将密码-工资对应到用户名
#         file.seek(0)
#         file.write(str(data))
#         file.tell()
#         break
#
# list = [#购物清单
#     ["iphone",5800],
#     ["sifei",800],
#     ["macbook",17500],
#     ["book",75],
#     ["apple",5]
# ]
#
# file_list_r = open("历史购物信息.txt","r+",encoding="utf-8")
# file_list_r = str(file_list_r.read())
# shoppinglist_dict = eval(file_list_r)
# if name not in shoppinglist_dict:
#     shoppinglist_dict[name] = []
# shoppinglist = shoppinglist_dict[name]
# shoppinglist_dict_now = []
# choose = input("\n是否需要查询历史购物记录(y/n)：")
# if choose == 'y':
#     print("\n\n---------->历史购物记录<----------")
#     print(shoppinglist)
#     print("---------->结束<----------")
#
# while not set:      #购物车开始
#     print("---------->商品清单<----------")
#     for index,item in enumerate(list,1):
#         print(index,item)
#     print("---------->结束<----------")
#     number = input("请输入想购买商品编号：")
#     if number == "q":
#         set = True
#         data[name][password] = str(salary)
#         file.seek(0)
#         file.write(str(data))
#         file.tell()
#         print("---------->购物清单<----------")
#         print(shoppinglist)
#         print("您的余额：",salary)
#         print("---------->结束<----------")
#         shoppinglist.extend(shoppinglist)
#         shoppinglist_dict[name] = shoppinglist
#     elif number.isdigit() == False:
#         print("\033[31;1m输入不是编号内容，请重新输入\033[0m")
#     elif int(number)>int(len(list)) or int(number)<= 0:         #输入值不在清单中，报错
#         print("\033[31;1m您所购买的商品不在清单中\033[0m")
#     else:
#         number_buy = int(number)-1
#         if list[number_buy][1]<(salary):            #如果余额足够，提示购买成功并显示余额。
#             salary = salary - int(list[number_buy][1])
#             msg = '\033[32;1m您已经将%s加入购物车中，余额为%d\033[0m'%(list[number_buy][0],salary)
#             print(msg)
#             shoppinglist.append(list[number_buy])           #将本次购物信息加到购买记录中
#         else:
#             print("\033[31;1m余额不足，无法购买!\033[0m")            #提示余额不足
