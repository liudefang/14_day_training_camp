# -*- encoding: utf-8 -*-
# @Time    : 18-6-26 上午9:37
# @Author  : mike.liu
# @File    : 本章练习.py

# 练习题
# 1、面向对象三大特性，各有什么用处，说说你的理解。
"""
封装(Encapsulation)：在类中对数据的赋值、内部调用对外部用户是透明的，这使类变成了一个胶囊或容器，里面包含着类的数据和方法

继承(Inheritance)：一个类可以派生出子类，在这个父类里定义的属性、方法自动被子类继承

多态(Polymorphism):多态是面向对象的重要特性，简单点说：一种接口，多种实现，指一个基类中派生出不同的子类，且每个子类在继承了同样的方法
名的同时又对父类的方法做了不同的实现，这就是同一种事物表现出的多种形态

"""
# 2、类的属性和对象的属性有什么区别?
"""
类有两种属性：数据属性和函数属性
类的数据属性：是所有对象共享的
类的函数属性：是绑定给对象用的，称为绑定到对象的方法
对象的属性是类的实例化
"""
# 3、面向过程编程与面向对象编程的区别与应用场景?
"""
面向过程：
概念：核心是“过程”二字，“过程”指的是解决问题的步骤，即先干什么再干什么，基于面向过程设计程序就好比在设计一条流水线，是一种机械化的思维方式
优点是：
复杂的问题流程化，进而简单化

缺点是：
扩展性比较差

面向对象：
概念：核心是“对象”二字，

优点是：
可扩展性好

缺点是：
编程的复杂度比较高

应用场景：
需求经常变化的软件中

面向过程：个人视角
面向对象：上帝视角

"""
#4、类和对象在内存中是如何保存的。
# 类的对象的属性：以字典形式保存的

# 5、什么是绑定到对象的方法、绑定到类的方法、解除绑定的函数、如何定义，如何调用，给谁用？有什么特性
"""
①、绑定到对象的方法：没有被任何装饰器装饰的方法
为对象量身定制
对象.boud_method(),自动将对象当作第一个参数传入
(属于类的函数，类可以调用，但是必须按照函数的规则来，没有自动传值那么一说）
由对象来调用，
def tell_info(self):
obj.tell_info()

②、绑定到类的方法：用classmethod 装饰器的方法
由类来调用
def from_conf(cls):
class.from_conf()

③、非绑定方法
不与类和对象绑定，谁都可以调用，
@staticmethod
def create_id():
obj.create_if()/class.create_id()
 
"""
# 6、使用实例进行获取、设置、删除数据, 分别会触发类的什么私有方法


# class A(object):
#     pass
#
#
# a = A()
#
# a["key"] = "val"
# a = a["key"]
# del a["key"]
# python中经典类和新式类的区别
#
# 如下示例, 请用面向对象的形式优化以下代码
#
#
# def exc1(host, port, db, charset, sql):
#     conn = connect(host, port, db, charset)
#     conn.execute(sql)
#     return xxx
#
#
# def exc2(host, port, db, charset, proc_name)
#     conn = connect(host, port, db, charset)
#     conn.call_proc(sql)
#     return xxx
#
#
# # 每次调用都需要重复传入一堆参数
# exc1('127.0.0.1', 3306, 'db1', 'utf8', 'select * from tb1;')
# exc2('127.0.0.1', 3306, 'db1', 'utf8', '存储过程的名字')
# class MySQLHandler:
#     def __init__(self, host, port, db, charset='utf-8'):
#         self.host = host
#         self.port = port
#         self.db = db
#         self.charset = charset
#         self.conn = connect(self.host, self.port, self.db, self.charset)
#     def exc1(self, sql):
#         return self.conn.execute(sql)
#
#     def exc2(self, sql):
#         return self.conn.call_proc(sql)
#
# obj = MySQLHandler('127.0.0.1', 3306, 'db1')
# obj.exc1('select * from tb1;')
# obj.exc2('存储过程的名字')

# 示例1, 现有如下代码， 会输出什么：

