import json

from django.forms import Form, fields, widgets
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from app01 import models
from app01.forms import RegisterForm


def index(request):
    if request.method == "POST":
        """
        两个return是一样的，用url反向解析就相当于下面的路径在urls里面
        协商别名name="index",但在模板中还是要用{%url"index"%}
        """
       # return redirect(reverse(index))
        return redirect("index.html")   # 跳转到个人主页
    return render(request, "hh.html")


# 1、创建规则
class TeacherForm(Form):    # 必须继承form
    # 创建字段，本质上是正则表达式
    username = fields.CharField(
        required=True,   # 必填字段
        error_messages={"required": "用户名不能为空!"},
        widget=widgets.TextInput(attrs={"placeholder": "用户名","class": "form-control"})   # 自动生成input框
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空!'},
        widget=widgets.TextInput(attrs={'placeholder': '密码', 'class': 'form-control'})
    )
    email = fields.EmailField(
        required=True,
        error_messages={"requeired": "邮箱不能为空!",
                        "invalid": "无效的邮箱格式"},
        widget=widgets.EmailInput(attrs={"placeholder":"邮箱", "class": "form-control"})
    )


# 2、使用规则：将数据和规则进行匹配
def teacherindex(request):
    teacher_obj = models.UserInfo.objects.all()
    print(teacher_obj)

    return render(request, "teacherindex.html", {"teacher_obj": teacher_obj})


def add(request):
    if request.method == "GET":
        form = TeacherForm()    # 只是显示一个input框
        return render(request, "add.html", {"form": form})
    else:
        form = TeacherForm(data=request.POST)

        if form.is_valid(): # 开始验证
            form.cleaned_data['ut_id'] = 1  # 要分的清是班主任还是讲师
            models.UserInfo.objects.all().create(**form.cleaned_data)
            return redirect("/teacherindex/")

        else:
            return render(request, "add.html", {"form": form})


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm(data = request.POST)
        regresponse = {"user": None, 'msg_errors': None}

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            tel = form.cleaned_data.get("tel")
            avatar_img = request.FILES.get("avatar_img")
            models.UserInfo.objects.create_user(username=username, password=password, tel=tel, avatar_img=avatar_img)
            regresponse["user"] = username
        else:
            regresponse["msg_errors"] = form.errors
        return HttpResponse(json.dumps(regresponse))