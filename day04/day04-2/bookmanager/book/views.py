from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo
from book.models import PeopleInfo
from django.core import paginator


# Create your views here.

def index(request):
    return HttpResponse('ok')


def book(request, cat_id, detail_id):
    query_string = request.GET
    a = query_string[a]
    b = query_string[b]


def book(request, cat_id, detail_id):
    query_string = request.GET
    alist = query_string.getlist('a')
    b = query_string.get('b')


# 查询属于书籍id为2的所有人物信息  一对多
book_1 = BookInfo.objects.get(id=2)
book_1.peopleinfo_set.all()
# 查询人物id为6所对应的书籍     多对一   这里是指   多个人物相当于多个对象  都属于书book类中  对应一个类
person = PeopleInfo.objects.get(id=6)
person.book  # 这里的book是指   在setting设置中  设置了外键的属性  这个接收变量就命名为book  通过这个外键的关系来查询
BookInfo.objects.filter(peopleinfo__description__contains='八')
BookInfo.objects.filter(Peopleinfo__name='郭靖')
people = peopleinfo.objects.all()
paginator = Paginator(object_list=people, per_page=2)
persons = paginator.page(2)
