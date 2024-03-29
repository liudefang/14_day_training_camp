# -*- encoding: utf-8 -*-
# @Time    : 2018-06-03 8:18
# @Author  : mike.liu
# @File    : 2 类与对象.py
# 1.只有在python2中才分新式类和经典类，python3中统一都是新式类
#
# 2.在python2中，没有显式的继承object类的类，以及该类的子类，都是经典类
#
# 3.在python2中，显式地声明继承object的类，以及该类的子类，都是新式类
#
# 4.在python3中，无论是否继承object，都默认继承object，即python3中所有类均为新式类



class OldboyStudent:
    school = 'oldboy'
    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

s1 = OldboyStudent('李坦克', '男', 18)  # 先调用类产生空对象s1，再调用OldboyStudent
s2 = OldboyStudent('王大炮', '男', 38)
s3 = OldboyStudent('牛弹琴', '女', 22)

print(s1.__dict__['name'])
print(s1.name)
# # 查
# s1 = OldboyStudent.school
# print(s1)
# # 修改
# s2 = OldboyStudent.school = '北京大学'
# print(s2)
#
# # 增加
# s3 = OldboyStudent.x = 223
# print(s3)

# # 删除
# del OldboyStudent.x