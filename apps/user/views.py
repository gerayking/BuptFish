import json
import regex as re
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View
from apps.user.Service.ShopCartService import shopcartservice
from apps.user.Service import GoodsService
from apps.user.Service.IndexService import indexview, countSelled, getincome, not_inorder
from apps.user.Service.CollectService import collectview
from apps.user.models import UserInfo as User, Collect, Shopcart, UserInfo
from apps.user.models import Orderdetail, Goods
from apps.user.utils import ClassTree
from apps.user.utils.ClassTree import classtree

goodsutils = ClassTree.classtree
goodservice = GoodsService.goodservice


def rjson(status: int, msg: str) -> json:
    return HttpResponse(json.dumps({
        "status": status,
        "msg": msg
    }))


def index(request):
    c_id = request.user.id
    name = request.user.username
    s_count = countSelled(c_id)
    income = getincome(c_id)
    not_in = not_inorder(name)
    orderlist = indexview(c_id)
    s_orderlist = orderlist.Sell
    b_orderlist = orderlist.Buy
    I_orderlist = orderlist.Ing
    # 根据用户的历史卖出商品返回图片路径

    return render(request, 'User/index.html', locals())


def delShopCart(request: HttpRequest):
    goodsId = request.POST["goodsId"]
    userName = request.POST["userName"]
    if userName == None or userName == "" or userName != request.user.username:
        return rjson(500, "用户验证失败")
    item = Shopcart.objects.filter(Q(goods_id=goodsId) & Q(user_name=userName))
    if item != None and len(item) != 0:
        item.delete()
        return rjson(500, "删除成功")
    return rjson(200, "不能删除不存在的物品")


def delCollect(request: HttpRequest):
    goodsId = request.POST["goodsId"]
    userName = request.POST["userName"]
    if userName == None or userName == "" or userName != request.user.username:
        return rjson(500, "用户验证失败")
    item = Collect.objects.filter(Q(goods_id=goodsId) & Q(user_name=userName))
    if item != None and len(item) != 0:
        item.delete()
        return rjson(500, "删除成功")
    return rjson(200, "不能删除不存在的物品")


def addShopCart(request: HttpRequest):
    data = request.POST
    goodsId = data["goodsId"]
    userName = data["userName"]
    if userName == None or userName == "":
        return rjson(500, "用户未登录")
    item = Shopcart.objects.filter(Q(goods_id=goodsId) & Q(user_name=userName))
    if item != None and len(item) != 0:
        return rjson(500, "购物车已存在")
    shopcart = Shopcart()
    shopcart.goods_id = goodsId
    shopcart.user_name = userName
    shopcart.save()
    return rjson(200, "加入购物车成功")


def addCollect(request: HttpRequest):
    print(request.body)
    goodsId = request.POST["goodsId"]
    userName = request.POST["userName"]
    if userName == None or userName == "":
        return rjson(500, "用户未登录")
    item = Collect.objects.filter(Q(goods_id=goodsId) & Q(user_name=userName))
    if item != None and len(item) != 0:
        return rjson(500, "无法重复收藏")
    collect = Collect()
    collect.goods_id = goodsId
    collect.user_name = userName
    collect.save()
    return rjson(200, "收藏成功")


def containShopCart(request: HttpRequest):
    data = request.POST
    goodsId = data["goodsId"]
    userName = data["userName"]
    item = Shopcart.objects.filter(Q(goods_id=goodsId) & Q(user_name=userName))
    if item == None or len(item) == 0:
        return rjson(200, "False")
    return rjson(200, "True")


def containCollect(request: HttpRequest):
    data = request.POST
    goodsId = data["goodsId"]
    userName = data["userName"]
    item = Collect.objects.get(Q(goods_id=goodsId) & Q(user_name=userName))
    if item == None and len(item) != 0:
        return rjson(200, "False")
    return rjson(200, "True")


def online_comm(request: HttpRequest, from_user: str, to_user: str):
    if from_user > to_user:
        room_name = from_user + to_user
    else:
        room_name = to_user + from_user
    from_user_object = UserInfo.objects.get(username = from_user)
    to_user_object = UserInfo.objects.get(username = to_user)
    return render(request, 'User/online_comm.html', locals())


