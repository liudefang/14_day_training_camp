import json
import os
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app01 import models


def index(request):
    if not request.user.is_authenticated():
        return redirect("/login/")
    else:
        return render(request, "index.html")


def log_out(request):
    auth.logout(request)
    return redirect("/login/")


def get_vaildCode_img(request):
    # 方式一：这样的方式把路径写死了，只能是那一张图片
    # path = os.path.join(settings.BASE_DIR, "static", "image", "3.jpg")
    # with open(path, "rb") as f:
    #     data = f.read()
    # return HttpResponse(data)

    # 方式二： 每次都显示不同的图片，利用pillow模块，安装一个pillow模块
    # img = Image.new(mode="RGB", size=(120, 40), color="green")  # 首先自己创建一个图片，参数szie(120, 40)代表长和高
    # f = open("validcode.png", "wb")     # 然后把图片放在一个指定的位置
    # img.save(f, "png")      # 保存图片
    # f.close()
    # with open("validcode.png", "rb") as f:
    #     data = f.read()
    # return HttpResponse(data)

    # 方式三：
    # 方式二也不怎么好，因为每次都要创建一个保存图片的文件，我们可以不让图片保存到硬盘上，
    # 在内存中保存，完了自动清除，那么就引入了方式三：利用BytesIO模块
    # img = Image.new(mode="RGB", size=(120, 40), color="blue")
    # f = BytesIO()   # 内存文件句柄
    # img.save(f, "png")
    # data = f.getvalue()     # 打开文件（相当于Python中的f.read())
    # return HttpResponse(data)

    # 方式四：1、添加画笔，也就是在图片上写上一些文字
            # 2、并且字体随机，背景颜色随机
    # 随机创建图片
    img = Image.new(mode="RGB", size=(150, 40), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img, "RGB")
    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, 120)
        y1 = random.randint(0, 40)
        x2 = random.randint(0, 120)
        y2 = random.randint(0, 40)

        draw.line((x1, y1, x2, y2), fill = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    font = ImageFont.truetype("KumoFont.ttf", 20)   # 20 表示20像素

    str_list = []   # 把每次生成的验证码保存起来

    # 随机生成五个字符
    for i in range(5):
        random_num = str(random.randint(0, 9))    # 随机数字
        random_lower = chr(random.randint(65, 90))  # 随机小写字母
        random_upper = chr(random.randint(97, 122)) # 随机大写字母
        random_char = random.choice([random_num, random_lower, random_upper])

        print(random_char, "random_char")
        str_list.append(random_char)
        # (5+i*24, 10) 表示坐标，字体的位置
        draw.text((5+i*24, 10), random_char,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                  font=font)

        print(str_list, "str_list")
        f = BytesIO()   # 内存文件句柄
        img.save(f, "png")  # img是一个对象
        data = f.getvalue() # 读取数据并返回至HTML
    vaild_str = "".join(str_list)
    print(vaild_str, "vaild_str")
    request.session["keep_valid_code"] = vaild_str  # 把保存到列表的东西存放至session中
    return HttpResponse(data)


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
    if request.method == "GET":
        return render(request, "login.html")
    else:

        username = request.POST.get("username")
        password = request.POST.get("password")
        vialdCode = request.POST.get("vialdCode")
        ret = {"flag": False, "error_msg": None}
        if vialdCode.upper() == request.session.get("keep_valid_code").upper():
            user = auth.authenticate(username=username, password=password)
            if user:
                # 如果验证成功就让登录
                auth.login(request, user)
                ret["flag"] = True
            else:
                ret["error_msg"] = "用户名或密码错误!"
        else:
            ret["error_msg"] = "验证码错误!"

    return HttpResponse(json.dumps(ret))

def test_ajax(request):
    print(request.GET)

    return HttpResponse("hello world")

def cal(request):
    print(request.POST)

    n1 = int(request.POST.get("n1"))
    n2 = int(request.POST.get("n2"))

    ret = n1 + n2
    return HttpResponse(ret)


def ajax_get(request):

    l=['mike', 'little mike']
    dic = {"name": "mike", "pwd": 123}

    # return HttpResponse(dic)
    # return HttpResponse(json.dumps(l))
    return HttpResponse(json.dumps(dic))


def serialize(request):
    name = request.POST.get('username')
    password = request.POST.get('password')
    checked = request.POST.getlist('hobby')

    return HttpResponse(json.dumps(name))

def formupload(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        file = request.FILES    # 拿到的是一个句柄
        file_obj = request.FILES.get("file")
        print(file_obj, file_obj.name)
        print(type(file_obj), type(file_obj.name))
        with open(file_obj.name, "wb") as f:
            for i in file_obj:
                f.write(i)

        return HttpResponse("上传成功....")
    return render(request, "formupload.html")


def ajaxupload(request):
    return render(request, "ajaxupload.html")

def get_upload(request):
    if request.method == "POST":
        print("FILE:", request.FILES)

        file_obj = request.FILES.get("avatar_img")
        print(file_obj, file_obj.name)
        with open(file_obj.name, "wb") as f:
            for i in file_obj:
                f.write(i)

        return HttpResponse("上传成功")