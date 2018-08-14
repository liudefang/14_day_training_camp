# -*- encoding: utf-8 -*-
# @Time    : 2018-07-14 8:03
# @Author  : mike.liu
# @File    : 练习题.py

# 1、简述计算机操作系统中的“中断”的作用？
"""
中断装置由一些特定的寄存器和控制线路组成，中央处理器和外围设备等识别到的事件保存在特定的寄存器中
中央处理器每执行完一条命令，均由中断装置判别是否有事件发生
若无事件发生，CPU继续执行
若有事件发生，则中断装置中断原有CPU的程序的执行，让操作系统的处理事件服务程序占用CPU，
对出现的事件进行处理，事件处理完后，再让原来的程序继续占用CPU执行

中断是指计算机在执行期间，系统内发生任何非寻常的或非预期的急需处理事件，使得CPU暂时中断
当前正在执行的程序，转去执行相应的事件处理程序，待处理完后有返回原来被中断处继续执行或
调度新的进程执行的过程，它使计算机考研更好利用有限的系统资源解决系统响应速度和运行效率
的一种控制技术，实时响应，系统调度
"""
# 2、简述计算机内存中的“内核态”和“用户态”；
"""
内核态：运行于内核态，管理硬件资源，运行操作系统的程序，os的数据存放
用户态：系统调用（运行于用户态，为应用程序提供系统调用的接口）
用户态的应用程序可以通过三种方式来访问内核态的资源：
1、系统调用
2、库函数
3、shell脚本
用户态到内核态的切换：
1、系统调用：用户程序主动发起的软中断os.fork() process
2、异常：被动的，当CPU正在执行运行在用户态的程序时，突然发生某些预先不可知的异常事件，这个
时候就会触发当前用户执行的进程转向内核态执行响应的异常事件，典型的如缺页异常
3、外围设备的硬中断:被动的
"""
# 3、进程间通信方式有哪些？
"""
1、管道pipe：管道是一种半双工的通信方式，数据只能单向流动，而且只能在具有亲缘关系的进程间使用。
进程的亲缘关系通常是指父子进程关系
2、命名管道FIFO：命名管道也是半双工的通信方式，但是它允许无亲缘关系进程的通信
3、队列queue:队列是由消息的链表，存放在内核中并由消息队列标识符标识，消息队列克服了信号传递信息小
管道只能承载不格式字节流以及缓冲区大小受限的缺点
4、共享存储sharedmemory：共享内存是映射一段能被其他进程所访问的内存，这段共享内存由一个进程创建
，但多个进程都可以访问
5、信号量semaphore：信号量是一个计算器，可以用来控制多个进程对共享资源的访问，它常作为一种锁机制
，防止某进程正在访问共享资源时，其它进程也访问该资源。因此，主要作为进程间以及同意进程内不同线程之间的同步手段
6、套接字socket：套接字也是一种进程间通信机制，与其它通信机制不同的是，它可用于不同及期间的进程通信

1、管道pipe：速度慢，容量有限，只有父子进程能通讯
2、FIFO：任何进程间都能通讯，但速度慢
3、队列：容量收到系统限制
4、信号量：不能传递复杂消息，只能用来同步
5、共享内存去
"""
# 4、简述你对管道、队列的理解；
"""
队列：是消息的链接表，存放在内核中，一个消息队列又一个标识符（即队列ID）来标识
1、特点：
    1.消息队列是面向记录的，其中的消息具有特定的格式已经特定的优先级
    2.消息队列独立于发送与接收进程。进程终止时，消息队列及其内容并不会被删除
    3.消息队列可以实现消息的随机查询，信息不一定要以先进先出的次序读取，也可以
    按消息的类型读取
    
管道：通常指无名管道，是Unix系统IPC最古老的形式
特点：
    1.它是半双工的（即数据只能在一个方向上流动），具有固定的读端和写端
    2.它只能用于具有亲缘关系的进程之间的通信
    3.它可以看成是一种特殊的文件，对于它的读写也可以使用普通的read，write等函数
"""
# 5、请列举你知道的进程间通信方式；
#
# 6、什么是同步I/O，什么是异步I/O？
"""
同步I/O：是同步传输，当发送一个数据请求时，会一直等待，直到有返回结果为止
异步I/O：是指异步传输，当发送一个数据请求时，会立即去处理别的事情，当有数据处理完毕后，会自动的返回结果

一般同步传输能够保证数据正确性，而异步能最大化性能

"""
# 7、请问multiprocessing模块中的Value、Array类的作用是什么？举例说明它们的使用场景

