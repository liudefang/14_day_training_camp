# -*- encoding: utf-8 -*-
# @Time    : 2018-05-28 20:50
# @Author  : mike.liu
# @File    : 第四章课后练习题.py
# logging模块有几个日志级别？
# 五个级别debug，info，warning，error，critical
# 请配置logging模块，使其在屏幕和文件里同时打印以下格式的日志
#
# 2017-10-18 15:56:26,613 - access - ERROR - account [1234] too many login attempts
import logging
# 屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# 文件
fh = logging.FileHandler
fh = logging.FileHandler('my.log')

# 格式
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formater)
fh.setFormatter(formater)

logger = logging.getLogger("access")
logger.setLevel(logging.ERROR)

logger.addHandler(ch)
logger.addHandler(fh)

logger.error("account [1234] too many login attempts")
# json、pickle、shelve三个区别是什么？
# 1、json是所有语言的序列化工具，优点跨语言，体积小，只能序列化一些基本的数据类型。int/str/list/tuple/dict
# 2、pickle只能使用在python语言中，所有数据类型都支持，存储数据占空间大
# 3、shelve是一个简单的k，v将内存数据通过文件持久化的模块，可以持久化任何pickle，可支持python数据格式

# json的作用是什么？
# 序列化是指把内存里的数据类型转变成字符串，以使其能存储到硬盘或通过网络传输到远程，因为硬盘或网络传输只能接受bytes
# subprocess执行命令方法有几种？
# run()方法
# call()方法
# popen()方法

# 为什么要设计好目录结构？
# 1、可读性高
# 2、可维护性高

# 打印出命令行的第一个参数。例如：
#
# python argument.py luffy
# 打印出 luffy

# 代码如下：
#
# '''
# Linux当前目录/usr/local/nginx/html/
# 文件名：01-module.html
# '''
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(01-module.html)))
# print(BASE_DIR)
# 打印的内容是什么？
# os.path.dirname和os.path.abspath含义是什么？
# os.path.dirname : 指定文件的目录
# os.path.abspath: 指定文件的绝对路径

# 通过configparser模块完成以下功能
#
# 文件名my.cnf
#
# [DEFAULT]
#
# [client]
# port = 3306
# socket = /data/mysql_3306/mysql.sock
#
# [mysqld]
# explicit_defaults_for_timestamp = true
# port = 3306
# socket = /data/mysql_3306/mysql.sock
# back_log = 80
# basedir = /usr/local/mysql
# tmpdir = /tmp
# datadir = /data/mysql_3306
# default-time-zone = '+8:00'
# 修改时区 default-time-zone = '+8:00' 为 校准的全球时间 +00:00
# import configparser
# config = configparser.ConfigParser()
# config.read('my.cnf')
# config.set('mysqld', 'default-time-zone', '+00:00')
# config.write(open('my.cnf', 'w'))
# print(config['mysqld']['default-time-zone'])
# 删除 explicit_defaults_for_timestamp = true
# import configparser
# config = configparser.ConfigParser()
# config.read('my.cnf')
# config.remove_option('mysqld', 'explicit_defaults_for_timestamp')
# config.write(open('my.cnf', 'w'))
# 为DEFAULT增加一条 character-set-server = utf8
# import configparser
# config = configparser.ConfigParser()
# config.read('my.cnf')
# config.set('DEFAULT', 'character-set-server', 'utf8')
# config.write(open('my.cnf', 'w'))
# 写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母.
# import random,string
# res = ''.join(random.sample(string.digits + string.ascii_letters, 6))
# print(res)
# 利用正则表达式提取到 luffycity.com ，内容如下
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#    <meta charset="UTF-8">
#    <title>luffycity.com</title>
# </head>
# <body>
# </body>
# </html>
# import re
# with open('str.txt', 'r', encoding='utf-8') as f:
#     data = f.read()
#     print(data)
#     res = re.search('\w+\.com', data).group()
#     print("结果:", res)
# 写一个用户登录验证程序，文件如下
# 1234.json
#
# {"expire_date": "2021-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
# 用户名为json文件名，密码为 password。
# 判断是否过期，与expire_date进行对比。

# 登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
# 把第12题三次验证的密码进行hashlib加密处理。即：json文件保存为md5的值，然后用md5的值进行验证。
#
# 最近luffy买了个tesla，通过转账的形式，并且支付了5%的手续费，tesla价格为75万。文件为json，请用程序实现该转账行为。
# 需求如下：
#
# 目录结构为
# .
# ├── account
# │   ├── luffy.json
# │   └── tesla.json
# └── bin
#       └── server_start.py
# 当执行start.py时，出现交互窗口
#
#    ------- Luffy Bank ---------
#   1.  账户信息
#   2.  转账
# 选择1 账户信息 显示luffy的当前账户余额。
# 选择2 转账 直接扣掉75万和利息费用并且tesla账户增加75万
# 对上题增加一个需求：提现。
# 目录结构如下
#
# .
# ├── account
# │   └── luffy.json
# ├── bin
# │   └── server_start.py
# └── core
#    └── withdraw.py
# 当执行start.py时，出现交互窗口
#
#    ------- Luffy Bank ---------
# 1.  账户信息
# 2.  提现
# 选择1 账户信息 显示luffy的当前账户余额和信用额度。
# 选择2 提现 提现金额应小于等于信用额度，利息为5%，提现金额为用户自定义。
# 尝试把上一章的验证用户登陆的装饰器添加到提现和转账的功能上。
#
# 对第15题的用户转账、登录、提现操作均通过logging模块记录日志,日志文件位置如下
#
#  .
#  ├── account
#  │   └── luffy.json
#  ├── bin
#  │   └── server_start.py
#  └── core
#  |   └── withdraw.py
#  └── logs
#      └── bank.log
# 本章作业：
# 模拟实现一个ATM + 购物商城程序
#
# 额度 15000或自定义
# 实现购物商城，买东西加入 购物车，调用信用卡接口结账
# 可以提现，手续费5%
# 支持多账户登录
# 支持账户间转账
# 记录每月日常消费流水
# 提供还款接口
# ATM记录操作日志
# 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
# 用户认证用装饰器
# 示例代码 https://github.com/triaquae/py3_training/tree/master/atm
#
# 简易流程图：https://www.processon.com/view/link/589eb841e4b0999184934329