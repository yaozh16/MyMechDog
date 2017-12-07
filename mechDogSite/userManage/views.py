# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import cookie
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django import forms

from models import User
# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())

def TokenCheck(request):
    username = request.COOKIES.get('username', '')
    user = User.objects.filter(username__exact=username)
    if user:
        return user[0]
    else:
        return None
def TokenGenerate(response,user):
    response.set_cookie('username', user.username, 3600)
    return response
def TokenRemove(response):
    response.delete_cookie('username')
    return response

def main(request):
    user=TokenCheck(request)
    if(user):
        # 登录
        return render(request, 'userManage/main_Y.html', {'user':user})
    else:
        # 未登录
        return render(request, 'userManage/main_N.html', {})

def register(request):
    return render(request, 'userManage/main_N.html', {'warning': ['registration not allowed now!','please contact adminstartors.']})
    '''if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            if(len(User.objects.filter(username__exact = username))!=0):
                return render(request, 'userManage/main_N.html', {'warning':'please change a username!'})
            # 添加到数据库
            User.objects.create(username=username, password=password)
            return HttpResponse('regist success!!')
    return HttpResponseRedirect('/user/')'''

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转
                response = HttpResponseRedirect('/user/')
                # 将username写入浏览器cookie,失效时间为3600
                response=TokenGenerate(response,user[0])
                return response
            else:
                return render(request, 'userManage/main_N.html', {'warining':['incorrect!']})
    return HttpResponseRedirect('/user/')

def logout(request):
    response = HttpResponseRedirect('/user/')
    # 清理cookie里保存username
    return TokenRemove(response)
