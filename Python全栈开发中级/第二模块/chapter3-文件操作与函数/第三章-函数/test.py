#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/5/4 18:22
# @Author  : mike.liu
# @File    : test.py
#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)