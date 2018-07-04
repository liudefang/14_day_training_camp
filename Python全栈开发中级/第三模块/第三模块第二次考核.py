# -*- encoding: utf-8 -*-
# @Time    : 2018-07-04 21:06
# @Author  : mike.liu
# @File    : 第三模块第二次考核.py


class Police:
    def __init__(self, name, wuqi, life_value, gjl, sex):
        self.name = name
        self.wuqi = wuqi
        self.life_value = life_value
        self.gjl = gjl
        self.sex = sex

    def attack(self, enemy):
        if isinstance(enemy, Police):
            print("都是警察")
        else:

            enemy.life_value -= self.gjl
            if enemy.life_value <= 0:
                print("已经死亡")
            else:
                print("剩下的生命值:", enemy.life_value)


class Terrorist:
    def __init__(self, name, wuqi, life_value, gjl, sex):
        self.name = name
        self.wuqi = wuqi
        self.life_value = life_value
        self.gjl = gjl
        self.sex = sex

    def attack(self, enemy):
        enemy.life_value -= self.gjl
        if enemy.life_value <= 0:
            print("已经死亡")
        else:
            print("剩下的生命值:", enemy.life_value)


p1 = Police('警察1', '手枪', 100, 20, '男')
T1 = Terrorist('大飞', 'AK47', 100, 50, '男')

p1.attack(T1)
p1.attack(p1)

print((8+4+7+8+5+12+13+13+18+17+11+20+10+21+7+10+20+20+30+35+30+21+34+40+30+40+25)/60)