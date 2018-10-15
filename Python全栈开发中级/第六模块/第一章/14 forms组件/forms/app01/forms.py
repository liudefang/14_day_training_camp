# -*- encoding: utf-8 -*-
# @Time    : 2018-10-14 17:06
# @Author  : mike.liu
# @File    : forms.py
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import Form, fields, widgets

from app01 import models

class RegisterForm(Form):
    username = fields.CharField(
        required=True,
        max_length=16,
        min_length=3,
        error_messages={
            "required": "用户名不能为空!",
            "max_length": "长度不能大于16",
            "max_length": "长度不能小于3",
        },
        widget=widgets.TextInput({"placeholder": "请输入用户名", "class": "form-control"})
    )
    password = fields.CharField(
        required=True,
        max_length=16,
        min_length=3,
        error_messages={
            "required": "密码不能为空!",
            "max_length": "长度不能大于16",
            "max_length": "长度不能小于3",
        },
        widget=widgets.PasswordInput({"placeholder": "请输入数字与字母组合的密码！", "class": "form-control"})
    )
    password_again = fields.CharField(
        required=True,
        max_length=16,
        min_length=3,
        error_messages={
            "required": "密码不能为空!",
            "max_length": "长度不能大于16",
            "max_length": "长度不能小于3",
        },
        widget=widgets.PasswordInput({"placeholder": "请再次输入密码！", "class": "form-control"})
    )

    email = fields.EmailField(
        required=True,
        error_messages={
            "required": "邮箱不能为空",
            "invalid": "邮箱格式有误"
        },
        widget=widgets.EmailInput({"placeholder": "请输入您的邮箱", "class": "form-control"})
    )
    tel = fields.CharField(
        required=True,
        max_length=11,
        min_length=11,
        error_messages={
            "required": "手机号码不能为空",
            "max_length": "长度必须是11位，请你正确输入",
            "min_length": "长度必须是11位，请你正确输入",
        },
        validators=[RegexValidator("\d+", "手机号码只能是数字")],
        widget=widgets.TextInput({"placeholder": "请您输入你的电话，要求11位哦", "class": "form-control"})
    )


# 局部钩子函数
def clean_username(self):
    username = self.cleaned_data.get("username")
    valid = models.UserInfo.objects.filter(username=username).first()
    if valid:
        raise ValidationError("用户名已存在！")
    return username


# 全局钩子函数：验证两次密码是否一致
def clean(self):
    if self.cleaned_data.get("password") == self.cleaned_data("password_again"):
        return self.cleaned_data
    else:
        raise ValidationError("两次密码不一致")