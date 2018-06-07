# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 20:01
# @Author  : mike.liu
# @File    : main.py

# 管理员视图
# from core.auth import Auth
from lib.Admin import Admin


class Admin_view(Admin):
    def __init__(self):
        Admin.__init__(self)

    def login(self):
        menu = '''
        ----------欢迎进入管理员页面----------
        \033[32;1m1. 学校管理
        2. 讲师管理
        3. 学员管理
        4. 课程管理
        5. 返回
        \033[0m'''
        menu_dic = {
            "1": Admin_view.school_manager,
            "2": Admin_view.teacher_manager,
            "3": Admin_view.student_manager,
            "4": Admin_view.course_manager,
            "5": logout
        }
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        auth = Auth.access_login(self, username, password)
        if auth:
            exit_flag = False
            while not exit_flag:
                print(menu)
                user_choice = input("请选择你要进行的操作:").strip()
                if user_choice in menu_dic:
                    menu_dic[user_choice](self)
                else:
                    print("\033[31;1m你选择的功能不存在!\033[0m")

    def school_manager(self):
        exit_flag = False
        while not exit_flag:
            print('''
            ----------欢迎进入学校管理页面----------
            \033[32;1m1. 创建学校
            2.  创建班级
            3.  返回
            \033[0m''')
            user_choice = input("请选择要进行的操作:").strip()
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice == 1:
                    Admin.create_school(self)
                elif user_choice == 2:
                    Admin.create_classes(self)
                else:
                    exit_flag = True


def logout():
    '''
    退出登录
    :return:
    '''
    print("\033[32;1m退出当前系统\033[0m".center(20, '-'))
    exit()


# 程序交互类
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
            # '1': Student_view,
            # '2': Teacher_view,
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

