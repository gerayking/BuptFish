from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from .views import LoginView, IndexView, RegisterView, LogoutView, ChangeAvatar

app_name = "user"
urlpatterns = [
                  url(r'^register/$', RegisterView.as_view(), name="register"),
                  url(r'^login/$', LoginView.as_view(), name='login'),
                  url(r'^login1/$', views.login1, name='login1'),
                  url(r'^index/$', IndexView.as_view(), name="index"),
                  url(r'^search_goods/$', views.search_goods, name="search_goods"),
                  url(r'^logout/$', LogoutView.as_view(), name="logout"),
                  url(r'^avatachange/$', ChangeAvatar.as_view(), name="ChangeAvatar")
                  # url('<int:pk>/userinfo/', views.userinfo.as_view(), name='userinfo')
              ]
