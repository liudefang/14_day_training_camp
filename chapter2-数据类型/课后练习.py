# -*- encoding: utf-8 -*-
# @Time    : 2018-04-25 23:01
# @Author  : mike.liu
# @File    : 课后练习.py
# 1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li=['alex', 'eric', 'rain']
# li=['alex', 'eric', 'rain']
# li1 = li[0]+"_"+li[1]+"_"+li[2]
# print(li1)
# 2、查找列表中元素，移除每个元素的空格，并查找以a和A开头并且以c结尾的所有元素
# li = ["alec", " aric", "Alex", "Tony", "rain"]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

# 列表
# for index, item in enumerate(li, 0):
#     item = item.strip()
#     li[index] = item
#     if item.endswith('c') and (item.startswith('a') or item.startswith('A')):
#         print(item)
# print(li)
#
# # 元组
# for item in tu:
#     item = item.strip()
#     print(item)
#     if item.endswith('c') and (item.startswith('a') or item.startswith('A')):
#         print(item)
# print(tu)
#
# print('字典'.center(20, '-'))
# # 字典
# for i, j in enumerate(dic, 0):
#     print(j)
#     dic[j] = dic[j].strip()
#     if dic[j].endswith('c') and (dic[j].startswith('a') or dic[j].startswith('A')):
#         print(dic[j])
# print(dic)
#
#
# print('另外一种方法'.center(20, '-'))
# for i in dic.values():
#     i = i.strip()
#     if i.endswith('c') and (i.startswith('a') or i.startswith('A')):
#         print(i)
# print(dic)
# 写代码，有如下列表，按照要求，实现每个功能
# li=['alex', 'eric', 'rain']
#
# # 计算列表长度并输出
# print(len(li))
#
# # 列表中追加元素“seven”,并输出添加后的列表
# li=['alex', 'eric', 'rain']
# li.append('seven')
# print(li)

# 请在列表的第一个位置插入元素“tony"，并输出添加后的列表
# li=['alex', 'eric', 'rain']
# li.insert(0, 'Tony')
# print(li)

# 请修改列表第2个位置的元素为“kelly"，并输出修改后的列表
# li=['alex', 'eric', 'rain']
# # li[1] = 'Kelly'
# # print(li)

# 请删除列表中的元素“eric”，并输出修改后的列表
# li=['alex', 'eric', 'rain']
# li.pop(1)
# print(li)

# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
# li=['alex', 'eric', 'rain']
# print(li.pop(1))
# print(li)

# 删除列表中的第3个元素，并输出删除元素后的列表
# li=['alex', 'eric', 'rain']
# li.pop(2)
# print(li)

# 删除列表中的第2至4个元素，并输出删除元素后的列表
# li=['alex', 'eric', 'rain']
# del li[2:4]
# print(li)

# 将列表所有的元素反转，并输出反转后的列表
# li=['alex', 'eric', 'rain']
# li.reverse()
# print(li)

# 请使用for、len、range输出列表的索引
# li=['alex', 'eric', 'rain']
# for i in range(len(li)):
#     print(i)

# 请使用enumrate输出列表元素和序号（序号从100开始）

# li=['alex', 'eric', 'rain']
# for index, item in enumerate(li, 100):
#     print(index, item)
# for item in li:
#     print('item:', item)

# 4、写代码，有如下列表，请按照功能要求实现每一个功能
# 请根据索引输出“Kelly”
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# print(li[2][1][1])

# 使用索引找到‘all’元素并将其修改为“all”
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# li[2][2] = 'ALL'
# print(li)

# 5、 写代码，有如下元组，请按照功能要求实现每一个功能

# 计算元组长度并输出
# tu = ('alex', 'eric', 'rain')
# print(len(tu))

# 获取元组的第2个元素，并输出
# tu = ('alex', 'eric', 'rain')
# print(tu[1])
#
# # 获取元组的第1-2个元素，并输出
# print(tu[0:2])
#
# # 请使用for输出元组的元素
# for item in tu:
#     print(item)
#
# # 请使用for、len、range输出列表的索引
# for index in range(len(tu)):
#     print(index)
#
# # 请使用enumrate输出列表元素和序号（序号从10开始）
# for index, item in enumerate(tu, 10):
#     print(index, item)

# 6、有如下变量，请实现要求的功能
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

# 讲述元组的特性
# 1. 元组不可变  2.元组本身不可变，如果元组中还包含其他科变元素，这些可变元素可以改变
# 功能：index， count， 切片

# 请在k2中添加元素“Seven”
# print(tu[1][2]['k2'].append('Seven') )
# print(tu)

# print(tu[1][2]['k3'].append('Seven'))
# print(tu)

# 7、 字典
dic =  {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 请循环输出所有的key
# for index in dic.keys():
#     print(index)

# 请循环输出所有的value
# for item in dic.values():
#     print(item)

# 请循环输出所有的key和value
# for index, item in enumerate(dic, 0):
#     print('%s. %s' % (index, item))

# 请在字典中添加一个键值对，“K4”：“V4”，输出添加后的字典
# dic['k4'] = 'V4'
# print(dic)

# 修改字典中“k1”对应的值为“Alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)

# 请在k3对应的值中追加一个元素44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)

# 请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)

# 8、转换
# 将字符串s="Alex"转换成列表
# s = "alex"
#
# print(s.split())     # split:字符串转换成列表

# 将字符串s="alex"转换成元组
# s = 'Alex'
# print(tuple(eval("(s)")))
# # 将列表li = ["alex","seven"]转成元组
# li = ["alex","seven"]
# print(tuple(li))
# 将元组tu=（'alex','seven')转换成列表
# tu=('alex','seven')
# print(list(tu))

# 将列表li=['alex','seven']转成字典且字典的key按照10开始向后递增
li=['alex','seven']
li_dict = {}
for index, item in enumerate(li,10):
    li_dict[index] = item.strip()
print(li_dict)
