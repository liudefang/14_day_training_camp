# -*- encoding: utf-8 -*-
# @Time    : 2018-05-23 22:38
# @Author  : mike.liu
# @File    : json&pickle模块.py

import pickle,json
data = {'k1':123, 'k2':'Hello'}
# pickle.dumps将数据通过特殊的形式转换为只有python语言认识的字符串
# p_str = pickle.dumps(data)
# print(p_str)
# p_load = pickle.loads(p_str)
# print(p_load)

# pickle.dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
# with open('old', 'w', encoding= 'utf-8') as fp:
#     pickle.dump(data, fp)

# json.dumps 将数据通过特殊的形式转换为所有程序语言都认识的字符串
# j_str = json.dumps(data)
# # print(j_str)

# json.dump 将数据通过特殊的形式转换只有python语言认识的字符串，并写入文件
with open('D:/result.json', 'w', encoding='utf8') as fp:
    json.dump(data, fp)
