import json
import os
import threading

from bs4 import BeautifulSoup
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import transaction
from django.db.models import Count, F
from django.db.models.functions import TruncMonth
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from blog import models
from blog.forms import RegForm
from blog.models import UserInfo
from blog.utlis import validCode, VaildCodeImg
from blog.utlis.VaildCodeImg import ValidCodeImg
from myblog import settings


def register(request):
    """
    注册视图函数：
        get请求响应注册页面
        post(ajax)请求，校验字段，响应字典
    :param request:
    :return:
    """
    if request.is_ajax():
        print(request.POST)
        form = RegForm(request.POST)

        respone = {"username": None, "msg": None}
        if form.is_valid():
            respone["username"] = form.cleaned_data.get("username")

            # 生成一条用户记录
            username = form.cleaned_data.get("username")
            print("username", username)
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            avatar_obj = request.FILES.get("avatar")

            extra = {}
            if avatar_obj:
                extra["avatar"] = avatar_obj

            UserInfo.objects.create_user(username=username, password=password, email=email, **extra)

        else:
            print(form.cleaned_data)
            print(form.errors)
            respone["msg"] = form.errors
        return JsonResponse(respone)
    form = RegForm()
    return render(request, "register.html", {"form": form})


def login(request):
    """
    登录视图函数：
        get请求响应页面
        post(Ajax）请求响应字典
    :param request:
    :return:
    """

    if request.method == "POST":

        respone = {"username": None, "msg": None}
        username = request.POST.get("username")
        password = request.POST.get("password")
        valid_code = request.POST.get("valid_code")

        valid_code_str = request.session.get("valid_code_str")
        if valid_code.upper() == valid_code_str.upper():
            username = auth.authenticate(username=username, password=password)
            if username:
                auth.login(request, username)
                respone["username"] = username.username
            else:
                respone["msg"] = "用户名或者密码错误!"

        else:
            respone["msg"] = "验证码错误!"
        return JsonResponse(respone)
    return render(request, "login.html")


def get_valid_code_img(request):
    """
    基于PIL模块动态生成响应状态码图片
    :param self:
    :param request:
    :return:
    """

    img_data = validCode.getValidCodeImg(request)

    return HttpResponse(img_data)


def index(request):
    """
    系统首页
    :param request:
    :return:
    """
    article_list = models.Article.objects.all()
    return render(request, "index.html", {"article_list": article_list})


def home_site(request, username, **kwargs):
    """
    个人站点的首页
    :param username:
    :param request:
    :return:
    """
    # 区分访问是的站点页面还是站点下的跳转页面
    print("kwargs:", kwargs)
    print("username:", username)

    user = UserInfo.objects.filter(username=username).first()
    # 判断用户是否存在
    if not user:
        return render(request, "not_found.html")

    # 查询当前站点对象
    blog = user.blog
    print("blog:", blog)

    # 当前用户或者当前站点对应所有文章
    # 基于对象查询
    # article_list = user.article_set.all()
    # 基于 __
    article_list = models.Article.objects.filter(user=user)
    if kwargs:
        condition = kwargs.get("condition")
        param = kwargs.get("param")

        if condition == "category":
            article_list = article_list.filter(category__title=param)
        elif condition == "tag":
            article_list = article_list.filter(user=user).filter(tags__title=param)
        else:
            year, month = param.split("-")
            article_list = article_list.filter(user=user).filter(create_time__year=year, create_time__month=month)

    return render(request, "home_site.html", {"username": username, "blog": blog, "article_list": article_list})


def get_classification_data(username):

    user = UserInfo.objects.filter(username=username).first()
    # 当前站点
    blog = user.blog

    cate_list = models.Category.objects.filter(blog=blog).values("pk").annotate(c=Count("article__title")).values_list(
        "title", "c")

    tag_list = models.Tag.objects.filter(blog=blog).values("pk").annotate(c=Count("article")).values_list("title", "c")

    date_list = models.Article.objects.extra(select={"standard_time": "strftime('%%Y-%%m',create_time)"
                }).values("standard_time").annotate(c=Count("nid")).values_list("standard_time", "c")

    return {"blog": blog, "cate_list": cate_list, "tag_list": tag_list, "date_list": date_list}


def article_detail(request, username, article_id):
    """
    文章详情页面
    :param request:
    :param username:
    :param article_id:
    :return:
    """
    user = UserInfo.objects.filter(username=username).first()
    blog = user.blog
    article_obj = models.Article.objects.filter(pk=article_id).first()

    comment_list = models.Comment.objects.filter(article_id=article_id)
    return render(request, "article_detail.html", {"blog": blog, "article_obj": article_obj, "username": username, "comment_list": comment_list})


