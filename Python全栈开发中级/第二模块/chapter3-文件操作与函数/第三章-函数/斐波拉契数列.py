# -*- encoding: utf-8 -*-
# @Time    : 2018-05-19 8:25
# @Author  : mike.liu
# @File    : 斐波拉契数列.py

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

# data = fib(10)
# print(data)
#
# print(data.__next__())
# print(data.__next__())
# print('干点别的事情')
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())

# for n in fib(10):
#     print(n)

g = fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break