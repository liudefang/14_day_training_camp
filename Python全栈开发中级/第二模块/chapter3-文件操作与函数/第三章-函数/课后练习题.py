# -*- encoding: utf-8 -*-
# @Time    : 2018-05-19 13:33
# @Author  : mike.liu
# @File    : 课后练习题.py

# 文件处理相关
# 编码问题
#
# 请说明python2 与python3中的默认编码是什么？
# python2是ASCII，python3是utf-8
# 为什么会出现中文乱码？你能列举出现乱码的情况有哪几种？
# 答案
#coding:utf-8 #.py文件是什么编码就需要告诉python用什么编码去读取这个.py文件。
# sys.stdout.encoding，默认就是locale的编码，print会用sys.stdout.encoding去encode()成字节流，交给terminal显示。所以locale需要与terminal一致，才能正确print打印出中文。
# sys.setdefaultencoding(‘utf8’)，用于指定str.encode() str.decode()的默认编码，默认是ascii。
# 以下几种(local 为软件运行时的语言环境):
#  终端为UTF-8，locale为zh_CN.GBK
#  终端为UTF-8，locale为zh_CN.UTF-8
#  终端为GBK，locale为zh_CN.GBK
#  终端为GBK，locale为zh_CN.UTF-8
# 如何进行编码转换？
# 答案
# 字符串在python内部中是采用unicode的编码方式，所以其他语言先decode转换成unicode编码，再encode转换成utf8编码。
# #-*-coding:utf-8-*- 的作用是什么？
#编码声明
# 解释py2 bytes vs py3 bytes的区别
#   Python 2 将 strings 处理为原生的 bytes 类型，而不是 unicode(python2 str == bytes)，

   # Python 3 所有的 strings 均是 unicode 类型(python3 中需要通过 unicode )
   # string -> encode  -> bytes
   #
   # bytes -> decode  -> string
# 文件处理
#
# r和rb的区别是什么？
# r:读
# rb:二进制读
# 解释一下以下三个参数的分别作用
#  open(f_name,'r',encoding="utf-8")
# 函数基础：
# 写函数，计算传入数字参数的和。（动态传参）

# def func_sum(x, y):
#     sum = x + y
#     return sum
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
# file = open("file.txt", 'r', encoding='utf-8')
# file_data = file.readline()
# file_daxie(file_data)

# 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
# def file_s(file):
#     n = 0
#     for i in file:
#         if i == ' ':
#             n += 1
#     print('有%s个空格' %n)
#
# file_s('ab c')
# file_s('[a , b, c]')
# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#
#
# PS:字典中的value只能是字符串或列表
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# def func(i):
#     for k, v in i.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#
#         else:
#             continue
#     return i
#
# print(func(dic))
# 解释闭包的概念
#
# 函数进阶：
# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]

#
# def cards():
#     num = []
#     for i in range(2, 11):
#         num.append(i)
#     num.extend(['J', 'Q', 'K', 'A'])
#     type = ['红心', '草花', '方块', '黑桃']
#     result = []
#     for i in num:
#         for j in type:
#             result.append((j, i))
#     return result
#
#
# print(cards())



# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
#
# 例如:min_max(2,5,7,8,4)
# 返回:{‘max’:8,’min’:2}
#
# def min_max(*args):
#     the_max = args[0]
#     the_min = args[0]
#     for i in args:
#         if i > the_max:
#             the_max = i
#         elif i < the_min:
#             the_min = i
#     return {'max': the_max, 'min': the_min}
#
# print(min_max(2, 4, 6, 48, -16, 999, 486))
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
import math

# print('''
#   请按照如下格式输出：
#       调用函数area(‘圆形’,圆半径) 返回圆的面积
#       调用函数area(‘正方形’,边长) 返回正方形的面积
#       调用函数area(‘长方形’,长，宽) 返回长方形的面积''')
# def area(name, *args):
#     def areas_rectangle(x, y):
#         print('计算长方形的面积:', x*y)
#     def area_square(x):
#         print('计算正方形的面积:', x**2)
#     def area_round(r):
#         print('计算圆形面积:', math.pi*r*r)
#
#     if name == '圆形':
#         return area_round(*args)
#     elif name == '长方形':
#         return areas_rectangle(*args)
#     else:
#         return area_square(*args)

