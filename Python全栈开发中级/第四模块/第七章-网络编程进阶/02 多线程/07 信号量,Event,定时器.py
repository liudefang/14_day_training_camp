# -*- encoding: utf-8 -*-
# @Time    : 18-7-11 下午4:33
# @Author  : mike.liu
# @File    : 07 信号量,Event,定时器.py

# from threading import Thread, Semaphore
# import threading
# import time
#
# def func():
#     sm.acquire()
#     print('%s get sm' % threading.current_thread().getName())
#     time.sleep(3)
#     sm.release()
#
#
# if __name__ == '__main__':
#     sm = Semaphore(5)
#     for i in range(23):
#         t = Thread(target=func)
#         t.start()

#
# from threading import Event
# Event.isSet()   # 返回Event的状态值
# Event.wait()    # 如果event.isSet()==False将阻塞线程；
# Event.set()     # 设置Event的状态值为True，所有阻塞池的线程激活进入就绪状态，等待操作系统调度
# Event.clear()   # 恢复Event的状态值为False

# from threading import Thread, Event
# import threading
# import time, random
# def conn_mysql():
#     count = 1
#     while not event.is_set():
#         if count > 3:
#             raise TimeoutError('链接超时')
#         print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
#         event.wait(0.5)
#         count += 1
#     print('<%s>链接成功' % threading.current_thread().getName())
#
# def check_mysql():
#     print('\033[45m[%s] 正在检查mysql\033[0m' % threading.current_thread().getName())
#     time.sleep(random.randint(2, 4))
#     event.set()
#
#
# if __name__ == '__main__':
#     event = Event()
#     conn1 = Thread(target=conn_mysql)
#     conn2 = Thread(target=conn_mysql)
#     check = Thread(target=check_mysql)
#
#     conn1.start()
#     conn2.start()
#     check.start()

from threading import Timer

def hello():

    print('hello, world')

t = Timer(1, hello)
t.start()