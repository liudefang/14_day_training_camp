# -*- encoding: utf-8 -*-
# @Time    : 2018-05-13 14:13
# @Author  : mike.liu
# @File    : 递归.py
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 递归特性:
#
# 必须有一个明确的结束条件
# 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
# 递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
# 栈就会加一层栈帧，每当函数返回，
# 栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出

# def calc(n):
#     print(n)
#     if int(n/2) ==0:
#         return n
#     return calc(int(n/2))
#
# calc(10)

# def calc(n):
#     v = int(n/2)
#     print(v)
#     if v>0:
#         calc(v)
#     print(n)
#
# calc(10)

data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]

def binary_search(dataset, find_num):
    print(dataset)

    if len(dataset) > 1:
        mid = int(len(dataset)/2)
        if dataset[mid] == find_num:
            print('找到数字:', dataset[mid])
        elif dataset[mid] > find_num:  # 找到数在mid左面
            print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
            return binary_search(dataset[0:mid], find_num)
        else:
            print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
            return binary_search(dataset[mid+1:], find_num)
    else:
        if dataset[0] == find_num:
            print("找到数字啦", dataset[0])
        else:
            print('没的分了,要找的数字[%s]不在列表里' % find_num)

binary_search(data, 1)