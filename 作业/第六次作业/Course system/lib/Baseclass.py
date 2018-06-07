# -*- encoding: utf-8 -*-
# @Time    : 18-6-7 下午3:24
# @Author  : mike.liu
# @File    : Baseclass.py
import os
import sys
import pickle

from conf import settings
from core import db_handler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


# 基础类，主要包括文件的读写操作
class Baseclass(object):
    def __init__(self):
        pass

    def save(self, type, dict):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = uid.create_md()
        dict['uid'] = filename
        file_path = "%s/%s" % (db_path, type)
        ab_file = "%s/%s" % (file_path, filename)
        if os.path.isfile(file_path):
            with open(ab_file, "wb", encoding="utf-8") as f:
                f.write(pickle.dumps(dict))
                if True:
                    print("\033[32;1m%s创建成功!\033[0m" % type)
                    for key in dict:
                        print(key, ":\t", dict[key])

    def seek_list(self, type, list):
        db_path = db_handler.db_handler(settings.DATABASE)
        filename = uid.create_md()
        dict['uid'] = filename
        file_path = "%s/%s" % (db_path, type)
        ab_file = "%s/%s" % (file_path, filename)
        if os.path.isfile(file_path):
            with open(ab_file, "wb", encoding="utf-8") as f:
                f.write(pickle.dumps(list))
                if True:
                    print("\033[32;1m%s创建成功!\033[0m" % type)
                    for key in list:
                        print(key, ":\t", dict[key])
                        print("\n")
        return True

    def open(self, type):
        all_data = []
        db_path = db_handler.db_handler(settings.DATABASE)
        file_path = "%s/%s" % (db_path, type)
        for i in os.listdir(file_path):
            if os.path.isfile(os.path.join(file_path, i)):
                db_file = os.path.join(file_path, i)
                with open(db_file, "rb", encoding="utf-8") as f:
                    file_dict = pickle.load(f)
                    all_data.append(file_dict)
        return all_data
