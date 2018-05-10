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
# http://www.51testing.com/html/08/n-3725208.html
# 员工数据表格
import os

from tabulate import tabulate

staff_db = 'staff_table.txt'
columns = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']


def print_log(msg, log_type="info"):
    if log_type == 'info':
        print('\033[32;1m%s\033[0m' % msg)
    elif log_type == 'error':
        print('\033[32;1m%s\033[0m' % msg)


# 表信息函数方法


def load_db(file_db):
    # 加载员工信息表，并转成指定的格式
    staff_data = {}
    for item in columns:
        staff_data[item] = []

    staff_info = open(file_db, 'r', encoding='utf-8')
    for line in staff_info:
        staff_id, name, age, phone, dept, enroll_date = line.split(",")
        staff_data['id'].append(staff_id)
        staff_data['name'].append(name)
        staff_data['age'].append(age)
        staff_data['phone'].append(phone)
        staff_data['dept'].append(dept)
        staff_data['enroll_date'].append(enroll_date)
    print_log(staff_data)
    return staff_data


def save_db():
    # 把内存数据存回硬盘
    f = open("%s.new" % staff_db, 'w', encoding='utf-8')
    for index, staff_id in enumerate(STAFF_DATA['id']):
        row = []
        for col in columns:
            row.append(STAFF_DATA[col][index])
        f.write("\n,".join(row))
    f.close()

    os.replace("%s.new" % staff_db, staff_db)





def op_gt(column, condtion_val):
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):
        if float(val) > float(condtion_val):    # 匹配上了
            record = []
            for col in columns:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    return matched_records


def op_lt(column, condtion_val):
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):
        if float(val) < float(condtion_val):
            record = []
            for col in columns:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)

    return matched_records


def op_eq(column, condtion_val):

    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):
        if val == condtion_val:      # 匹配上了
            record = []
            for col in columns:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    return matched_records


def op_like(column, condtion_val):

    mathed_records = []
    for index, val in enumerate(STAFF_DATA[column]):
        if condtion_val in val:     # 匹配上了

            record = []
            for col in columns:
                record.append(STAFF_DATA[col][index])
            mathed_records.append(record)
    return mathed_records


def syntax_where(clause):
    # 解析where条件，并过滤数据
    operators = {
        '>': op_gt,
        '<': op_lt,
        '=': op_eq,
        'like': op_like,
    }
    for op_key, op_func in operators.items():
        if op_key in clause:
            column, val = clause.split(op_key)
            matched_data = op_func(column.strip(), val.strip())  # 查询数据
            return matched_data
    else:
        # 只有在for执行完成，且中间被break的情况下，才执行
        # 没匹配上任何的条件公式
        print_log('语法错误:where条件只能支持[>,<,=,like]', 'error')

# 查找函数方法


def staff_find(data_set, query_clause):
    # 解析查询语句并从data_set中打印指定的列
    filter_cols_tmp = query_clause.split('from')[0][4:].split(',')
    filter_cols = [i.strip() for i in filter_cols_tmp]
    if '*' in filter_cols[0]:
        print(tabulate(data_set, headers=columns, tablefmt='grid'))
    else:
        reformat_data_set = []
        for row in data_set:
            filtered_vals = []  # 把要打印的字段放在这个列表里
            for col in filter_cols:
                col_index = columns.index(col)   # 拿到列的索引，依次取出每条记录里对应索引的值
                filtered_vals.append(row[col_index])
            reformat_data_set.append(filtered_vals)
        print(tabulate(reformat_data_set, headers=filter_cols, tablefmt='grid'))
    print_log('匹配到%s条数据!' % len(data_set))


# 增加函数方法


