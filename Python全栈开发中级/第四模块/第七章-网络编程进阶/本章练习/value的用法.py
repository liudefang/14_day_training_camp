# -*- encoding: utf-8 -*-
# @Time    : 2018-07-14 10:13
# @Author  : mike.liu
# @File    : value的用法.py

from multiprocessing import Process, Value

import time
import random


def save_money(money):
    for i in range(100):
        time.sleep(0.5)
        money.value += random.randint(1, 200)


def take_money(money):
    for i in range(100):
        time.sleep(0.5)
        money.value -= random.randint(1, 150)

# money 共享内存对象，给他一个初始值2000，类型为整型
# 相当于开辟了一个空间，同时绑定值2000


money = Value('i', 2000)

d = Process(target=save_money, args=(money, ))
d.start()
w = Process(target=take_money, args=(money, ))
w.start()

d.join()
w.join()
print(money.value)