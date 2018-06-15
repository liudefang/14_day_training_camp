# -*- encoding: utf-8 -*-
# @Time    : 18-6-15 上午9:25
# @Author  : mike.liu
# @File    : module_test.py
"""
程序目录：
    module_test.py
    index.py

当前文件：
    index.py
"""
# import module_test as obj
# # obj.test()
# print(hasattr(obj, 'test'))
# getattr(obj, 'test')()

# 3 为什么用反射之反射的好处
# 好处一：实现可插拔机制

# egon还没有实现的全部功能
class FtpClient:
    '''ftp客户端，但是还没有实现具体的功能'''
    def __init__(self, addr):
        print('正在连接服务器[%s]' % addr)
        self.addr = addr

# 不影响lili的代码编写
f1 = FtpClient('127.0.0.1')
if hasattr(f1, 'get'):
    func_get = getattr(f1, 'get')
    func_get()

else:
    print('---->不存在此方法')
    print('处理其它的逻辑')

# 好处二：动态导入模块（基于反射当前模块成员）

# 三 __setattr__,__delattr__,__getattr__
# 三者的用法演示
class Foo:
    x = 1
    def __init__(self, y):
        self.y = y

    def __getattr__(self, item):
        print('---->form getattr:你找的属性不存在')

    def __setattr__(self, key, value):
        print('----> from setattr')
        self.__dict__[key] = value  # 应该使用它

    def __delattr__(self, item):
        print('----> from delattr')
        self.__dict__.pop(item)

# __setattr__添加/修改属性会触发它的执行
f1 = Foo(10)
print(f1.__dict__)  # 因为你重写了__setattr__，凡是赋值操作都会触发它的运行，你啥都没有写，就是根本没有赋值，除非你直接操作属性字典，否则永远无法赋值
f1.z = 3
print(f1.__dict__)

# __delattr__ 删除属性的时候会触发
f1.__dict__['a'] = 3 # 我们可以直接修改属性字典，来完成添加/修改属性的操作
del f1.a
print(f1.__dict__)