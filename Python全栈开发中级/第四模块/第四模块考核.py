# -*- encoding: utf-8 -*-
# @Time    : 2018-07-25 21:13
# @Author  : mike.liu
# @File    : 第四模块考核.py

from threading import Thread


def task(name):
    print('%s is running' % name)


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task, args=('Alex_%s' % i, ))
        t.start()

    print('主')

# select * from student where sname = '张三';
#
# insert into student(sname,gender,class_id) values ('mike','男','2');
#
# update student set class_id = 3 where sid = 1
#
# delete from student where sid = 2