# -*- encoding: utf-8 -*-
# @Time    : 2018-04-16 23:57
# @Author  : mike.liu
# @File    : 购物车.py
#
# 数据结构：
# goods = [
# {"name": "电脑", "price": 1999},
# {"name": "鼠标", "price": 10},
# {"name": "游艇", "price": 20},
# {"name": "美女", "price": 998},
# ......
# ]
#
# 功能要求：
# 基础要求：
#
# 1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
#
# 2、允许用户根据商品编号购买商品
#
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#
# 4、可随时退出，退出时，打印已购买商品和余额
#
# 5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
#
#
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

# 定义字典
accounts = {}

# 定义购物车
shopping_cart = []

f = open("user_info", "r", encoding="utf-8")
for line in f:  # 循环文件
    u, p = line.split(',')
    accounts[u] = p.strip()

print(accounts)
f.close()

while True:
    username = input("请输入你的用户名:").strip()
    password = input("请输入你的密码:").strip()

    if username in accounts:
        if accounts[username] == password:  # 输入的密码和字典的密码是否一致
            print("登录成功", username)
            break
        else:
            print("用户名或密码错误，请重新输入!")
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
                pay = pay - goods[choice]['price']
                shopping_cart.append(goods[choice])
                print("\033[31;1m添加商品%s到购物车成功\033[0m, \033[31;1m当前余额为%s\033[0m" % (goods[choice], pay))
            else:
                print("你的余额不足，不能购买该商品")
                continue
        else:
            print("该商品编号不存在！")

    elif choice == 'q':
        if len(shopping_cart) > 0:
            print("----您已经购买的商品如下----")
            for index, item in enumerate(shopping_cart, 1):
                print("%s. %s" % (index,item))
            print("----您所剩余额为----")
            print("余额:", pay)
        exit_flag = True








