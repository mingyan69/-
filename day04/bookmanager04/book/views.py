from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return 'ok'


# def book(request, cat_id, detail_id):
#     print(cat_id, detail_id)
#     return HttpResponse('我喜欢看书')

#
# def book(request, cat_id, detail_id):
#     print(cat_id, detail_id)
#
#     query_string = request.GET  # 获取字符串的所有数据
#     a = query_string['a']
#     b = query_string['b']
#     print(a, b)
#     return HttpResponse('我喜欢看书')

# def book(request, cat_id, detail_id):
#     query_string = request.GET
#
#     alist = query_string.getlist('a')
#     b = query_string.get('b')
#     print(alist, b)
#     return HttpResponse('我喜欢看书')

def book(request, cat_id, detail_id):
    # query_string = request.GET
    # alist = query_string.getlist('a')
    # b = query_string.get('b')
    # print(alist,b)
    return HttpResponse('我喜欢看书')


def login(request):
    # return HttpResponse('login')

    body = request.POST
    print(body)

    return HttpResponse('login')


def weibo(request):

    body = request.body
    boody_str = body.decode()
    data = json.loads(body_str)
    return HttpResponse('weibo json')
