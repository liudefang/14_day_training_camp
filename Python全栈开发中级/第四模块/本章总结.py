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
# from threading import Thread
#
#
# def task(name):
#     print('%s is running' % name)
#     print('end ----')
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=task, args=('alex_%s' % i,))
#         t.start()
#
#     print('主 end ---')

# 3、请使用协程写一个消费者生产者模型；
# def consumer():
#     while True:
#         x = yield
#         print('消费：', x)
#
# def producter():
#     c = consumer()
#     next(c)
#     for i in range(10):
#         print('生产：', i)
#         c.send(i)
# producter()

# 4、写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；

# from threading import Thread,Event,currentThread
# import time
# import datetime
#
# def task():
#     event.wait(10)
#     print('线程名:%s----%s' % (currentThread().name, datetime.datetime.now()))
#
# if __name__ == '__main__':
#     event = Event()
#     for i in range(10):
#         t = Thread(target=task)
#         t.start()
#     time.sleep(10)
#     event.set()


# 5、写一个程序，包含十个线程，同时只能有五个子线程并行执行；
# 信号量
# from threading import Thread,Semaphore,currentThread
# import time
# sem = Semaphore(5)
# def task():
#     with sem:
#         print('%s in' % currentThread().getName())
#         time.sleep(2)
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=task,)
#         t.start()

# 用线程池
# from concurrent.futures import ThreadPoolExecutor
# from threading import currentThread
# import os,time
#
# def task():
#     print('name:%s in pid:%s' % (currentThread().getName(), os.getpid()))
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(5)
#     for i in range(10):
#         pool.submit(task,)
#     pool.shutdown(wait=True)


# 7、写一个程序，利用queue实现进程间通信；
# from multiprocessing import Process,current_process,Queue
# import time
#
# def consumer(q):
#     while True:
#         res = q.get()   # 接结果
#         if not res:
#             break
#         print('消费了：', res, '---', current_process().name)
#
# def producter(q):
#     for i in range(5):
#         print('生产：', i)
#         time.sleep(2)
#         q.put(i)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producter, args=(q,))
#     p2 = Process(target=producter, args=(q,))
#     c1 = Process(target=consumer, args=(q,))
#     c2 = Process(target=consumer, args=(q,))
#     c3 = Process(target=consumer, args=(q,))
#
#
#     p1.start()
#     p2.start()
#     c1.start()
#     c2.start()
#     c3.start()
#
#     p1.join()
#     p2.join()
#
#     q.put(None)
#     q.put(None)
#     q.put(None)
#     print('主')


# 8、写一个程序，利用pipe实现进程间通信；
from multiprocessing import Process, Pipe
def task(conn):
    conn.send('hello world')
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=task, args=(child_conn,))
    p.start()
    p.join()
    print(parent_conn.recv())