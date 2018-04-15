# -*- encoding: utf-8 -*-
# @Time    : 2018-04-14 18:23
# @Author  : mike.liu
# @File    : 字典.py

# 查找
'''info = {

    'stu1101': ['小泽',27],
    'stu1102': ['龙泽萝拉',24],

}

info["stu1103"] = "仓老师"

print (info)

info1 = {'stu1102': 'LongZe Luola', 'stu1103': 'XiaoZe Maliya', 'stu1101': '武藤兰'}
info1["stu1103"] = "小泽玛利亚"
print(info1)

print(info1.get("stu1102"))
print(info1["stu1102"])'''

# 多级嵌套
'''av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
av_catalog["大陆"]["1024"][1] += ",可以爬下来"
print(av_catalog["大陆"]["1024"])
print(av_catalog["大陆"])'''

# 其它方法
info = {'stu1102': 'LongZe Luola', 'stu1103': 'XiaoZe Maliya', 'stu1101': '武藤兰'}

#  values() 方法以列表返回字典中的所有值。
print(info.values())
# keys() 方法以列表返回一个字典所有的键
print(info.keys())

# items() 方法以列表返回可遍历的(键, 值) 元组数组
print(info.items())

# 循环
for key in info:
    print(key,info[key])