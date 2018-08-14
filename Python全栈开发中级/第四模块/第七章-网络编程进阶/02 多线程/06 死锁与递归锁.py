# -*- encoding: utf-8 -*-
# @Time    : 18-7-11 下午12:06
# @Author  : mike.liu
# @File    : 06 死锁与递归锁.py
# 死锁
# from threading import Thread, Lock
# import time
# mutexA = Lock()
# mutexB = Lock()
#
#
# class MyThread(Thread):
#     def run(self):
#         self.func1()
#         self.func2()
#
#     def func1(self):
#         mutexA.acquire()
#         print('\033[41m%s 拿到A锁\033[0m' % self.name)
#
#         mutexB.acquire()
#         print('\033[42m%s 拿到B锁\033[0m' % self.name)
#         mutexB.release()
#
#         mutexA.release()
#
#     def func2(self):
#         mutexB.acquire()
#         print('\033[43m%s 拿到B锁\033[0m' % self.name)
#         time.sleep(3)
#
#         mutexA.acquire()
#         print('\033[44m%s 拿到A锁\033[0m' % self.name)
#         mutexA.release()
#
#         mutexB.release()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()

# 递归锁
from threading import Thread, RLock
import time

mutexA = mutexB = RLock()       # 一个线程拿到锁，counter加1，该线程内又碰到加锁的情况，则counter继续加1，这期间所有其他线程都只能等待，等待该线程释放所有锁，即counter递减到0为止


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' % self.name)

        mutexB.acquire()
        print('%s 拿到B锁' % self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s 拿到B锁\033[0m' % self.name)

        mutexA.acquire()
        print('%s 拿到A锁' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()