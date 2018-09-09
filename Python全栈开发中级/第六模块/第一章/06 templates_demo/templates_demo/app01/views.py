from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import datetime
from django.template import Template,Context
# ================================原始的视图函数
def current_time(request):
#     now = datetime.datetime.now()
#     html = "<html><body>现在时刻:<h1>%s.</h1></body></html>" % now

# ================================django模板修改的视图函数


    # now = datetime.datetime.now()
    # t = Template('<html><body>现在的时刻是:<h1>{{current_date}}</h1></body></html>')
    # c = Context({'current_date':str(now)})
    # html = t.render(c)
    # return HttpResponse(html)

    # 另一种写法（推荐）
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': str(now)[:19]})

def index(request):
    s = "hello"
    l = [111, 222, 333]
    dic = {"name": "mike", "age": 20}   # 字典
    date = datetime.date(1998, 9, 9)    # 日期对象

    class Person(object):
        def __init__(self, name):
            self.name = name

    person_mike = Person("mike")    # 自定义类对象
    person_tom = Person("tom")
    person_jacke = Person("jacke")

    person_list = [person_mike, person_tom, person_jacke]

    ###############过滤器
    now = datetime.datetime.now()
    content = "hello yuan xiao bisheng hello yuan xiao bisheng hello yuan xiao bisheng hello yuan xiao bisheng"
    file_size = 12314556425254
    link = "<a href=''>click</a>"

   # return render(request, "index.html", {"l": l, "dic": dic, "date": date, "person_list": person_list})
    return render(request, "index.html", locals())
