# -*- encoding: utf-8 -*-
# @Time    : 18-6-7 下午3:24
# @Author  : mike.liu
# @File    : Baseclass.py
import os
import sys



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
from core import db_handler

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
                
