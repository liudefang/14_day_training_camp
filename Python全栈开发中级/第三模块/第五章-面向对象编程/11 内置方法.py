# -*- encoding: utf-8 -*-
# @Time    : 2018-06-14 22:29
# @Author  : mike.liu
# @File    : 11 内置方法.py

# 反射
# python面向对象中的反射：通过字符串的形式操作对象相关的属性，python中的一切事物皆对象
# 四个实现自身的函数
# hasattr(object, name)   # 判断object中有没有一个name字符串对应的方法和属性
# getattr(object, name, default=None)
# def getattr(object, name, default=None):
#     pass
# def setattr(x, y, v):
#     pass
#
# def delattr(x, y):
#     pass
#
# # 四个方法的使用演示
# class BlackMedium:
#     feature = 'Ugly'
#     def __init__(self, name, addr):
#         self.name = name
#         self.addr = addr
#
#     def sell_house(self):
#         print("%s黑中介卖房子啦,傻逼才买呢,但是谁能证明自己不傻逼" % self.name)
#
#     def rent_house(self):
#         print('%s 黑中介租房子啦,傻逼才租呢' %self.name)
# b1 = BlackMedium('万成置地', '回龙观天露园')
#
# # 检测是否含有某属性
# print(hasattr(b1, 'name'))
# print(hasattr(b1, 'sell_house'))
#
# # 获取属性
# n = getattr(b1, 'name')
# print(n)
# # func = getattr(b1, 'rent_house')
# # func()
#
# print(getattr(b1, 'aaaa','b不存在啊'))
#
# # 设置属性
# setattr(b1, 'sb', True)
# setattr(b1, 'show_name', lambda self:self.name + 'sb')
# print(b1.__dict__)
# # print(b1.show_name(b1))
#
# # 删除属性
# delattr(b1, 'addr')
# delattr(b1, 'show_name')
# delattr(b1, 'show_name111')     # 不存在，则报错
# print(b1.__dict__)

# 类也是对象
# class Foo(object):
#
#     staticField = "old boy"
#
#     def __init__(self):
#         self.name = 'wupeiqi'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
# print(getattr(Foo, 'staticField'))
# print(getattr(Foo, 'func'))
# print(getattr(Foo, 'bar'))

# 反射当前模块成员
# import sys
# def s1():
#     print('s1')
#
# def s2():
#     print('s2')
#
# this_module = sys.modules[__name__]
# hasattr(this_module, 's1')
# getattr(this_module, 's2')
#
# # 3 为什么用反射之反射的好处
# # 好处一：实现可插拔机制
#
# # egon还没有实现的全部功能
# class FtpClient:
#     '''ftp客户端，但是还没有实现具体的功能'''
#     def __init__(self, addr):
#         print('正在连接服务器[%s]' % addr)
#         self.addr = addr
#
# # 不影响lili的代码编写
# f1 = FtpClient('127.0.0.1')
# if hasattr(f1, 'get'):
#     func_get = getattr(f1, 'get')
#     func_get()
#
# else:
#     print('---->不存在此方法')
#     print('处理其它的逻辑')

# 好处二：动态导入模块（基于反射当前模块成员）

# 三 __setattr__,__delattr__,__getattr__
# 三者的用法演示
# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __getattr__(self, item):
#         print('---->form getattr:你找的属性不存在')
#
#     def __setattr__(self, key, value):
#         print('----> from setattr')
#         self.__dict__[key] = value  # 应该使用它
#
#     def __delattr__(self, item):
#         print('----> from delattr')
#         self.__dict__.pop(item)
#
# # __setattr__添加/修改属性会触发它的执行
# f1 = Foo(10)
# print(f1.__dict__)  # 因为你重写了__setattr__，凡是赋值操作都会触发它的运行，你啥都没有写，就是根本没有赋值，除非你直接操作属性字典，否则永远无法赋值
# f1.z = 3
# print(f1.__dict__)
#
# # __delattr__ 删除属性的时候会触发
# f1.__dict__['a'] = 3 # 我们可以直接修改属性字典，来完成添加/修改属性的操作
# del f1.a
# print(f1.__dict__)


