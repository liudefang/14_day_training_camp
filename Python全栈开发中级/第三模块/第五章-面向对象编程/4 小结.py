# -*- encoding: utf-8 -*-
# @Time    : 2018-06-08 20:20
# @Author  : mike.liu
# @File    : 4 小结.py
from pymysql import connect


class mysqlhandler:
    def __init__(self, host, port, db, charset="utf-8"):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset
        self.conn = connect(self.host, self.port, self.db, self.charset)

    def exc1(self, sql):
        return self.conn.execute(sql)

    def exc2(self, sql):
        return self.conn.call_proc(sql)


obj = mysqlhandler('127.0.0.1', 3306, 'db1')
obj.exc1('select * from tab1')
obj.exc2('存储过程的名字')


class chinese:
    country = 'China'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        info = '''
        国籍:%s
        姓名:%s
        年龄:%s
        性别:%s
        ''' % (self.country, self.name, self.age, self.sex)
        print(info)


p1 = chinese('egon', 18, 'male')
p2 = chinese('alex', 33, 'female')
p3 = chinese('wpq', 50, 'female')

print(p1.country)
p1.tell_info()