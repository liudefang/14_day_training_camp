#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/5/4 18:22
# @Author  : mike.liu
# @File    : 第九次作业.py
#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
# data = {
#     'no' : 1,
#     'name' : 'Runoob',
#     'url' : 'http://www.runoob.com'
# }
#
# json_str = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
# print ("Python 原始数据：", repr(data))
# print ("JSON 对象：", json_str)

# for x in range(-30, 30):
#     print(x)
#print(eval('{"name":"egon","password":"123"}'))

# file = "user_file.txt"
# f = open(file, 'r', encoding='utf-8')
# data = eval(f.readline())
# print(data)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
name = 'IBM'
print(portfolio('name')('shares'))