# 四 二次加工标准类型(包装)
# class List(list):    # 继承list所有的属性，也可以派生出自己新的，比如append和mid
#     def append(self, p_object):
#         '''派生自己的append：加上类型检查'''
#         if not isinstance(p_object, int):
#             raise TypeError('must be int')
#         super().append(p_object)
#
#     @property
#     def mid(self):
#         '新增自己的属性'
#         index = len(self)//2
#         return self[index]
#
# l = List([1, 2, 3, 4])
# print(l)
# l.append(5)
# print(l)
# #l.append('23')
#
# print(l.mid)
# l.insert(0, -123)
# print(l)
# l.clear()
# print(l)

# 练习（clear加权限限制）
# class List(list):
#     def __init__(self, item, tag=False):
#         super().__init__(item)
#         self.tag = tag
#
#     def append(self, p_object):
#         if not isinstance(p_object, str):
#             raise TypeError
#         super().append(p_object)
#
#     def clear(self):
#         if not self.tag:
#             raise PermissionError
#         super().clear()
#
# l = List([1, 2, 3], False)
# print(l)
# print(l.tag)
#
# l.append('saf')
# print(l)
#
# l.clear()   # 异常

# 授权示范一
# import time
# class FileHandle:
#     def __init__(self, filename, mode='r', encoding='utf-8'):
#         self.file = open(filename, mode, encoding= encoding)
#
#     def write(self, line):
#         t = time.strftime('%Y-%m-%d %T')
#         self.file.write('%s %s' % (t, line))
#
#     def __getattr__(self, item):
#         return getattr(self.file, item)
#
# f1 = FileHandle('b.txt', 'w+')
# f1.write('你好啊')
# f1.seek(0)
# print(f1.read())
# f1.close

#  授权示范二
# 加上b模式支持
import time
# class FileHandle:
#     def __init__(self, filename, mode='r', encoding='utf-8'):
#         if 'b' in mode:
#             self.file = open(filename, mode)
#         else:
#             self.file = open(filename, mode, encoding = encoding)
#
#         self.filename = filename
#         self.mode = mode
#         self.encoding = encoding
#
#     def write(self, line):
#         if 'b' in self.mode:
#             if not isinstance(line, bytes):
#                 raise TypeError('must be bytes')
#             self.file.write(line)
#
#     def __getattr__(self, item):
#         return getattr(self.file, item)
#
#     def __str__(self):
#         if 'b' in self.mode:
#             res = "<_io.BufferedReader name='%s'>" % self.filename
#         else:
#             res = "<_io.TextIOWrapper name='%s' mode='%s' encoding='%s'>" %(self.filename, self.mode, self.encoding)
#         return res
#
# f1 = FileHandle('b.txt', 'wb')
# f1.write('你好啊'.encode('utf-8'))
# print(f1)
# f1.close()

# 练习题（授权）
# 练习一
# class List:
#     def __init__(self, seq):
#         self.seq = seq
#
#     def append(self, p_object):
#         '派生自己的append加上类型检查，覆盖原有的append'
#         if not isinstance(p_object, int):
#             raise TypeError('must be int')
#         self.seq.append(p_object)
#
#     @property
#     def mid(self):
#         '新增自己的方法'
#         index = len(self.seq)//2
#         return self.seq[index]
#
#     def __getattr__(self, item):
#         return getattr(self.seq, item)
#
#     def __str__(self):
#         return str(self.seq)
#
# l = List([1, 2, 3])
# print(l)
#
# l.append(4)
# print(l)
#
# l.insert(0, -123)
# print(l)

# 五 __getattribute__
# 回顾__getattr__
# class Foo:
#     def __init__(self, x):
#         self.x = x
#
#     def __getattr__(self, item):
#         print('执行的是我')
#
# f1 = Foo(10)
# print(f1.x)
#
# # getattribute
# class Foo:
#     def __init__(self, x):
#         self.x = x
#
#     def __getattribute__(self, item):
#         print('不管是否存在，我都会执行')
#
# f1 = Foo(10)
# f1.x

