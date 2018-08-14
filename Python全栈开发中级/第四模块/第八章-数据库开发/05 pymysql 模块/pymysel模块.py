# -*- encoding: utf-8 -*-
# @Time    : 2018-07-21 22:41
# @Author  : mike.liu
# @File    : pymysel模块.py

import pymysql
user = input('用户名:').strip()
pwd = input('密码:').strip()

# 链接
conn = pymysql.connect(host='192.168.159.128', user='root', password='pertest', database='luffycity', charset='utf8')
# 游标
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示


# 执行sql语句
# sql='select * from userinfo where name="%s" and password = "%s"' % (user, pwd)
# print(sql)
# res = cursor.execute(sql)   # 执行sql语句，返回sql查询成功的记录数目
# print(res)
sql = "select * from userinfo where name =%s and password=%s"   # 注意%s需要去掉引号，
# 因为pymysql 会自动为我们加上
res = cursor.execute(sql,[user,pwd])    # pymysql模块自动帮我们解决sql注入的问题
print(res)

cursor.close()
conn.close()


if res:
    print('登录成功')
else:
    print('登录失败')
