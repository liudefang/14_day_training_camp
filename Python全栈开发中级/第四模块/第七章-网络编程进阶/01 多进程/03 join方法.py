# -*- encoding: utf-8 -*-
# @Time    : 18-7-6 上午8:29
# @Author  : mike.liu
# @File    : 03 join方法.py

from multiprocessing import Process
import time
import random


def task(name):
    print('%s is piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s is piao end' % name)


if __name__ == '__main__':
    # p1 = Process(target=task, args=('egon',))
    # p2 = Process(target=task, args=('alex',))
    # p3 = Process(target=task, args=('yuanhao',))
    # p4 = Process(target=task, args=('wupeiqi',))

    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    #
    # # 会有疑问：既然join是等待进程结束，那么我像下面这样写，进程不就又变成串行的吗？
    # # 当然不是了，必须明确：p.join()是让谁等？
    # # 很明显p.join()是让主进程等待p的结束，卡住是主进程而绝非子进程p，
    # p1.join()    # 等待p停止，才执行下一行代码
    # p2.join()
    # p3.join()
    # p4.join()

    # p_l = [p1, p2, p3, p4]
    #
    # for p in p_l:
    #     p.start()
    #
    # for p in p_l:
    #     p.join()

    # p1 = Process(target=task, args=('egon',))
    # p1.start()
    #
    # p1.terminate()  # 关闭进程，不会立即关闭，所以is_alive立刻查看的结果可能还是存活
    # print(p1.is_alive())    # 结果为True
    #
    # print('主进程')
    # print(p1.is_alive())    # 结果为False

    # 进程对象的其它属性：name和pid
    p1 = Process(target=task, args=('egon',), name='子进程1')      # 可以用关键参数来指定进程名
    p1.start()

    print(p1.name, p1.pid)