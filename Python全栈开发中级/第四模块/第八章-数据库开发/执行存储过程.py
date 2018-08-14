# -*- encoding: utf-8 -*-
# @Time    : 2018-07-22 15:02
# @Author  : mike.liu
# @File    : 执行存储过程.py

import pymysql
# 链接
conn = pymysql.connect(host='192.168.159.128', user='root', password='pertest', database='luffycity', charset='utf8')

# 游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行存储过程
cursor.callproc('p1', args=(1, 22, 3, 4))

# 获取执行完存储的参数
cursor.execute("select @_p1_0,@_p1_1,@p1_3")
result = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()

print(result)
