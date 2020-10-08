from django.urls import path

from . import views

app_name = "BuptFish"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/userinfo/', views.userinfo.as_view(), name='userinfo')
]
