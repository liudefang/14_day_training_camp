# -*- encoding: utf-8 -*-
# @Time    : 2018-05-04 20:34
# @Author  : mike.liu
# @File    : 闯关答辩.py
#
n1 = 123456
n2 = n1
print(id(n1), id(n2))
#
# gbk，utf8占用字节
# item1 = []
# item = "www.luffycity.com"
# # ['www','luffycity','com']
# item1 = item.split('.')
# print(item1)
#
# li = ['alex','egon','yuan','wusir','666']
#
# # 1.把666替换成999
# li[4] = '999'
# print(li)
#
# # 2.获取"yuan"索引
# index = li.index('yuan')
# print(index)

# 3.假设不知道前面有几个元素，得到最后的三个元素
# print[-3:]

d = {
        "Development":"开发小哥",
        "OP":"运维小哥",
        "Operate":"运营小仙女",
        "UI":"UI小仙女"
    }

# # 1, 增加： name : alex
# d['name'] = 'alex'
# print(d)
# # #    2, 修改： alex  改为 wusir
# d['name'] = 'wusir'
# print(d)
# # #    3, 删除： 删除 name 为 wusir
# # d.popitem('name')
# d.pop('name')
# print(d)
# # #    4, 查询： "UI":"UI小仙女"
# d.get('UI')
print(d['UI'])

# count = 0
# for i in range(101):
#     if i % 2 == 0:
#         count += i
# print(count)

# 2.判断闰年
# year = input('请输入年份:').strip()
# if year.isdigit():
#     year = int(year)
#
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print('%s年是闰年' % year)
#     else:
#         print('%s年是平年' % year)
# else:
#     print('年份只能为整数!')




# 1、先看视频,做客户练习
# 2、做作业
# 3、然后整理成博客
#
# str.
# # 常用的
# str.isdigit()
# str.find()
# str.join()
# str.replace()
# str.count()
# str.strip()
# str.center()
# str.split()
# str.format()
