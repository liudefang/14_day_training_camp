# -*- encoding: utf-8 -*-
# @Time    : 18-7-6 上午9:58
# @Author  : mike.liu
# @File    : 04 守护进程.py

from multiprocessing import Process
import time


def foo():
    print(123)
    time.sleep(1)
    print('end123')


def bar():
    print(456)
    time.sleep(3)
    print('end456')


if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon = True
    p1.start()
    p2.start()
    print("main-----")