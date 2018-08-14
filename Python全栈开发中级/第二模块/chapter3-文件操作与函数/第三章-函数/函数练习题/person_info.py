# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 22:01
# @Author  : mike.liu
# @File    : person_info.py

def print_person_info(accounts):
    info = """
--------个人信息如下--------
Username:   %s
Age:        %s
position:   %s
dept:       %s
phone:      %s
"""   % (accounts[username][2],
         accounts[username][3],
         accounts[username][4],
         accounts[username][5],
        accounts[username][6])

    print(info)
