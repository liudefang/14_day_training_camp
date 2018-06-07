# -*- encoding: utf-8 -*-
# @Time    : 18-6-7 下午3:20
# @Author  : mike.liu
# @File    : School.py
from lib.Baseclass import Baseclass

# 学校类


class School(Baseclass):
    def __init__(self, school_name, school_address):
        Baseclass.__init__(self)
        self.school_name = school_name
        self.school_address = school_address

