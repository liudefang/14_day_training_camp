# -*- encoding: utf-8 -*-
# @Time    : 18-7-11 下午6:57
# @Author  : mike.liu
# @File    : 08 线程queue.py

import queue

# 队列
# q = queue.Queue()
# q.put('first')
# q.put('second')
# q.put('third')
#
# print(q.get())
# print(q.get())
# print(q.get())

# 堆栈
# q = queue.LifoQueue()
#
# q.put('first')
# q.put('second')
# q.put('third')
#
# print(q.get())
# print(q.get())
# print(q.get())

# class queue.PriorityQueue(maxsize=0) #优先级队列：存储数据时可设置优先级的队列
q = queue.PriorityQueue()
q.put((20, 'a'))
q.put((10, 'b'))
q.put((30, 'c'))

print(q.get())
print(q.get())
print(q.get())