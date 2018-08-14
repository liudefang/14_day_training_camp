# -*- encoding: utf-8 -*-
# @Time    : 2018-07-14 10:26
# @Author  : mike.liu
# @File    : Array的用法.py

from multiprocessing import Process, Array

def func(m, n):
    for i in range(n):
        print(m[i])

# 此处不表数字类型为整型
# 表示开辟8个空间，且均为整型i，其实就是一个列表

m = Array('i', 3)

p = Process(target=func, args=(m, 4))
p.start()
p.join()