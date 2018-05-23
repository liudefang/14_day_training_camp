# -*- encoding: utf-8 -*-
# @Time    : 2018-05-22 23:23
# @Author  : mike.liu
# @File    : rando.py
import  random
print(random.randrange(1, 10))      # 返回1-10之间的一个随机数，不包括10
print(random.randint(1, 10))        # 返回1-10之间的一个随机数，包括10
print(random.randrange(0, 100, 2))  # 随机选取1到100间的偶数
print(random.random)    # 返回随机浮点数
print(random.choice('abce3#&@1'))       # 返回一个给定数据集合中的随机字符

print(random.sample('abcdefghij', 3))   # 从多个字符中选取特定数量的字符

# 生成随机字符串
import string
str1 = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
print(str1)

# 洗牌

print(random.shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))