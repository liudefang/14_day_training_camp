#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 1.可进行模糊查询，语法至少支持下面3种查询语法:
#
# find name,age from staff_table where age > 22
#
# find * from staff_table where dept = "IT"
#
# find * from staff_table where enroll_date like "2013"
# 2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
#
# 语法: add staff_table Alex Li,25,134435344,IT,2015-10-29
# 3.可删除指定员工信息纪录，输入员工id，即可删除
#
# 语法: del from staff_table where  id=3
# 4.可修改员工信息，语法如下:
#
# UPDATE staff_table SET dept="Market" WHERE  dept = "IT" 把所有dept=IT的纪录的dept改成Market
# UPDATE staff_table SET age=25 WHERE  name = "Alex Li"  把name=Alex Li的纪录的年龄改成25
# 5.以上每条语名执行完毕后，要显示这条语句影响了多少条纪录。 比如查询语句 就显示 查询出了多少条、修改语句就显示修改了多少条等。

# 员工数据表格
staff_db = 'staff_table.txt'

# 定义数据格式为列表
staff_order = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']


# 表信息函数方法
def staff_info():
    staff_info = open('staff_table.txt', 'r+', encoding='utf-8')
    staff = staff_info.readlines()

    staff_list = []
    for i in staff:
        staff_list.append(str(i).split(','))

    # 将txt文本文件信息转换成一个数组，每次调用此方法将返回数组
    return staff_list

# 查找函数方法
def staff_find():
    staff_value = staff_info()
    input_find = input("请输入查询语句:").strip()
    num1 = input_find[0:input_find.rfind('from', 0) + -1][5:]      # 截取 name,age格式
    num2 = input_find[input_find.rfind('>', 1)+ 2:]                # 截取age>22
    num3 = input_find[input_find.rfind('where', 1) + 6:]           # 截取dept=“TT

    if num1 == '*':                                                # 判断查询语句，关键字是否为*号
        value = 'dept = "TT"'
        if value == num3:
            count = 0
            for k in k[4]:
                if "TT"


