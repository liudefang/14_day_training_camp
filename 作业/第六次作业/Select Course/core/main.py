# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 21:50
# @Author  : mike.liu
# @File    : main.py
from core import logger, Manager,  Student, Teacher

# 初始化账号数据


user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None

}

# 日志记录到文件中
access_logger = logger.logger('system')


def interactive(msg, menu_dic):
    exit_flag = False
    while not exit_flag:
        print(msg)
        user_choice = input("请选择你要进行的操作:").strip()
        if user_choice in menu_dic:
            menu_dic[user_choice]()
        else:
            print("\033[31;1m你选择的功能不存在!\033[0m")


def Student_view():
    msg = '''\033[32;1m-------欢迎来到学生管理界面-------
            1、 注册新学生用户
            2、 查看上课记录
            3、 查看作业成绩
            4、 退出
            \033[0m'''
    menu_dic = {
        "1": Student.Student.resistered,
        "2": Student.Student.find_classrecord,
        "3": Student.Student.find_grade,
        "4": logout,
    }
    interactive(msg, menu_dic)


def Teacher_view():
    msg = '''\033[32;1m-------欢迎来到老师管理页面------
            1   创建新讲师
            2   创建学生上课情况
            3   创建学生考试成绩
            4   logout
    \033[0m'''
    menu_dic = {
        "1": Teacher.Teacher.resistered,
        "2": Teacher.Teacher.create_classrecord,
        "3": Teacher.Teacher.create_grade,
        "4": logout,
    }
    interactive(msg, menu_dic)

# 管理员视图
def Manager_view():
    msg = '''\033[32;1m----------欢迎来到管理员页面----------
            1. 创建讲师
            2. 创建学生
            3. 创建学校
            4. 创建课程
            5. 查看课程
            6. 查看学校
            7. 创建班级
            8. 查看班级
            9. 退出
            \033[0m'''
    menu_dic = {
        # "1": Manager.Manager.create_teacher,
        # "2": Manager.Manager.create_student,
        "3": Manager.Manager.create_school,
        "4": Manager.Manager.create_course,
        "5": Manager.Manager.show_course,
        "6": Manager.Manager.show_school,
        "7": Manager.Manager.create_class,
        # "8": Manager.Manager.show_class,
        "9": logout,
    }

    interactive(msg, menu_dic)


def logout():
    '''
    退出登录
    :return:
    '''
    print("\033[32;1m退出当前系统\033[0m".center(20, '-'))
    exit()


def begin():
    '''
    开始入口
    :return:
    '''
    msg = '''\033[32;1m----------欢迎登录学生选课系统----------
            1. 学生管理
            2. 老师管理
            3. 后台管理
            4. 退出系统
        \033[0m'''
    menu_dic = {
        "1": Student_view,
        "2": Teacher_view,
        "3": Manager_view,
        "4": logout,
    }

    interactive(msg, menu_dic)
