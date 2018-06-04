# -*- encoding: utf-8 -*-
# @Time    : 2018-06-03 9:06
# @Author  : mike.liu
# @File    : 3 属性查找与绑定方法.py

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
# 类的数据属性是所有对象共享的，id是一样的
# print(id(OldboyStudent.school))     # 4830576
# print(id(s1.school))        # 4830576
# print(id(s2.school))        # 4830576
# print(id(s3.school))        # 4830576

# 类的函数属性是绑定给对象使用的,obj.method称为绑定方法,内存地址都不一样
print(OldboyStudent.learn)      # <function OldboyStudent.learn at 0x0000000002879598>
print(s1.learn)                 # <bound method OldboyStudent.learn of <__main__.OldboyStudent object at 0x0000000002866898>>
print(s2.learn)                 # <bound method OldboyStudent.learn of <__main__.OldboyStudent object at 0x00000000028669E8>>
print(s3.learn)                 # <bound method OldboyStudent.learn of <__main__.OldboyStudent object at 0x0000000002866F98>>