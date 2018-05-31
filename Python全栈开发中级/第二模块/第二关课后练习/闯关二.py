# -*- encoding: utf-8 -*-
# @Time    : 2018-05-29 22:40
# @Author  : mike.liu
# @File    : 闯关二.py

# 2，读文件找到第9个字符，华 ，找到第二行的 实，删除最后一行 写入文件
# 桃之夭夭，灼灼其华。之子于归，宜其室家。
# 桃之夭夭，有蕡其实。之子于归，宜其家室。
# 桃之夭夭，其叶蓁蓁。之子于归，宜其家人。

# f = open("poem.txt", "r+", encoding="utf-8")
# # f.seek(3*8)
# # print(f.read(1))
# #
# # f.seek(3*28+2)
# # print(f.read(1))
#
# data_list = f.readlines()
# print(data_list)
# data_list.pop()
# print(data_list)
# f.seek(0)
# f.truncate()
# f.write(''.join(data_list))
# # f.close()

# 3，求出函数的执行时间，利用装饰器
# import time
# def timer(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         ret = func(*args, **kwargs)
#         stop_time = time.time() - start_time
#         print(stop_time)
#         return ret
#
#     return inner
#
# @timer
# def time_test(x, y):
#     time.sleep(1)
#     return x + y
#
# print(time_test(3, 9))

# def test():
#     print(luffy)
#     luffy = 'e'
#
#
# test()
# luffy = "the king of sea."
#
# test()
# 5，li = [1,2,3,5,5,6,7,8,9,9,8,3] 利用生成器功能，写一个所有数值乘以2的功能
# li = [1,2,3,5,5,6,7,8,9,9,8,3]
# res = (i*2 for i in li)
# print(list(res))

# 6.打印日志11/26/2017 10:44:21 PM bug 24 并写入文件example.log中
# import logging
# logging.basicConfig(filename='example.log', format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S %p', level=logging.DEBUG)
# logging.warning('bug 24')


# 把第三行的“不要回答”替换成“绝对不能回复”
import os

file1 = "02第二模块之三体语录"
file2 = "02第二模块之三体语录.new"
with open(file1, "r", encoding="utf-8") as f1:
    with open(file2, "w", encoding="utf-8") as f2:

        for line in f1:
            if "不要回答" in line:
                line = line.replace("不要回答", "绝对不能回复")
                f2.write(line)
            else:
                f2.write(line)
f1.close()
f2.close()
os.replace(file2, file1)
# def test():
#    print(luffy)
# luffy = "the king of sea."
# test()

# li = [1, 2, 3, 5, 5, 6, 7, 8, 9, 9, 8, 3]
# test = [i*2 for i in li]
# print(test)

# def test1():
#     n = 18
#     def test2():
#         print("我是test2。", n)
#         return n
#     return test2()
#
# print(test1())
