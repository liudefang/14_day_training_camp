# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 20:17
# @Author  : mike.liu
# @File    : Course.py

from lib.Baseclass import Baseclass
# 课程类


class Course(Baseclass):
    def __init__(self, course_name, course_period, course_prices):
        Baseclass.__init__(self)
        self.course_name = course_name
        self.course_period = course_period
        self.course_prices = course_prices
