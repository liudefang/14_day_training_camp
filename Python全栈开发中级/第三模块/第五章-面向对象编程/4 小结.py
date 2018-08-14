# -*- encoding: utf-8 -*-
# @Time    : 2018-06-08 20:20
# @Author  : mike.liu
# @File    : 4 小结.py
# from pymysql import connect
#
#
# class mysqlhandler:
#     def __init__(self, host, port, db, charset="utf-8"):
#         self.host = host
#         self.port = port
#         self.db = db
#         self.charset = charset
#         self.conn = connect(self.host, self.port, self.db, self.charset)
#
#     def exc1(self, sql):
#         return self.conn.execute(sql)
#
#     def exc2(self, sql):
#         return self.conn.call_proc(sql)
#
#
# obj = mysqlhandler('127.0.0.1', 3306, 'db1')
# obj.exc1('select * from tab1')
# obj.exc2('存储过程的名字')
#
#
# class chinese:
#     country = 'China'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def tell_info(self):
#         info = '''
#         国籍:%s
#         姓名:%s
#         年龄:%s
#         性别:%s
#         ''' % (self.country, self.name, self.age, self.sex)
#         print(info)
#
#
# p1 = chinese('egon', 18, 'male')
# p2 = chinese('alex', 33, 'female')
# p3 = chinese('wpq', 50, 'female')
#
# print(p1.country)
# p1.tell_info()

# 小节练习
# 练习1：编写一个学生类，产生一堆学生对象， (5分钟)
#
# 要求：
#
# 有一个计数器（属性），统计总共实例了多少个对象
# class Student:
#     count = 0
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         Student.count += 1
#
#     def learn(self):
#         print('%s is learing' % self.name)
#
# stu1 = Student('alex', 'male', 38)
# stu2 = Student('jinxing', 'female', 33)
# stu3 = Student('mike', 'male', 18)
#
# print(Student.count)
# 练习2：模仿王者荣耀定义两个英雄类， (10分钟)
#
# 要求：
#
# 英雄需要有昵称、攻击力、生命值等属性；
# 实例化出两个英雄对象；
# 英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。
class People:
    def __init__(self, name, gjl, smz):
        self.name = name
        self.gjl = gjl
        self.smz = smz

    def attack(self, enemy):
        enemy.smz -= self.gjl

class Grun(People):
    name = 'Grun'
    def attack(self, enemy):
        super().attack(enemy)

class Mike(People):
    name = 'Mike'
    def attack(self, enemy):
        super().attack(enemy)

G1 = Grun('Grun', 100, 30)
M1 = Mike('Mike', 100, 50)

M1.attack(G1)
print(M1.smz)
