from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01 import models



# def index(request):
#     # 查看表中所有的图书信息
#     book_list = models.Book.objects.all()
#     print(book_list)
#
#     return render(request, "01-module.html", {"book_list": book_list})


# -------------添加记录-------------
def db_index(request):
    # 方式一
    # book_obj=models.Book(title="PHP全栈开发",price=100,publishData="2015-08-08", author='王五', publish='机械工业出版社')
    # book_obj.save()

    # 方式二：
    # models.Book.objects.create(title="java全栈开发",price=150,publishData="2018-08-08", author='李四', publish='人民出版社')

# -------------查询记录-------------

    # 1、all():查看所有
    # book_obj = models.Book.objects.all()
    # print(book_obj)     # 打印的结果是QuerySet集合：<QuerySet [<Book: python全栈开发>, <Book: java全栈开发>]>
    #
    # # 2、filter()：   可以实现且关系，但是或关系需要借助Q查询实现
    # # 查不到的时候不会报错
    # print(models.Book.objects.filter(title="python全栈开发"))   # 查询书名为“python全栈开发”
    # print(models.Book.objects.filter(price="100", author="张三"))
    #
    #
    # # 3、get():如果找不到就会报错，如果有多个值，也会报错，只能拿一个值
    # print(models.Book.objects.get(title="python全栈开发"))  # 拿的是model对象
    #
    # # 4、exclude():排除条件
    # print(models.Book.objects.exclude(title="python全栈开发"))  # 查看除了书名是"python全栈开发"的信息
    # # 结果：<QuerySet [<Book: java全栈开发>, <Book: PHP全栈开发>, <Book: PHP全栈开发>, <Book: PHP全栈开发>, <Book: PHP全栈开发>]>
    #
    # # # 5、values():是queryset的一个方法（把对象转换成字典的形式）
    # print(models.Book.objects.filter(title="python全栈开发").values("publish", "author"))   # 查看书名为“Python全栈开发”的出版社和作者
    # # 结果：<QuerySet [{'publish': '机械工业出版社', 'author': '张三'}]>
    #
    # # 6、values_list():是queryset的一个方法（把对象转成元组形式）
    # print(models.Book.objects.filter(title="python全栈开发").values_list("publish", "author"))
    # # <QuerySet [('机械工业出版社', '张三')]>
    #
    # # 7、order_by():排序
    # print(models.Book.objects.all().order_by("id"))
    #
    # # # 8、reverse():倒序
    # print(models.Book.objects.all().reverse())
    #
    # # # 9、distinct():去重（只要结果里面有重复的）
    # print(models.Book.objects.filter(title="PHP全栈开发").values("price").distinct())
    # # 结果：<QuerySet [{'price': Decimal('100.00')}]>
    #
    # # # 10、count():查看有几条记录
    # print(models.Book.objects.filter(title="PHP全栈开发").count())
    #
    # # # 11、first():返回第一条记录
    # print(models.Book.objects.all().first())
    #
    # # 12、last()：返回最后一条记录
    # print(models.Book.objects.all().last())
    #
    # # 13、esits:查看有没有记录， 如果有返回True，没有返回False
    # #   并不需要判断所有的数据
    # if models.Book.objects.all().exists():
    #     print('ok')

    # -------------模糊查询记录-------------
    # ret=models.Book.objects.filter(price__gt=50, price__lt=150) # 查询价格在50到150之间的书籍信息
    # print(ret)
    #
    # ret = models.Book.objects.filter(price__in=[100, 250, 300])   # 查询价格等于100,250,300的数据
    # print(ret)
    #
    # ret = models.Book.objects.filter(title__startswith='p')     # 以“p”开头的书名
    # print(ret)
    #
    # ret = models.Book.objects.filter(title__contains='y')   # 包括“y”的书名
    # print(ret)
    #
    # ret = models.Book.objects.filter(title__icontains='p')  # 不区分大小写
    # print(ret)
    #
    # ret = models.Book.objects.filter(publishData__year=2018, publishData__month=8)  # 出版年月为2018年8月的
    # print(ret)

    # -------------修改表记录-------------
    # ret = models.Book.objects.filter(title="PHP全栈开发").update(title="测试开发全栈开发")
    # print(ret)

    # -------------删除表记录------------
    ret = models.Book.objects.filter(id="73").delete()
    print(ret)

    ret = models.Book.objects.filter(id="73").first().delete()



    return HttpResponse("OK")

    #return render(request, "db_index.html")

def index(request):
    return render(request, "01-module.html")