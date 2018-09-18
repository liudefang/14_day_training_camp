from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from app01 import models


def index(request):
    return render(request, "index.html")


# 注册
def reg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        print(username, password, password1)
        if username != str(User.objects.filter(username=username).first()) and len(username) != 0:
            s = "注册成功"
            if password == password1 and len(password) != 0:  # 当密码与确认密码一致的时候，注册成功
                User.objects.create_user(username=username, password=password)
                return render(request, "reg_succes.html", {"username": username, "s": s})
            elif len(password) == 0:
                return render(request, "reg.html", {"s3": "密码不能为空!"})
            else:
                s1 = "两次输入的密码不一致"
                return render(request, "reg.html", {"s1": s1})
        elif len(username) == 0:
            return render(request, "reg.html", {"s2": "用户名不能为空！"})

        else:
            mess = "用户名已经存在!"
            return render(request, "reg.html", {"mess": mess})

    return render(request, "reg.html")


def reg_succes(request):
    return render(request, "reg_succes.html")


# 登录
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = auth.authenticate(username=username, password=password)  # 验证用户名和密码
        if user is not None and user.is_active:
            #  如果认证成功，就让登录
            auth.login(request, user)
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect("/books/")
            return response
        elif user is None:
            return render(request, "index.html", {"s1": "用户名不存在!"})
        else:
            s = "用户名或密码错误"
            return render(request, "index.html", {"s": s})

    return render(request, "index.html")
