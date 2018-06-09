# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 19:48
# @Author  : mike.liu
# @File    : Admin.py
from lib.Baseclass import Baseclass
from lib.School import School
# admin类


class Admin(Baseclass):
    def __init__(self):
        Baseclass.__init__(self)

    def create_school(self):
        school_dict = {}
        school_name = input("请输入学校名称:").strip()
        school_address = input("请输入学校地址:").strip()
        s1 = School(school_name, school_address)
        school_dict["校名"] = s1.school_name
        school_dict["地址"] = s1.school_address
        Baseclass.save(self, "school", school_dict)