# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 20:20
# @Author  : mike.liu
# @File    : Student.py

from lib.Baseclass import Baseclass

# 学生类


class Student(Baseclass):
    def __init__(self, student_name, student_sex, student_school, student_classes):
        Baseclass.__init__(self)
        self.student_name = student_name
        self.student_sex = student_sex
        self.student_school = student_school
        self.student_classes = student_classes

    def student_registered(self):
        student_dict = {}
        print("欢迎进行学生注册页面".center(20, '-'))
        student_name = input("姓名:").strip()
        student_sex = input("性别:").strip()
        student_school = input("学校:").strip()
        student_classes = input("班级:").strip()
        st1 = Student(student_name, student_sex, student_school, student_classes)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        Baseclass.save(self, "student", student_dict)

    def student_pay_fees(self):
        pass

    def student_view_grade(self):
        student_school = input("学校:").strip()
        student_classes = input("班级:").strip()
        student_times = input("上课次数:").strip()
        student_name = input("姓名:").strip()
        class_grade_list = Baseclass.open(self, "class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_classes and j["上课次数"] == student_times and \
                        j["姓名"] == student_name:
                    for key in j:
                        print(key, j[key])
                    print("\n")

    def student_view_record(self):
        student_school = input("学校:").strip()
        student_classes = input("班级:").strip()
        student_times = input("上课次数:").strip()
        student_name = input("姓名:").strip()
        class_record_list = Baseclass.open(self, "class_grade")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_classes and j["上课次数"] == student_times and \
                        j["姓名"] == student_name:
                    for key in j:
                        print(key, j[key])
                    print("\n")