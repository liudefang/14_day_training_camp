"""08 bookms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addbook/', views.addbook),
    path('books/', views.books),
    re_path(r'books/(\d+)/change', views.changebook),
    re_path(r'books/(\d+)/delete/', views.delbook),
    path('query/', views.query),
    url(r'^reg/$', views.reg),
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^$', views.index),
    url(r'^logout/$', views.index),
]
