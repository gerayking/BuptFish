import hashlib
import json

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.urls import reverse
from django.views import generic, View
from django.views.generic import DetailView

from User.models import User
from User.models import Order
from  User.models import Orderdetail
import User.models


def index(request):
    order=Order.objects.get(order_id=1)
    return render(request, 'User/index.html',locals())


def userInfo(request):
    return render(request, 'User/userInfo.html')


def gallery(request):
    orderDetail=Orderdetail.objects.get(detail_id=1)
    goods_comment="我觉得不错"
    return render(request, 'User/gallery.html', locals())


def search_goods(request):
    text = "placeholder1"
    return render(request, 'User/search_goods.html',locals())

def login1(request):
    #text = "placeholder1"
    return render(request, 'User/login1.html',locals())


class Search_goodsView(View):
    def get(self, request: HttpRequest):
        text = "placeholder1"
        return render(request, 'User/search_goods.html', locals())

    def post(self, request: HttpRequest):
        form1Name=request.POST.get('form1Name')
        form1Name="xxx"
        return render(request, 'User/search_goods.html', locals())




class GalleryView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/gallery.html')


class UserInfoView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/userInfo.html')


def register(request, useremail, username, password: str):
    md5 = hashlib.md5()
    password = make_password(password)
    password = str(md5.hexdigest())
    user = User(user_email=useremail, user_password=password, user_name=username)
    user.save()
    render(request, '', context={
        'register': '注册成功',
        'status': '200'
    })


class userinfo(generic.DetailView):
    model = User
    template_name = 'User/userInfoold.html'


class IndexView(View):
    def get(self, request: HttpRequest):
        order = Order.objects.get(order_id=1)
        return render(request, 'User/index.html', locals())




class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/login.html')

    def post(self, request: HttpRequest):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            #login(request, user)
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
