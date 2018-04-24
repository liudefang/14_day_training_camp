#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/23 9:31
# @Author  : mike.liu
# @File    : 文件操作.py
# import chardet
# f = open(file='user_list', mode='r', encoding='gbk')
# for line in f:
#     print(line)
# f.close()


# f = open(file='user_list1', mode='r+', encoding='gbk')
# data = f.read()     # 可以读内容
# print(data)
# f.write('\nJacke,30,13898424616,Operation,2017-07-02')   # 可以写
# f.close()

f = open(file='user_list1', mode='r+', encoding='utf-8')
f.seek(6)
f.write("测试工程师")
f.close()