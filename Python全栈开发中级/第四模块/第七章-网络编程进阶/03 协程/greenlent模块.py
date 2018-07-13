# -*- encoding: utf-8 -*-
# @Time    : 18-7-12 上午10:24
# @Author  : mike.liu
# @File    : greenlent模块.py

# from greenlet import greenlet
#
#
# def eat(name):
#     print('%s eat 1' % name)
#     g2.switch('mike')
#     print('%s eat 2' % name)
#     g2.switch()
#
#
# def play(name):
#     print('%s play 1' % name)
#     g1.switch()
#     print('%s play 2' % name)
#
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
#
# g1.switch('mike')   # 可以在第一次switch时传入参数，以后都不需要

# import time
#
# def f1():
#     res = 1
#     for i in range(100):
#         res += i
#
#
# def f2():
#     res = 1
#     for i in range(100):
#         res *= i
#
#
# start = time.time()
# f1()
# f2()
# stop = time.time()
# print('run time is %s' % (stop-start))  # 1.7881393432617

# 切换
from greenlet import greenlet
import time


def f1():
    res = 1
    for i in range(100):
        res+=i
        g2.switch()


def f2():
    res = 1
    for i in range(100):
        res*=i
        g1.switch()


start = time.time()
g1 = greenlet(f1)
g2 = greenlet(f2)
g1.switch()
stop = time.time()
print('run time is %s' %(stop-start))   # 8.5592269897460
