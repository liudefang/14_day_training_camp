# -*- encoding: utf-8 -*-
# @Time    : 2018-04-15 16:39
# @Author  : mike.liu
# @File    : 三级菜单简单版1.py

# 作业题目: 三级菜单
# 需求：
#  可依次选择进入各子菜单
#  可从任意一层往回退到上一层
#  可从任意一层退出程序
#  所需新知识点：列表、字典
menu = {
    '北京':
        {
        '海淀':
            {
            '五道口':
                {
                'soho':
                    {},
                '网易':
                    {},
                'google':
                    {}
            },
            '中关村':
                {
                '爱奇艺':
                    {},
                '汽车之家':
                    {

                },
                'youku':
                    {},
            },
            '上地':
                {
                '百度':
                    {},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':
                    {},
                '北航':
                    {},
            },
            '天通苑':
                {},
            '回龙观':
                {},
        },
        '朝阳':
            {},
        '东城':
            {},
    },
    '上海':
        {
        '闵行':{
            "人民广场":
                {
                '炸鸡店':
                    {}
            }
        },
        '闸北':
            {
            '火车战':
                {
                '携程':
                    {}
            }
        },
        '浦东':
            {},
    },
    '山东':
        {},
}

while True:
    for i in menu:
        print(i)
    choice = input("请输入要进入的区域:").strip()
    if not choice:
        continue

    if choice in menu:
        while True:

            for choice2 in menu[choice]:
                print(choice2)
            choice2 = input("请输入要进入的第二级菜单:").strip()
            if not choice2:
                continue
            if choice2 in menu[choice]:
                while True:
                    for choice3 in menu[choice][choice2]:
                        print(choice3)

                    choice3 = input("请输入要进入的第三级菜单:").strip()
                    if not choice3:
                        continue
                    if choice3 in menu[choice][choice2]:
                        for choice4 in menu[choice][choice2][choice3]:
                            print(choice4)
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit("退出系统")
                    else:
                        print("该节点不存在")
            elif choice2 == 'b':
                break
            elif choice2 == 'q':
                exit("退出系统")
            else:
                print("该节点不存在")
    elif choice == 'b':
        break
    elif choice == 'q':
        exit("退出系统")

    else:
        print("该节点不存在")
