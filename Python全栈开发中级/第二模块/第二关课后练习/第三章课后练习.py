# -*- encoding: utf-8 -*-
# @Time    : 2018-05-27 8:44
# @Author  : mike.liu
# @File    : 第三章课后练习.py

# 函数基础：
# 写函数，计算传入数字参数的和。（动态传参）
# def func_sum(x, y):
#     sum = x + y
#     return sum
#
#
# data = func_sum(5,6)
# print(data)


# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
# def file_daxie(file):
#     a = []
#     for i in file:
#         b = i.capitalize()
#         a.append(b)
#     print(a)
#
# file = open("file.txt", "r", encoding='utf-8')
# file_data = file.readline()
# file_daxie(file_data)

# 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
from math import pi

# file = input("请输入内容:").strip()
# def file_s(file):
#     n = 0
#     for i in file:
#         if i == ' ':
#             n += 1
#     print("有%s个空格" % n)
# file_s(file)

# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
# 解释闭包的概念
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# def func_dic(i):
#     for k,v in i.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#         else:
#             continue
#     return i

# print(func_dic(dic))

# 函数进阶：
# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
# def func_pk():
#     num = []
#     for i in range(2, 11):
#         num.append(i)
#     num.extend(['J', 'Q', 'K', 'A'])
#     type = ['黑桃', '红心', '草花', '方块']
#     result = []
#     for i in num:
#         for j in type:
#             result.append((j, i))
#     return result
#
# print(func_pk())

# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
#
# 例如:min_max(2,5,7,8,4)
# 返回:{‘max’:8,’min’:2}
# def func(*args):
#     the_max = args[0]
#     the_min = args[0]
#
#
#     for i in args:
#         if i > the_max:
#             the_max = i
#         elif i < the_min:
#             the_min = i
#     return {'max': the_max, 'min': the_min}
#
# print(func(2,5,7,8,4))

# 写函数，专门计算图形的面积
#
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’,圆半径) 返回圆的面积
# 调用函数area(‘正方形’,边长) 返回正方形的面积
# 调用函数area(‘长方形’,长，宽) 返回长方形的面积
# def area():
#     def 计算长方形面积():
#         pass
#
#     def 计算正方形面积():
#         pass
#
#     def 计算圆形面积():
#         pass
# def area(name, *args):
#     def area_changfx(x, y):
#         return x * y
#
#     def area_zhengfx(x):
#         return x**2
#     def area_yx(r):
#         return pi * r**2
#
#     if name == '长方形':
#         return area_changfx(*args)
#     elif name == '正方形':
#         return area_zhengfx(*args)
#     elif name == '圆形':
#         return area_yx(*args)
#
# print(area('长方形', 4, 5))
# print(area('正方形', 6))
# print(area('圆形', 8))

# 写函数，传入一个参数n，返回n的阶乘
#
# 例如:cal(7)
# 计算7*6*5*4*3*2*1
def func(n):
    res = 1
    for i in range(n, 0, -1):
        res = res * i
    return res
print(func(7))


# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
#
# status_use = False
#
# def login(func):
#
#     def inner():
#         file = 'user_file.txt'
#         f = open(file, 'r', encoding='utf-8')
#         data_file = eval(f.readline())
#
#         global status_use
#         if status_use == False:
#             usernam = input('请输入用户名:').strip()
#             password = input('请输入密码:').strip()
#             if usernam in data_file['name']:
#                 if password == data_file['password']:
#                     print('欢迎登录,%s' % usernam)
#                     status_use = True
#
#                 else:
#                     print('用户名或密码错误')
#             else:
#                 print('用户名不存在!')
#         if status_use == True:
#             return func()
#     return inner
#
#
# @login
# def login_home():
#     print('欢迎登录到首页')
# @login
# def login_info():
#     print('欢迎登录到个人信息页面')

# login_home()
# login_info()

# 生成器和迭代器
# 生成器和迭代器的区别？
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# 生成器有几种方式获取value？
# 通过生成器写一个日志调用方法， 支持以下功能
#
# 根据指令向屏幕输出日志
# 根据指令向文件输出日志
# 根据指令同时向文件&屏幕输出日志
# 以上日志格式如下
#
# 2017-10-19 22:07:38 [1] test log db backup 3
# 2017-10-19 22:07:40 [2]    user alex login success
# #注意：其中[1],[2]是指自日志方法第几次调用，每调用一次输出一条日志
# 代码结构如下
#
#  def logger(filename,channel='file'):
#     """
#     日志方法
#     :param filename: log filename
#     :param channel: 输出的目的地，屏幕(terminal)，文件(file)，屏幕+文件(both)
#     :return:
#     """
#     ...your code...
#
#  #调用
#  log_obj = logger(filename="web.log",channel='both')
#  log_obj.__next__()
#  log_obj.send('user alex login success')


