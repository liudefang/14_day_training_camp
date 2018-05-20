# -*- encoding: utf-8 -*-
# @Time    : 2018-05-19 12:53
# @Author  : mike.liu
# @File    : 迭代器.py

from collections import Iterable,Iterator

print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('abc', Iterable) )

print(isinstance((x for x in range(10)), Iterable))

print(isinstance([], Iterator))

print(isinstance({}, Iterator))

print(isinstance('abc', Iterator) )

print(isinstance((x for x in range(10)), Iterator))

print(isinstance(iter([]), Iterator))

print(isinstance(iter({}), Iterator))
