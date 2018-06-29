# -*- encoding: utf-8 -*-
# @Time    : 2018-06-12 22:12
# @Author  : mike.liu
# @File    : 9 封装.py

# 首先说一下隐藏，在python中用双下划线开头的方式将属性隐藏起来（即设置成私有属性）
# 其实这仅仅这是一种变形操作
# 类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：

class A:
    __N = 0     # 类的数据属性就应该是共享的，但是语法上是可以把类的数据属性设置成私有的如__N,会变形为
    def __init__(self):
        self.__X = 10     # 变形为self._A__X
    def __foo(self):    # 变形为_A__foo
        print('from A')
    def bar(self):
        self.__foo()    # 只有在类内部才可以通过__foo的形式访问到

# A._A__N是可以访问到的，即这种操作并不是严格意义上的限制外部访问，仅仅是一种语法意义上的变形



# 3、在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
# 正常情况
# class A:
#     def fa(self):
#         print("from A")
#
#     def test(self):
#         self.fa()
#
# class B(A):
#     def fa(self):
#         print("from B")
#
# b = B()
# print(b.test())

# 把fa定义成私有的，即__fa
# class A:
#     def __fa(self):     # 在定义时就变成为__A__fa
#         print("from A")
#
#     def test(self):
#         self.__fa()     # 只会与自己所在的类为准，即调用__A__fa
#
# class B(A):
#     def __fa(self):
#         print("from B")
#
# b = B()
# print(b.test())

# 封装不是单纯意义的隐藏
# 1.封装数据
# class Teacher:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def tell_info(self):
#         print("姓名:%s, 年龄:%s" % (self.__name, self.__age))
#
#     def set_info(self, name, age):
#         if not isinstance(name, str):
#             raise TypeError("姓名必须是字符串类型")
#         if not isinstance(age, int):
#             raise TypeError("年龄必须是整型")
#
#         self.__name = name
#         self.__age = age
# #
# class B(A):
#     def fa(self):
#         print("from B")
#
# b = B()
# print(b.test())
# t = Teacher('egon', 18)
# t.tell_info()
#
# t.set_info('egon', 19)
# t.tell_info()

# 2、 封装方法，目的是隔离复杂度
# class ATM:
#     def __card(self):
#         print("插卡")
#
#     def __auth(self):
#         print("用户认证")
#
#     def __input(self):
#         print("输入数据")
#
#     def __print(self):
#         print('打牌账单')
#
#     def __take_money(self):
#         print("取款")
#
#     def __print_bill(self):
#         print("打印账单")
#
#     def withdraw(self):
#         self.__card()
#         self.__auth()
#         self.__input()
#         self.__print_bill()
#         self.__take_money()
#
# a = ATM()
# a.withdraw()
    # def withdraw(self):
    #     self.__class A:
    # def fa(self):
    #     print("from A")
    #
    # def test(self):
    #     self.fa()

# property 特性
# property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height**2)
#
# p1 = People('egon', 75, 1.85)
# print(p1.bmi)
#
# # 圆的周长和面积
# import math
# class Circle:
#     def __init__(self, radius): # 圆的半径radius
#         self.radius = radius
#
#     @property
#     def area(self):
#         return math.pi * self.radius**2     # 计算面积
#
#     @property
#     def perimter(self):
#         return 2 * math.pi * self.radius  # 计算周长
#
# c = Circle(10)
# print(c.radius)
# print(c.area)   # 可以向访问数据属性一样去访问area，会触发一个函数的执行，动态计算出一个值
# print(c.perimter)

# class Foo:
#     def __init__(self, val):
#         self.__NAME = val   # 将所有的数据属性都隐藏起来
#
#     @property
#     def name(self):
#         return self.__NAME  # obj.name访问的是self.__NAME(者也是真实的存放位置）
#
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):  # 在设定值之前进行类型检查
#             raise TypeError("%s must be str" % value)
#         self.__NAME = value     # 通过类型检查后，将值value存放到真实的位置self.__name
#
#     @name.deleter
#     def name(self):
#         raise TypeError("Can not delete")
#
# f = Foo('egon')
# print(f.name)
# del f.name


# 封装与扩展性
# 类的设计者
# class Room:
#     def __init__(self, name, owner, width, length, high):
#         self.name = name
#         self.owner = owner
#         self.__width = width
#         self.__length = length
#         self.__high = high
#
#     def tell_area(self):    # 对外提供的接口，隐藏内部的实现细节，此时我们想求的是面积
#         return self.__width * self.__length
#
# # 使用者
# r1 = Room('卧室', 'egon', 20, 20, 20)
# print(r1.tell_area())      # 使用者调用接口tell_area


# 类的设计者，轻松的扩展了功能，而类的使用者完全不需要改变自己的代码
# class Room:
#     def __init__(self, name, owner, width, length, high):
#         self.name = name
#         self.owner = owner
#         self.__width = width
#         self.__length = length
#         self.__high = high
#
#     def tell_area(self):      # 对外提供的接口，隐藏内部实现，此时我们想求的是体积，内部逻辑变了，只需求修改下列一行就可以很简单
#         return self.__width * self.__length * self.__high   # 的实现，而且外部调用感知不到，任然使用该方法，但是功能已经变了
#
# r1 = Room('卧室', 'egon', 20, 20, 20)
# print(r1.tell_area())
