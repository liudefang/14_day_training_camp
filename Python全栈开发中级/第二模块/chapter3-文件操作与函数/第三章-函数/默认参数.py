# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 8:53
# @Author  : mike.liu
# @File    : 默认参数.py


#def stu_register(name, age, country, course):
def stu_register(name, age, course, country='CN'):
    print('注册学生信息'.center(20, '-'))
    print('姓名:', name)
    print('年龄:', age)
    print('国籍:', country)
    print('课程:', course)

#stu_register('三炮', 22, 'CN', 'Python')
stu_register('三炮', 22, 'Python')