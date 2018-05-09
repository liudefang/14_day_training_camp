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
import os

staff_db = 'staff_table.txt'
columns = ['id', 'name', 'age', 'phone', 'dept', 'enrolled_date']


def print_log(msg, log_type="info"):
    if log_type == 'info':
        print('\033[32;1m%s\033[0m" %msg')
    elif log_type == 'error':
        print('\033[32;1m%s\033[0m" %msg')


# 表信息函数方法


def load_db(staff_db):
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
    num2 = input_find[input_find.rfind('>', 1) + 2:]                # 截取age>22
    num3 = input_find[input_find.rfind('where', 1) + 6:]           # 截取dept=“TT

    if num1 == '*':                                                # 判断查询语句，关键字是否为*号
        value = 'dept = "TT"'
        if value == num3:
            count = 0                                        # 计数器，每次加一
            for k in staff_value:                            # 遍历出来每个员工的信息
                if "IT" in k[4]:
                    str_i = ','.join(k).replace("\n", "")
                    str_ii = str_i.replace(',', " ")       # 将逗号替换成空格
                    print(str_ii)                         # 打印出属于IT的员工信息
                    count += 1
            print("查询到%s条语句!" % count)              # 打印出受影响的条数
        else:
            count = 0
            for k in staff_value:
                if "2013" in k[5]:
                    str_i = ','.join(k).replace("\n", "")
                    str_ii = str_i.replace(',', " ")
                    print(str_ii)
                    count += 1
            print("查询到%s条语句!" % count)
    else:
        count = 0
        for k in staff_value:
            if int(k[:][2]) > int(num2):
                print(k[1], k[2])
                count += 1
        print("查询到%s条语句!" % count)

# 增加函数方法


def staff_add():
    staff_value = staff_info()

    input_add = input("请输入新增语句:")
    input_cut = input_add[16:]
    input_list = list(input_cut.split(','))

    phone_list = []
    for i in staff_value:
        phone = i[3]
        phone_list.append(phone)

    if input_list[2] in phone_list:
        print("手机号码已存在!")
        exit()
    else:
        staff_count = (len(staff_value)+1)
        input_list.insert(0, str(staff_count))
        input_list_str = ','.join(input_list)

        staff_file = open(staff_db, 'a+', encoding='utf-8')
        staff_file.write("\n%s" % input_list_str)
        staff_file.close()

        print("新增1条数据成功!")

# 删除函数方法


def staff_delete():
    staff_value = staff_info()
    input_del = input('请输入删除语句：')
    id_value = input_del[input_del.rfind('=', 1) + 2:]  # 截取ID值

    if input_del[:32] == ("del from staff_table where id = "):
        data_file1 = open('staff_del', 'a+', encoding='utf-8')
        id_value_1 = (int(id_value) - 1)  # id值减一，因为删除数组下标值是从零开始
        del staff_value[id_value_1]

        for i in staff_value:
            str_i = ','.join(i).replace("\n", "")
            data_file1.write(str_i)
            data_file1.write("\n")

        data_file1.flush()
        data_file1.close()

        os.remove(staff_db)  # 将原文件删除
        os.rename("staff_del", staff_db)  # 将新文件更名为原文件名称

        print("删除1条数据成功!")

    else:
        print("您输入的格式不正确！")

# 修改函数方法


def staff_update():
    staff_value = staff_info()

    input_update = input('请输入修改语句：')
    if input_update[:22] == "UPDATE staff_table SET":
        num1 = input_update[:35][29:]                               # 截取dept="Market"
        num2 = input_update[:29][27:]                               # 截取age=25

        data_file1 = open('update_data', 'a+', encoding='utf-8')
        if input_update[:28] == "UPDATE staff_table SET dept=":
            count = 0
            for i in staff_value:
                if i[4] == 'IT':
                    i[4] = num1
                    count += 1

            for i in staff_value:
                str_i = ','.join(i).replace("\n", "")
                data_file1.write(str_i)
                data_file1.write("\n")

            data_file1.flush()
            data_file1.close()

            os.remove(staff_db)
            os.rename("update_data", staff_db)

            print("修改了%s条数据" % count)

        elif input_update[:27] == "UPDATE staff_table SET age=":
            count = 0
            for i in staff_value:
                if i[1] == 'Alex Li':
                    i[2] = num2
                    count += 1

            for i in staff_value:
                str_i = ','.join(i).replace("\n", "")
                data_file1.write(str_i)
                data_file1.write("\n")

            data_file1.flush()
            data_file1.close()

            os.remove(staff_db)
            os.rename("update_data", staff_db)

            print("修改了%s条数据" % count)
        else:
            print("您输入的格式不正确！")

    else:
        print("您输入的格式不正确！")

while True:
    print('''
    ***************************欢迎进入员工信息增删改查程序***************************
    1. 模糊查询  (语法： find name,age from staff_table where age > 22 
                       find * from staff_table where dept = "IT"
                       find * from staff_table where enroll_date like "2013" )
                       
    2. 新增信息  (语法： add staff_table Alex,25,134435344,IT,2015-10-29 )
    
    3. 删除信息  (语法： del from staff_table where id = 3)
    
    4. 修改信息  (语法： UPDATE staff_table SET dept="Market" WHERE dept = "IT"
                       UPDATE staff_table SET age=25 WHERE name = "Alex Li" )
******************************************************************************
    ''')
    choice = input('请选择要进入的功能：').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print('成功进入查询功能'.center(20, '-'))
            staff_find()
            break
        elif choice == 2:
            print('成功进入新增功能'.center(20, '-'))
            staff_add()
            break
        elif choice == 3:
            print('成功进入删除功能'.center(20, '-'))
            staff_delete()
            break
        elif choice == 4:
            print('成功进入修改功能'.center(20, '-'))
            staff_update()
            break
        else:
            # choice > 4 or choice < 1:
            print("查询功能不存在,请重新输入!")
    else:
        print("只能输入1-4的整数!")








