from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

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
        if username != str(User.objects.get(username="defang1")):
            s = "注册成功"
            if password == password1:  # 当密码与确认密码一致的时候，注册成功
                User.objects.create_user(username=username, password=password)
                return redirect("/login/")
            else:
                s1 = "两次输入的密码不一致"
                return render(request, "reg.html", {"s1": s1})
        else:
            mess = "用户名已经存在!"
            return render(request, "reg.html", {"mess": mess})

    return render(request, "reg.html")


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
        else:
            s = "用户名或密码错误"
            return render(request, "index.html", {"s": s})

    return render(request, "index.html")


@login_required
# 新增书籍
def addbook(request):
    if request.method == "POST":

        title = request.POST.get("title")
        date = request.POST.get("date")
        author = request.POST.get("author")
        price = request.POST.get("price")
        publish = int(request.POST.get("publish"))

        book_obj = models.Book.objects.create(title=title, publish_id=publish, publishData=date, price=price)
        authors = models.Author.objects.filter(id_in=author)
        book_obj.authorlist.add(*authors)
        return redirect("/books")
    else:
        pub_obj = models.Publish.objects.all()  # 查询出所有的出版社对象

        authorlist = models.Author.objects.all()
        return render(request, "addbook.html", {"publist": pub_obj, "authorlist": authorlist})


@login_required
def books(request):

    book_list = models.Book.objects.all()
    username = request.session.get('user')

    return render(request, "books.html", {"user": username}, locals())


@login_required
def changebook(request, id):
    book_obj = models.Book.objects.filter(id=id).first()

    if request.method == "POST":

        title = request.POST.get("title")
        date = request.POST.get("date")
        author = request.POST.get("author")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        models.Book.objects.filter(id=id).update(title=title, publishData=date, author=author, price=price, publish=publish)

        return redirect("/books")
    return render(request, "changebook.html", {"book_obj": book_obj})


@login_required
def delbook(request, id):
    models.Book.objects.filter(id=id).delete()
    return redirect("/books")

@login_required
def logout(request):
    auth.logout(request)
    return redirect("/index")

def query(request):
    # 1、查询老男孩出版社出版过的价格大于200的书籍
    # book_obj = models.Book.objects.filter(publish="老男孩出版社", price__gt=200)
    # print(book_obj)
    # # 2、查询2017年8月出版的所有以py开头的书籍名称
    # book_obj = models.Book.objects.filter(publishData__year=2017, publishData__month=8, title__startswith='Py').values("title")
    # print(book_obj)
    # # 3、查询价格为50, 100 或者150的所有书籍名称及其出版社名称
    # book_obj = models.Book.objects.filter(price__in=[50, 100, 150]).values("title", "publish")
    # print(book_obj)
    # # 4、查询价格在100到200之间的所有书籍名称及其价格
    # book_obj = models.Book.objects.filter(price__gt=100, price__lt=200).values("title", "price")
    # print(book_obj)
    # #  查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
    # book_obj = models.Book.objects.filter(publish="人民出版社").values("price").distinct().order_by("-price")
    # print(book_obj)
    user_obj = "defang1"
    if user_obj == str(User.objects.get(username=user_obj)):
        mess = "用户名已经存在!"
        print("用户名已经存在!")
    else:
        print("不存在")
        print(User.objects.get(username=user_obj))
    return HttpResponse("OK")