class ShopCart(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            userName = request.user.username
            goodlist = shopcartservice.getCartByName(userName)
        return render(request, 'User/shopping_cart.html', locals())


class collect(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            userName = request.user.username
            goodlist = collectview(userName)
        return render(request, 'User/collect.html', locals())

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        goodsId = data["goodsId"]
        userName = data["userName"]
        collect = Collect()
        collect.user_name = goodsId
        collect.goods_id = userName
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


def info_edit(request):
    if request.POST:
        name = request.POST['name']
        print(name)
        email = request.POST['email']
        print(email)
        Head = request.POST['Head']
        print(Head)
        phone = request.POST['phone']
        print(phone)
        address = request.POST['address']
        print(address)
        password1 = request.POST['password1']
        print(password1)
        password2 = request.POST['password2']
        print(password2)
        avatart = request.POST['avatar']
    return render(request, 'User/info_edit.html', locals())


def message(request):
    return render(request, 'User/message.html', locals())


class search_goods(View):
    def get(self, request: HttpRequest, ):
        searchservice = GoodsService.goodservice
        goodslist = Goods.objects.filter(state="not_in_order")  # 没有进行交易
        userlist_t = UserInfo.objects.all()
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword is not None and keyword != '':
                userlist = [item for item in userlist_t if re.search(keyword, item.username)]
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword is not None and keyword != '':
                goodslist = [item for item in goodslist if re.search(keyword, item.goods_name)]
        if 'minprice' in request.GET:
            minprice = str(request.GET['minprice'])
            if minprice is not None and minprice != '' and minprice.isdigit():
                minprice = int(minprice)
                goodslist = [item for item in goodslist if item.price >= minprice]
        if 'maxprice' in request.GET:
            maxprice = str(request.GET['maxprice'])
            if maxprice is not None and maxprice != '' and maxprice.isdigit():
                maxprice = int(maxprice)
                goodslist = [item for item in goodslist if item.price <= maxprice]
        if 'type' in request.GET:
            type = request.GET['type']
            goodservice.get_goods_type()
            if type is not None and type != '':
                typeid = classtree.str2typeid(type)
                goodslist = [item for item in goodslist if item.class_id == typeid]
        goods_type = searchservice.get_goods_type()
        goods_price = searchservice.get_price_dis()
        return render(request, 'User/search_goods.html', locals())

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        searchname = str(data["type"])
        minprice = 0 if "minprice" not in data else data["minprice"]
        maxprice = 100000000 if "maxprice" not in data else data["maxprice"]
        searchservice = GoodsService.goodservice
        goodslist = searchservice.searchgoods(searchname, minprice, maxprice)
        goodslist = [str(item) for item in goodslist]
        return HttpResponse(json.dumps(str(goodslist)))


def Userinfo_other(request, uid: int):
    # user=getUserbyId(uid)
    name = UserInfo.objects.get(id=uid).username
    s_count = countSelled(uid)
    income = getincome(uid)
    not_in = not_inorder(name)
    orderlist = indexview(uid)
    s_orderlist = orderlist.Sell
    b_orderlist = orderlist.Buy
    I_orderlist = orderlist.Ing
    # 根据用户的历史卖出商品返回图片路径
    return render(request, 'User/Userinfo_other.html', locals())


def item(request, gid: int):
    goods = goodservice.getGoodsById(gid)
    goodsClassName = goodsutils.getTypeNameById(goods.class_id)
    goods_user = UserInfo.objects.get(username=goods.user_name)
    return render(request, 'User/item.html', locals())


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


class userinfo(View):
    def get(self, request: HttpRequest):
        return render(request, "User/infoedit.html", locals())

    def post(self, request: HttpRequest):
        print(request.body)
        if not request.user.is_authenticated:
            return rjson(500, "用户未登录")
        userinfo = request.user
        if "avatar" in request.POST and request.POST["avatar"] != "":
            userinfo.avatar = request.POST["avatar"]
        if "address" in request.POST and request.POST["address"] != "":
            userinfo.address = request.POST["address"]
        if "password1" in request.POST and request.POST["password1"] != "":
            userinfo.set_password(request.POST["password1"])
        if "phone" in request.POST and request.POST["phone"] != "":
            userinfo.phone = request.POST["phone"]
        userinfo.save()
        return rjson(200, "信息更新完成")


# class IndexView(View):
#     def get(self, request: HttpRequest):
#         order = Orderdetail.objects.get(detail_id=1)
#         order1 = order[0]
#         photo_paths_sell = ["https://i.loli.net/2020/11/02/WxsILKP7kX9iTbZ.jpg",  # 图片port1
#                             "https://i.loli.net/2020/11/02/iGuQr6RgHoLE4UW.jpg",  # 图片port2
#                             "https://i.loli.net/2020/11/02/AOcV49gWoNDRrlK.jpg",  # 图片port3
#                             "https://i.loli.net/2020/11/02/QpWvltj85E6uJia.jpg",  # 图片port4
#                             "https://i.loli.net/2020/11/02/7fpEKYHXjW36PMF.jpg",  # 图片port5
#                             "https://i.loli.net/2020/11/02/eqHvPVzDXjlNaK1.jpg"]  # 图片port6
#
#         return render(request, 'User/index.html', locals())


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

# def IndexView(request):
#     return None