# 写函数，传入一个参数n，返回n的阶乘
#
# 例如:cal(7)
# 计算7*6*5*4*3*2*1
# def cal(n):
#     res = 1
#     for i in range(n, 0, -1):
#         res = res * i
#     #print(res)
#     return res
# print(cal(7))
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
# user_status = False
#
# def login(func):
#     def inner():
#         file = "user_file.txt"
#         f = open(file, 'r', encoding='utf-8')
#         data = eval(f.readline())
#         global user_status
#         if user_status == False:
#
#             user_name = input('请输入用户名:').strip()
#             password = input('请输入密码:').strip()
#             if user_name == data['name']:
#                 if password == data['password']:
#                     print('欢迎登录成功, %s' % user_name)
#                     user_status = True
#
#
#                 else:
#                     print('用户名或密码错误,请重新输入!')
#             else:
#                 print('用户名不存在')
#         if user_status == True:
#             return func()
#     return inner
#
# @login
# def home():
#     print('登录到用户首页!')
# @login
# def info():
#     print('登录到用户个人信息页面!')

#
# home()
# info()

# 生成器和迭代器
# 生成器和迭代器的区别？
# 答案
# 对于list、string、tuple、dict等这些容器对象,使用for循环遍历是很方便的。
# 在后台for语句对容器对象调用iter()函数。iter()是python内置函数。
# iter()函数会返回一个定义了 next()方法的迭代器对象，它在容器中逐个访问容器内的
# 元素。next()也是python内置函数。在没有后续元素时，next()会抛出
# 一个StopIteration异常，通知for语句循环结束。
# 迭代器是用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用next()函数的
# 时候，迭代器会向我们返回它所记录位置的下一个位置的数据。实际上，在使用next()函数
# 的时候，调用的就是迭代器对象的_next_方法（Python3中是对象的_next_方法，
# Python2中是对象的next()方法）。所以，我们要想构造一个迭代器，
# 就要实现它的_next_方法。但这还不够，python要求迭代器本身也是可迭代的，
# 所以我们还要为迭代器实现_iter_方法，而_iter_方法要返回一个迭代器，
# 迭代器自身正是一个迭代器，所以迭代器的_iter_方法返回自身self即可。
# 生成器有几种方式获取value？
# 答案
# 两种方式获取：
#    for  循环
#    next 获取
# 通过生成器写一个日志调用方法， 支持以下功能
#
# 根据指令向屏幕输出日志
# 根据指令向文件输出日志
# 根据指令同时向文件&屏幕输出日志
# 以上日志格式如下
#
# 2017-10-19 22:07:38 [1] 第九次作业 log db backup 3
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
# def sb(x):
#     return x+'_sb'
#
# res = map(sb, name)
# print(list(res))

# 用filter函数处理数字列表，将列表中所有的偶数筛选出来
#
# def is_odd(n):
#     if n % 2 == 1:
#         return True
#
#
#
# newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(newlist))
# num = [1,3,5,6,7,8]
# def num_list(n):
#     if n % 2 == 0:
#         return True
# new_list = filter(num_list, num)
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
ret = map(lambda d:{d['name']:round(d['shares']* d['price'],2)},portfolio)
print(list(ret))
# 用filter过滤出，单价大于100的股票有哪些
#
# 1、请分别介绍文件操作中不同的打开方式之间的区别：
#
# f = filter(lambda d:d['price']>= 100, portfolio)
# print(list(f))
# 模式	含义
# r
# rb
# r+
# rb+
# w
# wb
# w+
# wb+
# a
# ab
# a+
# ab+
# 2、有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'], 请将以字母“a”开头的元素的首字母改为大写字母；
#
# 3、有如下程序, 请给出两次调用show_num函数的执行结果，并说明为什么：
#
#    num = 20
#
#    def show_num(x=num):
#        print(x)
#
#    show_num()
#
#    num = 30
#
#    show_num()
# 4、有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'], 请以列表中每个元素的第二个字母倒序排序；
#
# 5、有名为poetry.txt的文件，其内容如下，请删除第三行；
#
#    昔人已乘黄鹤去，此地空余黄鹤楼。
#
#    黄鹤一去不复返，白云千载空悠悠。
#
#    晴川历历汉阳树，芳草萋萋鹦鹉洲。
#
#    日暮乡关何处是？烟波江上使人愁。
# 6、有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在"alex", 如果没有，则将字符串"alex"添加到该文件末尾，否则提示用户该用户已存在；
#
#    pizza
#    alex
#    egon
# 7、有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行；
#
#    pizza,100001
#    alex, 100002
#    egon, 100003
# 8、有名为user_info.txt的文件，其内容格式如下，写一个程序，将id为100002的用户名修改为alex li；
#
#    pizza,100001
#    alex, 100002
#    egon, 100003
# 9、写一个计算每个程序执行时间的装饰器；
#
# 10、lambda是什么？请说说你曾在什么场景下使用lambda？
#
# 11、题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。
#
# 要求：三个骰子，摇大小，每次打印摇骰子数。