# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 23:21
# @Author  : mike.liu
# @File    : main.py


import sys,os
import json
import pickle

from bin import course


#数据库文件路径
from core import uid

db_DIR = course.BASE_DIR + r"\db"
db_school = db_DIR + r"\school"
db_teacher = db_DIR + r"\teacher"
db_student = db_DIR + r"\student"
db_classes = db_DIR + r"\classes"
db_course = db_DIR + r"\course"
db_admin = db_DIR + r"\admin"
db_class_record = db_DIR + r"\class_record"
db_class_grade = db_DIR + r"\class_grade"

#基础类，主要包括文件的读写操作
class Baseclass(object):
    def __init__(self):
        pass
    def save(self,type,dict):
        filename = uid.create_md()
        dict['uid'] = filename
        file_path = "%s\%s" %(db_DIR,type)
        ab_file = "%s\%s" %(file_path,filename)
        if os.path.isdir(file_path):
            with open(ab_file,"wb") as f:
                f.write(pickle.dumps(dict))
                if True:
                    print(
                    "-------",type,"创建成功","-------")
                    for key in dict:
                        print(key,":\t",dict[key])
    def seek_list(self,type,list):
        filename = uid.create_md()
        file_path = "%s\%s" %(db_DIR,type)
        ab_file = "%s\%s" %(file_path,filename)
        if os.path.isdir(file_path):
            with open(ab_file,"wb") as f:
                f.write(pickle.dumps(list))
                if True:
                    print(
                    "-------",type,"创建成功","-------")
                    for i in list:
                        for key in i:
                            print(key,i[key])
                        print("\n")
        return True

    def open(self,type):
        all_data = []
        db_path = "%s\%s" %(db_DIR,type)
        for i in os.listdir(db_path):
            if os.path.isfile(os.path.join(db_path,i)):
                db_file = os.path.join(db_path,i)
                with open(db_file,"rb") as f:
                    file_dict = pickle.load(f)
                    all_data.append(file_dict)
        return all_data

#管理员类
class Admin(Baseclass):
    def __init__(self):
        Baseclass.__init__(self)
    def create_school(self):
        school_dict = {}
        school_name = input("校名：")
        school_address = input("地址：")
        s1 = School(school_name, school_address)
        school_dict["校名"] = s1.school_name
        school_dict["地址"] = s1.school_address
        Baseclass.save(self, "school", school_dict)
    def create_teacher(self):
        teacher_dict = {}
        teacher_name = input("讲师姓名：")
        teacher_salary = input("讲师工资：")
        teacher_school = input("所属学校：")
        t1 = Teacher(teacher_name, teacher_salary, teacher_school)
        teacher_dict["姓名"] = t1.teacher_name
        teacher_dict["工资"] = t1.teacher_salary
        teacher_dict["所属学校"] = t1.teacher_school
        print(teacher_dict)
        Baseclass.save(self, "teacher", teacher_dict)
    def create_student(self):
        student_dict = {}
        student_name = input("学员姓名：")
        student_sex = input("学员性别：")
        student_school = input("所属学校：")
        student_classes = input("学员班级：")
        st1 = Student(student_name, student_sex, student_school, student_classes)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        Baseclass.save(self, "student", student_dict)
    def create_course(self):
        course_dict = {}
        course_name = input("课程名：")
        course_period = input("周期：")
        course_prices = input("价格：")
        c1 = Course(course_name, course_period, course_prices)
        course_dict["课程名"] = c1.course_name
        course_dict["周期"] = c1.course_period
        course_dict["价格"] = course_prices
        Baseclass.save(self, "course", course_dict)
    def create_classes(self):
        classes_dict = {}
        classes_name = input("班级名：")
        classes_teachter = input("负责讲师：")
        classes_course = input("所学课程：")
        cs1 = Classes(classes_name, classes_teachter, classes_course)
        classes_dict["班级名"] = cs1.classes_name
        classes_dict["负责讲师"] = cs1.classes_teacher
        classes_dict["课程"] = cs1.classes_course
        Baseclass.save(self, "classes", classes_dict)