# 二者同时出现
# 当__getattribute__与getattr同时存在，只会只会执行__getattribute__,除非__getattribute__在执行过程中抛出AttributeError
# class Foo:
#     def __init__(self, x):
#         self.x = x
#
#     def __getattr__(self, item):
#         print('执行的是我')
#
#     def __getattribute__(self, item):
#         print('不管是否存在，我都会执行')
#         # raise AttributeError('哈哈')
#
# f1 = Foo(10)
# print(f1.x)

# 六 描述符(__get__,__set__,__delete__)
# 定义一个描述符
# class Foo:  # 在Python3中foo是新式类，它实现了三种方法，这个类被称作一个描述符
#     def __get__(self, instance, owner):
#         pass
#
#     def __set__(self, instance, value):
#         pass
#
#     def __delete__(self, instance):
#         pass
#
# # 描述符是干什么的：描述符的作用是用来代理另外一个类的属性的（必须把描述符定义成这个类的类属性，不能定义到构造函数中）
# # 引子：描述符类产生的实例进行属性操作并不会触发三个方法的执行
# class Foo:
#     def __get__(self, instance, owner):
#         print('触发get')
#
#     def __set__(self, instance, value):
#         print('触发set')
#
#     def __delete__(self, instance):
#         print('触发delete')
#
# # 包含这三个方法的新式类称为描述符，由这个类产生的实例进行属性的调用/赋值/删除,并不会触发这三个方法
# f1 = Foo()
# f1.name = 'mike'
# print(f1.name)

# from multiprocessing import Process
# import time
#
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)
#
#
# if __name__ == '__main__':
#     # Process(target=task,kwargs={'name':'子进程1'})
#     p = Process(target=task,args=('子进程1',))
#     p.start()  # 仅仅只是给操作系统发送了一个信号
#
#     print('主')

# 描述符应用之何时?何地?
# 描述符str
# class Str:
#     def __get__(self, instance, owner):
#         print('Str 调用')
#
#     def __set__(self, instance, value):
#         print('Str 设置')
#
#     def __delete__(self, instance):
#         print('Str 删除。。')
#
# class Int:
#     def __get__(self, instance, owner):
#         print('Int 调用')
#
#     def __set__(self, instance, value):
#         print('Int 设置')
#
#     def __delete__(self, instance):
#         print('Int 删除。。')
#
# class People:
#     name = Str()
#     age = Int()
#     def __init__(self, name, age):  # name被str类代理,age被int类代理
#         self.name = name
#         self.age = age
#
# # 何地：定义成另外一个类的类属性
# # 何时：且看下列演示
# p1 = People('mike', 20)
#
# # 描述Str的使用
# # p1.name
# # p1.name = 'egon'
#
# # 描述Int的使用
# p1.age
#
# # 我们来瞅瞅到底发送了什么？
# print(p1.__dict__)
# print(People.__dict__)
# print(type(p1) == People)
# print(type(p1).__dict__ == People.__dict__)


# 3 描述符分两种
# 一 数据描述符:至少实现了__get__()和__set__()
# class Foo:
#     def __set__(self, instance, value):
#         print('set')
#
#     def __get__(self, instance, owner):
#         print('get')
#
# # 二、非数据描述符：没有实现__set__()
# class Foo:
#     def __get__(self, instance, owner):
#         print('get')

# 注意事项：
# 一、描述符本身应该定义成新式类，被代理的类也应该是新式类
# 二、必须把描述符定义成这个类的类属性，不能为定义到构造函数中
# 三、要严格遵循该优先级，优先级由高到低分别是1.类属性 2.数据描述符 3.实例属性 4.非数据描述符 5.找不到的属性触发__getattr__()

# 类属性>数据属性

