# -*- encoding: utf-8 -*-
# @Time    : 2018-06-13 22:00
# @Author  : mike.liu
# @File    : settings.py
import sys
import os
# 主程序目录文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.insert(0, BASE_DIR)

HOST = '127.0.0.1'
PORT = 3306
DB_PATH = os.path.join(BASE_DIR, "第五章-面向对象编程")
print(DB_PATH)