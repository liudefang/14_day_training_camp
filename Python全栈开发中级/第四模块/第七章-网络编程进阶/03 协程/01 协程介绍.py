# -*- encoding: utf-8 -*-
# @Time    : 18-7-12 上午9:06
# @Author  : mike.liu
# @File    : 01 协程介绍.py

# # 串行执行
# import time
#
#
# def consumer(res):
#     '''任务1： 接收数据，处理数据'''
#     pass
#
#
# def producer():
#     '''任务2：生成数据'''
#     res = []
#     for i in range(100):
#         res.append(i)
#     return res
#
#
# start = time.time()
# # 串行执行
# res = producer()
# consumer(res)       # 写成consumer(producer())会降低执行效率
# stop = time.time()
# print(stop-start)   # 1.835823059082031

# 基于yield并发执行
# import time
#
#
# def consumer():
#     '''任务1：接收数据，处理数据'''
#     while True:
#         x = yield
#
#
# def producer():
#     '''任务2：生产数据'''
#     g = consumer()
#     next(g)
#     for i in range(100):
#         g.send(i)
#
#
# start = time.time()
# # 基于yield保存状态，实现两个任务直接来回切换，即并发的效果
# # ps：如果每个任务中都加上打印，那么明显地看到两个任务的打印是你一次我一次，即并发执行的
# producer()
#
#
# stop = time.time()
# print(stop-start)

# yield并不能实现遇到io切换

import time


def consumer():
    '''任务1：接收数据，处理数据'''
    while True:
        x = yield

def producer():
    '''任务2：生产数据'''
    g = consumer()
    next(g)
    for i in range(100):
        g.send(i)
        time.sleep(2)

start = time.time()
producer()  # 并发执行，但是任务producer遇到io就会阻塞住，并不会切换到该线程内的其它任务去执行

stop = time.time()
producer(stop-start)
