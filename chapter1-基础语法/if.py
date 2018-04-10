#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/10 9:05
# @Author  : mike.liu
# @File    : if.py

# 1、输入姓名、性别、判断如果是女生，打印我喜欢女生，否则，打印一起搞基
'''sex = '女生'
UserName = input("请输入你的姓名：")
Sex = str(input("请输入你的性别:"))

if sex == Sex:
    print("我喜欢美女")
else:
    print("一起来搞基！")'''


#输入姓名，性别，年龄，判断如果是女生且年龄小于28岁，打印我喜欢美女，否则，打印姐弟恋也很好奥！
'''sex = '女生'
age = 28
UserName = str(input("请输入你的姓名："))
Sex = str(input("请输入你的性别:"))
Age = int(input("请输入你的年龄:"))
if sex == Sex and age > Age:
    print("我喜欢美女!")
else:
    print("姐弟恋也很好奥！")'''


#输入姓名，性别，年龄，判断如果是女生且年龄小于28岁，打印我喜欢美女，否则，打印姐弟恋也很好奥！否则，打印一起搞基
'''sex = '女生'
age = 28
UserName = str(input("请输入你的姓名："))
Sex = str(input("请输入你的性别:"))
Age = int(input("请输入你的年龄:"))
if sex == Sex :
    if  age > Age:
        print("我喜欢美女!")
    else:
        print("姐弟恋也很好奥！")

else:
    print("一起来搞基！")'''

#写一个猜年龄的游戏
'''age_of_oldboy = 38
guess = int(input("输入年龄:"))
if guess > age_of_oldboy:
    print("猜的太大了，往小里试试。。。")
elif guess < age_of_oldboy:
    print("猜的太小了，往大里试试。。。")
else:
    print("恭喜你，猜对了。。。")'''

#匹配成绩的小程序，成绩有ABCDE5个等级，与分数的对应关系如下：
'''A 90 - 100
B 80 - 89
C 60 - 79
D 40 - 59
E 0 - 39
要求用户输入0-100的数字后，你能正确打印他的对应成绩'''

Score = int(input("请输入0-100的数字："))
if Score > 100:
    print("只能输入0-100的数字！")
elif Score >= 90 and Score <= 100:
    print("成绩等级为A！")
elif Score >= 80 and Score <= 89:
    print("成绩等级为B！")
elif Score >= 60 and Score <= 79:
    print("成绩等级为C！")
elif Score >= 40 and Score <= 59:
    print("成绩等级为D！")
elif Score < 0:
    print("成绩不能小于0！")
else:
    print("成绩等级为E！")

#猜年龄游戏升级版，允许用户最多猜3次


