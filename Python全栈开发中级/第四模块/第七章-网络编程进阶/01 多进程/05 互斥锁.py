# -*- encoding: utf-8 -*-
# @Time    : 18-7-6 上午10:20
# @Author  : mike.liu
# @File    : 05 互斥锁.py


from multiprocessing import Process, Lock
import os
import time
import json

#
# def work():
#     print('%s is running' % os.getpid())
#     time.sleep(2)
#     print('%s is done' % os.getpid())
#
# if __name__ == '__main__':
#     for i in range(3):
#         p = Process(target=work)
#         p.start()

# 由并发变成了串行，牺牲了运行效率，但避免了竞争



# def work(lock):
#     lock.acquire()  # 加锁
#     print('%s is running' % os.getpid())
#     time.sleep(2)
#     print('%s is done' % os.getpid())
#     lock.release()  # 释放锁
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(3):
#         p = Process(target=work, args=(lock,))
#         p.start()

# 二 模拟抢票练习
# 加锁
# 文件db.txt的内容为：{"count":1}
# 注意一定要用双引号，不然json无法识别

# def search(name):
#     dic = json.load(open('db.txt'))
#     time.sleep(1)
#     print('\033[43m %s 查询到剩余票数%s\033[0m' % (name, dic['count']))
#
#
# def get(name):
#     dic = json.load(open('db.txt'))
#     time.sleep(1)   # 模拟读数据的网络延迟
#     if dic['count'] > 0:
#         dic['count'] -= 1
#         time.sleep(1)   # 模拟写数据的网络延迟
#         json.dump(dic, open('db.txt', 'w'))
#         print('\033[46m %s 购票成功\033[0m' % name)
#
#
# def task(name):
#     search(name)
#     with lock:  # 相当于lock.acquire(),执行完自代码块自动执行lock.release()
#         get(name)
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):  # 模拟并发10个客户端抢票
#         name = '<路人%s>' % i
#         p = Process(target=task, args=(name,))
#         p.start()

# 三 互斥锁与join
def search(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)
    print('\033[43m %s 查询到剩余票数%s\033[0m' % (name, dic['count']))


def get(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)   # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(1)   # 模拟写数据的网络延迟
        json.dump(dic, open('db.txt', 'w'))
        print('\033[46m %s 购票成功\033[0m' % name)


def task(name):
    search(name)    # 并发执行

    lock.acquire()
    get(name)   # 串行执行
    lock.release()


if __name__ == '__main__':
    lock = Lock()

    for i in range(10):  # 模拟并发10个客户端抢票
        name = '<路人%s>' % i
        p = Process(target=task, args=(name,))
        p.start()
        p.join()