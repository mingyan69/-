from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


# Create your views here.
# 区分请求方式

def index(request):
    pass


from django.views import View


class JDLogin(View):
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')


"""
    定义个人中心
    必须要用户登入
    多继承的使用
    判断是否登入 需要继承LoginRequiredMixin
    View的顺序问题  
    
    查看mro方法  centerview.__mro__

"""
from django.contrib.auth.mixins import LoginRequiredMixin


class CenterView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('center-get')

    def post(self, request):
        return HttpResponse('center-post')
