import hashlib
import json

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.urls import reverse
from django.views import generic, View
from django.views.generic import DetailView

from User.models import User


def index(request):
    return render(request, 'User/index.html')


class userinfo(generic.DetailView):
    model = User
    template_name = 'User/userInfo.html'


def register(request, useremail, username, password: str):
    md5 = hashlib.md5()
    password = make_password(password)
    password = str(md5.hexdigest())
    user = User(user_email=useremail, user_password=password, user_name=username)
    user.save()
    render(request, '', context={
        'register': '注册成功',
        'status': '200'
    })


class IndexView(View):
    def get(self, request:HttpRequest):
        return render(request, 'User/index.html')

class LoginView(View):
    def get(self, request:HttpRequest):
        return render(request, 'User/login.html')
    def post(self, request:HttpRequest):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user/index/')
        else:
            return HttpResponse(json.dumps({"status": 0, "msg": "用户未激活"}))

class RegisterView(View):
    def get(self, request):
        return render(request, 'User/register.html')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))