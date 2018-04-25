# -*- encoding: utf-8 -*-
# @Time    : 2018-04-25 23:01
# @Author  : mike.liu
# @File    : 课后练习.py
# 1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li=['alex', 'eric', 'rain']
# li=['alex', 'eric', 'rain']
# li1 = li[0]+"_"+li[1]+"_"+li[2]
# print(li1)
# 2、查找列表中元素，移除每个元素的空格，并查找以a和A开头并且以c结尾的所有元素
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

for index, item in enumerate(li, 0):
    item = item.strip()
    li[index] = item
    if item.endswith('c') and (item.startswith('a') or item.startswith('A')):
        print(item)
print(li)
