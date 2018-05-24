# -*- encoding: utf-8 -*-
# @Time    : 2018-05-24 21:49
# @Author  : mike.liu
# @File    : configparser模块.py

import configparser
config = configparser.ConfigParser()  # 实例化（生成对象）
data = config.read('example.ini')
print(data)

print(config.sections())    # 调用sections方法（默认不会读取default）
print('bitbucket.org' in config)        # 判断元素是否在sections列表里

print(config['bitbucket.org']['User'])      # 通过字典的形式取值
print(config['topsecret.server.com']['Port'])

for key in config['bitbucket.org']:  # for 循环bitucket.org字典的key
    print(key)

config = configparser.ConfigParser()
config.read('group.ini')

secs = config.sections()
print(secs)
options = config.options('group2')  # 获取指定section的keys
print(options)

items_list = config.items('group2')  # 获取指定 section 的 keys & values ,key value 以元组的形式
print(items_list)
va1 = config.get('group1', 'k1')
print(va1)

sec=config.remove_section('group1')  # 删除section 并返回状态(true, false)
config.write(open('group.ini', 'w'))

sec = config.has_section('test')
sec = config.add_section('test')
config.write(open('group.ini', 'w', encoding= 'utf-8'))

config.set('group2', 'k3', '333')
config.write(open('group.ini', 'w'))

config.remove_option('group2', 'k1')
config.write(open('group.ini', 'w'))