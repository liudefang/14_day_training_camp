# -*- encoding: utf-8 -*-
# @Time    : 2018-04-19 22:23
# @Author  : mike.liu
# @File    : 函数.py


def sayhi():  # 函数名
    print("Hello, I'm nobody!")

# 调用函数
sayhi()


# 下面这段代码
a, b = 5, 8
c = a ** b
print(c)

# 改成函数写
def calc(x, y):
    res = x**y
    return res    # 返回函数执行结果

c = calc(a, b)     # 结果赋值给c变量
print(c)