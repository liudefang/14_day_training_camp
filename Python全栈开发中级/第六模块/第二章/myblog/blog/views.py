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
            avatar_obj = request.FILES.get("avatar")

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


def home_site(request, username, **kwargs):
    """
    个人站点视图函数
    :param request:
    :param username:
    :param kwargs:
    :return:
    """

    print("kwargs", kwargs)     # 区分访问是的站点页面还是站点下的跳转页面
    print("username", username)
    user = UserInfo.objects.filter(username=username).first()
    # 判断用户是否存在
    if not user:
        return render(request, "not_found.html")

    # 查询当前站点对象
    blog = user.blog

    # 当前用户或者当前站点对应所有文章
    # 基于对象查询
    # article_list = user.article_set.all()

    article_list = models.Article.objects.filter(user=user)

    if kwargs:
        condition = kwargs.get("condition")
        param = kwargs.get("param")

        if condition == "category":
            article_list = article_list.filter(category__title=param)
        elif condition == "tag":
            article_list = article_list.filter(tags__title=param)
        else:
            year, month = param.split("/")
            article_list = article_list.filter(create_time__year=year, create_time__month=month)
    # 每一个后的表模型.objects.values("pk").annotate(聚合函数(关联表_统计字段)).values(“表模型的所有字段以及统计字段")
    # 查询每一个分类名称已经对应的文章数
    # 每一个后的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")

    # 查询每一个分类名称以及对应的文章数

    # ret=models.Category.objects.values("pk").annotate(c=Count("article__title")).values("title","c")
    # print(ret)

    # 查询当前站点的每一个分类名称以及对应的文章数

    # cate_list=models.Category.objects.filter(blog=blog).values("pk").annotate(c=Count("article__title")).values_list("title","c")
    # print(cate_list)

    # 查询当前站点的每一个标签名称以及对应的文章数

    # tag_list=models.Tag.objects.filter(blog=blog).values("pk").annotate(c=Count("article")).values_list("title","c")
    # print(tag_list)

    # 查询当前站点每一个年月的名称以及对应的文章数

    # ret=models.Article.objects.extra(select={"is_recent":"create_time > '2018-09-05'"}).values("title","is_recent")
    # print(ret)

    # 方式1:
    # date_list=models.Article.objects.filter(user=user).extra(select={"y_m_date":"date_format(create_time,'%%Y/%%m')"}).values("y_m_date").annotate(c=Count("nid")).values_list("y_m_date","c")
    # print(date_list)

    # 方式2:

    # from django.db.models.functions import TruncMonth
    #
    # ret=models.Article.objects.filter(user=user).annotate(month=TruncMonth("create_time")).values("month").annotate(c=Count("nid")).values_list("month","c")
    # print("ret----->",ret)

    return render(request, "home_site.html", {"username": username, "blog": blog, "article_list": article_list})


def upload(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        obj = request.FILES.get('avatar')
        with open(obj.name, 'wb') as f:
            for line in obj:
                f.write(line)
        return HttpResponse('ok')
    return render(request, 'upload.html')