#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/9 9:33
# @Author  : mike.liu
# @File    : 格式化输出.py

name = input("Name:")
age = input("Age:")
job = input(str("Job:"))
hometown = input(str("Hometown:"))

info = """
---------------info of %s-------------
Name:          %s
Age:           %s
Job:           %s
Hometown:      %s
"""  %(name,name,age,job,hometown)

print("info:",info)
