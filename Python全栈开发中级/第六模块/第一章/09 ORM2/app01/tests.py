from django.test import TestCase

# Create your tests here.

# 帮我写个python脚本，给mysql数据库的一个表写入数据，多线程的方式插入 或者性能最好的方式，
# 表字段，有时间类型，有字符串类型，有整数类型，有浮点数类型，可以吗？
from app01 import models

# publish_obj = models.Publish.objects.create(name="邮电出版社", city="北京", email="555@qq.com")
# print(publish_obj)
import pymysql

# 链接
conn = pymysql.connect(host='10.1.2.71', user='root', password='testjfz', database='luffycity', charset='utf8')

# 游标
cursor = conn.cursor()


for i in range(5):

    # par3,插入多行
    sql = "insert into pythondb(title,publishData,author,price,publish,pages) values (%s,%s,%s,%s,%s,%s);"
    res = cursor.executemany(sql, [("测试书籍"+str(i), "2012-10-18", "测试", "55.50", "邮电出版社", 50)])   # 执行sql语句，返回sql影响成功的行数
    print(res)

conn.commit()   # 提交后才发现表中插入记录成功
cursor.close()
conn.close()