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

# 10，说一下__new__和__init__的区别
# 根据官方文档：
# __init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
# __new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
# 也就是，__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
# 　　 在python2.x中，从object继承得来的类称为新式类（如class
# A(object)）不从object继承得来的类称为经典类（如class
# A()
# 新式类跟经典类的差别主要是以下几点:
# 　　1.
# 新式类对象可以直接通过__class__属性获取自身类型: type
# 　　2.
# 继承搜索的顺序发生了改变, 经典类多继承时属性搜索顺序: 先深入继承树左侧，再返回，开始找右侧（即深度优先搜索）;新式类多继承属性搜索顺序: 先水平搜索，然后再向上移动
# 例子：
# 经典类: 搜索顺序是(D, B, A, C)
# >> >
#
# class A: attr = 1
#
#
# ...
# >> >
#
# class B(A): pass
#
#
# ...
# >> >
#
# class C(A): attr = 2
#
#
# ...
# >> >
#
# class D(B, C): pass
#
#
# ...
# >> > x = D()
# >> > x.attr
# 1
#
# 新式类继承搜索程序是宽度优先
# 新式类：搜索顺序是(D, B, C, A)
# >> >
#
# class A(object): attr = 1
#
#
# ...
# >> >
#
# class B(A): pass
#
#
# ...
# >> >
#
# class C(A): attr = 2
#
#
# ...
# >> >
#
# class D(B, C): pass
#
#
# ...
# >> > x = D()
# >> > x.attr
# 2
#
# 　　3.
# 新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中。
# 　　4.
# 新式类增加了__getattribute__方法
# 　　5.
# 新式类内置有__new__方法而经典类没有__new__方法而只有__init__方法
# 注意：Python
# 2.
# x中默认都是经典类，只有显式继承了object才是新式类
# 　　   而Python
# 3.
# x中默认都是新式类（也即object类默认是所有类的祖先），不必显式的继承object（可以按照经典类的定义方式写一个经典类并分别在python2.x和3.x版本中使用dir函数检验下。
# 例如：
#
# class A()：
#
# 　　　　　　pass
#
# 　　　 print(dir(A))
#
# 　　
# 会发现在2.x下没有__new__方法而3.x下有。
# 接下来说下__new__方法和__init__的区别：
# 在python中创建类的一个实例时，如果该类具有__new__方法，会先调用__new__方法，__new__方法接受当前正在实例化的类作为第一个参数（这个参数的类型是type，这个类型在c和python的交互编程中具有重要的角色，感兴趣的可以搜下相关的资料），其返回值是本次创建产生的实例，也就是我们熟知的__init__方法中的第一个参数self。那么就会有一个问题，这个实例怎么得到？
# 注意到有__new__方法的都是object类的后代，因此如果我们自己想要改写__new__方法（注意不改写时在创建实例的时候使用的是父类的__new__方法，如果父类没有则继续上溯）可以通过调用object的__new__方法类得到这个实例（这实际上也和python中的默认机制基本一致），如：
#
# class display(object):
#     def __init__(self, *args, **kwargs):
#         print("init")
#
#     def __new__(cls, *args, **kwargs):
#         print("new")
#         print(type(cls))
#         return object.__new__(cls, *args, **kwargs)
#
#
# a = display()
#
# 　　运行上述代码会得到如下输出：
# new
#
# <
#
# class 'type'>
#
#
# init
#
# 　　
# 因此我们可以得到如下结论：
# 在实例创建过程中__new__方法先于__init__方法被调用，它的第一个参数类型为type。
# 如果不需要其它特殊的处理，可以使用object的__new__方法来得到创建的实例（也即self)。
# 于是我们可以发现，实际上可以使用其它类的__new__方法类得到这个实例，只要那个类或其父类或祖先有__new__方法。
#
# class another(object):
#     def __new__(cls, *args, **kwargs):
#         print("newano")
#         return object.__new__(cls, *args, **kwargs)
#
#
# class display(object):
#     def __init__(self, *args, **kwargs):
#         print("init")
#
#     def __new__(cls, *args, **kwargs):
#         print("newdis")
#         print(type(cls))
#         return another.__new__(cls, *args, **kwargs)
#
#
# a = display()
#
# 　　上面的输出是：
# newdis
# <
#
# class 'type'>
#
#
# newano
# init
#
# 　　所有我们发现__new__和__init__就像这么一个关系，__init__提供生产的原料self(
#     但并不保证这个原料来源正宗，像上面那样它用的是另一个不相关的类的__new__方法类得到这个实例)，而__init__就用__new__给的原料来完善这个对象（尽管它不知道这些原料是不是正宗的）


# 15，简述静态方法和类方法
# 1：绑定方法（绑定给谁，谁来调用就自动将它本身当作第一个参数传入）：
# 　　绑定方法分为绑定到类的方法和绑定到对象的方法，具体如下：
# 1.
# 绑定到类的方法：用classmethod装饰器装饰的方法。
# 为类量身定制
# 类.boud_method(), 自动将类当作第一个参数传入
# （其实对象也可调用，但仍将类当作第一个参数传入）
#
# 2.
# 绑定到对象的方法：没有被任何装饰器装饰的方法。
# 为对象量身定制
# 对象.boud_method(), 自动将对象当作第一个参数传入
# （属于类的函数，类可以调用，但是必须按照函数的规则来，没有自动传值那么一说）
#
# 2：非绑定方法：用staticmethod装饰器装饰的方法
# 1.
# 不与类或对象绑定，类和对象都可以调用，但是没有自动传值那么一说。就是一个普通工具而已
# 　　　　注意：与绑定到对象方法区分开，在类中直接定义的函数，没有被任何装饰器
# 装饰的，都是绑定到对象的方法，可不是普通函数，对象调用该方法会自动传值，而
# staticmethod装饰的方法，不管谁来调用，都没有自动传值一说
#
# 　　具体见：http: // www.cnblogs.com / wj - 1314 / p / 8675548.
# html
# 3，类方法与静态方法说明
# 　　1：self表示为类型为类的object，而cls表示为类也就是class
# 　　2：在定义普通方法的时候，需要的是参数self, 也就是把类的实例作为参数传递给方法，如果不写self的时候，会发现报错TypeError错误，表示传递的参数多了，其实也就是调用方法的时候，将实例作为参数传递了，在使用普通方法的时候，使用的是实例来调用方法，不能使用类来调用方法，没有实例，那么方法将无法调用。
# 　　3：在定义静态方法的时候，和模块中的方法没有什么不同，最大的不同就是在于静态方法在类的命名空间之间，而且在声明静态方法的时候，使用的标记为 @ staticmethod，表示为静态方法，在叼你用静态方法的时候，可以使用类名或者是实例名来进行调用，一般使用类名来调用
# 　　4：静态方法主要是用来放一些方法的，方法的逻辑属于类，但是有何类本身没有什么交互，从而形成了静态方法，主要是让静态方法放在此类的名称空间之内，从而能够更加有组织性。
# 　　5：在定义类方法的时候，传递的参数为cls.表示为类，此写法也可以变，但是一般写为cls。类的方法调用可以使用类，也可以使用实例，一般情况使用的是类。
# 　　6：在重载调用父类方法的时候，最好是使用super来进行调用父类的方法。静态方法主要用来存放逻辑性的代码，基本在静态方法中，不会涉及到类的方法和类的参数。类方法是在传递参数的时候，传递的是类的参数，参数是必须在cls中进行隐身穿
# 　　7：python中实现静态方法和类方法都是依赖python的修饰器来实现的。静态方法是staticmethod，类方法是classmethod。