# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 9:23
# @Author  : mike.liu
# @File    : 返回值.py
# 返回值
# 注意
#
# 函数在执行过程中只要遇到return语句，就会停止执行并返回结果，so 也可以理解为 return 语句代表着函数的结束
# 如果未在函数中指定return,那这个函数的返回值为None

def stu_register(name, age, course, country='CN'):
    print('注册学生信息'.center(20, '-'))
    print('姓名:', name)
    print('年龄:', age)
    print('国籍:', country)
    print('课程:', course)
    if age > 22:
        return False
    else:
        return True

registriation_status = stu_register('三炮', 22, 'CN', 'Python')

if registriation_status:
    print('注册成功!')
else:
    print('注册失败!')