# class People(object):
#     __name = "luffy"
#     __age = 18
#
#
# p1 = People()
# print(p1.__dict__)
# # 示例2, 现有如下代码， 会输出什么：
#
# class People(object):
#
#     def __init__(self):
#         print("__init__")
#
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         return object.__new__(cls, *args, **kwargs)
#
#
# People()
# 请简单解释Python中
# staticmethod（静态方法）和
# classmethod（类方法）, 并分别补充代码执行下列方法。
#
# class A(object):
#
#     def foo(self, x):
#         print("executing foo(%s, %s)" % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s, %s)" % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % (x))
#
#
# a = A()
# a.foo(5)
# a.class_foo(6)
# a.static_foo(10)
# 请执行以下代码，解释错误原因，并修正错误。
#
# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def eat(self):
#         print(" %s is eating" % self.name)
#
#
# d = Dog("ChenRonghua")
# d.eat
# 下面这段代码的输出结果将是什么？请解释。
#
class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
#
# # 1 1 1 继承自父类的类属性x，所以都一样，指向同一块内存地址
# # 1 2 1 更改Child1，Child1的x指向了新的内存地址
# # 3 2 3 更改Parent，Parent的x指向了新的内存地址
# 多重继承的执行顺序，请解答以下输出结果是什么？并解释。
#
# class A(object):
#     def __init__(self):
#         print('A')
#         super(A, self).__init__()
#
#
# class B(object):
#     def __init__(self):
#         print('B')
#         super(B, self).__init__()
#
#
# class C(A):
#     def __init__(self):
#         print('C')
#         super(C, self).__init__()
#
#
# class D(A):
#     def __init__(self):
#         print('D')
#         super(D, self).__init__()
#
#
# class E(B, C):
#     def __init__(self):
#         print('E')
#         super(E, self).__init__()
#
#
# class F(C, B, D):
#     def __init__(self):
#         print('F')
#         super(F, self).__init__()
#
#
# class G(D, B):
#     def __init__(self):
#         print('G')
#         super(G, self).__init__()
#
#
# if __name__ == '__main__':
#     g = G()
#     f = F()
#
# # G
# # D
# # A
# # B
# #
# # F
# # C
# # B
# # D
# # A
# 请编写一段符合多态特性的代码.
#
# import abc
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def talk(self):
#         pass
#
# class People(Animal):
#     def talk(self):
#         print('say hello')
# 很多同学都是学会了面向对象的语法，却依然写不出面向对象的程序，原因是什么呢？原因就是因为你还没掌握一门面向对象设计利器，即领域建模，请解释下什么是领域建模，以及如何通过其设计面向对象的程序？http: // www.cnblogs.com / alex3714 / articles / 5188179.
# html
# 此blog最后面有详解
#
# 请写一个小游戏，人狗大站，2 个角色，人和狗，游戏开始后，生成2个人，3条狗，互相混战，人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。注意，请按题14领域建模的方式来设计类。
# class Animal:
#     def __init__(self, name, life_value, gjl):
#         self.name = name
#         self.life_value = life_value
#         self.gjl = gjl
#
#
#
# class People(Animal):
#     def attack(self, enemy):
#         if not isinstance(enemy, People):
#             enemy.life_value -= self.gjl
#             if enemy.life_value <= 0:
#                 print("已经死亡")
#             else:
#                 print("剩下的生命值为:", enemy.life_value)
#             print('人进行攻击')
#         else:
#             print('同类')
#
#
#
# class Dog(Animal):
#     def attack(self, enemy):
#         if not isinstance(enemy, Dog):
#             enemy.life_value -= self.gjl
#             print(self.gjl)
#             if enemy.life_value <= 0:
#                 print("已经死亡")
#             else:
#                 print("剩下的生命值为:", enemy.life_value)
#             print('狗咬人')
#         else:
#             print('同类')
#
#
# p1 = People('tom', 100, 30)
# p2 = People('jack', 100, 50)
#
# d1 = Dog('dog1', 100, 20)
# d2 = Dog('dog2', 100, 30)
#
# d1.attack(d2)
# p1.attack(d2)
# p2.attack(d2)
# p1.attack(d2)
#
# 编写程序, 在元类中控制把自定义类的数据属性都变成大写.
#
class Mymetaclass(type):
    def __new__(cls, name, bases, attrs):
        update_attrs = {}
        for k, v in attrs.items():
            if not callable(v) and not k.startswith('__'):
                update_attrs[k.upper()] = v
            else:
                update_attrs[k] = v
        return type.__new__(cls, name, bases, update_attrs)

