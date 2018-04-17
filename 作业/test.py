# -*- encoding: utf-8 -*-
# @Time    : 2018-04-16 22:27
# @Author  : mike.liu
# @File    : test.py
# f = open('D:\\Python\\14_day_training_camp\\一周感想.txt', mode='r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    {"name": "飞机", "price": 9999}
]
for index,items in enumerate(goods):
    print(index,items)
    commodity = int(input("input goods what your want to buy:"))
    if commodity == 1:
        price = goods[commodity]['price']
        print("price:",price)

#print(goods[].values())