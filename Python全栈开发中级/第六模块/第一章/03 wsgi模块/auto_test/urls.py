# -*- encoding: utf-8 -*-
# @Time    : 18-9-5 下午7:23
# @Author  : mike.liu
# @File    : urls.py

from app01.views import *


URLpattern = (
    ("/login", login),
    ("/favicon.ico", fav),
)