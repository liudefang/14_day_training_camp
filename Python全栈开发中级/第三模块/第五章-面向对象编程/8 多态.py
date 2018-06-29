# -*- encoding: utf-8 -*-
# @Time    : 18-6-27 下午4:39
# @Author  : mike.liu
# @File    : 8 多态.py

# 多态指一种事物有多种形态，那为什么要使用多态呢？
# 1.增加了程序的灵活性
#
# 　　以不变应万变，不论对象千变万化，使用者都是同一种形式去调用，如func(animal)
#
# 2.增加了程序额可扩展性
#
# 　通过继承animal类创建了一个新的类，使用者无需更改自己的代码，还是用func(animal)去调用
#
# 举个例子：
# >>> class Cat(Animal): #属于动物的另外一种形态：猫
# ...     def talk(self):
# ...         print('say miao')
# ...
# >>> def func(animal): #对于使用者来说，自己的代码根本无需改动
# ...     animal.talk()
# ...
# >>> cat1=Cat() #实例出一只猫
# >>> func(cat1) #甚至连调用方式也无需改变，就能调用猫的talk功能
# say miao

'''
这样我们新增了一个形态Cat，由Cat类产生的实例cat1，使用者可以在完全不需要修改
自己代码的情况下。使用和人、狗、猪一样的方式调用cat1的talk方法，即func(cat1)
'''