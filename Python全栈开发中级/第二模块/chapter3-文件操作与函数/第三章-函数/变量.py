# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 12:37
# @Author  : mike.liu
# @File    : 变量.py
name = 'mike'

def change_name():
    global name
    #print('before change:', name)
    name = 'mike,很拉风的男人'
    print('after change:', name)

change_name()
print('在外面看看name改了么?', name)