"""
基本特点：
1、共享内存是一种最为高效的进程间通信方式，进程可以直接读写内存，而不需要任何数据的拷贝
2、为了在多个进程间交换信息，内核专门留出了一块内存区，可以由需要访问的进程将其映射到自己的私有地址空间
3、由于多个进程共享一段内存，因此也需要依靠某种同步机制
优缺点：
优点：快速在进程间传递数据
缺点：数据安全上存在风险，内存中的内容会被其他进程覆盖或篡改

基本语法：
value：将一个值存放在内存中
array：将多个数据存放在内存中，但要求数据类型一致

Value：
功能：得到一个共享内存对象，并且存入初始值，method of multiprcocessing

Array:
若为数字，表示开辟的共享内存中的空间大小（value表示为该空间绑定一个数值）
若为数组，表示在共享内存中存入数组

"""
# 8、请问multiprocessing模块中的Manager类的作用是什么？与Value和Array类相比，Manager的优缺点是什么？
"""
Manager类的作用：共享资源，manger的优点是可以在poor进程池中使用，缺点是Windows环境下性能比较差，因为
Windows平台需要把manager.list放在if name='main'下，而在实例化子进程时，必须把manager对象传递给子进程
，否则lists无法被共享，而这个过程会消耗巨大资源，因此性能很差
multiprocessing是一个使用方法类似threading模块的进程模块，允许程序员做并发开发，并且可以在Unix和Windows下运行
通过创建一个process类型并且通过调用call()方法spawn一个进程

"""
# 9、写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；
# from threading import Thread
# import time
#
# def func(name):
#     time.sleep(10)
#     print(name, time.strftime('%Y-%m-%d %H:%H:%S', time.localtime()))
#
#
# if __name__ == '__main__':
#
#     for i in range(10):
#         p = Thread(target=func, args=('线程%s' % i,))
#         p.start()
#     print('主')

# 10、写一个程序，包含十个线程，同时只能有五个子线程并行执行；
# from concurrent.futures import ThreadPoolExecutor
# from threading import currentThread, Thread
# import time
#
#
# def task():
#     print('%s is runing' % currentThread().getName())
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     p = ThreadPoolExecutor(5)
#     for i in range(10):
#
#         p.submit(task)


# 11、写一个程序，要求用户输入用户名和密码，要求密码长度不少于6个字符，且必须以字母开头，如果密码合法，则将该密码使用md5算法加密后的十六进制概要值存入名为password.txt的文件，超过三次不合法则退出程序；
import re
import hashlib
import pickle
def func():
    count = 0
    while count < 3:

        username = input("请输入用户名:").strip()
        passwd = input("请输入密码:").strip()

        if username == 'mike':
            if len(passwd) >= 6 and re.search("\A([a-z]|[A-Z])", passwd):
                md5_password = hashlib.md5(passwd.encode('utf-8')).hexdigest()
                file_obj = {"username":username,
                            "passwd":md5_password}
                f = open('password.txt', 'ab')
                pickle.dump(file_obj, f)

                print("登录成功")
            else:
                print("密码长度小于6位或密码必须以字母开头")
                count +=1
    else:
        print("错误次数已经超过3次")


if __name__ == '__main__':
    func()


