# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 20:03
# @Author  : mike.liu
# @File    : Teacher.py

# 讲师类
from lib.Baseclass import Baseclass


class Teacher(Baseclass):
    def __init__(self, teacher_name, teacher_salary, teacher_school):
        Baseclass.__init__(self)
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school

    def create_class_record(self):
        class_record = []
        student_school = input("请选择学校:").strip()
        student_classes = input("请选择班级:").strip()
        student_times = input("上课次数:").strip()
        student_list = Baseclass.open(self, "student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_status = input("%s 上课情况:" % student_name)
                i["上课情况"] = student_status
                i["上课次数"] = student_times
                class_record.append(i)
        Baseclass.seek_list(self, "class_record", class_record)

    def create_class_grade(self):
        class_grade = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课次：")
        student_list = Baseclass.open(self, "student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_grade = input("%s 成绩：" % student_name)
                i["成绩"] = student_grade
                i["课次"] = student_times
                class_grade.append(i)
        Baseclass.seek_list(self, "class_grade", class_grade)

    def teacher_view_grade(self):
        grade_list = []
        student_school = input("校名：")
        student_class = input("班级：")
        student_times = input("课次：")
        class_grade_list = Baseclass.open(self, "class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times:
                    grade_list.append(j)
        for i in grade_list:
            for key in i:
                print(key, i[key])
            print("\n")

    def tacher_view_record(self):
        record_list = []
        student_school = input("校名：").strip()
        student_class = input("班级：").strip()
        student_times = input("课次：").strip()
        class_record_list = Baseclass.open(self, "class_record")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times:
                    record_list.append(j)
        for i in record_list:
            for key in i:
                print(key, i[key])
            print("\n")
