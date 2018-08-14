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

user_list = {}

# 定义购物车
shopping_cart = []

f = open(file='user_info', mode='r', encoding='utf-8')
for item in f:
    u, p = item.split(',')
    user_list[u] = p.strip()
print(user_list)
f.close()

while True:
    user_name = input("请输入用户名:").strip()
    pass_word = input("请输入密码:").strip()
    if user_name in user_list:
        if pass_word == user_list[user_name]:
            print('欢迎登录', user_name)
            break
        else:
            print("输入的用户名或密码错误,请重新输入!")
    else:
        print('用户名不存在!')
while True:
    pay = input('请输入的你的工资:')
    if pay.isdigit():
        pay = int(pay)
        break
    else:
        print('工资只能为数字！')
print("商品列表如下:".center(20, '-'))
for index, goodname in enumerate(goods):
    print('%s. %s' % (index, goods[index]))
exit_flag = False
while not exit_flag:
    choice = input('请输入商品编号:').strip()
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(goods):
            if pay >= goods[choice]['price']:
                shopping_cart.append(goods[choice])
                pay = pay - goods[choice]['price']
                print('\033[31;1m加入商品 %s 到购物车成功,价格 %s 元,当前余额为 %s 元\033[0m' % (
                    goods[choice]['name'], goods[choice]['price'], pay))
            else:
                print('余额不足')

        elif choice >= len(goods):
            print('输入的商品编号不存在!')
        elif choice < 0:
            print('商品编号只能为正整数!')

    elif choice == 'q':
        if len(shopping_cart) > 0:
            print('已经购买商品列表'.center(20, '-'))
            for index, name in enumerate(shopping_cart, 1):

                print('\033[31;1m你已经购买的商品 %s. %s \033[0m' % (index, name))
            print('\033[31;1m您所剩余额为:%s 元\033[0m' % pay)
        exit_flag = True
