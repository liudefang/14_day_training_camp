# -*- encoding: utf-8 -*-
# @Time    : 18-5-20 下午4:28
# @Author  : mike.liu
# @File    : authentication.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
__db_user_dict = BASE_DIR + r"\db\users_dict"
__db_creditcard_dict = BASE_DIR + r"\db\creditcard_dict"

'''认证装饰器'''
