# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 下午12:29
# @Author  : mike.liu
# @File    : ftpserver.py
import logging
import os
import json

from FTP.ftpserver.conf import settings
from FTP.ftpserver.modules import auth_user


def create_db():
    '''创建数据库文件'''
    logging.info("创建数据库文件开始")
    user_data = {}
    encryption = auth_user.User_operation()
    limitsize = settings.LIMIT_SIZE
    for k, v in settings.USERS_PWD.items():
        username = k
        password = encryption.hash(v)
        # password = v
        user_db_path = settings.DATABASE + r"\%s.db" % username
        user_home_path = 'home' + r"\%s" % username
        user_data["username"] = username
        user_data["password"] = password
        user_data["limitsize"] = limitsize
        user_data["homepath"] = user_home_path
        if not os.path.isfile(user_db_path):
            with open(user_db_path, "w", encoding="utf-8") as file:
                file.write(json.dumps(user_data))
                # print("创建数据库文件%s成功!" % username)
                logging.info("创建数据库文件%s成功!" % username)

        else:
            logging.info("该数据库文件已经存在!")


def create_dir():
    '''创建用户宿主目录'''
    for username in settings.USERS_PWD:
        user_home_path = settings.HOME_PATH + r"\%s" % username
        if os.path.isdir(user_home_path):
            logging.info("该目录已经存在!")
        else:
            os.makedirs(user_home_path)
            logging.info("创建用户宿主目录【%s】成功!" % user_home_path)
