from django.conf.urls import url
from django.urls import path

from . import views
from .views import LoginView, IndexView, RegisterView, LogoutView

app_name = "user"
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^index/$', IndexView.as_view(), name="index"),
    url('<int:pk>/userinfo/', views.userinfo.as_view(), name='userinfo')

]
