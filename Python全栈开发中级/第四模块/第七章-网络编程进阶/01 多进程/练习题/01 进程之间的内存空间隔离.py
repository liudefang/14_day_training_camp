# -*- encoding: utf-8 -*-
# @Time    : 18-7-5 上午9:53
# @Author  : mike.liu
# @File    : 01 进程之间的内存空间隔离.py

from multiprocessing import Process

n = 100

def work():
    global n
    n = 0
    print('子进程：', n)


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    print("主进程内:", n)