class Chinese(metaclass=Mymetaclass):
    country = 'China'
    tag = 'Legend of the Dragon'    # 龙的传人
    def walk(self):
        print('%s is walking' % self.name)

print(Chinese.__dict__)
# 编写程序, 在元类中控制自定义的类无需init方法.
#
# 编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生.
class Student:
    count = 0
    def __init__(self, name, country, age):
        self.name = name
        self.country = country
        self.age = age
        Student.count += 1

s1 = Student('mike', 'china', 18)
s2 = Student('mike1', 'china', 18)
print(Student.count)


# 编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
class B:
    def handle(self):
        pass

class A(B):
    def handle(self):
        super().handle(self)
# 编写程序, 如下有三点要求：
#
#
# 自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
# e.g
# {
#     "egon": {"password": "123", 'status': False, 'timeout': 0},
#     "alex": {"password": "456", 'status': False, 'timeout': 0},
# }
# 定义用户类，定义方法db，例如
# 执行obj.db可以拿到用户数据结构
# 在该类中实现登录、退出方法, 登录成功将状态(status)
# 修改为True, 退出将状态修改为False(退出要判断是否处于登录状态).密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于10秒即不允许登录)
import json
import time
import os

user_dict =  {
    "egon": {"password": "123", 'status': False, 'timeout': 0},
    "alex": {"password": "456", 'status': False, 'timeout': 0},
}

class User:
    def __init__(self):
        if not os.path.isfile('user.json'):
            self.write()

    def db(self):
        with open('user.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    def login(self):
        count = 0
        while count < 3:
            username = input("请输入用户名:").strip()
            passwd = input("请输入密码:").strip()
            user_info = self.db()
            if username in user_info.keys():
                passwd = user_info.get(username).get("passwd")
                time_o = user_info.get(username).get("timeout")
                login_t = time.time()
                print(username, login_t, time_o)
                if login_t - time_o > 10:
                    
# 用面向对象的形式编写一个老师角色, 并实现以下功能, 获取老师列表, 创建老师、删除老师、创建成功之后通过
# pickle
# 序列化保存到文件里，并在下一次重启程序时能
# 读取到创建的老师, 例如程序目录结构如下.
#
# .
# | -- bin /
# | | -- main.py
# 程序运行主体程序(可进行菜单选择等)
# | -- config /
# | | -- settings.py
# 程序配置(例如: 配置存储创建老师的路径相关等)
# | -- db
# 数据存储(持久化, 使得每次再重启程序时, 相关数据对应保留)
# | | -- teachers / 存储所有老师的文件
# | | -- ......
# | -- src / 程序主体模块存放
# | | -- __init__.py
# | | -- teacher.py
# 例如: 实现老师相关功能的文件
# | | -- group.py
# 例如: 实现班级相关的功能的文件
# | -- manage.py
# 程序启动文件
# | -- README.md
# 程序说明文件
# 根据23
# 题, 再编写一个班级类, 实现以下功能, 创建班级, 删除班级, 获取班级列表、创建成功之后通过
# pickle
# 序列化保存到文件里，并在下一次重启程序时能
# 读取到创建的班级.
#
# 根据
# 23
# 题, 编写课程类, 实现以下功能, 创建课程(创建要求如上), 删除课程, 获取课程列表
#
# 根据23
# 题, 编写学校类, 实现以下功能, 创建学校, 删除学校, 获取学校列表
#
# 通过23题, 它们雷同的功能, 是否可以通过继承的方式进行一些优化
#
# 伪代码
#
#
# class Behavior(object):
#
#     def fetch(self, keyword):
#         通过
#         keyword
#         参数
#         查询出对应的数据列表
#
#
# class School(Behavior):
#     pass
#
#
# class Teacher(Behavior):
#     pass
#
#
# s = School()
# t = Teacher()
#
# s.fetch("school")
# t.fetch("teacher")