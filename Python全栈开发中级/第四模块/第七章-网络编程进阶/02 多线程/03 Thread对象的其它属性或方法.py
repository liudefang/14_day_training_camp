# -*- encoding: utf-8 -*-
# @Time    : 18-7-10 上午9:07
# @Author  : mike.liu
# @File    : 03 Thread对象的其它属性或方法.py

# from threading import Thread
# import threading
# from multiprocessing import Process
# import os
# import time
#
# def work():
#     time.sleep(3)
#     print(threading.current_thread().getName())
#
#
# if __name__ == '__main__':
#     # 在主进程下开启线程
#     t = Thread(target=work)
#     t.start()
#
#     print(threading.current_thread().getName())
#     print(threading.current_thread())   # 主线程
#     print(threading.enumerate())    # 连同主线程在内有两个运行的线程
#     print(threading.active_count())
#     print('主线程/主进程')


# 主线程等待子线程结束
from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)

if __name__ == '__main__':
    t = Thread(target=sayhi, args=('mike', ))
    t.start()
    t.join()
    print('主线程')
    print(t.is_alive())