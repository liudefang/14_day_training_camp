# -*- encoding: utf-8 -*-
# @Time    : 18-5-16 下午3:12
# @Author  : mike.liu
# @File    : love.py
from timeit import time

words = input('请输入要表白的话:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y) % len(item)] if((x*0.05)**2 + (y*0.1)**2-1)**3-(x*0.05)**2 * (y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(12, -12, -1)]))
    time.sleep(1.5)


# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if((x*0.05)**2 + (y*0.1)**2-1)**3-(x*0.05)**2 * (y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))