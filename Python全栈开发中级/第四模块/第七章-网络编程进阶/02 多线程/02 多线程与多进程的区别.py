# -*- encoding: utf-8 -*-
# @Time    : 18-7-10 上午8:31
# @Author  : mike.liu
# @File    : 02 多线程与多进程的区别.py

# 1、在主进程下开启线程
# from threading import Thread
#
# def work():
#     print("hello")
#
# if __name__ == '__main__':
#     t = Thread(target=work)
#     t.start()
#     print("主线程/主进程")

# 2、在主进程下开启子进程
# from multiprocessing import Process
#
# def work():
#     print('hello')
#
#
# if __name__ == '__main__':
#     # 在主进程下开启子进程
#     p = Process(target=work)
#     p.start()
#     print('主线程/主进程')

# 二 瞅一瞅pid？
from threading import Thread
# from multiprocessing import Process
# import os
#
# def work():
#     print('hello', os.getpid())
#
#
# if __name__ == '__main__':
#     # p1 = Thread(target=work)
#     # p2 = Thread(target=work)
#     p1 = Process(target=work)
#     p2 = Process(target=work)
#     p1.start()
#     p2.start()
#     print('主线程/主进程', os.getpid())

# 三 同一进程内的线程共享该进程的数据？
# 1、进程之间地址空间是隔离的
# from multiprocessing import Process
# import os
#
# def work():
#     global n
#     n = 0
#
#
# if __name__ == '__main__':
#     n = 100
#     p = Process(target=work)
#     p.start()
#     p.join()
#     print('主', n)

# 2、同一进程内开启的多个线程是共享该进程地址空间的
from threading import Thread
import os

def work():
    global n
    n = 0


if __name__ == '__main__':
    n = 100
    t = Thread(target=work)
    t.start()
    t.join()
    print('主', n)