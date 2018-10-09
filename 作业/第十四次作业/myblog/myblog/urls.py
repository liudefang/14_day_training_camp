"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^get_validCode_img/$', views.get_valid_code_img),
    url(r'^index/$', views.index),
    re_path('^$', views.index),
    url(r'^logout/$', views.logout),

    # 文本编辑器上传图片url
    path('upload/', views.upload),

    # media配置:
    re_path(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),


    # 后台管理
    re_path("cn_backend/$", views.cn_backend),
    re_path("cn_backend/add_article/$", views.add_article),
    re_path(r'article/(\d+)/(delete|edit)', views.edit_article),

    # 文章详情页面
    re_path('^(?P<username>\w+)/articles/(?P<article_id>\d+)$', views.article_detail), # article_detail(request,username="yuan","article_id":article_id)

    # 点赞
    path("digg/", views.digg),

    # 评论
    url(r'^comment/$', views.comment),
    # 获取评论树相关数据
    path("get_comment_tree/", views.get_comment_tree),

    # 个人站点url
    re_path('^(?P<username>\w+)/$', views.home_site),  # home_site(reqeust,username="yuan")

    # 个人站点的跳转
    re_path('^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)/$', views.home_site),



]
