# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 13:29
# @Author  : mike.liu
# @File    : 高阶函数.py
# 变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

res = add(3, -6, abs)
print(res)