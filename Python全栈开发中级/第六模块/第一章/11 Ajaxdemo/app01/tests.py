from django.test import TestCase

# Create your tests here.

import json
i = 10
s = "dsfdsf"
l = [11, 22, 33]
dic = {"name": "mike", "age": 22}
b = True

# 把基本数据类型转换成字符串的形式
print(json.dumps(i), type(json.dumps(i)))
print(json.dumps(s), type(json.dumps(s)))
print(json.dumps(l), type(json.dumps(l)))
print(json.dumps(dic), type(json.dumps(dic)))
print(json.dumps(b), type(json.dumps(b)))


# ===========json反序列化===========
d = {"a": 1, "b": "faddfd"}
data = json.dumps(d)
print(data, type(data))
f = open("a.txt", "w")
f.write(data)
f.close()




# =========json序列化=========
f = open("a.txt", "r")
datat = f.read()
print(datat, type(data))
data = json.loads(datat)
print(data, type(data))