# -*- encoding: utf-8 -*-
# @Time    : 18-7-10 上午9:30
# @Author  : mike.liu
# @File    : 04 守护线程.py
#
# from threading import Thread
# import time
#
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=sayhi, args=('mike', ))
#     t.setDaemon(True)   # 必须在t.start()之前设置
#     t.start()
#
#     print('主线程')
#     print(t.is_alive())


from threading import Thread
import time

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)


    t1.daemon = True
    t1.start()
    t2.start()
    print("main-----")