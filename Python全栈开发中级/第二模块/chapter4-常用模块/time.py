
# -*- encoding: utf-8 -*-
# @Time    : 2018-05-22 22:53
# @Author  : mike.liu
# # @File    : time.py
# import time
#
# print(time.localtime())
# print(time.gmtime())
# print(time.time())
# print(time.strftime("%Y-%m-%d %X", time.localtime()))
# print(time.strptime("2018-05-22 22:56","%Y-%m-%d %H:%M"))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(1527001118.9302464)))

import datetime
d = datetime.datetime.now()

print(d.timestamp())
print(d.today())
print(d.year)
print(d.timetuple())
print(d.fromtimestamp(322222))

print(d)
print(datetime.datetime.now() + datetime.timedelta(5))  # 当前时间+5天

print(datetime.datetime.now() + datetime.timedelta(hours=5))

print(d.replace(year=2009, month=2, day=20))