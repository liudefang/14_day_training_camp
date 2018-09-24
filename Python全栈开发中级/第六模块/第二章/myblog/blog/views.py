from django.contrib import auth
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from blog import models
from blog.Myforms import UserForm
from blog.models import UserInfo
from blog.utils import validCode


def login(request):
    """
    登录视图函数
        get请求响应页面
        post(Ajax)请求响应字典
    :param request:
    :return
    """
    if request.method == "POST":
        response = {"user": None, "msg": None}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        valid_code = request.POST.get("valid_code")

        valid_code_str = request.session.get("valid_code_str")
        if valid_code.upper() == valid_code_str.upper():
            user = auth.authenticate(username=user, password=pwd)
            if user:
                auth.login(request, user)
                response["user"] = user.username
            else:
                response["msg"] = "用户名或密码错误"

        else:
            response["msg"] = "验证码错误!"

        return JsonResponse(response)
    return render(request, "login.html")


def index(request):
    """
    系统首页
    :param request:
    :return:
    """
    article_list = models.Article.objects.all()
    return render(request, "index.html", {"article_list": article_list})


def get_valid_code_img(request):
    """
    基于PIL模块动态生成响应状态码图片
    :param request:
    :return:
    """
    img_data = validCode.get_valid_code_img(request)
    return HttpResponse(img_data)


def register(request):
    """
    注册视图函数：
        get请求响应注册页面
        POst(Ajax)请求，校验字段，响应字典
    :param request:
    :return:
    """
    if request.is_ajax():
        print(request.POST)
        form = UserForm(request.POST)

        response = {"user": None, "msg": None}
        if form.is_valid():
            response["user"] = form.cleaned_data.get("user")

            # 生成一条用户记录
            user = form.cleaned_data.get("user")
            print("user", user)
            pwd = form.cleaned_data.get("pwd")
            email = form.cleaned_data.get("email")
            avatar_obj = request.FILES.get("avater")

            extra = {}
            if avatar_obj:
                extra["avatar"] = avatar_obj
            UserInfo.objects.create_user(username=user, password=pwd, email=email, **extra)

        else:
            print(form.cleaned_data)
            print(form.errors)
            response["msg"] = form.errors

        return JsonResponse(response)

    form = UserForm()
    return render(request, "register.html", {"form": form})


    return render(request, "register.html")