# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 21:50
# @Author  : mike.liu
# @File    : main.py
from core import logger, Manager, auth

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
            print("\033[31;1m 你选择的功能不存在!\o33[0m")


# def Student_view():
#     msg = '''\033[32;1m-------欢迎来到学生管理界面-------
#             1、 注册新学生用户
#             2、 查看上课记录
#             3、 查看作业成绩
#             4、 退出
#             \033[0m'''
#     menu_dic = {
#         "1": Student.Student.resistered,
#         "2":Student.Student.find_classrecord,
#         "3":Student.Student.find_grade,
#         "4":logout,
#     }
#     interactive(msg, menu_dic)

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
        # "3": Manager.Manager.create_school,
        "4": Manager.Manager.create_course,
        "5": Manager.Manager.show_course,
        # "6": Manager.Manager.show_shool,
        # "7": Manager.Manager.create_class,
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
        # "1": Student_viem,
        # "2": Teacher_viem,
        "3": Manager_view,
        "4": logout,
    }

    interactive(msg, menu_dic)


def login_judge():
    # 调用认证模块，返回用户文件json.load后的字典，传入access_logger日志对象

    access_data = auth.access_login(user_data, access_logger)
    if user_data['is_authenticated']:    # 如果用户认证成功
        user_data["account_data"] = access_data