def staff_add(data_set, query_clause):
    column_vals = [col.strip() for col in query_clause.split('staff_table')[1].split(',')]
    print('column_vals:', column_vals)
    if len(column_vals) == len(columns[1:]):  # 不包含id，id是自增的
        init_staff_id = 0
        for i in STAFF_DATA['id']:
            if int(i) > init_staff_id:
                init_staff_id = int(i)

        init_staff_id += 1
        STAFF_DATA['id'].append(str(init_staff_id))
        for index, col in enumerate(columns[1:]):
            STAFF_DATA[col].append(column_vals[index])

    else:
        print_log('输入的新增语句字段不足，必须字段%s' % columns[1:], 'error')

    print(tabulate(STAFF_DATA, headers=columns))
    save_db()
    print_log('成功添加1条记录!')

#
# # 删除函数方法
#
#
# def staff_delete():
#     staff_value = staff_info()
#     input_del = input('请输入删除语句：')
#     id_value = input_del[input_del.rfind('=', 1) + 2:]  # 截取ID值
#
#     if input_del[:32] == ("del from staff_table where id = "):
#         data_file1 = open('staff_del', 'a+', encoding='utf-8')
#         id_value_1 = (int(id_value) - 1)  # id值减一，因为删除数组下标值是从零开始
#         del staff_value[id_value_1]
#
#         for i in staff_value:
#             str_i = ','.join(i).replace("\n", "")
#             data_file1.write(str_i)
#             data_file1.write("\n")
#
#         data_file1.flush()
#         data_file1.close()
#
#         os.remove(staff_db)  # 将原文件删除
#         os.rename("staff_del", staff_db)  # 将新文件更名为原文件名称
#
#         print("删除1条数据成功!")
#
#     else:
#         print("您输入的格式不正确！")
#
# # 修改函数方法


def staff_update(data_set, query_clause):
    # UPDATE staff_table SET age=25

    formula_raw = query_clause.split('SET')
    if len(formula_raw) > 1:   # 有set关键字
        col_name, new_val = formula_raw[1].strip().split('=')
        for matched_row in data_set:
            staff_id = matched_row[0]
            staff_id_index = STAFF_DATA['id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val
        print(STAFF_DATA)

        save_db()    # 修改后的数据保存到硬盘上
        print_log('成功修改了%s条数据!' % len(data_set))
    else:
        print_log('语法错误:未找到set关键词!', 'error')



def syntax_parser(cmd):
    # 解析数据

    syntax_list = {
        'find': staff_find,
        # 'del': staff_delete,
        'update': staff_update,
        'add': staff_add,
    }

    if cmd.split()[0] in ('find', 'add', 'update'):
        if 'where' in cmd:
            query_clause, where_clause = cmd.split('where')
            matched_records = syntax_where(where_clause)
        else:
            matched_records = []
            for index, staff_id in enumerate(STAFF_DATA['id']):
                record = []
                for col in columns:
                    record.append(STAFF_DATA[col][index])
                matched_records.append(record)
            query_clause = cmd
        cmd_action = cmd.split()[0]
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_records, query_clause)
    else:
        print_log('语法错误:\n[find\\add\del\\update] [column1,..] from [staff_table] [where] [column][>,..]'
                  '[condtion]\n', 'error')


def main():

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
                cmd = input("请输入查询条件:").strip()
                if not cmd:
                    continue

                syntax_parser(cmd.strip())

            elif choice == 2:
                print('成功进入新增功能'.center(20, '-'))
                cmd = input("请输入新增语句:").strip()
                if not cmd:
                    continue

                syntax_parser(cmd.strip())
                break
        #     # elif choice == 3:
        #     #     print('成功进入删除功能'.center(20, '-'))
        #     #     staff_delete()
        #     #     break
            elif choice == 4:
                print('成功进入修改功能'.center(20, '-'))
                cmd = input("请输入修改语句:").strip()
                if not cmd:
                    continue

                syntax_parser(cmd.strip())

        #     else:
        #         # choice > 4 or choice < 1:
        #         print("查询功能不存在,请重新输入!")
        # else:
        #     print("只能输入1-4的整数!")



if __name__ == '__main__':
    STAFF_DATA = load_db(staff_db)
    main()




