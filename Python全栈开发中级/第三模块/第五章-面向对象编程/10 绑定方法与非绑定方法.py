# -*- encoding: utf-8 -*-
# @Time    : 18-6-13 下午12:14
# @Author  : mike.liu
# @File    : 10 绑定方法与非绑定方法.py

# 类中定义的函数分成两大类
# 一、绑定方法
# 1、绑定到类的方法：用classmethod装饰器的方法
# 2、绑定到对象的方法：没有被任何装饰器装饰的方法
'''
为对象量身定制
对象.boud_method()，自动将对象当作第一个参数传入
（属于类的函数，类可以调用，但是必须按照函数的规则来，没有自动传值那么一说）
'''

# 二、非绑定方法：用staticmethod装饰器的方法
# 1. 不与类或对象绑定，类和对象都可以调用，但是没有自动传值这么一说，就是一个普通工具而已

# 绑定方法
# 绑定给类的方法（classmethod）
# settings.py
# HOST = '127.0.0.1'
# PORT = 3306
# DB_PATH = 'db'
# db_path = ''
#
# import settings
# class MySQL:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#
#     @classmethod
#     def from_conf(cls):
#         print(cls)
#         return cls(settings.HOST, settings.PORT)
#
# print(MySQL.from_conf())
# conn = MySQL.from_conf()
#
# conn.from_conf()    # 对象也可以调用，但是默认传的第一个参数任然是类

# 在类内部用staticmethod装饰的函数即非绑定方法，就是普通函数
#
# statimethod不与类或对象绑定，谁都可以调用，没有自动传值效果
# import hashlib
# import time
#
# class MySQL:
#     def __init__(self, host, port):
#         self.id = self.create_id()
#         self.host = host
#         self.port = port
#
#     @staticmethod
#     def create_id():    # 就是一个普通工具
#         m = hashlib.md5(str(time.time()).encode('utf-8'))
#         return m.hexdigest()
#
# print(MySQL.create_id())
# conn = MySQL('127.0.0.1', 3306)
# print(conn.create_id())

#classmethod与staticmethod的对比
import settings
class MySQL:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @staticmethod
    def from_conf():
        return MySQL(settings.HOST, settings.PORT)

    def __str__(self):
        return '就不告诉你'

class Mariadb(MySQL):
    def __str__(self):
        return '<%s:%s>' % (self.host, self.port)

m = Mariadb.from_conf()
print(m)        # 我们的意图是想触发Mariadb.__str__，但是结果触发了MySQL.__str__的执行，打印就不告诉
