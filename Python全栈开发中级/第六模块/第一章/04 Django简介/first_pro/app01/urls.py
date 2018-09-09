# -*- encoding: utf-8 -*-
# @Time    : 18-9-7 下午3:48
# @Author  : mike.liu
# @File    : urls.py
from django.urls import re_path
from app01 import views
app_name = 'app01'
urlpatterns = [
    re_path("index/", views.index, name="index"),
]