# -*- encoding: utf-8 -*-
# @Time    : 18-9-29 上午10:27
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

    cat_list = models.Category.objects.filter(blog=blog).values("pk").annotate(c=Count("article_title")).values_list("title", "c")
    tag_list = models.Tag.objects.filter(blog=blog).values("pk").annotate(c=Count("article")).values_list("title", "c")
    date_list = models.Article.objects.filter(user=user).extra(select={"y_m_date": "date_format(create_time, '%%Y/%%m')"
                                           }).values("y_m_date").annotate(c=Count("nid")).values_list("y_m_date", "c")

    return {"blog": blog, "cate_list": cat_list, "date_list": date_list, "tag_list": tag_list}