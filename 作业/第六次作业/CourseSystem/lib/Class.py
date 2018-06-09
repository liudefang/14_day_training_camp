# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 20:40
# @Author  : mike.liu
# @File    : Class.py
from lib.Baseclass import Baseclass

# 课程类


class Classes(Baseclass):
     def __init__(self, classes_name, classes_teachter, classes_course):
        Baseclass.__init__(self)
        self.classes_name = classes_name
        self.classes_teacher = classes_teachter
        self.classes_course = classes_course
