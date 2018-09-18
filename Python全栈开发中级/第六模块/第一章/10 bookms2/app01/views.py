from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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


@login_required
# 新增书籍
def addbook(request):
    publish_list = models.Publish.objects.all()  # 查询出所有的出版社对象
    author_list = models.Author.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        price = request.POST.get("price")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")
        if title != str(models.Book.objects.filter(title=title).first()) and len(title) !=0:
            book_obj = models.Book.objects.create(title=title, publish_id=publish_id, publishData=date, price=price)

            book_obj.authorlist.add(*authors_id_list)
            return redirect("/books")
        elif len(title) == 0:
            return render(request, "addbook.html", {"s": "书籍名称不能为空!", "publish_list": publish_list,
                                                    "author_list": author_list})
        else:
            return render(request, "addbook.html", {"s1": "书籍名称已经存在!", "publish_list": publish_list,
                                                    "author_list": author_list})

    return render(request, "addbook.html", {"publish_list": publish_list, "author_list": author_list})


# 查看图书列表
@login_required
def books(request, field_id=0, field_type='src'):
    '''
    图书列表有3种情况：
    点击查看图书列表（books）显示的的图书
    点击出版社（publishs)显示的图书
    点击作者（authors)显示的图书
    :param request:
    :param field_id
    :param field_type: /publishs /anthors
    :return:
    '''
    if field_type == 'publishs':
        book_list = models.Book.objects.filter(publish_id=field_id).all()
    elif field_type == 'authors':
        book_list = models.Book.objects.filter(authorlist__id=field_id).all()
    else:
        book_list = models.Book.objects.all()

    username = request.session.get('user')

    paginator = Paginator(book_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)

    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)

    return render(request, "books.html", {"user": username, "book_list": book_list, "paginator": paginator,
                                          "currentPage": currentPage})


# 编辑图书
@login_required
def changebook(request, id):
    edit_book_obj = models.Book.objects.filter(id=id).first()

    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        price = request.POST.get("price")
        authors_id_list = request.POST.getlist("authors_id_list")
        publish_id = request.POST.get("publish_id")
        if len(title) != 0:
            models.Book.objects.filter(id=id).update(title=title, publishData=date, price=price, publish_id=publish_id)
            edit_book_obj.authorlist.set(authors_id_list)
            return redirect("/books")
        else:
            return render(request, "changebook.html", {"s": "书籍名称不能为空!"})

    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    return render(request, "changebook.html", {"edit_book_obj": edit_book_obj, "publish_list": publish_list,
                                               "author_list": author_list})


# 删除图书
@login_required
def delbook(request, id):
    models.Book.objects.filter(id=id).delete()
    return redirect("/books")


# 注销登录
@login_required
def logout(request):
    auth.logout(request)
    return redirect("/index")


@login_required
# 添加作者
def addauthor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        if name != (models.Author.objects.filter(name=name).first()) and len(name) != 0:
            models.Author.objects.create(name=name, age=age)
            return redirect("/authors/")
        elif len(name) == 0:
            return render(request, "addauthor.html", {"s": "作者姓名不能为空!"})
    return render(request, "addauthor.html")


# 编辑作者
def editauthor(request, id):
    author_obj = models.Author.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        if name != (models.Author.objects.filter(name=name).first()) and len(name) != 0:
            models.Author.objects.filter(id=id).update(name=name, age=age)
            return redirect("/authors/")
        elif len(name) == 0:
            return render(request, "addauthor.html", {"s": "作者姓名不能为空!"})
    return render(request, "editauthor.html", {"author_obj": author_obj})


# 删除作者
def delauthor(request, id):
    models.Author.objects.filter(id=id).delete()

    return redirect("/authors/")


@login_required
def authors(request):
    author_list = models.Author.objects.all()
    return render(request, "author.html", locals())


@login_required
# 添加出版社
def addpublish(request):
    if request.method == "POST":
        name = request.POST.get("name")
        addr = request.POST.get("addr")
        email = request.POST.get("email")
        if name != (models.Publish.objects.filter(name=name).first()) and len(name) != 0:
            models.Publish.objects.create(name=name, addr=addr, email=email)
            return redirect("/publishs/")
        elif len(name) == 0:
            return render(request, "addpublish.html", {"s": "出版社名称不能为空!"})
        else:
            return render(request, "addpublish.html", {"s1": "出版社名称已经存在!"})
    return render(request, "addpublish.html")


# 查看出版社
@login_required
def publishs(request):
    pub_list = models.Publish.objects.all()
    return render(request, "publish.html", locals())


# 编辑出版社
def editpublish(request, id):
    pub_obj = models.Publish.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get("name")
        addr = request.POST.get("addr")
        email = request.POST.get("email")
        if name != (models.Publish.objects.filter(name=name).first()) and len(name) != 0:
            models.Publish.objects.create(name=name, addr=addr, email=email)
            return redirect("/publishs/")
        elif len(name) == 0:
            return render(request, "editpublish.html", {"s": "出版社名称不能为空!"})
        else:
            return render(request, "editpublish.html", {"s1": "出版社名称已经存在!"})
    return render(request, "editpublish.html", {"pub_obj": pub_obj})


# 删除出版社
def delpublish(request, id):
    models.Publish.objects.filter(id=id).delete()
    return redirect("/publishs/")


def query(request):
    # book_list = models.Book.objects.filter(authorlist=5).all()
    book_list = models.Book.objects.filter(publish_id=5).all()
    print(book_list)

    return HttpResponse("OK")
