#_*_coding:utf-8_*_


#把10不断除2，只到不能除为止，打印每次结果
import sys
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())



def calc(n,count):
    print(n,count)
    if count < 5:
        return calc(n/2,count+1 )
    else:
        return n


res = calc(188,1 )
print('res ',res)

#
# def calc(n):
#     n = int(n/2)
#     print(n)
#     if n > 0:
#         calc(n)
#     print(n)
#
# calc(10)


#递归练习题

menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': []},
                {'text': '回龙观', 'children': []},
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': []},
            {'text': '金山', 'children': []},
        ]
    }
]
#深度查询
#1. 打印所有的节点
#2. 输入一个节点名字，沙河， 你要遍历找，找到了，就打印它，并返回true,