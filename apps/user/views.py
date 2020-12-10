import json

from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render

from django.urls import reverse
from django.views import generic, View

from apps.user.Service import GoodsService
from apps.user.Service.IndexService import indexview
from apps.user.Service.CollectService import collectview
from apps.user.models import UserInfo as User
from apps.user.models import Orderdetail, Goods
from apps.user.utils import ClassTree

goodsutils = ClassTree.classtree
goodservice = GoodsService.goodservice


def index(request):
    c_id = request.user.id
    orderlist = indexview(c_id)
    s_orderlist = orderlist.Sell
    b_orderlist = orderlist.Buy
    I_orderlist = orderlist.Ing
    # 根据用户的历史卖出商品返回图片路径
    return render(request, 'User/index.html', locals())


def shopping_cart(request):
    return render(request, 'User/shopping_cart.html', locals())


class collect(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            user_id = request.user.id
            goodlist = collectview(user_id)
        return render(request, 'User/collect.html', locals())

    def post(self, request: HttpRequest):
        return render(request, 'User/collect.html', locals())


class release_goods(View):
    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        goods = Goods()
        goods.goods_name = str(data["name"])  # 根据类型和价格区间返回筛选出的内容
        goods.price = float(data["price"])
        goods.picture = str(data["picture"])
        goods.goods_num = int(data["goods_num"])
        goods.user_name = str(request.user.username)
        goodstype = str(data["type"])
        goods.class_id = goodsutils.str2typeid(goodstype)
        goods.secprice = float(data["price"])
        goods.condition = str(data["condition"])
        return goodservice.savagoods(goods)

    def get(self, request: HttpRequest):
        goods_type = goodservice.get_goods_type()
        return render(request, 'User/release_goods.html', locals())


def userInfo(request):
    return render(request, 'User/userInfo.html')


class search_goods(View):
    def get(self, request: HttpRequest):
        searchservice = GoodsService.goodservice
        goods_type = searchservice.get_goods_type()
        goods_price = searchservice.get_price_dis()
        return render(request, 'User/search_goods.html', locals())

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        searchname = str(data["type"])
        minprice = 0 if "minprice" not in data else data["minprice"]
        maxprice = 100000000 if "maxprice" not in data else data["maxprice"]
        searchservice = GoodsService.goodservice
        resultlist = searchservice.searchgoods(searchname, minprice, maxprice)
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
        order = Orderdetail.objects.get(detail_id=1)
        order1 = order[0]
        photo_paths_sell = ["https://i.loli.net/2020/11/02/WxsILKP7kX9iTbZ.jpg",  # 图片port1
                            "https://i.loli.net/2020/11/02/iGuQr6RgHoLE4UW.jpg",  # 图片port2
                            "https://i.loli.net/2020/11/02/AOcV49gWoNDRrlK.jpg",  # 图片port3
                            "https://i.loli.net/2020/11/02/QpWvltj85E6uJia.jpg",  # 图片port4
                            "https://i.loli.net/2020/11/02/7fpEKYHXjW36PMF.jpg",  # 图片port5
                            "https://i.loli.net/2020/11/02/eqHvPVzDXjlNaK1.jpg"]  # 图片port6

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
            return HttpResponse(json.dumps({"status": 201, "msg": "登录失败,帐号或密码错误"}))


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return HttpResponseRedirect(reverse("user:index"))


class RegisterView(View):
    def get(self, request: HttpRequest):
        return render(request, 'User/register.html')

    def post(self, request: HttpRequest):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username == "" or username is None:
            return HttpResponse(json.dumps({"status": 201, "msg": "用户名不能为空"}))
        if password == "" or password is None:
            return HttpResponse(json.dumps({"status": 201, "msg": "密码不能为空"}))
        if email == "" or email is None:
            return HttpResponse(json.dumps({"status": 201, "msg": "邮箱不能为空"}))
        user = User.objects.filter(email=email)
        if len(user) != 0:
            return HttpResponse(json.dumps({"status": 201, "msg": "邮箱已被使用"}))
        user = User.objects.filter(username=username)
        if len(user) != 0:
            return HttpResponse(json.dumps({"status": 201, "msg": "用户名已注册"}))
        user = User()
        user.set_password(password)
        user.username = username
        user.email = email
        user.save()
        return HttpResponse(json.dumps({"status": 200, "msg": "注册成功"}))
