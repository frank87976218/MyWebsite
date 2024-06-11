from django.shortcuts import render, HttpResponse, redirect
from app01.models import Department,UserInfo
def index(request):
     return HttpResponse("歡迎使用")

def user_list(request):
     return render(request,"user_list.html")

def user_add(request):
     return render(request,"user_add.html")

def tpl(request):
     name = "柴虎"
     roles = ["管理員","CEO","保安"]
     user_into = {"name":"柴虎","salary":"10萬","role":"CTO"}

     data_list=[
          {"name": "柴虎", "salary": "10萬", "role": "CTO"},
          {"name": "小路", "salary": "10萬", "role": "CTO"},
          {"name": "達瓦", "salary": "10萬", "role": "CTO"}
     ]

     return render(request,"tpl.html",{"n1":name,"n2":roles,"n3":user_into,"n4":data_list})

def news(request):
     import requests
     res = requests.get("https://kemono.games/_next/data/sh7XB1p3e80xXeC5Gta0Q/zh-Hant/game/Firefighter-Connor/comment.json?gameSlug=Firefighter-Connor&tab=comment")
     data_list = res.json()
     return render(request,"news.html",{"new_list":data_list})

def something(request):
     return redirect("https://www.baidu.com")

def login(request):
     if request.method == "GET":
          return render(request,"login.html")

     print(request.POST)
     username = request.POST.get("user")
     password = request.POST.get("pwd")

     if username == "root" and password == "123":
          return HttpResponse("登錄成功")

     return render(request,"login.html",{"error_message":"用戶名或密碼錯誤"})


def info_list(request):
     data_list = Department.objects.all()
     print(data_list)
     return render(request,"info_list.html")
