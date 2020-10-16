import json

from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth.models import User

from apps.user.models import Order
from apps.user.models import Orderdetail


def index(request):
    order = Order.objects.get(order_id=1)
    return render(request, 'User/index.html', locals())


def userInfo(request):
    return render(request, 'User/userInfo.html')


def gallery(request):
    orderDetail = Orderdetail.objects.get(detail_id=1)
    goods_comment = "我觉得不错"
    return render(request, 'User/gallery.html', locals())


def search_goods(request):
    text = "placeholder1"
    return render(request, 'User/search_goods.html', locals())


def login1(request):
    # text = "placeholder1"
    return render(request, 'User/login1.html', locals())


class Search_goodsView(View):
    def get(self, request: HttpRequest):
        text = "placeholder1"
        return render(request, 'User/search_goods.html', locals())

    def post(self, request: HttpRequest):
        form1Name = request.POST.get('form1Name')
        form1Name = "xxx"
        return render(request, 'User/search_goods.html', locals())


class GalleryView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/gallery.html')


class UserInfoView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/userInfo.html')


def register(request, useremail: str, username: str, password: str):
    email = useremail
    user = User.objects.get(email=email)
    if user is not None:
        return HttpResponse(json.dumps({"status": 201, "msg": "邮箱已被注册"}))
    user = User.objects.get(username=username)
    if user is not None:
        return HttpResponse(json.dumps({"status": 202, "msg": "用户名已存在"}))
    user = User(username=username, email=useremail, password=password)
    user.save()
    return HttpResponse(json.dumps({"status": 200, "msg": "注册成功"}))


class userinfo(generic.DetailView):
    user = User.objects.get(id=1)
    model = user
    template_name = 'User/userInfo.html'


class IndexView(View):
    def get(self, request: HttpRequest):
        order = Order.objects.get(order_id=1)
        return render(request, 'User/index.html', locals())


class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/login1.html')
    def post(self, request: HttpRequest):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            # login(request, user)
            print("登陆成功！")
            return HttpResponse(json.dumps({"status": 1, "msg": "登录成功"}))
        else:
            print("登陆失败！用户未激活")
            return HttpResponse(json.dumps({"status": 0, "msg": "用户未激活"}))


class RegisterView(View):
    def get(self, request):
        return render(request, 'User/register.html')



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))
