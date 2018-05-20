# -*- encoding: utf-8 -*-
# @Time    : 2018-05-19 8:17
# @Author  : mike.liu
# @File    : 生成器.py
g = (x * x for x in range(10))
print(g)
print(next(g))
for n in g:
    print(n)