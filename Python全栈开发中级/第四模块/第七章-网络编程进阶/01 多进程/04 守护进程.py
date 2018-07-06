# -*- encoding: utf-8 -*-
# @Time    : 18-7-6 上午9:35
# @Author  : mike.liu
# @File    : 04 04 守护进程.py

from multiprocessing import Process
import time
import random

def task(name):
    print('%s is piaoing' % name)
    time.sleep(random.randrange(1, 3))
    print('%s is piao end' % name)

if __name__ == '__main__':
    p = Process(target=task, args=('egon',))
    p.daemon=True   # 一定要在p.start()前设置，设置p为守护进程，禁止p创建子进程，并且父进程代码执行结束，p即终止运行
    p.start()
    print('主')  # 只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了