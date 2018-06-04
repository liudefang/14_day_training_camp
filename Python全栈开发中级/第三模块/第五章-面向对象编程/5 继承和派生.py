# -*- encoding: utf-8 -*-
# @Time    : 2018-06-04 21:07
# @Author  : mike.liu
# @File    : 5 继承和派生.py


# 属性查找小练习
class Foo:
    def f1(self):
        print('from Foo.f1')

    def f2(self):
        print('from Foo.f2')
        self.f1() # b.f1()

class Bar(Foo):
    def f1(self):
        print('from Bar.f1')

b = Bar()
b.f2()