"""first_pro URL Configuration

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
from django.contrib import admin
from django.urls import include, re_path, path, register_converter

from app01 import views, converters
register_converter(converters.FourDigitYearConverter, 'yyyy')
urlpatterns = [
    # 路由配置：路径---------->视图函数
    # re_path('admin/', admin.site.urls),
    # re_path(r'^articles/2003/$', views.special_case_2003),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # 分发：
    # re_path(r'app01/', include(('app01.urls', "app01"))),
    # re_path(r'blog/', include('blog.urls'))
    # path("articles/<mm:month>", views.path_month),
    # 反向解析
    re_path(r'^articles/([0-9]{4})/$', views.year_archive, name='news-year-archive'),
    re_path(r'^index/', views.index),

    re_path(r'^app01/', include("app01.urls", namespace="app01")),

    # 2.0版本
    path('articles/2018', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug>/', views.month_archive),

    # 注册自定义转化器
    path('articles/<yyyy:year>', views.year_archive)

]
