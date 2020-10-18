from django.conf.urls import url

from . import views
from .views import LoginView, IndexView, RegisterView

app_name = "user"
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^userInfo/$', views.userinfo, name="userInfo"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^search_goods/$', views.search_goods, name="search_goods"),
    #url('<int:pk>/userinfo/', views.userinfo.as_view(), name='userinfo')

]
