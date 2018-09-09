from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
import time
def index(request):

    print("method", request.method)     # get

    print(request.GET)
    print(request.GET.get("name"))
    print(request.POST)

    print(request.path)
    print(request.get_full_path())


    ctime = time.time()

    # return HttpResponse("<h1>OK</h1>")

    return render(request, "index.html", {"timer": ctime})   # index.html模板文件

def login(request):

    if request.method == "POST":

        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if user == "mike" and pwd == "123":
            return redirect("/index/")

    return render(request, "login.html")