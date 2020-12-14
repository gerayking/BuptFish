from django.conf.urls import url
from django.urls import path, re_path

import IChannel
from IChannel import consumers
from . import views
from .views import LoginView, RegisterView, LogoutView, search_goods, release_goods, collect, ShopCart, \
    userinfo,Userinfo_other

app_name = "user"
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name="register"),  # 注册界面
    url(r'^login/$', LoginView.as_view(), name='login'),  # 登录界面
    url(r'^release_goods/$', release_goods.as_view(), name="release_goods"),  # 发布界面
    url(r'^index/$', views.index, name="index"),  # 个人主页
    url(r'^userinfo/$', userinfo.as_view(), name="userinfo"),
    url(r'^search_goods/$', search_goods.as_view(), name="search_goods"),  # 商品搜索界面
    url(r'^logout/$', LogoutView.as_view(), name="logout"),  # 登出界面
    url(r'^shopping_cart/$', ShopCart.as_view(), name="shopping_cart"),  # 登出界面
    url(r'^collect/$', collect.as_view(), name="collect"),  # 收藏夹
    url(r'^item/(?P<gid>[\d+])/$', views.item, name="item"),  # 物品详情
    url(r'^Order_details_1/(?P<oid>[\d+])/$', views.Order_details_1, name="Order_details_1"),  # 物品详情1
    url(r'^Order_details_2/(?P<oid>[\d+])/$', views.Order_details_2, name="Order_details_2"),  # 物品详情2
    url(r'^Order_details_3/(?P<oid>[\d+])/$', views.Order_details_3, name="Order_details_3"),  # 物品详情3
    url(r"^changeOrderstate/$",views.changeOrderstate,name="changeOrderstate"),
    url(r'^addCollect/$', views.addCollect, name="addCollect"),  # 添加收藏夹
    url(r'^addShopCart/$', views.addShopCart, name="addShopCart"),  # 添加购物车
    url(r'^containCollect', views.containCollect, name="containCollect"),
    url(r'^containShopCart', views.containShopCart, name="containShopCart"),
    url(r"^delCollect/$",views.delCollect,name="delCollect"),
    url(r"^delShopCart/$",views.delShopCart,name="delShopCart"),
    url(r'^message/$', views.message, name="message"),
    url(r'^Userinfo_other/(?P<uid>[\d+])/$', views.Userinfo_other, name="online_comm"),
    url(r'^online_comm/(?P<from_user>[a-z_A-Z0-9]+)/(?P<to_user>[a-z_A-Z0-9]+)/$', views.online_comm, name="online_comm"),  # consumers.Chatting 是该路由的消费者
    url(r'^push/(?P<username>[a-zA-Z0-9]+)', IChannel.consumers.push,name="push"),
    url(r'^deal/$', views.deal, name="deal")
    # url('<int:pk>/userinfo/', views.userinfo.as_view(), name='userinfo')

]
