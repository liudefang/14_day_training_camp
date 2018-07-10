# -*- encoding: utf-8 -*-
# @Time    : 2018-07-08 12:45
# @Author  : mike.liu
# @File    : 01 开启线程的两种方式.py

# 方式一
# from threading import Thread
# import time
#
#
# def sayhi(name):
#     time.sleep(2)
#     print("%s say hello" % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=sayhi, args=('mike', ))
#     t.start()
#     print("主线程")

# 方式二
from threading import Thread
import time


class Sayhi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('mike')
    t.start()
    print("主线程")