# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 13:24
# @Author  : mike.liu
# @File    : 匿名函数.py

# 匿名函数就是不需要显式的指定函数名

# def calc(x, y):
#     return x**y
#
# print(calc(2, 5))
#
# # 换成匿名函数
# calc = lambda x, y:x**y
# print(calc(2, 5))

res = map(lambda x:x**2, [1, 5, 7, 4, 8])
for i in res:
    print(i)