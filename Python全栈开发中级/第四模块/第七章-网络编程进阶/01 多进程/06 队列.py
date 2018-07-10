# -*- encoding: utf-8 -*-
# @Time    : 2018-07-08 8:43
# @Author  : mike.liu
# @File    : 06 队列.py

from multiprocessing import Queue

q = Queue(3)

q.put(1)
q.put(2)
q.put(3)
print(q.full())     # 满了
# q.put(4)  # 再放就阻塞住了

print(q.get())
print(q.get())
print(q.get())
print(q.empty())    # 空了
print(q.get())  # 再取就阻塞住了