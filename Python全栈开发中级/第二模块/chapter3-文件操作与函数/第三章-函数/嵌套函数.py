# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 13:18
# @Author  : mike.liu
# @File    : 嵌套函数.py

name = 'mike'

def change_name():
    name = 'mike.liu'

    def change_name2():
        name = 'TOM'
        print('第三层打印:', name)

    change_name2()   # 调用内层函数
    print('第二层打印:', name)

change_name()
print('最外层打印:', name)