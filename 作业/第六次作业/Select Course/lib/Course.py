# -*- encoding: utf-8 -*-
# @Time    : 2018-06-06 23:03
# @Author  : mike.liu
# @File    : Course.py
# 创建课程，包括课程名称，课程周期，课程价格
from core import accounts


class Course:
    def __init__(self):
        pass

    @staticmethod
    def create_course():
        name = "course"
        print("\033[32;1m欢迎来到创建课程页面\033[0m".center(20, '-'))
        course_data = accounts.MyPicke.load_coursedata(name)
        course_dict = {}
        accounts.MyPicke.load_school('school')
        course_school = input("请输入学校对应的课程:").strip()
        course_name = input("请输入课程名称:").strip()
        course_period = input("请输入课程周期:").strip()
        course_prices = input("请输入课程价格:").strip()
        course_dict["course_school"] = course_school
        course_dict["course_name"] = course_name
        course_dict["course_period"] = course_period
        course_dict["course_prices"] = course_prices
        print("\033[32;1m创建的课程信息如下:\033[0m".center(20, '-'))
        print("\033[31;1m%s\033[0m" % course_dict)
        accounts.MyPicke.save_course(course_dict)
        accounts.MyPicke.save_coursedata(name, course_name)

    @staticmethod
    def show_course():
        '''
        请输入课程信息
        :return:
        '''
        print("\033\32;1m欢迎来到课程查询页面".center(20, '-'))
        name = "course"
        accounts.MyPicke.load_coursedata(name)
        course_name = input("请输入要查找的课程名:").strip()
        accounts.MyPicke.load_course(course_name)