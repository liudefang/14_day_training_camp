# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 9:02
# @Author  : mike.liu
# @File    : 关键参数.py

def stu_register(name, age, course='PY', country='CN'):
    print('注册学生信息'.center(20, '-'))
    print('姓名:', name)
    print('年龄:', age)
    print('国籍:', country)
    print('课程:', course)

stu_register('三炮', course='PY', age=22, country='CN')

# 这样不行
# stu_register('三炮', 25, age=22, country='CN')