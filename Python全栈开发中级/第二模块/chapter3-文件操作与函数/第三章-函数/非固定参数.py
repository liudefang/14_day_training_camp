# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 9:13
# @Author  : mike.liu
# @File    : 非固定参数.py
# def stu_register(name, age, *args):
#     print(name, age, args)

# stu_register('三炮', 22)

# 输出
# 三炮 22 ()   后面这个（）就是args，没有传值，就是空的
# stu_register('三炮', 22, 'CN', 'python')
# 输出
# 三炮 22 ('CN', 'python')

# 还可以有**kwargs
def stu_register(name, age, *args, **kwargs):
    print(name, age, args, kwargs)
stu_register('三炮', 22, 'CN', 'python')
stu_register('三炮', 22, 'CN', 'python', sex='男',province='湖南')
# 输出
# 三炮 22 ('CN', 'python') {}  :{}:就是**kwargs

# 三炮 22 ('CN', 'python') {'sex': '男', 'province': '湖南'}