from django.conf.urls import url
from django.urls import path

from . import views
from .views import LoginView, IndexView, RegisterView, LogoutView, UserInfoView, GalleryView, Search_goodsView

app_name = "user"
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^login1/$', views.login1, name="login1"),

    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^userInfo/$', views.userinfo, name="userInfo"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^search_goods/$', views.search_goods, name="search_goods"),
    #url('<int:pk>/userinfo/', views.userinfo.as_view(), name='userinfo')

]
