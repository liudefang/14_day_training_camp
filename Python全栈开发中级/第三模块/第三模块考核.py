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

class Cs:
    def __init__(self, name, life_value, wuqi, sex):
        self.name = name
        self.life_value = life_value
        self.wuqi = wuqi
        self.sex = sex

    def attack(self, enemy):
        enemy.life_value -= self.life_value

class Police(Cs):
    pass

class Terorist(Cs):
    pass

g1 = Police('警察1', 100, '手枪', '男')
r1 = Terorist('大飞', 100, 'AK47', '男')
g1.attack(r1)
print(r1.life_value)
