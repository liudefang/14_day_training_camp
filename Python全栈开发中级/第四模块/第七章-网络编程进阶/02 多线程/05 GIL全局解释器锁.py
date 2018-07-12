# -*- encoding: utf-8 -*-
# @Time    : 18-7-11 上午8:38
# @Author  : mike.liu
# @File    : 05 GIL全局解释器锁.py

# import os
# import time
# print(os.getpid())
# time.sleep(30)

# from threading import Thread,Lock
# import os
# import time
#
# def work():
#     global n
#     lock.acquire()
#     temp = n
#     time.sleep(0.5)
#     n = temp - 1
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     n = 100
#     l = []
#     for i in range(100):
#         p = Thread(target=work)
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     print(n)    # 结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全，不加锁则结果可能为99

# 如果并发的多个任务是计算密集型：多进程效率高
# from multiprocessing import Process
# from threading import Thread
# import os,time
#
#
# def work():
#     res = 0
#     for i in range(10000):
#         res *= i
#
#
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count())
#     start = time.time()
#     for i in range(4):
#         p = Process(target=work)
#         p = Thread(target=work)
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop = time.time()
#     print('运行时间: %s' % (stop-start))

# 如果并发的多个任务是I/O密集型：多线程效率高
from multiprocessing import Process
from threading import Thread
import threading
import os,time

def work():
    time.sleep(2)
    print('===>')


if __name__ == '__main__':
    l = []
    print(os.cpu_count())
    start = time.time()
    for i in range(400):
        #p = Process(target=work)
        p = Thread(target=work)     # 耗时2秒多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print('运行时间:%s' %(stop-start))


