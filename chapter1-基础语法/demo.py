#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/11 17:16
# @Author  : mike.liu
# @File    : demo·.py
f = open("user.txt",'r')
for line in f.readlines():
    print("line:", line)