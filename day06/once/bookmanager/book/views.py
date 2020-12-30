from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


# Create your views here.

def index(request):
    pass


# 区分get 和 post请求  面向对象来写 自动区分功能继承自View
from django.views import View


class JDLogin(View):

    def get(self, request):
        return HttpResponse('login-get')

    def post(self, request):
        return HttpResponse('login-post')

    def abc(self, request):
        return HttpResponse('可以被调用吗')
    # 在View中没有这个方法  所以 可以在内部调用 但是不会被系统执行时直接调用


"""
    定义个人中心
    必须要用户登入
    多继承的使用
    判断是否登入 需要继承LoginRequiredMixin
    View的顺序问题  
    
    查看mro方法  centerview.__mro__

"""
from django.contrib.auth.mixins import LoginRequiredMixin


class CenterView(LoginRequiredMixin,View):

    def get(self, request):
        return HttpResponse('center-get')

    def post(self, request):
        return HttpResponse('center-post')
