#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/18 14:35
# @Author  : mike.liu
# @File    : 购物车_别人实现的.py

set = False   #设置set 当输入为q就可以退出
file = open("购物车用户信息档案.txt","r+",encoding="utf-8")   #读取购物车用户信息文件
f = str(file.read())   #将文件内容转化成字符串
for line in f:
    file_str = str(f)
data = eval(file_str)   #将字符串转换为字典data
print("data", data)

name = input("输入姓名：")
password = input("输入密码：")
while True:
    if name in data:            #用户在档案中
        if password in data[name]:          #密码和用户名对应，校验正确，登录。
            salary = float(data[name][password])
            print('''\033[32;1m欢迎登录，当前余额为%s\033[0m'''%salary)
            break
        else:           #否则密码错误，请重新输入
            password = input("密码错误，请重新输入：")
            continue
    else:           #否则判断为首次登录，将用户名，密码，工资存到用户信息文件中
        password_salary = {}
        salary_str = input("欢迎首次登录，请输入你的工资：")
        salary = float(salary_str)
        password_salary[password] = salary          #工资对应到密码
        data[name] = password_salary            #将密码-工资对应到用户名
        file.seek(0)
        file.write(str(data))
        file.tell()
        break

list = [#购物清单
    ["iphone",5800],
    ["sifei",800],
    ["macbook",17500],
    ["book",75],
    ["apple",5]
]

file_list_r = open("历史购物信息.txt","r+",encoding="utf-8")
file_list_r = str(file_list_r.read())
shoppinglist_dict = eval(file_list_r)
if name not in shoppinglist_dict:
    shoppinglist_dict[name] = []
shoppinglist = shoppinglist_dict[name]
shoppinglist_dict_now = []
choose = input("\n是否需要查询历史购物记录(y/n)：")
if choose == 'y':
    print("\n\n---------->历史购物记录<----------")
    print(shoppinglist)
    print("---------->结束<----------")

while not set:      #购物车开始
    print("---------->商品清单<----------")
    for index,item in enumerate(list,1):
        print(index,item)
    print("---------->结束<----------")
    number = input("请输入想购买商品编号：")
    if number == "q":
        set = True
        data[name][password] = str(salary)
        file.seek(0)
        file.write(str(data))
        file.tell()
        print("---------->购物清单<----------")
        print(shoppinglist)
        print("您的余额：",salary)
        print("---------->结束<----------")
        shoppinglist.extend(shoppinglist)
        shoppinglist_dict[name] = shoppinglist
    elif number.isdigit() == False:
        print("\033[31;1m输入不是编号内容，请重新输入\033[0m")
    elif int(number)>int(len(list)) or int(number)<= 0:         #输入值不在清单中，报错
        print("\033[31;1m您所购买的商品不在清单中\033[0m")
    else:
        number_buy = int(number)-1
        if list[number_buy][1]<(salary):            #如果余额足够，提示购买成功并显示余额。
            salary = salary - int(list[number_buy][1])
            msg = '\033[32;1m您已经将%s加入购物车中，余额为%d\033[0m'%(list[number_buy][0],salary)
            print(msg)
            shoppinglist.append(list[number_buy])           #将本次购物信息加到购买记录中
        else:
            print("\033[31;1m余额不足，无法购买!\033[0m")            #提示余额不足