# 描述符Str
# class Str:
#     def __get__(self, instance, owner):
#         print('str调用')
#
#     def __set__(self, instance, value):
#         print('str设置')
#
#     def __delete__(self, instance):
#         print('str删除')
#
# class People:
#     name = Str()
#     def __init__(self, name, age):  # name被str类代理，age被int类代理
#         self.name = name
#         self.age = age
#
# People.name     # 调用类属性name，本质就是调用描述符str，触发了__get__()
#
# People.name = 'egon'    # 那赋值呢？并没有触发__set__()
# del People.name # 赶紧试试del，也没有触发__delete__()
# # 结论： 描述符对类没有作用
#
# # 原因：描述符在使用时被定义成另外一个类的类属性，因而类属性比二次加工的描述符伪装而来的类属性有更高的优先级
# People.name # 调用类属性name,找不到就去找描述符伪装的类属性name，触发了__get__()
#
# People.name = 'egon'  # 那赋值呢？直接赋值了一个类属性，它拥有更高的优先级，相当于覆盖了描述符，肯定不会触发描述符的__set__()

# 数据描述符> 实例属性

# 描述符str
# class Str:
#     def __get__(self, instance, owner):
#         print('Str调用')
#
#     def __set__(self, instance, value):
#         print('Str设置')
#
#     def __delete__(self, instance):
#         print('Str 删除')
#
# class People:
#     name = Str()
#     def __init__(self, name, age):  # name 被str类代理
#         self.name = name
#         self.age = age
#
# p1 = People('mike', 20)
#
# # 如果描述符是一个数据描述符（即有__get__ 又有__set__),那么p1.name的调用与赋值都是触发描述符的操作，于p1本身无关了，相当于覆盖了实例的属性
#
# p1.name = 'egonnnnn'
# p1.name
# # 实例的属性字典中没有name，因为name是一个数据描述符，优先级高于实例属性，查看/赋值/删除都是跟描述符有关系，与实例无关了
# print(p1.__dict__)

# 实例属性>非数据描述符
# class Foo:
#     def func(self):
#         print('我胡汉三又回来了')
#
# f1 = Foo()
# f1.func()   # 调用类的方法，也可以说是调用非数据描述符
# # 函数是一个非数据描述符对象（一切皆对象)
# print(dir(Foo.func))
# print(hasattr(Foo.func, '__set__'))
# print(hasattr(Foo.func, '__get__'))
# print(hasattr(Foo.func, '__delete__'))

"""
有人可能会问，描述符不都是类么，函数怎么算也应该是一个对象啊，怎么就是描述符了
描述符是类没有问题，描述符在应用的时候不都是实例化成一个类属性么
函数就是一个由非描述符类实例化得到的对象
没错，字符串也一样
"""

# 再次验证：实例属性>非数据描述符
# class Foo:
#     def __set__(self, instance, value):
#         print('set')
#
#     def __get__(self, instance, owner):
#         print('get')
#
# class Room:
#     name = Foo()
#     def __init__(self, name, width, length):
#         self.name = name
#         self.width = width
#         self.length = length
#
# # name 是一个数据描述符，因为name=Foo()而Foo是实现了get和set方法，因而比实例属性有更高的优先级
# # 对实例的属性操作，触发都是描述符的
# r1 = Room('厕所', 1, 1)
# r1.name
# r1.name = '厨房'

# class Foo:
#
#
#     def __get__(self, instance, owner):
#         print('get')
#
# class Room:
#     name = Foo()
#     def __init__(self, name, width, length):
#         self.name = name
#         self.width = width
#         self.length = length
#
# # name 是一个非数据描述符，因为name=Foo()而Foo没有实现get方法，因而比实例属性有更低的优先级
# # 对实例的属性操作，触发都是描述符的
# r1 = Room('厕所', 1, 1)
# r1.name
# r1.name = '厨房'

# 非数据描述符>找不到
class Foo:
    def func(self):
        print('我胡汉三又回来了')

    def __getattr__(self, item):
        print('找不到了当然是找我啊', item)
f1 = Foo()
f1.item



