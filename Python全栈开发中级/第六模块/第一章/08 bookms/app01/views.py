from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from app01 import models

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app01 import models


def addbook(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        author = request.POST.get("author")
        price = request.POST.get("price")
        publish = request.POST.get("publish")

        book_obj = models.Book.objects.create(title=title, publish=publish, publishData=date, author=author,
                                              price=price)

        return redirect("/books")

    return render(request, "addbook.html")


def books(request):
    book_list = models.Book.objects.all()

    return render(request, "books.html", locals())


def changebook(request, id):
    book_obj = models.Book.objects.filter(id=id).first()

    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        author = request.POST.get("author")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        models.Book.objects.filter(id=id).update(title=title, publishData=date, author=author, price=price,
                                                 publish=publish)

        return redirect("/books")
    return render(request, "changebook.html", {"book_obj": book_obj})


def delbook(request, id):
    models.Book.objects.filter(id=id).delete()
    return redirect("/books")

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

