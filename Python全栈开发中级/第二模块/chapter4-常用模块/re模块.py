# -*- encoding: utf-8 -*-
# @Time    : 2018-05-25 23:20
# @Author  : mike.liu
# @File    : re模块.py
import re
# f = open("兼职联系方式", 'r', encoding='utf-8')
# phones = []

# for line in f:
#     name, city, height, weight, phone = line.split()
#     if phone.startswith('1') and len(phone) == 11:
#         phones.append(phone)
# data = f.read()
# phones = re.findall("[0-9]{11}", data)
# print(phones)

# '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
# '^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
print(r"^a", "\nabc\neee", re.MULTILINE)
# '$'     匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1
print(re.search('foo.$', 'fool\nfoo2\n', re.MULTILINE).group())
# '*'     匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa'
print(re.search('a*','aaaabbac'))
# '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
print(re.findall('ab+', 'ab+cd+abb+bba'))
# '?'     匹配前一个字符1次或0次 ,re.search('b?','alex').group() 匹配b 0次
print(re.search('a?', 'albebx').group())
# '{m}'   匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb'
print(re.search('b{3}', 'alexbbbs').group())
# '{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
print(re.findall("ab{1,3}", "abb abc abbcbbb"))
# '|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
print(re.search("abc|ABC", "ABCBabcCD").group())
# '(...)' 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45'
#
#
# '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^
# '\Z'    匹配字符结尾，同$
# '\d'    匹配数字0-9
# '\D'    匹配非数字
# '\w'    匹配[A-Za-z0-9]
# '\W'    匹配非[A-Za-z0-9]
# 's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
#
# '(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}

# re的匹配语法有以下几种
# re.match 从头开始匹配
# re.search 匹配包含
# re.findall 把所有匹配到的字符放到以列表中的元素返回
# re.split 以匹配到的字符当做列表分隔符
# re.sub 匹配字符并替换
# re.fullmatch 全部匹配


# phone = input("请输入手机号码:").strip()
#
# def func_yz(phone):
#
#     if phone.isdigit():
#
#         if phone.startswith('1') and len(phone) == 11:
#             print("手机号码合法!")
#         elif len(phone) > 11 or len(phone) < 11:
#             print("手机号码长度只能为11位!")
#         else:
#             print("手机号码格式错误!")
#
#     else:
#         print("手机号码只能为数字!")
#
#
# func_yz(phone)

# res = re.match(r'^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+){1,}$', 'mashijia985.bj@163.com')
# print(res)

def validateEmail(email):
    if re.match(r'^[0-9A-Za-z\_\-]+(\.[0-9A-Za-z\_\-]+)*@[0-9A-Za-z]+(\.[0-9A-Za-z]+){1,}$', email) != None:
        print('邮箱地址正确!')
    else:
        print('邮箱地址错误!')

validateEmail('mike.liu@jfz.com')


