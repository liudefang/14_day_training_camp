from django.shortcuts import render

# Create your views here.
from app01 import models



# def index(request):
#     # 查看表中所有的图书信息
#     book_list = models.Book.objects.all()
#     print(book_list)
#
#     return render(request, "index.html", {"book_list": book_list})

def db_index(request):
    book_obj=models.Book(title="python全栈开发",price=100,publishData="2015-08-08", author='张三', publish='机械工业出版社')
    book_obj.save()

    return render(request, "db_index.html")

def index(request):
    return render(request, "index.html")