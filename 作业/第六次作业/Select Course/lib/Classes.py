# -*- encoding: utf-8 -*-
# @Time    : 2018-06-06 22:51
# @Author  : mike.liu
# @File    : Classes.py
from core import accounts


class Classes:
    def __init__(self):
        pass

    @staticmethod
    def create_class():
        name = "class"
        print("\033[32;1m欢迎来到班级创建页面".center(20, '-'))

        class_name = input("请输入班级名称:").strip()
        accounts.MyPickle.save_class(name, class_name)
        print("\033[34;1m创建[%s]班级成功\033[0m" % class_name)

    @staticmethod
    def show_class():
        print("\033[32;1m欢迎来到班级查看页面".center(20, '-'))
        name = "class"
        accounts.MyPickle.load_class(name)
