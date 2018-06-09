# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 21:03
# @Author  : mike.liu
# @File    : auth.py
import os
import sys
import json
from conf import settings
from core import db_handler
from lib.Baseclass import Baseclass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 登录认证


class Auth(Baseclass):
    def __init__(self):
        Baseclass.__init__(self)

    def access_login(self, useranem, password):
        db_path = db_handler.db_handler(settings.DATABASE)
        admin_file = "%s/%s.json" % (db_path, useranem)
        if os.path.isfile(admin_file):
            with open(admin_file, "r", encoding="utf-8") as f:
                admin_data = json.load(f)

            if admin_data["name"] == useranem:
                if admin_data["password"] == password:
                    print("%s登录成功" % useranem)
                    return True
                else:
                    print("用户名或密码错误!")
            else:
                print("用户名不存在!")