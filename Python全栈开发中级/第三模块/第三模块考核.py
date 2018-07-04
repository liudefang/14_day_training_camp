# -*- encoding: utf-8 -*-
# @Time    : 2018-07-01 8:42
# @Author  : mike.liu
# @File    : 第三模块考核.py

# 服务端
# import socket
#
# ip_port = ('127.0.0.1', 8080)
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_server.bind(ip_port)
# socket_server.listen(1)
#
# conn, addr = socket_server.accept()
#
# recv_data = conn.recv(1024)
# print('这是收到的信息:', recv_data)
# cmd = input("server输入要发送的数据:").strip()
# conn.send(cmd.encode('utf-8'))
# conn.close()
# socket_server.close()
#
# # 客户端
# import socket
#
# ip_port = ('127.0.0.1', 8080)
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_server.connect()
# print("开始发送数据")
# cmd = input("客户端发送数据:").strip()
# socket_server.send(cmd.encode('utf-8'))
# recv_data = socket_server.recv(1024)
# print("客户端收到的信息:", recv_data)
# socket_server.close()
#
# # 定义一个学生类
# class Student(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def talk(self):
#         print("hello, my name is %s" % self.name)
#
# p = Student('mike', 20, 'male')
# p.talk()
#
# class ParentClass1: # 定义父类
#     pass
#
# class ParentClass2: # 定义父类
#     pass
#
# class SubClass1(ParentClass1): # 单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
# class SubClass2(ParentClass1,ParentClass2): # python支持多继承，用逗号分隔开多个继承的类
#
# SubClass1.__bases__

"""
模拟cs游戏：
    人物角色分为警察和匪徒两种，定义成两个类
    所有的警察的角色都是police
    每个警察都有自己独有名字，生命值，武器，性别
    每个都可以开枪攻击敌人，且攻击目标不能是police
    所有的匪徒的角色都是terorist
    每个匪徒都有自己独有名字，生命值，武器，性别
    每个都可以开枪攻击敌人，且攻击目标不能是terrorist
    a.实例化一个警察，一个匪徒，警察攻击匪徒，匪徒掉血
"""

# class Cs:
#     def __init__(self, name, life_value, gjl, wuqi, sex):
#         self.name = name
#         self.life_value = life_value
#         self.gjl = gjl
#         self.wuqi = wuqi
#         self.sex = sex
#
#
# class Police(Cs):
#
#     def attack(self, enemy):
#         if not isinstance(enemy, Police):
#             enemy.life_value -= self.gjl
#             if enemy.life_value <= 0:
#                 print("已经死亡")
#             else:
#                 print("警察[%s]攻击了匪徒,匪徒剩下的生命值[%s]：" % (self.name, enemy.life_value))
#         else:
#             print("都是警察")
#
# class Terorist(Cs):
#
#     def attack(self, enemy):
#         if not isinstance(enemy, Terorist):
#             enemy.life_value -= self.gjl
#             if enemy.life_value <= 0:
#                 print("已经死亡")
#             else:
#                 print("剩下的生命值：", enemy.life_value)
#         else:
#             print("都是匪徒")
#
#
# g1 = Police('警察1', 100, 30, '手枪', '男')
# r1 = Terorist('大飞', 100, 50, 'AK47', '男')
# g1.attack(r1)
# g1.attack(g1)
# r1.attack(r1)
# r1.attack(g1)

# 7.有一个类定义：
# class Person：
# def __init__(self,name,age):
# self.name = name
# self.age = age
#
# 1）初始化10个不同的对象
#
# 2）求最高age的对象的name

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person('mike1', 20)
# p2 = Person('mike2', 30)
# p3 = Person('mike3', 18)
# p4 = Person('mike4', 76)
# p5 = Person('mike5', 60)
# p6 = Person('mike6', 50)
# p7 = Person('mike7', 45)
# p8 = Person('mike8', 35)
# p9 = Person('mike9', 26)
# p10 = Person('mike10', 55)
#
# l1 = [p1, p2, p3, p4, p5, p6, p7, p8, p8, p10]
# print(p1.name)
# num = 0
# for i in l1:
#     if i.age > num:
#         num = i.age
# print()




# 1.定义两个类（人）实例化出：老王和小明
#
# 　　i.共同属性及技能：出生地，吃饭
#
# 　　不同属性及技能：a.属性：名字，年龄；
#
# 　　　　　　　　　　b.老王技能1：讲课；
#
# 　　　　　　　　　　c.老王技能2：布置作业
#
# 　　　　　　　　　　d.小明技能1：罚站
#
# 　　　　　　　　　　e老王技能3：打小明（假设小明有100点血，被打之后就掉了50点血了）
#
# 　　　　　　　　使用到了继承：共同技能和属性
#
# 　　　　　　　　定义了老王的攻击力：50
#
# 　　　　　　　　定义了小明的血量：100　


class Person:
    country = 'China'
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 正在吃饭" % self.anme)


class Person1(Person):

    def __init__(self, name, age, life_value, aggresivity):
        self.name = name
        self.age = age
        self.life_value = life_value
        self.aggresivity = aggresivity

    def eat(self):
        super().eat()

    def teacheer1(self):
        print("老王讲课")

    def have_homework(self):
        print("老王布置作业")

    def attack(self, xm_obj):
        xm_obj.life_value -= self.aggresivity
        print("小明被打了,剩下的生命值为:", xm_obj.life_value)

class Person2(Person):
    def __init__(self, name, age, life_value):
        self.name = name
        self.age = age
        self.life_value = life_value

    def eat(self):
        super().eat()

    def faz(self):
        print("小明被罚站了")

p1 = Person1("老王", 50, 100, 50)
p2 = Person2("小明", 15, 100)

p1.attack(p2)


# 11 读代码
#
# class Base:
#     def f1(self):
#         self.f2()
#
#     def f2(self):
#         print('...')
#
# class Foo(Base):
#     def f2(self):
#         print('9999')
#
# obj = Foo()
# obj.f1()
#
# 问题1:面向对象中的self指的什么？
#
# 答：指的是实例化的对象本身
#
# 问题2:运行结果并简述原因
#
# 答：实例化了一个obj，因为Foo的父类是Base所以，子类没有f1就用父类的f1，有f2就用子类的f2
# 然后obj调用了f1,在f1中因为self是对象本身，所以f1方法中调用了obj的f2，而因为继承的规则，不调用父类的f2，所以结果是9999




