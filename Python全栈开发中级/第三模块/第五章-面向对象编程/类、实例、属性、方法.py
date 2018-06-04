# -*- encoding: utf-8 -*-
# @Time    : 2018-06-02 16:13
# @Author  : mike.liu
# @File    : 类、实例、属性、方法.py

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("my name is %s, I'm %s year old!" %(self.name, self.age))

    def __del__(self):
        print("running del method, this person must be died.")


p = Person("Alex", 22)
print(p.name, p.age)
p.talk()

del p
print('--end program--')