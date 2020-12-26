from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse('登入页面')


def book(request, cat_id, detail_id):
    print(cat_id, detail_id)
    return HttpResponse('我喜欢看书')

# from book.models import BookInfo
#
# book=BookInfo.objects.get(id=2)
# book.peopelinfo_set.all()
# from book.models import PeopelInfo
# people = PeopelInfo.objects.get(id=6)
# people.book

# BookInfo.objects.filter(peopelinfo__description__contains='八')
    qury_string=request.GET
    a = qury_string['a']
    b = qury_string('b')
    print(a,b)
def get(requst):
    a = requst.GET.get('a')
    b = requst.GET.get('b')
    alist = requst.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return  HttpResponse('OK')
