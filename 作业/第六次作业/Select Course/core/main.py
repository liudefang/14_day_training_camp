# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 21:50
# @Author  : mike.liu
# @File    : main.py
from core import logger

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


def Student_view():
    msg = '''\033[32;1m-------欢迎来到学生管理界面-------
            1、 注册新学生用户
            2、 查看上课记录
            3、 查看作业成绩
            4、 退出
            \033[0m'''
    menu_dic = {
        "1": Student.Student.resistered,
        "2":Student.Student.find_classrecord,
        "3":Student.Student.find_grade,
        "4":logout,
    }
    interactive(msg, menu_dic)


def logout():
    '''
    退出登录
    :return:
    '''
    print("\033[32;1m退出当前系统\033[0m".center(20, '-'))
    exit()
