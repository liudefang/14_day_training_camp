# -*- encoding: utf-8 -*-
# @Time    : 2018-10-05 11:38
# @Author  : mike.liu
# @File    : my_tags.py
from django import template
from django.db.models import Count

from blog import models

register = template.Library()


@register.inclusion_tag("classification.html")
def get_classification_style(username):

    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog

    cate_list = models.Category.objects.filter(blog=blog).values("pk").annotate(c=Count("article__title")
                                                                                ).values_list("title", "c")
    tag_list = models.Tag.objects.filter(blog=blog).values("pk").annotate(c=Count("article")).values_list("title", "c")
    date_list = models.Article.objects.extra(select={"standard_time": "strftime('%%Y-%%m',create_time)"}
                                             ).values("standard_time").annotate(c=Count("nid")
                                                                                ).values_list("standard_time", "c")

    return {"blog": blog, "cate_list": cate_list, "date_list": date_list, "tag_list": tag_list, "username": username}
