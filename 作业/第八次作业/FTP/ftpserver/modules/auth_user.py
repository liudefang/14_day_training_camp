# -*- encoding: utf-8 -*-
# @Time    : 18-6-11 上午10:25
# @Author  : mike.liu
# @File    : auth_user.py
import os
import json
import hashlib

from FTP.ftpserver.core.Log import *
from FTP.ftpserver.conf import settings


class User_operation():
    '''对登录信息进行认证，登录成功返回用户名，失败返回None'''
    def authentication(self, login_info):
        user_list = login_info.split(":")    # 对信息进行分割
        login_name = user_list[0]
        login_password = self.hash(user_list[1])
        DB_FILE = settings.DATABASE + r"/%s.db" % login_name
        if os.path.isfile(DB_FILE):
            user_data = self.cat_database(DB_FILE)      # 用户数据库信息
            if login_name == user_data["username"]:
                if login_password == user_data["password"]:

                    return user_data
                else:
                    logging.info("用户名或密码错误,请重新输入!")

            else:
                logging.info("用户名不存在!")

        else:
            logging.info("该用户目录不存在!")

    def cat_database(self, DB_FILE):
        # 获取数据库信息
        with open(DB_FILE, "r", encoding="utf-8") as file:
            data = json.loads(file.read())
            return data

    def hash(self, password):
        '''对密码进行md5加密'''
        m = hashlib.md5()
        m.update(password.encode("utf-8"))
        return m.hexdigest()
