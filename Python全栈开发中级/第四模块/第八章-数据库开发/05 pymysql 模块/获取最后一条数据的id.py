# -*- encoding: utf-8 -*-
# @Time    : 2018-07-22 11:36
# @Author  : mike.liu
# @File    : 获取最后一条数据的id.py

import pymysql

# 链接
conn = pymysql.connect(host='192.168.159.128', user='root', password='pertest', database='luffycity', charset='utf8')

# 游标
cursor = conn.cursor()

sql = 'insert into userinfo(name, password) values ("mike6", "123");'
rows = cursor.execute(sql)
print(cursor.lastrowid)     # 在插入语句后查看

conn.commit()

cursor.close()
conn.close()