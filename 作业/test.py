# -*- encoding: utf-8 -*-
# @Time    : 2018-04-16 22:27
# @Author  : mike.liu
# @File    : 第九次作业.py
# f = open('D:\\Python\\14_day_training_camp\\一周感想.txt', mode='r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
#     {"name": "飞机", "price": 9999}
# ]
# for index,items in enumerate(goods):
#     print(index,items)
#     commodity = int(input("input goods what your want to buy:"))
#     if commodity == 1:
#         price = goods[commodity]['price']
#         print("price:",price)

#print(goods[].values())

# shop_cart = {{"name": "电脑", "price": 1999}}
# shop_cart.append({"username":"tom"})
# print(shop_cart)
# staff_info = open('staff_table.txt', 'r+', encoding='utf-8')
# staff = staff_info.readlines()
#
# staff_list = []
# for i in staff:
#     staff_list.append(str(i).split(','))
#     print(staff_list)

# print(3000*0.0049*10000)
#

# query_clause = 'update staff_table set age=25 where name="Alex Li"'
# formula_str = query_clause.split("set")
# col_name, new_val = formula_str[-1].strip().split('=')
# print(col_name, new_val)
query_clause = 'update staff_table set age=25 where name="Alex Li" '

if "set" in query_clause:


    formula_str = query_clause.split("set")
    where = formula_str[1].split('where')
    col_name, new_val = where[0].split('=')
print('formula_str:',formula_str)
print('where:', where)
print('col_name:', col_name)
print('new_val:', new_val)
# STAFF_INFO[col_name]
# if new_val.find("'") == 0:
#     new_val = new_val.replace("'", "")
# elif new_val.find("\"") == 0:
#     new_val = new_val.replace("\"", "")
# for row in dataset:
#     staff_id = row[0]  # 得到id值
#     staff_index = STAFF_INFO['id'].index(staff_id)  # 得到id值在STAFF_INFO[id]的索引
#     STAFF_INFO[col_name][staff_index] = new_val  # 修改col_name值
# # print_log(STAFF_INFO)
#     save_db()
#     print("成功修改了%s条数据!" % len(dataset))
# else:
#     print("语法错误，未检测到set", "error")