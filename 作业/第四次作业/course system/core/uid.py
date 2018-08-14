# -*- encoding: utf-8 -*-
# @Time    : 2018-06-07 23:21
# @Author  : mike.liu
# @File    : uid.py

import hashlib
import time

def create_md():
    m = hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()