def digg(request):
    """
    点赞功能
    :param request:
    :return:
    """
    print(request.POST)

    article_id = request.POST.get("article_id")
    is_up = json.loads(request.POST.get("is_up"))
    # 点赞人即当前登录人
    user_id = request.user.pk
    obj = models.ArticleUpDown.objects.filter(user_id=user_id, article_id=article_id).first()

    response = {"state": True}
    if not obj:
        ard = models.ArticleUpDown.objects.create(user_id=user_id, article_id=article_id, is_up=is_up)

        queeryset = models.Article.objects.filter(pk=article_id)
        if is_up:
            queeryset.update(up_count=F("up_count") + 1)
        else:
            queeryset.update(down_count=F("down_count") + 1)
    else:
        response["state"] = False
        response["handled"] = obj.is_up
    return JsonResponse(response)


def comment(request):
    """
    提交评论
    功能：
        1. 保存评论
        2. 创建事务
        3. 发送邮件
    :param request:
    :return:
    """
    print(request.POST)

    article_id = request.POST.get("article_id")
    pid = request.POST.get("pid")
    content = request.POST.get("content")
    user_id = request.user.pk

    article_obj = models.Article.objects.filter(pk=article_id).first()

    # 事务操作
    with transaction.atomic():
        comment_obj = models.Comment.objects.create(user_id=user_id, article_id=article_id, content=content,
                                                    parent_comment_id=pid)
        models.Article.objects.filter(pk=article_id).update(comment_count=F("comment_count") + 1)

    response = {"create_time": comment_obj.create_time.strftime("%Y-%m-%d %X"), "username": request.user.username,
                "content": content}

    # 发送邮件

    t = threading.Thread(target=send_mail, args=("您的文章%s新增了一条评论内容" % article_obj.title,
                                                 content,
                                                 settings.EMAIL_HOST_USER,
                                                 ["450791890@qq.com"]))
    t.start()
    return JsonResponse(response)


def get_comment_tree(request):
    """
    获取评论树
    :param request:
    :return:
    """
    article_id = request.GET.get("article_id")
    response = list(models.Comment.objects.filter(article_id=article_id).order_by("pk").values("pk", "content",
                                                                                               "parent_comment_id"))

    return JsonResponse(response, safe=False)


@login_required
def cn_backend(request):
    """
    后台管理的首页
    :param request:
    :return:
    """
    article_list = models.Article.objects.filter(user=request.user)

    return render(request, "backend/backend.html", locals())


@login_required
def add_article(request):
    """
    后台管理的添加文章
    :param request:
    :return:
    """
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        # 防止xss攻击，过滤script标签
        soup = BeautifulSoup(content, "html.parser")
        for tag in soup.find_all():

            print(tag.name)
            if tag.name == "script":
                tag.decompose()

        # 构建摘要数据，获取标签字符串的文本前150个符号

        desc = soup.text[0:150]+"...."
        if len(title) != 0:

            models.Article.objects.create(title=title, desc=desc, content=str(soup), user=request.user)
            return redirect("/cn_backend")
        else:
            return render(request, "backend/add_article.html", {"error_msg": "文章标题不能为空!"})

    return render(request, "backend/add_article.html")


@login_required
def edit_article(request, pid, option):
    """
    后台文件的管理（删除，编辑）
    :param request:
    :param option:
    :param pid:
    :return:
    """
    article_obj = models.Article.objects.filter(pk=pid).first()
    print("article_obj:", article_obj)
    if article_obj and option == "delete":
        try:
            article_obj.delete()
            reg = {'status': 0, 'msg': '删除成功!'}
        except Exception as e:
            reg = {'status': 1, 'msg': '删除失败'}

        return HttpResponse(json.dumps(reg))

    elif article_obj and option == "edit":
        if request.method == "POST":
            title = request.POST.get("title")
            content = request.POST.get("content")

            # 防止xss攻击，过滤scrip标签
            soup = BeautifulSoup(content, "html.parser")
            for tag in soup.find_all():

                if tag.name == "script":
                    tag.decompose()

            # 构建摘要数据，获取标签字符串的文本前150个字符
            desc = soup.text[0:150]+"...."

            if len(title) != 0:
                models.Article.objects.filter(nid=pid).update(title=title, desc=desc, content=str(soup), user=request.user)
                return redirect("/cn_backend")
            else:
                return render(request, "backend/edit_article.html",  {"error_msg": "文章标题不能为空!"})

        return render(request, "backend/edit_article.html", {"article_obj": article_obj})
    else:
        return render(request, "not_found.html")


def upload(request):
    """
    编辑器上传文件接收
    :param request:
    :return:
    """
    ret = {"error": 0, "url": ""}

    img_obj = request.FILES.get("upload_img")

    path = os.path.join(settings.MEDIA_ROOT, "add_article_img", img_obj.name)

    with open(path, "wb") as f:

        for line in img_obj:
            f.write(line)

    ret["url"] = "/media/add_article_img/" + img_obj.name
    return JsonResponse(ret)


def logout(request):
    """
    退出系统
    :param request:
    :return:
    """
    auth.logout(request)
    return redirect("/login/")