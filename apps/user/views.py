import json

from django.contrib.auth import authenticate, logout, login
from django.forms import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from apps.user.models import Order, Goods
from apps.user.models import Orderdetail


def index(request):
    # order = Order.objects.get(order_id=1)
    photo_paths = ["https://i.loli.net/2020/11/02/WxsILKP7kX9iTbZ.jpg",  # 图片port1
                   "https://i.loli.net/2020/11/02/iGuQr6RgHoLE4UW.jpg",  # 图片port2
                   "https://i.loli.net/2020/11/02/AOcV49gWoNDRrlK.jpg",  # 图片port3
                   "https://i.loli.net/2020/11/02/QpWvltj85E6uJia.jpg",  # 图片port4
                   "https://i.loli.net/2020/11/02/7fpEKYHXjW36PMF.jpg",  # 图片port5
                   "https://i.loli.net/2020/11/02/eqHvPVzDXjlNaK1.jpg"]  # 图片port6
    return render(request, 'User/index.html', locals())


def userInfo(request):
    return render(request, 'User/userInfo.html')


def search_goods(request):
    placeholder = "输入搜索内容"
    goods_type = ['衣服','食品','母婴','电子产品']
    if request.POST:
        goods_input = request.POST['form1Name']
        photo_paths=["https://i.loli.net/2020/11/02/WxsILKP7kX9iTbZ.jpg",#图片port1
                     "https://i.loli.net/2020/11/02/iGuQr6RgHoLE4UW.jpg",#图片port2
                     "https://i.loli.net/2020/11/02/AOcV49gWoNDRrlK.jpg",#图片port3
                     "https://i.loli.net/2020/11/02/QpWvltj85E6uJia.jpg",#图片port4
                     "https://i.loli.net/2020/11/02/7fpEKYHXjW36PMF.jpg",#图片port5
                     "https://i.loli.net/2020/11/02/eqHvPVzDXjlNaK1.jpg"]#图片port6
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
        return render(request, 'User/index.html')


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
    user = User.objects.filter(id=1)
    model = user
    template_name = 'User/userInfo.html'


class IndexView(View):
    def get(self, request: HttpRequest):
        order = Order.objects.filter(order_id=1)
        return render(request, 'User/index.html', locals())


class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/login.html')

    def post(self, request: HttpRequest):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return HttpResponse(json.dumps({"status": 200, "msg": "登录成功"}))
        else:
            return HttpResponse(json.dumps({"status": 201, "msg": "登录失败"}))


class LogoutView(View):
    def get(self, request:HttpRequest):
        logout(request)
        return HttpResponseRedirect(reverse("user:index"))

class RegisterView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/register.html')
    def post(self, request: HttpRequest):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username =="" or username is None:
            return HttpResponse(json.dumps({"status": 201, "msg": "用户名不能为空"}))
        if password =="" or password is None:
            return HttpResponse(json.dumps({"status": 201, "msg": "密码不能为空"}))
        if email == "" or email is None:
            return HttpResponse(json.dumps({"status": 201, "msg": "邮箱不能为空"}))
        user = User.objects.filter(email=email)
        if len(user) != 0:
            return HttpResponse(json.dumps({"status": 201, "msg": "邮箱已被使用"}))
        user = User.objects.filter(username=username)
        if len(user) !=0:
            return HttpResponse(json.dumps({"status": 201, "msg": "用户名已注册"}))
        user = User()
        user.set_password(password)
        user.username = username
        user.email = email
        user.save()
        return HttpResponse(json.dumps({"status": 200, "msg": "注册成功"}))
