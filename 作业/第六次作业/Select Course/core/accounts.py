# -*- encoding: utf-8 -*-
# @Time    : 2018-06-06 21:53
# @Author  : mike.liu
# @File    : accounts.py

import os
import sys
import pickle,json
import logging



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
        if os.path.isfile(account_file):
            with open(account_file, "rb", encoding="utf-8") as f:
                account_data = pickle.load(f)
                return account_data
        else:
            print("\033[31;1m用户名信息不存在!\033[0m" % account)
            exit()

    # 保存学校信息
    def save_school(name, school_name):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = '%s/%s' % (db_path, name)
        with open(filename, 'a+', encoding="utf-8") as f:
            f.write(school_name)
            f.write(',')

    # 查看学校信息
    def load_school(name):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, name)
        if os.path.isfile(account_file):
            with open(account_file, 'r', encoding="utf-8") as f:
                account_data = f.readlines()
                print("\033[34;1m目前存在的学校\033[0m".center(20, '-'))
                print("\033[31;1m%s\033[0m" % account_data)
                return account_data
        else:
            print("\033[31;1m学校不存在\033[0m")
            exit()