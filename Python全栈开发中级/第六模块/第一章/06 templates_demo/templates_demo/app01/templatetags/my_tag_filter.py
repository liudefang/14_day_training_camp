# -*- encoding: utf-8 -*-
# @Time    : 18-9-11 下午8:18
# @Author  : mike.liu
# @File    : my_tag_filter.py
from django import template

register=template.Library()     # register的名字是固定的，不可改变

@register.filter    # 过滤器
def multi_fliter(x, y):
    return x*y

@register.simple_tag    # 标签
def multi_tag(x, y):

    return x*y