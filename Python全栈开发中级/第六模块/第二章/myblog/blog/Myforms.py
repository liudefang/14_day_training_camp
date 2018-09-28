# -*- encoding: utf-8 -*-
# @Time    : 2018-09-24 13:11
# @Author  : mike.liu
# @File    : Myforms.py
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from blog.models import UserInfo


class UserForm(forms.Form):

    user = forms.CharField(max_length=32,
                           error_messages={"required": "该字段不能为空!"},
                           label="用户名",
                           widget=widgets.TextInput(attrs={"class": "form-control"},)
                           )
    pwd = forms.CharField(max_length=32,
                          error_messages={"required": "该字段不能为空!"},
                          label="密码",
                          widget=widgets.PasswordInput(attrs={"class": "form-control"},)
                          )
    re_pwd = forms.CharField(max_length=32,
                             error_messages={"required": "该字段不能为空!"},
                             label="确认密码",
                             widget=widgets.PasswordInput(attrs={"class": "form-control"},)
                             )
    email = forms.EmailField(max_length=32,
                             error_messages={"required": "该字段不能为空!"},
                             label="邮箱",
                             widget=widgets.EmailInput(attrs={"class": "form-control"},)
                             )
    # 局部钩子
    def clean_user(self):
        val = self.cleaned_data.get("user")

        user = UserInfo.objects.filter(username=val).first()
        if not user:
            return val
        else:
            raise ValidationError("该用户已注册!")

    # 校验局部钩子的时候，没有办法拿到所有的数据
    # 任何校验两个字段？全局钩子

    # 全局钩子得到任何一个干净的数据

    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if pwd and re_pwd:
            if pwd == re_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致!")
        else:
            return self.cleaned_data