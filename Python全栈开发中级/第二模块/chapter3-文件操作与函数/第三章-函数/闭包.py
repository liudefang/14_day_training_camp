# -*- encoding: utf-8 -*-
# @Time    : 18-5-15 上午9:37
# @Author  : mike.liu
# @File    : 闭包.py
def outer():
    name = 'mike'

    def inner():
        print('在inner里打印外层函数的变量', name)

    return inner

f = outer()

f()