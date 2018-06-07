# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 22:56
# @Author  : mike.liu
# @File    : School.py
from core import accounts


class School:
    def __init__(self):
        pass

    @staticmethod
    def create_school():
        name = 'school'
        print("\033[32;1m欢迎来到创建学校页面\033[0m".center(20, '-'))
        school_name = input("请输入学校名称:").strip()
        accounts.MyPickle.save_school(name, school_name)
        print("\033[34;1m创建学校【%s】成功!\033[0m" % school_name)

    @staticmethod
    def show_school():
        print("\033[32;1m欢迎来到查看学校页面\033[0m".center(20, '-'))
        name = 'school'
        accounts.MyPickle.load_school(name)