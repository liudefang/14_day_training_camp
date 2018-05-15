# -*- encoding: utf-8 -*-
# @Time    : 18-5-14 上午11:39
# @Author  : mike.liu
# @File    : 作用域.py

level = 'L0'
n = 22

def func():
    level = 'L1'
    n = 33
    print(locals())

    def outer():
        n = 44
        level = 'L2'
        print(locals(), n)

        def inner():
            level = 'L3'
            print(locals(), n)  # 此处打印的n是多少?
        inner()
    outer()

func()