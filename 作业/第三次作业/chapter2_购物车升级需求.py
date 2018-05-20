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
import os
from tabulate import tabulate

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    {"name": "飞机", "price": 9999}
]

# 购物车
shop_list = {}
# 历史购物车
tmp_shop_list = []

salary = 0
total_cost = 0
while True:
    username = input("请输入你的用户名:").strip()
    password = input("请输入你的密码:").strip()

    f_path = "account/%s" % username
    if os.path.isfile(f_path):
        f_obj = open(f_path, encoding='gbk')
        user_list = eval(f_obj.read())    # 把账号数据加载到内存中
        f_obj.close()
        print(user_list['account'])
        if username in user_list['account']['user']:
            if password == user_list['account']['password']:
                print('欢迎登录', username)
                break
            else:
                print('用户名或密码错误,请重新输入!')
    else:
        exit('用户名不存在!')

while True:
    pay = input("请输入你的工资:").strip()
    if pay.isdigit():
        pay = int(pay)
        break
    else:
        print("工资只能为整数!")
print("--------商品列表如下:-------")
for index, item in enumerate(goods):
    print("%s. %s %s" % (index, item['name'], item['price']))

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
            salary = user_list['account']['balance']
            total_salary = salary + pay
            if goods[choice]['price'] <= total_salary:
                salary = total_salary - goods[choice]['price']    # 扣钱
                # 1. 判断商品名称是否在购物车里面存在，如果不在初始化一条
                # 2. 如果存在，在原来的基础上面增加一条
                # 3. 余额是当前用户的余额和工资进行相加
                if goods[choice]['name'] not in user_list['shop_list']:
                    user_list['shop_list'][goods[choice]['name']] = {"count": 0, "price": 0}
                user_list['shop_list'][goods[choice]['name']]['count'] += 1
                user_list['shop_list'][goods[choice]['name']]['price'] += goods[choice]['price']
                user_list['account']['balance'] = salary

                print("\033[31;1m添加商品:%s 到购物车成功'\033[0m, \033[31;1m价格为:%s元\033[0m, \033[31;1m当前余额为: %s元\033[0m" % (
                            goods[choice]['name'], goods[choice]['price'], salary))

            else:
                print("你的余额不足，不能购买该商品")
                continue
        else:
            print("该商品编号不存在！")
    elif choice == 'q':
        print("----\033[31;1m您已经购买的商品如下\033[0m----")
        for p in user_list['shop_list']:
            tmp_shop_list.append([p, user_list['shop_list'][p]["count"],
                                  user_list['shop_list'][p]["price"]/user_list['shop_list'][p]["count"],
                                  user_list['shop_list'][p]["price"],
                                  ])
            total_cost += user_list['shop_list'][p]["price"]
        tmp_shop_list.append(["总价", "", total_cost])

        print(tabulate(tmp_shop_list, headers=['商品', '数量', '单价', '总价'], tablefmt="grid"))
        print("\033[31;1m你的余额为\033[0m: %s" % user_list['account']['balance'])

        # 保存数据到文件中
        f = open(f_path, 'w', encoding='GBK')
        f.write(str(user_list))
        f.close()
        break
    elif choice == 'h':
        print("----\033[31;1m您的消费记录如下\033[0m----")
        for p in user_list['shop_list']:
            tmp_shop_list.append([p, user_list['shop_list'][p]["count"],
                                  user_list['shop_list'][p]["price"]/user_list['shop_list'][p]["count"],
                                  user_list['shop_list'][p]["price"],
                                  ])
            total_cost += user_list['shop_list'][p]["price"]
        tmp_shop_list.append(["总价", "", total_cost])
        print(tabulate(tmp_shop_list, headers=['商品', '数量', '单价', '总价'], tablefmt="grid"))
        print("\033[31;1m你的余额为\033[0m: %s" % user_list['account']['balance'])
        exit_flag = True
