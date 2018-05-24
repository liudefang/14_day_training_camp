# -*- encoding: utf-8 -*-
# @Time    : 2018-05-24 20:09
# @Author  : mike.liu
# @File    : shelve模块.py
# pickle进行了封装，可以dump多次

# 序列化
import shelve
f = shelve.open("shelve_test")  # 打开一个文件
names = ['mike', 'alex', 'test']
info = {'name': 'alex', 'age': 22}

f['names'] = names   # 持久化列表
f['info_dic'] = info

f.close()

# 反序列化
d = shelve.open("shelve_test")
print(d["names"])
print(d["info_dic"])

