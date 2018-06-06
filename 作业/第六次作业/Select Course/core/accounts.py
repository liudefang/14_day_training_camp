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


class MyPicke:
    def __init__(self):
        pass


    def load_account(self, account):
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = '%s/%s' % (db_path, account)
        if os.path.isfile(account_file):
            with open(account_file, "rb", encoding="utf-8") as f:
                account_data = pickle.load(f)
                return account_data
        else:
            print("\033[31;1m用户名信息不存在!\033[0m" % account)
            exit()

