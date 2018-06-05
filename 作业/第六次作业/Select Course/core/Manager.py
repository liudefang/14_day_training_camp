# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 22:47
# @Author  : mike.liu
# @File    : Manager.py
from core import Student


class Manager:
    def __init__(self):
        pass

    @staticmethod
    def create_student():
        Student.Student.resistered()

    @staticmethod
    def create_class():
        Classes.Classes.create_class()

    @staticmethod
    def show_class():
        Classes.Classes.show_class()

    @staticmethod
    def create_school():
        School.School.create_school()

    @staticmethod
    def show_shool():
        School.Shool.show_school()