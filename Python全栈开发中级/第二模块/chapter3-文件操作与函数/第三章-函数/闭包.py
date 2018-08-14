# -*- encoding: utf-8 -*-
# @Time    : 18-5-15 上午9:37
# @Author  : mike.liu
# @File    : 闭包.py
# 关于闭包，即函数定义和函数表达式位于另一个函数的函数体内(嵌套函数)
# 闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，
# 这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域

def outer():
    name = 'mike'

    def inner():
        print('在inner里打印外层函数的变量', name)

    return inner

f = outer()

f()