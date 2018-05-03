#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/5/3 9:45
# @Author  : mike.liu
# @File    : 函数参数.py

# 默认参数
# def stu_register(name, age, course, country = "CN" ):
#     print("注册学生信息".center(20, '-'))
#     print("姓名", name)
#     print("age", age)
#     print("国籍", country)
#     print("课程", course)
#
# stu_register("张三", 22,  "python")
# stu_register("王五", 23,  "linux")
# stu_register("李四", 25,  "Java")

# 关键参数


# def stu_register(name, age, course='py', country="CN"):
#     print("注册学生信息".center(20, '-'))
#     print("姓名", name)
#     print("age", age)
#     print("国籍", country)
#     print("课程", course)
#
# stu_register("张三", course='py', age=22, country="CN")

# 非固定参数
# def stu_register(name, age, *args, **kwargs):   # *args 会把多传入的参数变成一个元组形式  *kwargs会把多传入的参数变成一个dict形式
#     print(name, age, args, kwargs)
#
# stu_register("张三", 22, "CN", "python", sex="M", province="湖南")

# 返回值
# def stu_register(name, age, course='py', country="CN"):
#     print("注册学生信息".center(20, '-'))
#     print("姓名", name)
#     print("age", age)
#     print("国籍", country)
#     print("课程", course)
#     if age > 22:
#         return False
#     else:
#         return True
#
# registration_status = stu_register("张三", 22, course="python全栈开发", country="CN")
#
# if registration_status:
#     print("注册成功!")
# else:
#     print("注册信息有误!")

# 全局和局部变量
# name = "张三"
#
# def change_name():
#     global name
#
#     name = "张三买了一辆特斯拉"
#     print("修改后的姓名:", name)
#
# change_name()
# print("在外面看看name改了吗？", name)

# 嵌套函数
name = "张三"

def change_name():
    name = "张三丰"

    def change_name2():
        name = "张山峰"
        print("张山峰打印:", name)

    change_name2()    # 调用内层函数
    print("第二层打印:", name)


change_name()
print("最外层打印:", name)