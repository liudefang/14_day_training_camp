# -*- encoding: utf-8 -*-
# @Time    : 18-7-12 上午11:19
# @Author  : mike.liu
# @File    : 03 gevent模块.py

# 遇到IO阻塞时会自动切换任务
from gevent import monkey;monkey.patch_all()
import gevent
import time

def eat(name):
    print('%s eat 1' % name)
    time.sleep(2)
    print('%s eat 2' % name)

def play(name):
    print('%s play 1' % name)
    time.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'mike')
g2 = gevent.spawn(play, 'mike')
g1.join()
g2.join()

print('主')