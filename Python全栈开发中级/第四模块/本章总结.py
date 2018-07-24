# -*- encoding: utf-8 -*-
# @Time    : 2018-07-24 21:51
# @Author  : mike.liu
# @File    : 本章总结.py
#
# import pymysql
#
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port='3306',
#     user='root',
#     password='123',
#     db='db_bj',
#     charset='utf-8'
#
# )
# cursor = conn.cursor()
# sql = 'insert into student(sname,credit,class_id) values (%s,%s,%s)'
# rows = cursor.execute(sql,('alcie','123',1))
#
# conn.commit()
# cursor.close()
# conn.close()
#
# if rows:
#     print('成功')
# else:
#     print('失败')


# mysqldump -uroot -p123 db_bj student > /home/**.sql
# 创建触发器
# delimiter //
# create trigger tri_after_student after insert on student for each row
#     begin
#     insert into student insert_log values(new.ID,now());
# end //
# delimiter;

# 1、请写一个包含10个线程的程序，主线程必须等待每一个子线程执行完成之后才结束执行，每一个子线程执行的时候都需要打印当前线程名、当前活跃线程数量；
# from threading import Thread,currentThread,activeCount
#
# import time
# def task(n):
#     print('线程名:%s----%s' % (currentThread().name,n))
#     time.sleep(2)
#     print('数量:%s' % activeCount())
#
# if __name__ == '__main__':
#     t_li = []
#     for i in range(10):
#         t = Thread(target=task, args=(i,))
#         t.start()
#         t_li.append(t)
#     for t in t_li:
#         t.join()
#
#     print('主')

# 2、请写一个包含10个线程的程序，并给每一个子线程都创建名为"name"的线程私有变量，变量值为“Alex”；
from threading import Thread


def task(name):
    print('%s is running' % name)
    print('end ----')


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task, args=('alex_%s' % i,))
        t.start()

    print('主 end ---')