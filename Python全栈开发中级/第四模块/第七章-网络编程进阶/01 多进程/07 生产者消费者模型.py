# -*- encoding: utf-8 -*-
# @Time    : 2018-07-08 9:16
# @Author  : mike.liu
# @File    : 07 生产者消费者模型.py
from multiprocessing import Process, Queue
import time
import random
import os


# def consumer(q, name):
#     while True:
#         res = q.get()
#         time.sleep(random.randint(1, 3))
#         print("\033[43m %s 吃%s\033[0m" % (name, res))
#
#
# def producer(q, name, food):
#     for i in range(3):
#         time.sleep(random.randint(1, 3))
#         res = "%s%s" % (food, i)
#         q.put(res)
#         print("\033[45m %s 生产了 %s\033[0m" % (name, res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者们:即厨师们
#     p1 = Process(target=producer, args=(q, 'egon', '包子'))
#
#     # 消费者们：即吃货们
#     c1 = Process(target=consumer, args=(q, 'mike'))
#
#     # 开始
#     p1.start()
#     c1.start()
#     print('主')


# 二、跳出死循环
# def consumer(q, name):
#     while True:
#         res = q.get()
#         if res is None:
#             break
#         time.sleep(random.randint(1, 3))
#         print("\033[43m %s 吃%s\033[0m" % (name, res))
#
#
# def producer(q, name, food):
#     for i in range(3):
#         time.sleep(random.randint(1, 3))
#         res = "%s%s" % (food, i)
#         q.put(res)
#         print("\033[45m %s 生产了 %s\033[0m" % (name, res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者们:即厨师们
#     p1 = Process(target=producer, args=(q, 'egon1', '包子'))
#     p2 = Process(target=producer, args=(q, 'egon2', '烧麦'))
#     p3 = Process(target=producer, args=(q, 'egon3', '豆浆'))
#
#     # 消费者们：即吃货们
#     c1 = Process(target=consumer, args=(q, 'mike1'))
#     c2 = Process(target=consumer, args=(q, 'mike2'))
#
#     # 开始
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     q.put(None)
#     q.put(None)
#     q.put(None)
#     print('主')

# 三、JoinableQueue实现生产者消费者模型
from multiprocessing import Process, JoinableQueue
import time
import random


def consumer(q, name):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('%s 吃 %s' % (name, res))
        q.task_done()  # 发送信号给q.join(),说明已经从队列中取走一个数据并处理完毕


def producer(q, name, food):
    for i in range(3):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (food, i)
        q.put(res)
        print('%s 生产了 %s' % (name, res))
    q.join()    # 等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束


if __name__ == '__main__':
    q = JoinableQueue()     # 使用JoinableQueue()

    # 生产者：即厨师们
    p1 = Process(target=producer, args=(q, 'egon1', '包子'))
    p2 = Process(target=producer, args=(q, 'egon2', '烧麦'))
    p3 = Process(target=producer, args=(q, 'egon3', '豆浆'))

    # 消费者们：即吃货们
    c1 = Process(target=consumer, args=(q, 'mike1'))
    c2 = Process(target=consumer, args=(q, 'mike2'))
    c1.daemon = True
    c2.daemon = True

    # 开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    # 1、主进程等生产者p1,p2,p3结束
    # 2、而p1，p2，p3，是在消费者把所有数据都取干净之后才会结束
    # 3、所以一旦p1,p2,p3结束了，证明消费者也没必要存在了，应该随着主进程一块死掉，因而需要将生产者们设置成守护进程
    print("主")