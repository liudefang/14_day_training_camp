# -*- encoding: utf-8 -*-
# @Time    : 2018-06-13 22:01
# @Author  : mike.liu
# @File    : test.py
# import settings
#
#
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
#
# print(MySQL.from_conf())
# conn = MySQL.from_conf()
# conn.from_conf()

# 非绑定方法
# import hashlib
# import time
# class MySQL:
#     def __init__(self, host, port):
#         self.id = self.create_id()
#         self.host = host
#         self.port = port
#
#     @classmethod
#     def create_id(cls):    # 就是一个普通工具
#         m = hashlib.md5(str(time.time()).encode('utf-8'))
#         return m.hexdigest()
#
# print(MySQL.create_id)
# conn = MySQL('127.0.0.1', 3306)
# print(conn.create_id)

# classmethod与staticmethod的对比
# import settings
# class MySQL:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#
#     @staticmethod
#     def from_conf():
#         return MySQL(settings.HOST, settings.PORT)
#
#     def __str__(self):
#         return "就不告诉你"
#
# class Mariadb(MySQL):
#     def __str__(self):
#         return "<%s:%s>" % (self.host, self.port)
#
# m = Mariadb.from_conf()
# print(m)
#
# 练习1：定义MySQL类
#
# 要求：
#
# 1.对象有id、host、port三个属性
#
# 2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一
#
# 3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化
#
# 4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号，
# 保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象
import hashlib
import time

import settings
import os
import pickle


class MySQL:
    def __init__(self, host, port):
        # 为每个对象创建一个ID
        self.id = self.create_id()
        self.host = host
        self.port = port

    @staticmethod
    def create_id():
        id = hashlib.md5(str(time.clock()).encode("utf-8"))
        return id.hexdigest()

    # 从配置文件中读取在这里用到了classmethod
    @classmethod
    def from_conf(cls):
        return cls(settings.HOST, settings.PORT)

    def save(self):
        file_path = r"%s/%s%s" % (settings.DB_PATH + r"/db", os.sep, self.id)
        if os.path.isfile(file_path):
            print("该文件已经存在!")
        else:

            # 将这个对象以二进制的形式写到硬盘中
            pickle.dump(self, open(file_path, "wb"))

    def get(self):
        # 在这里通过id的方式保证了文件的名字是唯一的
        file_path = r"%s/%s/%s" % (settings.DB_PATH + r"/db", os.sep, self.id)
        return pickle.load(open(file_path, "rb"))


if __name__ == '__main__':
    conn1 = MySQL(settings.HOST, settings.PORT)
    print(conn1.id)
    conn1.save()
    result = conn1.get()
    print(result.id)

