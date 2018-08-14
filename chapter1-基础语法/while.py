#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/10 10:40
# @Author  : mike.liu
# @File    : while.py

'''count = 0
while count <=100:
    print("count:",count)
    count += 1'''

#打印1到100的偶数
'''count = 1
while count <=100:
    if count%2 ==0:
        print("count:",count)
    count +=1'''

#循环打印1-100，第50次不打印值，第60-80次，打印对应值的平方
count = 1
while count <=100:
    if count == 50:
        print()

    elif count >= 60 and count <= 80:
        print("loop:",count * count)
    else:
        print("loop:",count)
    count +=1