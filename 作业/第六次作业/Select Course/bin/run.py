# -*- encoding: utf-8 -*-
# @Time    : 2018-06-05 21:41
# @Author  : mike.liu
# @File    : run.py

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    main.begin()
