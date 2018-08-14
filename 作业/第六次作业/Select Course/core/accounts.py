# -*- encoding: utf-8 -*-
# @Time    : 2018-06-06 21:53
# @Author  : mike.liu
# @File    : accounts.py

import os
import sys
import pickle


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
from core import db_handler


class MyPickle:
    def __init__(self):
        pass

    def load_account(account):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, account)
        if os.path.isfile(account_file):  # 如果用户名存在
            with open(account_file, 'rb') as f:
                account_data = pickle.load(f)
                return account_data
            f.close()
        else:
            print("\033[31;1m用户不存在!\033[0m" % account)
            exit()

    def save_account(account_dic):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, account_dic['account'])
        with open(filename, "wb") as f:
            pickle.dump(account_dic, f)

        f.close()

    def save_course(account_dic):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, account_dic['course_name'])
        with open(filename, 'wb') as f:
            pickle.dump(account_dic, f)

        f.close()

    def load_course(course_name):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, course_name)
        if os.path.isfile(account_file):  # 如果文件名存在
            with open(account_file, 'rb') as f:
                account_data = pickle.load(f)
                print("\033[34;1m--------这是您查找的课程信息----------\033[0m")
                print('\033[32;1m%s\033[0m' % account_data)
                return account_data
            f.close()
        else:
            print("\033[31;1m课程 [%s] 信息不存在!\033[0m" % course_name)
            exit()

    def save_class(name, class_name):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, name)
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(class_name)
            f.write(',')
        f.close()

    def load_class(name):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, name)
        if os.path.isfile(account_file):  # 如果用户名存在
            with open(account_file, 'r', encoding='utf-8') as f:
                account_data = f.read()
                print("----------\033[34;1m目前存在的班级\033[0m----------")
                print("\033[31;1m%s\033[0m" % account_data)
                print("-----------------------------------")
                return account_data
            f.close()
        else:
            print("\033[31;1m班级信息不存在!\033[0m" % name)
            exit()

    def save_classrecord(name, classrecord_dict):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, name)
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(classrecord_dict)
            f.write(',')
        f.close()

    def load_classrecord(name):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, name)
        if os.path.isfile(account_file):  # 如果用户名存在
            with open(account_file, 'r', encoding='utf-8') as f:
                account_data = f.read()
                print("-----------------课堂记录-------------------")
                print("\033[31;1m%s\033[0m" % account_data)
                print("-------------------------------------------")
                return account_data
            f.close()
        else:
            print("\033[31;1m上课记录信息不存在!\033[0m")
            exit()

    def save_classgrade(name, classgrade_dict):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, name)
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(classgrade_dict)
            f.write(',')
        f.close()

    def load_classgrade(name):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, name)
        if os.path.isfile(account_file):  # 如果用户名存在
            with open(account_file, 'r', encoding='utf-8') as f:
                account_data = f.read()
                print("-----------------学生成绩-------------------")
                print("\033[31;1m%s\033[0m" % account_data)
                print("-------------------------------------------")
                return account_data
            f.close()
        else:
            print("\033[31;1m成绩信息不存在!\033[0m")
            exit()

    def save_school(name, school_name):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, name)
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(school_name)
            f.write(',')
        f.close()

    def load_school(name):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, name)
        if os.path.isfile(account_file):  # 如果用户名存在
            with open(account_file, 'r', encoding='utf-8') as f:
                account_data = f.read()
                print("----------\033[34;1m目前存在的学校\033[0m----------")
                print("\033[31;1m%s\033[0m" % account_data)
                print("-----------------------------------")
                return account_data
            f.close()
        else:
            print("\033[31;1m学校不存在!\033[0m")
            exit()

    def save_coursedata(name, course_school, course_name, course_period, course_prices):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, name)
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(course_school)
            f.write(',')
            f.write(course_name)
            f.write(',')
            f.write(course_period)
            f.write(',')
            f.write(course_prices)
            f.write('\n')
        f.close()

    def load_coursedata(name):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, name)
        if os.path.isfile(account_file):  # 如果用户名存在
            with open(account_file, 'r', encoding='utf-8') as f:
                account_data = f.read()
                print("----------\033[34;1m这是已经有的课程\033[0m----------")
                print("\033[31;1m%s\033[0m" % account_data)
                print("----------------------------------------------------")
                return account_data
            f.close()
        else:
            print("\033[31;1m课程不存在!\033[0m")
            exit()
