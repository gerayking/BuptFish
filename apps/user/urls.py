from django.conf.urls import url

from . import views
from .views import LoginView, IndexView, RegisterView, LogoutView

app_name = "user"
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name="register"),#注册界面
    url(r'^login/$', LoginView.as_view(), name='login'),#登录界面
    url(r'^release_goods/$', views.release_goods, name="release_goods"),#发布界面
    url(r'^index/$', views.index, name="index"),#个人主页
    url(r'^userInfo/$', views.userinfo, name="userInfo"),
    url(r'^search_goods/$', views.search_goods, name="search_goods"),#商品搜索界面
    url(r'^logout/$', LogoutView.as_view(), name="logout"),#登出界面
    url(r'^shopping_cart/$', views.shopping_cart, name="shopping_cart"),#登出界面
    url(r'^collect/$',views.collect,name="collect")#收藏夹


    # url('<int:pk>/userinfo/', views.userinfo.as_view(), name='userinfo')

]
