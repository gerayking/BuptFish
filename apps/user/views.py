import json

from django.contrib.auth import authenticate, logout, login
from django.forms import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from apps.user.models import Order, Goods
from apps.user.models import Orderdetail


def index(request):
    # # order = Order.objects.get(order_id=1)
    photo_paths = ["https://i.loli.net/2020/11/02/WxsILKP7kX9iTbZ.jpg",  # 图片port1
                   "https://i.loli.net/2020/11/02/iGuQr6RgHoLE4UW.jpg",  # 图片port2
                   "https://i.loli.net/2020/11/02/AOcV49gWoNDRrlK.jpg",  # 图片port3
                   "https://i.loli.net/2020/11/02/QpWvltj85E6uJia.jpg",  # 图片port4
                   "https://i.loli.net/2020/11/02/7fpEKYHXjW36PMF.jpg",  # 图片port5
                   "https://i.loli.net/2020/11/02/eqHvPVzDXjlNaK1.jpg"]  # 图片port6
    return render(request, 'User/index.html', locals())

def shopping_cart(request):
    return render(request, 'User/index.html', locals())


def release_goods(request):
    return render(request, 'User/release_goods.html', locals())


def userInfo(request):
    return render(request, 'User/userInfo.html')


def search_goods(request):
    placeholder = "输入搜索内容"
    if request.GET:#搜索内容提交
        goods_input = request.GET['form1Name']
        print(goods_input)#根据goods_input的值从数据库挑选内容放入以下数组，并且返回类型下拉选择框和价格区间下拉选择框
        goods_type = ['衣服','食品','母婴','电子产品']
        goods_price = ['100以下', '100~500', '500~1000', '1000以上']
        photo_paths = ["https://i.loli.net/2020/11/02/WxsILKP7kX9iTbZ.jpg",  # 图片port1
                       "https://i.loli.net/2020/11/02/iGuQr6RgHoLE4UW.jpg",  # 图片port2
                       "https://i.loli.net/2020/11/02/AOcV49gWoNDRrlK.jpg",  # 图片port3
                       "https://i.loli.net/2020/11/02/QpWvltj85E6uJia.jpg",  # 图片port4
                       "https://i.loli.net/2020/11/02/7fpEKYHXjW36PMF.jpg",  # 图片port5
                       "https://i.loli.net/2020/11/02/eqHvPVzDXjlNaK1.jpg"]  # 图片port6



    if request.POST:#筛选内容提交
        data = json.loads(request.body)
        goods_type = data["type"]#根据类型和价格区间返回筛选出的内容
        goods_price=data["price"]
        print(goods_type)
        print(goods_price)
        result_list = ["https://i.loli.net/2020/11/02/eqHvPVzDXjlNaK1.jpg",# 图片port1
                       "https://i.loli.net/2020/11/02/QpWvltj85E6uJia.jpg",# 图片port5
                       "https://i.loli.net/2020/11/02/WxsILKP7kX9iTbZ.jpg",# 图片port3
                       "https://i.loli.net/2020/11/02/iGuQr6RgHoLE4UW.jpg",# 图片port2
                       "https://i.loli.net/2020/11/02/AOcV49gWoNDRrlK.jpg",# 图片port4
                       "https://i.loli.net/2020/11/02/7fpEKYHXjW36PMF.jpg"] # 图片port6

        # data = {
        #     'name': "candy",
        #     'age': 13,
        # }
        # list = ['a', 'b', 'c', 'd']
        # return render(request, 'User/search_goods.html', {
        #     'List': json.dumps(result_list),
        # })
        return HttpResponse(json.dumps(result_list),
            content_type='application/json')


    return render(request, 'User/search_goods.html', locals())


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
