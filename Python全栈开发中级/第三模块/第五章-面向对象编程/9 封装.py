# -*- encoding: utf-8 -*-
# @Time    : 2018-06-12 22:12
# @Author  : mike.liu
# @File    : 9 封装.py

# class A:
#     __N = 0     # 类的数据属性就应该是共享的，但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A_N
#     def __init__(self):
#         self.__X = 10   # 变形为self.__A__X
#
#     def __foo(self):    # 变形为__A__foo
#         print('from A')
#
#     def bar(self):
#         self.__foo()    # 只有在类内部才可以通过__foo的形式访问到
#
# A.__A__N

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
class ATM:
    def __card(self):
        print("插卡")

    def __auth(self):
        print("用户认证")

    def __input(self):
        print("输入数据")

    def __print(self):
        print('打牌账单')

    def __take_money(self):
        print("取款")

    def __print_bill(self):
        print("打印账单")

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a = ATM()
a.withdraw()
    # def withdraw(self):
    #     self.__class A:
    # def fa(self):
    #     print("from A")
    #
    # def test(self):
    #     self.fa()

# property 特性
# property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height**2)

p1 = People('egon', 75, 1.85)
print(p1.bmi)

# 圆的周长和面积
import math
class Circle:
    def __init__(self, radius): # 圆的半径radius
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2     # 计算面积

    @property
    def perimter(self):
        return 2 * math.pi * self.radius  # 计算周长

c = Circle(10)
print(c.radius)
print(c.area)   # 可以向访问数据属性一样去访问area，会触发一个函数的执行，动态计算出一个值
print(c.perimter)