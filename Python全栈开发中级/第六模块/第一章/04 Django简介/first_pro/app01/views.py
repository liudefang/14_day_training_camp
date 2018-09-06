from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def special_case_2003(request):
    return HttpResponse("special_case_2003")


def year_archive(request, year):
    return HttpResponse(year)


def month_archive(request, m, y):
    print(m)
    print(type(m))
    print(y)
    print(type(y))

    m = int(m)

    return HttpResponse(y+"-"+m)