# 12、写一个程序，使用socketserver模块，实现一个支持同时处理多个客户端请求的服务器，要求每次启动一个新线程处理客户端请求；
#
# 9、简述多线程和多进程的使用进程？
# 多线程适用于io密集型
#
# 多进程适用于计算密集型
#
# 10、简述select
# 和
# epoll
# 的区别？
# select
# 是不断轮询去监听的socket，socket个数有限制，一般为1024个；
#
# poll还是采用轮询方式去监听，只不过没有个数限制。
#
# epoll并不用采用轮询方式去监听，而是当socket有变化时通过回调方式主动告知用户进程。
#
# select支持多平台，epoll只支持linux平台。
#
# 11、请问multiprocessing模块中的Manager类的作用是什么？与Value和Array类相比，Manager的优缺点是什么？
# Manager类的作用共享资源，manger的的优点是可以在poor进程池中使用，缺点是windows下环境下性能比较差，因为windows平台需要把Manager.list放在if
# name = 'main'
# 下，而在实例化子进程时，必须把Manager对象传递给子进程，否则lists无法被共享，而这个过程会消耗巨大资源，因此性能很差。
#
# 12、什么是协程？使用协程与使用线程的区别是什么？
# 协程是一种用户态的轻量化的线程。线程是系统级别的，它们是由操作系统调度；协程是程序级别的，由程序员根据需要自己调度。我们把一个线程中的一个个函数叫做子程序，
# 那么子程序在执行过程中可以中断去执行别的子程序；别的子程序也可以中断回来继续执行之前的子程序，这就是协程
#
# 13、说说你所知道的MySQL数据库存储引擎，InnoDB存储引擎和MyISM存储引擎的区别？
# MYSQL5.7
# 支持的引擎有INNODB, MyISAM，Memory、merge、archive、csv、federated、BLACKHOLE。
# 可以通过show
# engines \G 查看
#
# InnoDB支持事务、数据缓存、外键不支持全文索引（mysql5.6支持），InnoDB的存储限制为64TB。
# MYISAM不支持事务、数据缓存、外键，但是支持全文索引，MYISAM的存储限制是256TB。
#
# 14、主键具有什么特征？
# 唯一性，不能为空。
#
# 15、什么情况下需要是用事务
# 需要捆绑多条sql语句同时为真，比如转账。
#
# 16、索引的本质是什么？索引有什么优点，缺点是什么？
# 索引在mysql中也称为键，本质是都是通过不断缩小想要获取的数据范围来筛选最终想要的结果，同时把随机的事件变成有序的事件，也就是说，有了索引机制，我们可以总是用同一种查找方式来锁定数据。
#
# 编程题
# 一.数据库
# 1、创建一个表student，包含ID(学生学号)，sname(学生姓名)，gender(性别)，credit(
#     信用卡号), 四个字段，要求：ID是主键，且值自动递增，sname是可变长字符类型，gender是枚举类型, credit是可变长字符类型；
#
# 2、在上面的student表中增加一个名为class_id的外键，外键引用class表的cid字段；
#
# 3、向该表新增一条数据，ID为1，学生姓名为alex，性别女，修改ID为1的学生姓名为wupeiqi，删除该数据；
#
# 4、查询student表中，每个班级的学生数；
#
# 5、修改credit字段为unique属性；
#
# 6、请使用命令在你本地数据库中增加一个用户，并给该用户授予创建表的权限；
#
# 7、请使用pymsql模块连接你本地数据库，并向student表中插入一条数据；
#
# 8、请使用mysqldump命令备份student表；
#
# 1、
# create
# table
# student
# (sid int primary key auto_increment,
# sname varchar(16select),
# gender
# enum('男', '女'),
# credit
# varchar(4)
# );
#
# 2、
# create
# table
#al
#
# mysql> create table class(
#     -> cid int not null unique,
#     -> cname varchar(20) not null
#     -> );
#
#
# insert
# into
#
#
# class values(1);
#
#mysql> alter table student add class_id int not null;


# mysql> alter table student add foreign key(class_id) references class(cid) on delete cascade on update cascade;
#
#
# 3、
# insert
# into
# student
# values(1, 'alex', '女', '1111', 1);
# update
# student
# set
# sname = 'wupeiqi'
# where
# sid = 1;
# delete
# from student where
#
# sid = 1;
#
# 4、
# select
# count(sid)
# from student group
#
# by
# class_id;
#
# 5、
# alter
# table
# student
# modify
# credit
# varchar(4)
# unique;
#
# 6、
# create
# user
# 'egon'
# identified
# by
# '123';
# grant
# create
# on *.*to
# 'egon' @ 'loclahost'
# identified
# by
# '123';
# flush
# privileges;
# select
# user, host, create_priv
# from mysql.user where
#
# user = 'egon';
# 7、
# import pymysql
#
# conn = pymysql.connect(host='localhost',
#                        port=3306,
#                        user='root',
#                        password='123',
#                        db='db11',
#                        charset='utf8')
#
# cursor = conn.cursor()
# sql = 'insert into student values(%s,%s,%s,%s,%s)'
# rows = cursor.execute(sql, (2, 'egon', '男', '2222', 1))
# conn.commit()
# cursor.close()
# conn.close()
# 8、
#
# mysqldump - uroot - p
# db11
# student > C: / backup / student.sql
# 二.请使用协程写一个消费者生产者模型；
#
# def consumer():
#     while True:
#         res = yield
#         print('消耗了', res)
#
#
# def producer(c):
#     next(c)
#     for i in range(10):
#         c.send(i)
#         print('生产了', i)
#
#
# c = consumer()
# p = producer(c)
# 作业
# 基于线程开发一个FTP服务器
#
# 作业需求:
#
# 1.在之前开发的FTP基础上，开发支持多并发的功能
#
# 2.不能使用SocketServer模块，必须自己实现多线程
#
# 3.必须用到队列Queue模块，实现线程池
#
# 4.允许配置最大并发数，比如允许只有10个并发用户