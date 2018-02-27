from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.http.response import HttpResponse
from .models import UserInfo,UserGroup

def login(request):
    return HttpResponse('index')

def logout(request):
    return HttpResponse('index')

#多对多关系，中间表建立数据方法
def index(request):
    u1=UserInfo.objects.get(id=1)
    g1=UserGroup.objects.get(id=1)

    g1.user.add(u1)

    u1.usergroup_set.add(g1)   #第二种方法
    return HttpResponse('OK')


