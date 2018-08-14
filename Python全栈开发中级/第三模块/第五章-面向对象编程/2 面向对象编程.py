# -*- encoding: utf-8 -*-
# @Time    : 2018-06-02 15:31
# @Author  : mike.liu
# @File    : 2 面向对象编程.py

def person(name, attack_val, life_value):
    def attack(d):
        """人打狗功能"""
        d['life_value'] -= attack_val   # 被打了，要掉血
        print("人[%s] 打了狗[%s]...,[%s]的生命值还有[%s]" % (name, d['name'], d['name'], d['life_value']))

    data = {
        'name': name,
        'attack_val' : attack_val,
        'life_value': life_value,
        'attack': attack
    }
    return data

def dog(name, attack_val, life_value):
    def bite(p):
        """狗咬人功能"""
        p['life_value'] -= attack_val
        print("狗[%s] 咬了 人[%s]。。。,[%s]的生命值还有[%s]" % (name, p['name'], p['name'], p['life_value']))

    data = {
        'name': name,
        'attack_val': attack_val,
        'life_value' : life_value,
        'bite' : bite
    }
    return data

alex = person("Alex", 100, 1000)
black_girl = person("Black girl", 80, 700)

d = dog("PeiQi", 200, 800)

alex['attack'](d)
d['bite'](black_girl)