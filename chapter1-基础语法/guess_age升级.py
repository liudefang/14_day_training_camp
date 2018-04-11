#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/10 12:11
# @Author  : mike.liu
# @File    : guess_age升级.py
#优化猜年龄游戏，允许用户最多猜3次，中间猜对了，直接跳出循环
'''age_of_oldboy = 38
count = 1
while count <=3:
    guess = int(input("输入年龄:"))
    if guess > age_of_oldboy:
        print("猜的太大了，往小里猜。。。。")
    elif guess < age_of_oldboy:
        print("猜的太小了，往大里猜。。。。")
    else:
        print("恭喜你猜对了。。。")
        break
    count +=1'''

#优化猜年龄游戏，允许用户最多猜3次，猜了3次后，再问是否还想玩，如果用户选y，再允许猜3次，以次往复


age_of_oldboy = 38
count = 0
while count <3:
    guess = int(input("输入年龄:"))
    if guess > age_of_oldboy:
        print("猜的太大了，往小里猜。。。。")
    elif guess < age_of_oldboy:
        print("猜的太小了，往大里猜。。。。")
    else:
        print("恭喜你猜对了。。。")
        break
    count +=1
    if count == 3:
        msg = input("是否还想玩?输入(y|Y):")
        if msg == 'y' or msg == 'Y':
            count = 0
        else:
            print("输入错误！")
