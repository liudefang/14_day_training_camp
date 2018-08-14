# -*- encoding: utf-8 -*-
# @Time    : 2018-05-02 22:03
# @Author  : mike.liu
# @File    : 课后练习题.py

# 8.写代码：
# a.使用while循环实现输出2-3+4-5+6...+100的和
# count = 2
# sum = 0
# while count <= 100:
#     if count % 2 == 0:
#         sum += count
#     else:
#         sum -= count
#     count += 1
# print('sum:', sum)


# b. 使用while循环实现输出1,2,3,4,5,7,8,9,11,12
# i = 1
# while i <= 12:
#     if i == 6 or i == 10:
#         pass
#     else:
#         print(i)
#     i += 1

# c. 使用while循环输出100-50，从大到小，如100,99,88.。。，到50时再从0循环输出到50，然后结束
# i = 101
# while True:
#     if i > 50:
#         i -= 1
#         print(i)
#     else:
#         print(50-i)
#         i -= 1
#     if i< 0:
#         break

# d.使用while循环实现输出1-100内的所有奇数
# i = 1
# while i <= 100:
#     if i % 2 !=0:
#         print(i)
#     i += 1

# d.使用while循环实现输出1-100内的所有奇数
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# 2.判断闰年
# year = input('请输入年份:').strip()
# if year.isdigit():
#     year = int(year)
#
#     if year % 4 == 0 and year % 100 != 0:
#         print('%s年是闰年' % year)
#
#     elif year % 400 == 0:
#         print('%s年是闰年' % year)
#     else:
#         print('%s年是平年' % year)

# 假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
year = 0

mony = 10000
while mony <= 20000:
    year += 1
    mony = mony * (1+0.0325)
    print(year, mony)
print(year)


