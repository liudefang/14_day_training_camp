# -*- encoding: utf-8 -*-
# @Time    : 2019/8/18 15:59
# @Author  : mike.liu
# @File    : 21game.py
from random import shuffle

import numpy as np

# 洗牌函数，shuffle作用随机生成数据


# 初始化扑克牌


playing_cards = {
    "黑桃A": 1, "黑桃2": 2, "黑桃3": 3, "黑桃4": 4, "黑桃5": 5, "黑桃6": 6, "黑桃A": 1, "黑桃7": 7,
    "黑桃8": 8, "黑桃9": 9, "黑桃10": 10, "黑桃J": 10, "黑桃Q": 10, "黑桃K": 10,
    "红桃A": 1, "红桃2": 2, "红桃3": 3, "红桃4": 4, "红桃5": 5, "红桃6": 6, "红桃A": 1, "红桃7": 7,
    "红桃8": 8, "红桃9": 9, "红桃10": 10, "红桃J": 10, "红桃Q": 10, "红桃K": 10,
    "方块A": 1, "方块2": 2, "方块3": 3, "方块4": 4, "方块5": 5, "方块6": 6, "方块A": 1, "方块7": 7,
    "方块8": 8, "方块9": 9, "方块10": 10, "方块J": 10, "方块Q": 10, "方块K": 10,
    "梅花A": 1, "梅花2": 2, "梅花3": 3, "梅花4": 4, "梅花5": 5, "梅花6": 6, "梅花A": 1, "梅花7": 7,
    "梅花8": 8, "梅花9": 9, "梅花10": 10, "梅花J": 10, "梅花Q": 10, "梅花K": 10,
}

poker_name = list(playing_cards.keys())
# 扑克的数量，几副扑克
poker_count = 1
porker_list = poker_name * poker_count

# 用于判断手中的牌是否有A，根据分数来进行选A的牌的分值是0还是1
four_a = {"黑桃A", "红桃A", "梅花A", "方块A"}

# 计分器，玩家：电脑，初始的分数都是0
total_score = np.array([0, 0])

# 记录游戏是第几回合
game_round = 1

"""
洗牌：重新对扑克牌进行随机排列
"""


def random_card(poker_name_list):
    shuffle(poker_name_list)


"""
计算手里的牌的分数
"""


def score_count(hand_poker):
    # 声明一个变量，这个变量用来记录牌的总分数
    poker_score = 0
    # 标记：判断是否有A的标记，默认没有
    have_a = False

    # 计算手中牌的分数
    for k in hand_poker:
        poker_score += playing_cards[k]

    # 判断手中的牌是否有A，然后再根据A的规则进行分数计算
    for i in hand_poker:
        if i in four_a:
            have_a = True
            break
        else:
            continue

    if have_a == True:
        if poker_score + 10 <= 21:
            poker_score = poker_score + 10

    return poker_score

"""
判断输赢
"""


def who_win(your_score, pc_score):
    if your_score > 21 and pc_score > 21:
        print("平局了")
        return  np.array([0, 0])
    elif your_score > 21 and pc_score <= 21:
        print("对不起，你输了")
        return np.array([0, 1])
    elif your_score <= 21 and pc_score > 21:
        print("恭喜，你赢了")
    elif your_score <= 21 and pc_score <=21:
        if your_score < pc_score:
            print("对不起，玩家赢了")
            return np.array([0, 1])
        elif your_score > pc_score:
            print("恭喜你，玩家赢了")
            return np.array([1, 0])
        else:
            print("平局了")
            return np.array([0, 0])


"""
是否继续要牌
"""
def if_get_next_poker():
    if_continue = input("是否继续要下一张牌?(Y/N)")

print(82890*120)