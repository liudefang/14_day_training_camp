# -*- encoding: utf-8 -*-
# @Time    : 2018-06-04 21:07
# @Author  : mike.liu
# @File    : 5 继承和派生.py

# 继承：
#     继承就是类与类的关系，是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类可以称为基类或超类，新建的类称为派生类或子类。
#
# python中类的继承分为：单继承和多继承
# class ParentClass1: #定义父类
#     pass
#
# class ParentClass2: #定义父类
#     pass
#
# class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
# class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
#     pass
#
# 查看继承：
# >>> SubClass1.__bases__
# #__base__只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
# (<class '__main__.ParentClass1'>,)
# >>> SubClass2.__bases__
# (<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)

# 属性查找小练习
# class Foo:
# #     def f1(self):
# #         print('from Foo.f1')
# #
# #     def f2(self):
# #         print('from Foo.f2')
# #         self.f1() # b.f1()
# #
# # class Bar(Foo):
# #     def f1(self):
# #         print('from Bar.f1')
# #
# # b = Bar()
# # b.f2()
# python 中类的继承分为：单继承和多继承

class parentclass1: # 定义父类
    pass

class parentclass2: # 定义父类
    pass

class subclass1(parentclass1):   # 单继承，基类是parentclass1,派生类是subclass
    pass

class subclass2(parentclass2):  # python支持多继承，用逗号分隔开多个继承的类
    pass

# 查看继承


print(subclass1.__bases__)      # 只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
print(subclass2.__bases__)

# 经典类和新式类
'''
1.只有python2中才分新式类和经典类，python3中统一都是新式类
2.在python2中，没有显示的继承object类的类，以及该类的子类，都是经典类
3.在python3中，显示地声明继承object的类，以及该类的子类，都是新式类
4.在python3中，无论是否继承object，都默认继承object，即python3中所有类均为新式类'''
# print(parentclass1.__bases__)
#
# # 继承和重用性
# # 通过继承的方式新建类B，让B继承A，B会‘遗传’A的所有属性(数据属性和函数属性)，实现代码重用


class Hero:
    def __init__(self, nickname, aggressivity, life_value):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value

    def move_forward(self):
        print("%s move forward" % self.nickname)

    def mvove_backward(self):
        print("%s move backward" % self.nickname)

    def move_left(self):
        print("%s move backward" % self.nickname)

    def move_righe(self):
        print("%s move backward" % self.nickname)

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    pass

class Rive(Hero):
    pass
#
#
# g1 = Garen("草丛伦", 100, 300)
# r1 = Rive("锐雯雯", 58, 200)
#
# print(g1.life_value)
# r1.attack(g1)
# print(g1.life_value)

# 再看属性查找
# 提示：像g1.life_value之类的属性引用，会先从实例中找file_value，然后去类中找，然后再去父类中找，直到最顶级的父类
# class Foo:
#     def f1(self):
#         print('from Foo.f1')
#
#     def f2(self):
#         print('from Foo.f2')
#         self.f1() # b.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('from Bar.f1')
#
# b = Bar()
# b.f2()
# 打印结果:
# Foo.f2
# Bar.f1

# 派生
# 一旦重新定义了自己的属性且月父类重名，那么调用新增的属性时，就以自己为准了
class Riven(Hero):
    camp = "Noxus"

    def __init__(self, nickname, aggressivity, life_value, skin):
        Hero.__init__(self, nickname, aggressivity, life_value) # 调用父类的功能
        self.skin = skin    # 新属性

    def attack(self, enemy):    # 在自己这里定义新的attack，不再使用父类的attack，且不会影响父类
        Hero.attack(self, enemy)
        print("from riven")

    def fly(self):  # 在自己这里定义新的
        print("%s is flying" % self.nickname)


r1 = Riven('锐雯雯', 57, 200, '比基尼')
r1.fly()
print(r1.skin)

# 继承的实现原理
# 并所有父类的MRO列表并遵循如下三条准则:

# 子类会先于父类被检查
# 多个父类会根据它们在列表中的顺序被检查
# 如果对下一个类存在两个合法的选择,选择第一个父类
# 在Java和C#中子类只能继承一个父类，而Python中子类可以同时继承多个父类，
# 如果继承了多个父类，那么属性的查找方式有两种，分别是：深度优先和广度优先

# 当类是经典类时，多继承情况下，在要查找属性不存在时，会按照深度优先的方式查找下去
# 当类是新式类时，多继承情况下，在要查找属性不存在时，会按照广度优先的方式查找下去

# 示例代码
# class A(object):
#     def test(self):
#         print("from A")
#
# class B(A):
#     def test(self):
#         print("from B")
#
# class C(A):
#     def test(self):
#         print("from C")
#
# class D(B):
#     def test(self):
#         print("from D")
#
# class E(C):
#     def test(self):
#         print("from E")
#
# class F(D, E):
#     def test(self):
#         print("from F")
#
# f1 = F()
# f1.test()
# print(F.__mro__)    # 只有新式类才有这个属性可以查看线性列表，经典类没有这个属性
#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C

# 在子类中调用父类的方法
# 两种方式
# 方式一：指名道姓，即父类名.父类方法()
# class Vehicle: # 定义交通工具类
#     Country = "China"
#
#     def __init__(self, name, speed, load, power):
#         self.name = name
#         self.speed = speed
#         self.load = load
#         self.power = power
#
#     def run(self):
#         print("开动啦...")
#
#
# class Subway(Vehicle): # 地铁
#     def __init__(self, name, speed, load, power, line):
#         Vehicle.__init__(self, name, speed, load, power)
#         self.line = line
#
#     def run(self):
#         print("地铁%s号线欢迎您" % self.line)
#         Vehicle.run(self)
#
#
# line13=Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
# line13.run()

# 方式二：super()


class Vehicle: # 定义交通工具类
    Country = "China"

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print("开动啦...")


class Subway(Vehicle): # 地铁
    def __init__(self, name, speed, load, power, line):
        # Vehicle.__init__(self, name, speed, load, power)
        super().__init__(name, speed, load, power)
        self.line = line

    def run(self):
        print("地铁%s号线欢迎您" % self.line)
        # Vehicle.run(self)
        super(Subway, self).run()


line13=Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
line13.run()