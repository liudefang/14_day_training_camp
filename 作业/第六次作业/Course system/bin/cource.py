# -*- encoding: utf-8 -*-
# @Time    : 18-6-7 下午3:15
# @Author  : mike.liu
# @File    : cource.py

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    a = main.Run()
    a.interactive()