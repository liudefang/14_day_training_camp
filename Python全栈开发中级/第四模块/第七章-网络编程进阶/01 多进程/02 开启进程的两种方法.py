# -*- encoding: utf-8 -*-
# @Time    : 18-7-5 上午8:44
# @Author  : mike.liu
# @File    : 02 开启进程的两种方法.py

# Process类的介绍
"""
创建进程的类：
Process[group [, target [, name [, args [, kwargs]]]]]),由该类实例化得到的对象，可用来开启一个子进程

强调：
1.需要使用关键字的方式来指定参数
2.args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号

参数介绍
group 参数未使用，值始终为None
target 表示调用对象，即子进程要执行的任务
args 表示调用对象的位置参数元组，args=(1,2,'egon',)
kwargs 表示调用对象的字典，kwargs={‘name’：‘egon’,'age':18}
name 为子进程的名称

方法介绍：
p.start():启动进程，并调用该子进程中的p.run()
p.run():进程启动是运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法

p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么将不会被释放，进而导致死锁
p.is_alive():如果p仍然运行，返回True

p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间


属性介绍：
p.daemon: 默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置

p.name:进程的名称

p.pid ：进程的pid

三 Process类的使用
注意：在Windows中process()必须放到# if __name__ == '__main__':下
"""

# 创建并开启子进程的方式一
# import time
# import random
# from multiprocessing import Process
#
#
# def piao(name):
#     print('%s piaoing' % name)
#     time.sleep(random.randrange(1, 5))
#     print('%s piao end' % name)
#
#
# if __name__ == '__main__':
#     # 实例化得到四个对象
#     p1 = Process(target=piao, args=('egon',))   # 必须加,号
#     p2 = Process(target=piao, args=('alex',))
#     p3 = Process(target=piao, args=('wupeqi',))
#     p4 = Process(target=piao, args=('yuanhao',))
#
#     # 调用对象下的方法，开启四个进程
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     print('主进程')

# 创建并开启进程的方式二
# import time
# import random
# from multiprocessing import Process
#
#
# class Piao(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('%s piaoing' % self.name)
#
#         time.sleep(random.randrange(1,5))
#         print('%s piao end' % self.name)
#
#
# if __name__ == '__main__':
#     # 实例化得到四个对象
#     p1 = Piao('egon')
#     p2 = Piao('alex')
#     p3 = Piao('wupeiqi')
#     p4 = Piao('yuanhao')
#
#     # 调用对象下的方法，开启四个进程
#     p1.start()   # start会自动调用run
#     p2.start()
#     p3.start()
#     p4.start()
#     print('主')

# 练习题