# 内置函数
# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
#
# name=['alex','wupeiqi','yuanhao','nezha']
# name=['alex','wupeiqi','yuanhao','nezha']
# def sb(x):
#     return x + '_sb'
#
# res = map(sb, name)
# print(list(res))
# 用filter函数处理数字列表，将列表中所有的偶数筛选出来
#
# num = [1,3,5,6,7,8]
# def oushu(n):
#     if n % 2 == 0:
#         return True
#
# new_list = filter(oushu, num)
# print(list(new_list))
# 如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
#
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 计算购买每支股票的总价
# ret = map(lambda d:{d['name']:round(d['shares']*d['price'],2)},portfolio)
# print(list(ret))
# 用filter过滤出，单价大于100的股票有哪些
# f = filter(lambda d:d['price'] >= 100,portfolio)
# print(list(f))
# 2、有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'], 请将以字母“a”开头的元素的首字母改为大写字母；
li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# li_new = []
# for i in li:
#     if i.startswith('a'):
#         li_new.append(i.capitalize())
#     else:
#         li_new.append(i)
#
# print(li_new)
# for i in range(len(li)):
#     if li[i][0] == 'a':
#         li[i]=li[i].capitalize()
#     else:
#         continue
# print(li)
# 3、有如下程序, 请给出两次调用show_num函数的执行结果，并说明为什么：
#
# num = 20
#
# def show_num(x=num):
#    print(x)
#
# show_num()
#
# num = 30
#
# show_num()
# 4、有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'], 请以列表中每个元素的第二个字母倒序排序；
# li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# print(sorted(li, key=lambda x:x[1], reverse = True))
# 5、有名为poetry.txt的文件，其内容如下，请删除第三行；
#
#    昔人已乘黄鹤去，此地空余黄鹤楼。
#
#    黄鹤一去不复返，白云千载空悠悠。
#
#    晴川历历汉阳树，芳草萋萋鹦鹉洲。
#
#    日暮乡关何处是？烟波江上使人愁。
import os
# p = "poetry.txt"
# file = open(p, 'r', encoding= 'utf-8')
#
# print(file)
# pnew = "%s.new" % p
# filenew = open(pnew, 'w', encoding='utf-8')
# str1 = "晴川历历汉阳树，芳草萋萋鹦鹉洲。"
# for i in file:
#     if str1 in i:
#         i = ''
#         filenew.write(i)
#     else:
#         filenew.write(i)
# file.close()
# filenew.close()
# os.replace(pnew, p)
# f1 = open("poetry.txt", 'r', encoding= 'utf-8')
# str1 = "晴川历历汉阳树，芳草萋萋鹦鹉洲。"
# with open("poetry1.txt", 'w', encoding= 'utf-8') as f2:
#     ff1 = "poetry.txt"
#     ff2 = "poetry1.txt"
#     for i in f1:
#         if str1 in i:
#             i = ''
#             f2.write(i)
#         else:
#             f2.write(i)
# f1.close()
# f2.close()
# os.replace(ff2, ff1)

# 6、有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在"alex", 如果没有，则将字符串"alex"添加到该文件末尾，否则提示用户该用户已存在；
#
#    pizza
# #    alex
# #    egon
# username = 'alexs'
# with open("username.txt", "r+", encoding="utf-8") as file:
#     i = file.read()
#     if username in i:
#         print('用户名%s已经存在' % username)
#
#     else:
#         file.write("\n%s" % username)
# file.close()


# 7、有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行；
#
#    pizza,100001
#    alex, 100002
#    egon, 100003
# a = "user_info.txt"
# b = "user_info1.txt"
# with open(a, "r", encoding="utf-8") as file:
#     with open(b, "w", encoding="utf-8") as file1:
#         for i in file:
#
#             if "100003" in i:
#                 pass
#             else:
#                 file1.write(i)
# file.close()
# file1.close()
# os.replace(b, a)
# 8、有名为user_info.txt的文件，其内容格式如下，写一个程序，将id为100002的用户名修改为alex li；
#
#    pizza,100001
#    alex, 100002
#    egon, 100003
# file = "user_info.txt"
# old_str = "100002"
# new_str = "alex li, 100002"
# file_data = ''
# with open(file, "r", encoding="utf-8") as f1:
#     for i in f1:
#         if old_str in i:
#             i = new_str
#         file_data += i
#         with open(file, "w", encoding="utf-8") as f1:
#             f1.write(file_data)
#             f1.close()



# 9、写一个计算每个程序执行时间的装饰器；
# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args)
#         stop_time = time.time()
#         print(stop_time-start_time)
#     return  wrapper
#
# @timer
# def syahi():
#     print("hello word")
#
# syahi()
#
# 10、lambda是什么？请说说你曾在什么场景下使用lambda？
# lambda 函数就是可以接受任意多个参数（包括可选参数）并且返回单个表达式值的函数
# 好处：
# 1、lambda函数笔记轻便，即用即扔，适合完成只在一处使用的简单功能
# 2、匿名函数，一般用来给filter，map这样的函数式编程服务
# 3、作为回调函数，传递给某些应用，比如消息处理
# 11、题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。
#
# 要求：三个骰子，摇大小，每次打印摇骰子数。
import random

def roll_dice(numbers = 3,points=None):
    """
    定义骰子，循环三次
    :param numbers:
    :param points:
    :return:
    """
    print('摇骰子'.center(20, '-'))
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers -= 1
    return points

def roll_result(total):
    """
    定义大小，三个大或者一个小两个大，三个小或者两个小一个大
    :param total:
    :return:
    """

    is_big = 11 <= total <= 18
    is_small = 3 <= total <= 10
    if is_big:
        return "大"
    elif is_small:
        return "小"

def start_game():
    your_money = 1000
    while your_money > 0:
        print('游戏开始'.center(20, '-'))
        choices = ["大", "小"]
        your_choice = input("请下注，大 or 小:").strip()
        your_bet = input("下注金额:").strip()
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            you_win = your_choice == roll_result(total)
            if you_win:
                your_money = your_money + int(your_bet)
                print("骰子点数", points)
                print("恭喜, 你赢了%s元,你现在的本金%s元" % (your_bet, your_money + int(your_bet)))
            else:
                your_money = your_money - int(your_bet)
                print("骰子点数", points)
                print("很遗憾,你输了%s元,你现在的本金%s元" % (your_bet, your_money - int(your_bet)))
        else:
            print("格式错误，请重新输入！")
    else:
        print("game over")

start_game()