# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 22:21
# @Author  : mike.liu
# @File    : Student.py
'''
学生视图，学生创建姓名，年龄，所报的班级，所报的学校
'''


class Student:
    def __init__(self):
        pass

    # 学生注册
    @staticmethod
    def resistered():
        student_dict = {}
        print('\033[32;1m欢迎来到学生注册页面\033[0m'.center(20, '-'))
        student_name = input("请输入姓名:").strip()
        student_password = input("请输入密码:").strip()
        Manager.Manager.show_school()
        student_school = input("请选择学校:").strip()
        Manager.Manager.show_class()
        student_class = input("请选择班级:").strip()
        accounts.MyPickle.load_coursedata('course')
        student_course = input("请选择地区:").strip()
        student_score = None
        student_identity = 'student'
        student_dict['account'] = student_name
        student_dict['password'] = student_password
        student_dict['school'] = student_school
        student_dict['class'] = student_class
        student_dict['course'] = student_course
        student_dict['score'] = student_score
        student_dict['identity'] = student_identity
        print("\033[32;1m您的注册信息如下:\033[0m".center(20, '-'))
        print("\033[31;1m%s\033[0m" % student_dict)
        accounts.MyPickle.save_account(student_dict)

    # 查看上课记录
    @staticmethod
    def find_classrecord():
        '''上课记录是老师给的'''
        print("\033[32;1m欢迎来到上课记录查询页面\033[0m".center(20, '-'))
        name = 'class_record'
        accounts.MyPickle.load_classrecord(name)

    # 查看作业成绩
    @staticmethod
    def find_grade():
        '''成绩是老师给的'''
        print("\033[32;1m欢迎来到成绩查询页面\033[0m".center(20, '-'))
        name = 'class_grade'
        accounts.MyPickle.load_classgrade(name)
