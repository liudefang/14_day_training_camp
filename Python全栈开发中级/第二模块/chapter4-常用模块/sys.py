# -*- encoding: utf-8 -*-
# @Time    : 2018-05-23 21:32
# @Author  : mike.liu
# @File    : sys.py
import sys
print(sys.argv)         # 命令参数list，第一个元素是程序本身路径
print(sys.exit())       # 退出程序，正常退出是exit(0)
print(sys.version)      # 获取python解释程序的版本信息
print(sys.maxint())       # 最大的int值
print(sys.path)         # 返回模块的搜索路径，初始化时使用Pythonpath环境变量的值
print(sys.platform)     # 返回操作系统平台名称
print(sys.stdout.write('please:'))  # 标准输出，引出进度条的例子，注py3上不行，可以用print代替
print(val=sys.stdin.readline()[:-1])    # 标准输入
print(sys.getrecursionlimit())  # 获取最大递归层数
print(sys.setrecursionlimit(120))   # 设置最大递归层数
print(sys.getdefaultencoding())     # h获取解释器默认编码
print(sys.getfilesystemencoding)        # 获取内存数据存到文件里的默认编码