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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from blog import views
from myblog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^get_validCode_img/$', views.get_valid_code_img),
    url(r'^index/$', views.index),
    url(r'^upload/$', views.upload),
    url(r'^calend/$', views.calend),

    # media配置:
    re_path(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),

    # 个人站点的跳转
    re_path('^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)/$', views.home_site), # home_site(reqeust,username="yuan",condition="tag",param="python")

    # 个人站点url
    re_path('^(?P<username>\w+)/$', views.home_site),   # home_site(reqeust,username="yuan")
]
