from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views import generic
from django.views.generic import DetailView

from BuptFish.models import User


def index(request):
    return  render(request, 'index.html')
class userinfo(generic.DetailView):
    model = User
    template_name = 'userInfo.html'
