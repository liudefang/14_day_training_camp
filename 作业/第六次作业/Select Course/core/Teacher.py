# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 23:49
# @Author  : mike.liu
# @File    : Teacher.py
from core import Manager, accounts


class Teacher:
    def __init__(self):
        pass

    # 讲师注册
    @staticmethod
    def resistered():
        teacher_dict = {}
        print('\033[32;1m-------欢迎来到讲师注册系统------\033[0m')
        teacher_name = input("请输入老师姓名:").strip()
        teacher_password = input("请输入密码:").strip()
        Manager.Manager.show_school()
        teacher_school = input("请输入学校:").strip()
        Manager.Manager.show_class()
        teacher_class = input("请输入所教班级:").strip()
        teacher_identity = 'teacher'
        teacher_dict['account'] = teacher_name
        teacher_dict['password'] = teacher_password
        teacher_dict['school'] = teacher_school
        teacher_dict['class'] = teacher_class
        teacher_dict['identity'] = teacher_identity
        print("\033[32;1m--------这是您登记的信息，请查看----------\033[0m")
        print('\033[31;1m%s\033[0m' % teacher_dict)
        accounts.MyPickle.save_account(teacher_dict)

    # 创建上课记录,想法是每一个人对应一个记录，比如王某：8次
    @staticmethod
    def create_classrecord():
        classrecord_dict = {}
        print('\033[32;1m-------欢迎来到上课记录登记页面------\033[0m')
        student_name = input("请输入学生姓名:").strip()
        class_record = input("请输入上课次数:").strip()
        classrecord_dict[student_name] = class_record
        name = 'class_record'
        classrecord_dict = str(classrecord_dict)
        accounts.MyPickle.save_classrecord(name, classrecord_dict)

    # 创建作业成绩，想法是每一个人对应一个记录，比如王某：98
    @staticmethod
    def create_grade():
        classgrade_dict = {}
        print('\033[32;1m-------欢迎来到作业成绩登记页面------\033[0m')
        student_name = input("请输入学生姓名:").strip()
        class_grade = input("请输入作业成绩:").strip()
        classgrade_dict[student_name] = class_grade
        name = 'class_grade'
        classgrade_dict = str(classgrade_dict)
        accounts.MyPickle.save_classgrade(name, classgrade_dict)