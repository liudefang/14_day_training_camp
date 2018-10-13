from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Book


def index(request):
   # 批量导入数据
   #  Booklist = []
   #  for i in range(100):
   #      Booklist.append(Book(title="book"+str(i), price=30.00, publishData='2010-10-10', publish_id=1))
   #  Book.objects.bulk_create(Booklist)
   #
   #  # publish_obj = Publish.objects.create(name="邮电出版社", addr="北京", email="555@qq.com")
   #  # print(publish_obj)
   #
   #  # Author_obj = Author.objects.create(name='张三', age=20)

   # 分页器的使用
   #  book_list = Book.objects.all()
   #  paginator = Paginator(book_list, 10)
   #
   #  print("count:", paginator.count)     # 数据总数
   #  print("num_pages:", paginator.num_pages)    # 总页数
   #  print("page_range:", paginator.page_range)  # 页码的列表
   #
   #  page1=paginator.page(1)     # 第1页的page对象
   #  for i in page1:
   #      print(i)
   #  print(page1.object_list)        # 第1页的所有数据
   #
   #  page2 = paginator.page(2)
   #
   #  print(page2.has_next())     # 是否有下一页
   #  print(page2.next_page_number())     # 下一页的页码
   #  print(page2.previous_page_number())     # 上一页的页码
   #
   #  # 抛错
   #  page=paginator.page(12)
   #  page=paginator.page("z")
   #  return HttpResponse("ok")

    book_list = Book.objects.all()

    paginator = Paginator(book_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)

    try:
       print(page)
       book_list = paginator.page(page)
    except PageNotAnInteger:
       book_list = paginator.page(paginator.num_pages)


    return render(request, "index.html", {"book_list": book_list, "paginator": paginator, "currentPage": currentPage})