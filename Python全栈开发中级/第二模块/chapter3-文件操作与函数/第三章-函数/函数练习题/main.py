# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 14:45
# @Author  : mike.liu
# @File    : main.py
# 修改个人信息程序
#
# 在一个文件里存多个人的个人信息，如以下
#
# username password  age position department
# alex     abc123    24   Engineer   IT
# rain     df2@432    25   Teacher   Teching
# ....
# 1.输入用户名密码，正确后登录系统 ，打印
#
#     1. 修改个人信息
#     2. 打印个人信息
#     3. 修改密码
#
# 2.每个选项写一个方法
#
# 3.登录时输错3次退出程序


def print_person_info(accounts):
    info = """
--------个人信息如下--------
Username:   %s
Age:        %s
position:   %s
dept:       %s
phone:      %s
""" % (accounts[username][2],
        accounts[username][3],
        accounts[username][4],
        accounts[username][5],
        accounts[username][6])

    print(info)


accounts = {}

user_list = 'account.txt'
f = open(user_list, 'r+', encoding='utf-8')
user_data = f.readlines()
for line in user_data:
    if not line.startswith('#'):
        line = line.strip()
        items = line.split(',')
        accounts[items[0]] = items
f.close()
print('account:', accounts)


count = 0
while count < 3:
    username = input('请输入用户名:').strip()
    password = input('请输入密码:').strip()
    if username in accounts:
        if password == accounts[username][1]:
            print('欢迎登录成功, %s' % username)
            while True:
                print('进行如下操作'.center(20, '-'),
                """
                    1. 打印个人信息
                    2. 修改个人信息
                    3. 修改密码
                    """)
                choice = input('请选择要操作的序号:').strip()
                choice = int(choice)
                if choice == 1:
                    print('打印个人信息')
                    print_person_info(accounts)
                elif choice == 2:
                    print('修改个人信息')
                elif choice == 3:
                    print('修改密码!')
                elif choice == 'q':
                    exit('退出系统')
                else:
                    print('序号不存在')

        else:
            print('用户名或密码错误,请重新输入!')
        count += 1
    else:
        print('用户名不存在!')

else:
    print('错误次数太多了,请稍后再试!')