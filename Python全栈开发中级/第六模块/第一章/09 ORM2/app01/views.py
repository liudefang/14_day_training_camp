from django.db.models import ForeignKey, Avg, Max, Min, Count, Sum
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01 import models



def query(request):

    # publish_obj = models.Publish.objects.create(name="邮电出版社", city="北京", email="555@qq.com")
    # print(publish_obj)
    # 一对多插入
    # 方式一：
    # publish_obj = models.Publish.objects.get(id=1)
    # book_obj = models.Book.objects.create(title="性能测试案例分析", publishDate="2010-12-12", price=100, publish=publish_obj)
    # print(book_obj)
    #
    # # 方式二：
    # models.Book.objects.create(title="Python全栈开发", publishDate="2015-05-05", price="150", publish_id=2)
    #
    # # 方式三：
    # publish_obj = models.Publish.objects.get(name="邮电出版社")
    # book_obj = models.Book(title="未来简史", publishDate="2010-10-10", price=200, publish=publish_obj)
    # book_obj.save()
    # print(book_obj)


    # --------------多对多添加--------------
    # 方式一：
    # authordetail_obj = models.AuthorDetail.objects.create(birthday="2012-08-12", telephone="15912245678",addr="北京")
    # print(authordetail_obj)
    # author_obj = models.Author.objects.create(name="jacke", age=30, authorDetail_id=3)
    # print(author_obj)
    # pub_obj=models.Publish.objects.filter(name="机械工业出版社").first()
    # book_obj = models.Book.objects.create(title="人类简史",publishDate="2008-10-8", price="122", publish=pub_obj)
    # # 通过作者的名字django默认找到id
    # author_obj = models.Author.objects.filter(name="mike")[0]
    # tom_obj = models.Author.objects.filter(name="tom")[0]
    # jack_obj = models.Author.objects.filter(name="jacke")[0]
    # book_obj.authors.add(author_obj, tom_obj, jack_obj)
    #
    #
    # # 方式二：查出所有的作者
    # pub_obj = models.Publish.objects.filter(name="邮电出版社").first()
    # book_obj = models.Book.objects.create(title="零成本实现性能测试", publishDate="2018-08-08", price="225", publish=pub_obj)
    # author_obj = models.Author.objects.all()
    # # 绑定多对多关系
    # book_obj.authors.add(*author_obj)


    # ---------------解除绑定-------------------
    # 解除多对多的关系(remove)
    # book_obj = models.Book.objects.filter(title="零成本实现性能测试").last()     # 找到书对象
    # author_obj = models.Author.objects.filter(id__lt=3)     # 找到符合条件的作者对象
    # book_obj.authors.remove(*author_obj)    # 因为清除是多条，得加*
    #
    # # 清除关系方法（clear）
    # book_obj = models.Book.objects.filter(title="人类简史")
    # for book_obj_item in book_obj:
    #     book_obj_item.authors.clear()

    # ------------基于对象的跨表查询（相当于sql语句的where子查询）--------------
    # 一对一的查询
    # 正向查询：手机好为15812345678的作者的姓名
    # deital_obj = models.AuthorDetail.objects.filter(telephone="15812345678").first()
    # print(deital_obj.author.name)
    #
    # # 反向查询：查询mike的手机号
    # mike_obj = models.Author.objects.filter(name="mike").first()
    # print(mike_obj.authorDetail.telephone)

    # # 一对多查询
    # # 正向查询：查询“零成本实现性能测试”这本书的出版社的地址
    # book_obj = models.Book.objects.filter(title="零成本实现性能测试")[0]     # 找对象
    # print(book_obj.publish)     # 拿到的是关联出版社的对象
    # print(book_obj.publish.city)
    #
    # # 反向查询：查询邮电出版社出版过的所有书的价格和名字
    # pub_obj = models.Publish.objects.filter(name="邮电出版社")[0]
    # book_dic = pub_obj.book_set.all().values("price", "title")[0]
    # print(book_dic)
    # print(book_dic["price"])
    #
    # # 查询邮电出版社出版过的所有书籍
    # publish = models.Publish.objects.get(name="邮电出版社")      # get得到的直接是一个对象，不过get只能查看有一条记录
    # book_list = publish.book_set.all()      # 与邮电出版社关联的所有书籍对象集合
    # for book_obj in book_list:
    #     print(book_obj.title)


    # # 多对多查询
    # # 正向查询：查询“人类简史”的这本书的所有作者的姓名和年龄
    # book_obj = models.Book.objects.filter(title="人类简史").first()
    # auth_list = book_obj.authors.all()
    # for auth_obj in auth_list:
    #     print(auth_obj.name, auth_obj.age)
    #
    # # 反向查询：查询作者是Mike的这个人出了哪几本书的信息
    # mike_obj = models.Author.objects.filter(name="mike").first()
    # print(mike_obj.book_set.all().first().title)    # 与该作者关联的所有书对象的集合

    # 查询邮电出版社出版过的所有书籍
    # publish = ForeignKey(models.Book, related_name = 'bookList')
    # publish = models.Publish.objects.get(name="邮电出版社")
    # book_list=publish.bookList.all()    # 与人民出版社关联的所有书籍对象集合
    # print(book_list)


    # ------------------基于双下划线的跨表查询--------------------
    # 基于下划线的方式查找-----------一对多
    # 练习1、查询人民出版社出版过的所有的书的价格和名字
    # 第一种方法
    # ret = models.Publish.objects.filter(name="机械工业出版社").values("book__price", "book__title")
    # print(ret)
    #
    # # 第二种方法
    # ret2 = models.Book.objects.filter(publish__name="邮电出版社").values("price", "title")
    # print(ret2)

    # 查询某出版社出版过的所有的书籍
    # ret3 = models.Book.objects.filter(publish__name="邮电出版社").all()
    # print(ret3)

    # 练习2、查询“人类简史”这本书的出版社的地址：filter先过滤，values显示要求的字段
    # 第一种方式
    # ret = models.Book.objects.filter(title="人类简史").values("publish__city")
    # print(ret)
    # # 第二种方式
    # ret2 = models.Publish.objects.filter(book__title="人类简史").values("city")
    # print(ret2)

    # 多对多查询
    # # 练习1、查询mike出过的所有书的名字
    # # 方式一
    # ret = models.Author.objects.filter(name="mike").values("book__title")
    # print(ret)
    # # 方式二
    # ret2 = models.Book.objects.filter(authors__name="mike").values("title")
    # print(ret2)

    # 进阶练习（连续跨表）
    # 练习2、查询手机号以158开头的作者出版过的所有书的名称以及出版社的名称
    # 方式一
    # ret = models.AuthorDetail.objects.filter(telephone__startswith="158").first()
    # print(ret.author.book_set.all().values("title", "publish__name"))
    # print(ret)
    #
    # # 方式二
    # ret = models.Book.objects.filter(authors__authorDetail__telephone__regex="158").values("title", "publish__name")
    # print(ret)

    # 练习3、查询邮电出版社出版过的所有书籍的名字以及作者的姓名
    # 正向查询
    # ret = models.Book.objects.filter(publish__name='邮电出版社').values_list("title", "authors__name")
    # print(ret)
    #
    # # 反向查询
    # ret = models.Publish.objects.filter(name="邮电出版社").values_list("book__title", "book__authors__age", "book__authors__name")
    # print(ret)


    # ----------------聚合查询与分组查询--------------------
    # 计算所有图书的平均价格
    # price_avg = models.Book.objects.all().aggregate(Avg('price'))
    # print(price_avg)

    # print(models.Book.objects.aggregate(average_price=Avg('price')))

    # 返回平均值，最大值，最小值
    # print(models.Book.objects.aggregate(Avg('price'), Max('price'), Min('price')))

    # (1) 练习：统计每一个出版社的最便宜的书
    # 方式一
    # print(models.Book.objects.values("publish__name").annotate(MinPrice=Min('price')))  # 注意：values内的字段即group by字段，也就是分组
    #
    # # 方式二
    # print(models.Publish.objects.all().annotate(minprice=Min("book__price")).values("name", "minprice"))
    #
    # # 方式三
    # publish_list = models.Publish.objects.annotate(MinPrice=Min("book__price"))
    # for publish_obj in publish_list:
    #     print(publish_obj.name, publish_obj.MinPrice)

    # (2)    练习：统计每一本书的作者个数
    # # 方式一
    # author_list = models.Book.objects.all().annotate(Count_author=Count("authors__name")).values("Count_author")
    # print(author_list)
    #
    #
    # # 方式二
    # book_list = models.Book.objects.all().annotate(authorNum=Count("authors__name"))
    # for book_obj in book_list:
    #     print(book_obj.title, book_obj.authorNum)

    # (3)   统计每一本以py开头的书籍的作者个数：
    # book_list = models.Book.objects.all().filter(title__startswith="Py").annotate(authorNum=Count("authors__name"))
    # for book_obj in book_list:
    #     print(book_obj.title, book_obj.authorNum)

    # (4)    统计不止一个作者的图书：
    # author_obj = models.Book.objects.annotate(num_authors=Count('authors')).filter(num_authors__gt=1)
    # print(author_obj)
    #
    # # (5) 根据一本图书作者数量的多少对查询集 QuerySet进行排序:
    # author_boj = models.Book.objects.annotate(num_authors=Count('authors')).order_by('num_authors')
    # print(author_boj)
    #
    # # (6)  查询各个作者出的书的总价格:
    # ret = models.Author.objects.annotate(SumPrice=Sum("book__price")).values_list("name", "SumPrice")
    # print(ret)

















    return HttpResponse("OK")