#学校类
class School(Baseclass):
    def __init__(self,school_name,school_address):
        Baseclass.__init__(self)
        self.school_name = school_name
        self.school_address = school_address

#讲师类
class Teacher(Baseclass):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        Baseclass.__init__(self)
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school
    def create_class_record(self):
        class_record = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课次：")
        student_list = Baseclass.open(self,"student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_status = input("%s 上课情况：" % student_name)
                i["上课情况"] = student_status
                i["课次"] = student_times
                class_record.append(i)
        Baseclass.seek_list(self,"class_record",class_record)
    def create_class_grade(self):
        class_grade = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课次：")
        student_list = Baseclass.open(self,"student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_grade = input("%s 成绩：" % student_name)
                i["成绩"] = student_grade
                i["课次"] = student_times
                class_grade.append(i)
        Baseclass.seek_list(self,"class_grade",class_grade)
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
                print(key,i[key])
            print("\n")

    def tacher_view_record(self):
        record_list = []
        student_school = input("校名：")
        student_class = input("班级：")
        student_times = input("课次：")
        class_record_list = Baseclass.open(self, "class_record")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times:
                    record_list.append(j)
        for i in record_list:
            for key in i:
                print(key,i[key])
            print("\n")

#课程类
class Course(Baseclass):
    def __init__(self,course_name,course_period,course_prices):
        Baseclass.__init__(self)
        self.course_name = course_name
        self.course_period = course_period
        self.course_prices = course_prices

#学员类
class Student(Baseclass):

    def __init__(self,student_name,student_sex,student_school,student_classes):
        Baseclass.__init__(self)
        self.student_name = student_name
        self.student_sex = student_sex
        self.student_school = student_school
        self.student_classes = student_classes
    def student_registered(self):
        student_dict = {}
        print("欢迎进入学生注册系统")
        student_name = input("注册姓名：")
        student_sex = input("性别：")
        student_school = input("学校：")
        student_class = input("班级：")
        st1 = Student(student_name,student_sex,student_school,student_class)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        Baseclass.save(self, "student", student_dict)
    def student_pay_fees(self):
        pass
    def student_view_grade(self):
        student_school = input("校名：")
        student_class = input("班级：")
        student_times = input("课次：")
        student_name = input("姓名：")
        class_grade_list = Baseclass.open(self,"class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times \
                    and j["姓名"] == student_name:
                    for key in j:
                        print(key,j[key])
                    print("\n")
    def student_view_record(self):
        student_school = input("校名：")
        student_class = input("班级：")
        student_times = input("课次：")
        student_name = input("姓名：")
        class_record_list = Baseclass.open(self,"class_record")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times \
                    and j["姓名"] == student_name:
                    for key in j:
                        print(key,j[key])
                    print("\n")

#课程类
class Classes(Baseclass):
    def __init__(self,classes_name,classes_teachter,classes_course):
        Baseclass.__init__(self)
        self.classes_name = classes_name
        self.classes_teacher = classes_teachter
        self.classes_course = classes_course

#管理员视图，继承Admin类
class Admin_view(Admin):
    def __init__(self):
        Admin.__init__(self)
    def auth(self,username,password):
        admin_file = "%s/%s.json" %(db_admin,username)
        if os.path.isfile(admin_file):
            with open(admin_file, 'r') as f:
                admin_data = json.load(f)
            if admin_data["name"] == username and admin_data["password"] == password:
                return True
            else:
                print("用户名或密码错误")
    def login(self):
        menu = u'''
        ------- 欢迎进入管理视图 ---------
            \033[32;1m 1.  校区管理
            2.  讲师管理
            3.  学员管理
            4.  课程管理
            5.  返回
            \033[0m'''
        menu_dic = {
            '1': Admin_view.school_manager,
            '2': Admin_view.teacher_manager,
            '3': Admin_view.student_manager,
            '4': Admin_view.course_manager,
            '5': "logout",
        }
        username = input("输入用户名:").strip()
        password = input("输入密码:").strip()
        auth = Admin_view.auth(self,username,password)
        if auth:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option = input("请选择：").strip()
                if option in menu_dic:
                    if int(option) == 5:
                        exit_flag = True
                    else:
                        print(menu_dic[option])
                        menu_dic[option](self)
                else:
                    print("\033[31;1m输入错误，重新输入\033[0m")
    def school_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入校区管理 ---------
                \033[32;1m1.  创建校区
                2.  创建班级
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_school(self)
            elif int(option) == 2:
                Admin.create_classes(self)
            else:
                exit_flag = True
    def teacher_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入讲师管理 ---------
                \033[32;1m 1.  创建讲师
                2.  ...
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_teacher(self)
            elif int(option) == 2:
                print("扩展中")
            else:
                exit_flag = True

    def student_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入学员管理 ---------
                \033[32;1m 1.  创建学员
                2.  ...
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_student(self)
            elif int(option) == 2:
                print("扩展中")
            else:
                exit_flag = True
    def course_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入课程管理 ---------
                \033[32;1m 1.  创建课程
                2.  ...
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_course(self)
            elif int(option) == 2:
                print("扩展中")
            else:
                exit_flag = True

#讲师视图类，继承Teacher类
class Teacher_view(Teacher,):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        Teacher.__init__(self,teacher_name,teacher_salary,teacher_school)
    def login(self):
        menu = u'''
        ------- 欢迎进入讲师视图 ---------
            \033[32;1m  1.  创建上课记录
            2.  创建学员成绩
            3.  查看学员上课记录
            4.  查看学员成绩
            5.  返回
            \033[0m'''
        menu_dic = {
            '1': Teacher.create_class_record,
            '2': Teacher.create_class_grade,
            '3': Teacher.tacher_view_record,
            '4': Teacher.teacher_view_grade,
            '5': "logout",
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option = input("请选择：").strip()
                if option in menu_dic:
                    if int(option) == 5:
                        exit_flag = True
                    else:
                        print(menu_dic[option])
                        menu_dic[option](self)
                else:
                    print("\033[31;1m输入错误，重新输入\033[0m")

#学员视图类，继承Student类
class Student_view(Student):
    def __init__(self,student_name,student_sex,student_school,student_classes):
        Student.__init__(self,student_name,student_sex,student_school,student_classes)

    def login(self):
        menu = u'''
        ------- 欢迎进入学生管理视图 ---------
        \033[32;1m 1.  注册
        2.  交学费
        3.  查看上课记录
        4.  查看作业成绩
        5.  返回
        \033[0m'''
        menu_dic = {
            '1': Student.student_registered,
            '2': Student.student_pay_fees,
            '3': Student.student_view_record,
            '4': Student.student_view_grade,
            '5': "logout",
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option = input("请选择：").strip()
                if option in menu_dic:
                    if int(option) == 5:
                        exit_flag = True
                    else:
                        menu_dic[option](self)
                else:
                    print("\033[31;1m输入错误，重新输入\033[0m")

#程序交互类
class Run(object):
    def __init__(self):
        pass
    def interactive(self):
        menu = u'''
        ------- 欢迎进入选课系统 ---------
        \033[32;1m 1.  学生视图
        2.  讲师视图
        3.  管理视图
        4.  退出
        \033[0m'''
        menu_dic = {
            '1': Student_view,
            '2': Teacher_view,
            '3': Admin_view,
            # '4': logout,
        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            option_view = input("请选择视图：").strip()
            if option_view in menu_dic:
                if int(option_view) == 4:
                    exit_flag = True
                else:
                    menu_dic[option_view].login(self)
            else:
                print("\033[31;1m输入错误，重新输入\033[0m")

