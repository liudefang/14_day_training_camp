# -*- encoding: utf-8 -*-
# @Time    : 2018-07-22 11:10
# @Author  : mike.liu
# @File    : 增删改.py
import pymysql

# 链接
conn = pymysql.connect(host='192.168.159.128', user='root', password='pertest', database='luffycity', charset='utf8')

# 游标
cursor = conn.cursor()

# 执行sql语句
# 新增
# part1
# sql = "insert into userinfo(name,password) values ('mike','123');"
# res = cursor.execute(sql)   # 执行sql语句，返回sql影响成功的行数
# print(res)

# par2
sql = "insert into userinfo(name,password) values (%s,%s);"
res = cursor.execute(sql, ("mike2", "123"))   # 执行sql语句，返回sql影响成功的行数
print(res)

# par3,插入多行
sql = "insert into userinfo(name,password) values (%s,%s);"
res = cursor.executemany(sql, [("mike2", "123"), ("mike3", "123"), ("mike4", "123")])   # 执行sql语句，返回sql影响成功的行数
print(res)

conn.commit()   # 提交后才发现表中插入记录成功
cursor.close()
conn.close()