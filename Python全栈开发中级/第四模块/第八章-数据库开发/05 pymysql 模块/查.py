# -*- encoding: utf-8 -*-
# @Time    : 2018-07-22 11:28
# @Author  : mike.liu
# @File    : 查.py

import pymysql

# 链接
conn = pymysql.connect(host='192.168.159.128', user='root', password='pertest', database='luffycity', charset='utf8')

# 游标
cursor = conn.cursor()

# 执行sql语句
sql = 'select * from userinfo;'
rows = cursor.execute(sql)  # 执行sql语句，返回sql影响成功的行数rows，将结果放入一个集合，等待被查询

# cursor.scroll(3, mode='absolute')   # 相对均对位置移动
# cursor.scroll(3, mode='relative')   # 相对当前位置移动

res1 = cursor.fetchone()
res2 = cursor.fetchone()
res3 = cursor.fetchone()
res4 = cursor.fetchmany(2)
res5 = cursor.fetchall()
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print('%s row in set(0.00 sec)' % rows)

conn.commit()
cursor.close()
conn.close()