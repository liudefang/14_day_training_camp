# -*- encoding: utf-8 -*-
# @Time    : 2018-04-15 20:57
# @Author  : mike.liu
# @File    : 三级菜单升级版2.py


menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

# 定义当前层等于这个列表
current_layer = menu
last_layer = []

while True:
    for i in current_layer:   # menu[北京]
        print(i)

    choice = input("请输入要进入的区域:").strip()
    if not choice:
        continue
    if choice in current_layer:   # menu[北京]
        last_layer.append(current_layer)   # 在进入下一层的时候，保存当前状态
        current_layer = current_layer[choice]  # menu[北京][昌平]
    elif choice == 'b':
        current_layer = last_layer.pop()  #
        print(current_layer)
    elif choice == 'q':
        exit('退出系统！')
    else:
        print('该节点不存在!')




