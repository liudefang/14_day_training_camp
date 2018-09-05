# -*- encoding: utf-8 -*-
# @Time    : 18-9-5 上午9:01
# @Author  : mike.liu
# @File    : models.py.py

import pymysql
# 连接数据库
conn = pymysql.connect(host='10.1.2.71', port=3306, user='root', passwd='testjfz', db='blog') #db：库名
#创建游标
cur = conn.cursor()


# sql='''
# create table userinfo(
#         id int primary key,
#         name varchar(32),
#         password varchar(32)
#         )'''


# cur.execute(sql)
# sql = "insert into userinfo values (%s,%s,%s)"
# var = [(1, 'mike', 123), (2, 'tom', 123)]
# cur.executemany(sql, var)
sql = ("select * from userinfo where name='mike'")
cur.execute(sql)

# 提交
conn.commit()
# 关闭指针对象
cur.close()
# 关闭连接对象
conn.close()