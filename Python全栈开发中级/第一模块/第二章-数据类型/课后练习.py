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
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
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
# li=['alex','seven']
# li_dict = {}
# for index, item in enumerate(li,10):
#     li_dict[index] = item.strip()
# print(li_dict)

# 9、元素分类
# 有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，
# 将小于66的值保存至第二个key的值中。
# 即{'k1':大于66的所有值，'k2':小于66的所有值}
# new_dic = {'k1': [], 'k2': []}
# line = [11,22,33,44,55,66,77,88,99,90]
# for item in line:
#     if item > 66:
#         new_dic['k1'].append(item)
#     elif item < 66:
#         new_dic['k2'].append(item)
# print(new_dic)

# 10、输出商品列表，用户输入序号，显示用户选中的商品
# 商品li=["手机","电脑","鼠标垫","游艇"]
# 允许用户添加商品
# 用户输入序号显示内容

# li = ["手机", "电脑", "鼠标垫", "游艇"]
# print('开始添加商品:'.center(20, '-'))
# li.append('美女')
# print('新商品列表为:', li)
# for index in range(len(li)):
#     print('%s. %s' % (index, li[index]))
# print(len(li))
#
# choice = input('请输入商品编号:').strip()
# if choice.isdigit():
#     choice = int(choice)
#     if 0 <= choice < len(li):
#
#         print('显示的商品为:%s' % (li[choice]))
#     elif choice >= len(li):
#         print('输入的商品编号不存在!')
#     else:
#         print('商品编号只能为整数!')

# 13、有两个列表
# l1 = [11,22,33]
# l2 = [22,33,44]
# 获取内容相同的元素列表
# 获取l1中有，l2中没有的元素
# 获取l1和l2中内容都不同的元素
# l1 = [11, 22, 33]
# l2 = [22, 33, 44]
# l3 = []
# l4 = []
# l5 = []
# l6 = {22, 33, 44}
# for item in l1:
#     if item in l2:
#         # print(item)
#         l3.append(item)
#     elif item not in l2:
#         l4.append(item)
#     else:
#         l5.append(item)
# print(l3)
# print(l4)
# print(l5)


# print('%s' % l3.append(22))
# 14、利用for循环和range输出：
# for循环从到小输出1-100

# for item in range(101):
#     if item > 0:
#         print(item)

# 利用for循环和range输出9*9乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j <= i:
#
#             print('{} * {} = {}'.format(j, i, j*i),end=' ')
#     print()

for i in range(1, 10):
    for j in range(1, i+1):
        d = i * j
        print('%d * %d = %2d' % (j, i, d), end='  ')
    print()


# 功能要求：
# 基础要求：
#
# 1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
#
# 2、允许用户根据商品编号购买商品
#
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#
# 4、可随时退出，退出时，打印已购买商品和余额
#
# 5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
#
#
# 扩展需求：
#
# 1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
#
# 2、允许查询之前的消费记录
#
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
#     {"name": "飞机", "price": 9999}
# ]
#
# user_list = {}
#
# # 定义购物车
# shopping_cart = []
#
# f = open(file='user_info', mode='r', encoding='utf-8')
# for item in f:
#     u, p = item.split(',')
#     user_list[u] = p.strip()
# print(user_list)
# f.close()
#
# while True:
#     user_name = input("请输入用户名:").strip()
#     pass_word = input("请输入密码:").strip()
#     if user_name in user_list:
#         if pass_word == user_list[user_name]:
#             print('欢迎登录', user_name)
#             break
#         else:
#             print("输入的用户名或密码错误,请重新输入!")
#     else:
#         print('用户名不存在!')
# while True:
#     pay = input('请输入的你的工资:')
#     if pay.isdigit():
#         pay = int(pay)
#         break
#     else:
#         print('工资只能为数字！')
# print("商品列表如下:".center(20, '-'))
# for index, goodname in enumerate(goods):
#     print('%s. %s' %(index, goods[index]))
# exit_flag = False
# while not exit_flag:
#     choice = input('请输入商品编号:').strip()
#     if choice.isdigit():
#         choice = int(choice)
#         if 0 <= choice < len(goods):
#             if pay >= goods[choice]['price']:
#                 shopping_cart.append(goods[choice])
#                 pay = pay - goods[choice]['price']
#                 print('\033[31;1m加入商品 %s 到购物车成功,价格 %s 元,当前余额为 %s 元\033[0m' % (goods[choice]['name'], goods[choice]['price'], pay))
#             else:
#                 print('余额不足')
#
#         elif choice >= len(goods):
#             print('输入的商品编号不存在!')
#         elif choice < 0:
#             print('商品编号只能为正整数!')
#
#     elif choice == 'q':
#         if len(shopping_cart) > 0:
#             print('已经购买商品列表'.center(20, '-'))
#             for index, name in enumerate(shopping_cart,1):
#
#                 print('\033[31;1m你已经购买的商品 %s. %s \033[0m' % (index, name))
#             print('\033[31;1m您所剩余额为:%s 元\033[0m' % pay)
#         exit_flag = True




