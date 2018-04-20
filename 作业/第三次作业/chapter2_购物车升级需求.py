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

# 定义一个用户字典
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
    value_price = value_interm[2]

    shopping_cart[value_username] = {
        "username": value_username,
        "goodsname": value_goodsname,
        "price": value_price

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
salary = 0
while True:
    username = input("请输入你的用户名:").strip()
    password = input("请输入你的密码:").strip()

    if username in user_dict:
        if username in shopping_cart:

            if user_dict[username]["password"] == password:  # 输入的密码和字典的密码是否一致
                salary = float(user_dict[username]["salary"])
                print("\033[32;1m登录成功:%s,您的余额为:%s元\033[0m" % (username, salary))
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

    print("------请输入如下类型:------\n"
          "1.上面的商品编号:\n"
          "2.输入q退出购物:\n"
          "3.输入h查看历史消费清单:\n")
    choice = input("请选择输入:").strip()
    if choice.isdigit():  # 校验是否为整数
        choice = int(choice)
        if 0 <= choice < len(goods):
            total_salary = salary + pay
            if goods[choice]['price'] <= total_salary:
                salary = total_salary - goods[choice]['price']
                # shopping_cart.append(goods[choice])

                f = open("user_shop_cart", 'a', encoding="utf-8")
                f.write("%s, %s, %s\n" % (username, goods[choice]['name'], goods[choice]['price']))
                f.close()
                user_dict[username]["salary"] = salary
                f1 = open("user_list", "w+", encoding="utf-8")
                # 将字典转换成列表，将改变的信息写入到文件中
                for value in user_dict.values():
                    user = [value["username"], value["password"], str(value["salary"])]
                    user = ",".join(user)
                    f1.write(user + "\n")
                    f1.close()
                print("\033[31;1m添加商品:%s 到购物车成功'\033[0m, \033[31;1m价格为:%s元\033[0m, \033[31;1m当前余额为: %s元\033[0m" % (goods[choice]['name'],goods[choice]['price'], salary))

            else:
                print("你的余额不足，不能购买该商品")
                continue
        else:
            print("该商品编号不存在！")

    elif choice == 'q':
        print("----您已经购买的商品如下----")
        goods_name = shopping_cart[username]["goodsname"]
        print("商品名称:", goods_name)
        print("----您所剩余额为----")
        print("\033[31;1m余额:%s元\033[0m:" % salary)
        break

    elif choice == 'h':
        print("----您的消费记录如下----")
        goods_name = shopping_cart[username]["goodsname"]
        price = float(shopping_cart[username]["price"])
        print("\033[31;1m商品名称:%s\033[0m, \033[31;1m价格:%s元\033[0m" % (goods_name, price))
        exit_flag = True
