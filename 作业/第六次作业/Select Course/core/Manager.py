# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 22:47
# @Author  : mike.liu
# @File    : Manager.py
from core import Student, Teacher
from lib import Classes, School, Course


class Manager:
    def __init__(self):
        pass

    @staticmethod
    def create_student():
        Student.Student.resistered()

    @staticmethod
    def create_teacher():
        Teacher.Teacher.resistered()

    @staticmethod
    def create_course():
        Course.Course.create_course()

    @staticmethod
    def show_course():
        Course.Course.show_course()

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
    def show_school():
        School.School.show_school()
