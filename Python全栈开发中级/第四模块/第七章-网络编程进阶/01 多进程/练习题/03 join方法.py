# -*- encoding: utf-8 -*-
# @Time    : 18-7-6 上午9:11
# @Author  : mike.liu
# @File    : 03 join方法.py

from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1, 3))
    print('------>%s' % n)

if __name__ == '__main__':
    p1 = Process(target=task, args=(1,))
    p2 = Process(target=task, args=(2,))
    p3 = Process(target=task, args=(3,))

# 效果一：保证最先输出-------->4
#     p1.start()
#
#     p2.start()
#     p3.start()
#
#     print('------->4')
#     p1.join()

# 效果二：保证最后输出-------->4
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     print('------->4')


# 效果三：保证按顺序输出
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()


    print('------->4')


