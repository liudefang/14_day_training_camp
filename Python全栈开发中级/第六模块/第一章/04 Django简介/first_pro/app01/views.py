from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime

# Create your views here.
from django.urls import reverse


def special_case_2003(request):
    return HttpResponse("special_case_2003")


def year_archive(request, year):
    return HttpResponse(year)


def month_archive(request, month, year):
    print(month)
    print(type(month))
    print(year)
    print(type(year))

    #m = int(m)

    return HttpResponse(str(year)+"-"+str(month))

def index(request):

    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")

    return render(request, "index.html", {"ctime": ctime})

def path_year(request, year):
    print(year)
    print(type(year))


    return HttpResponse("path year....")


def path_month(request, month):
    print(month, type(month))

    return HttpResponse("path month....")


# def index(request):
#     return HttpResponse(reverse("app01:index"))

def login(request):

    print(request.method)

    if request.method=="GET":
        return render(request, "login.html")
    else:
        print(request.GET)
        print(request.POST)
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        if user=="mike" and pwd=="123":
            return HttpResponse("登录成功！")
        else:
            return HttpResponse("用户名或密码错误")

def redirect_to_year(request):
    year = 2008
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))