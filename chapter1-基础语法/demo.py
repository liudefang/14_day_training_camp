#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/11 17:16
# @Author  : mike.liu
# @File    : demo·.py
'''f = open("user.txt",'r')
for line in f.readlines():
    print("line:", line)'''

products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]

shopping_cart = []

exit_flag = False
while not exit_flag:
    print("--------商品列表---------")
    for index,p in enumerate(products):
        print("%s. %s   %s" %(index,p[0],p[1]  ) )

    choice = input("输入想买的商品编号:")
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(products):
            shopping_cart.append(products[choice])
            print("Added product %s into shopping cart." %(products[choice]))
        else:
            print("商品不存在")
    elif choice == 'q':
        if len(shopping_cart) >0:
            print("-------你已购买以下商品-------")
            for index,p in enumerate(shopping_cart):
                print("%s. %s   %s" % (index, p[0], p[1]))

        #break
        #run_flag = False
        exit_flag = True