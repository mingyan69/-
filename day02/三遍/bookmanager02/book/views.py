from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("OK")


from book.models import BookInfo, PeopleInfo

book = BookInfo(
    name='python入门',
    pub_date='2010-1-1'
)
book.save()

PeopleInfo.objects.create(
    name='itheima',
    book=book
)

book = BookInfo.objects.get(id=5)
book.name = "沙雕"
book.pub_date = '2000-01-01'
book.save()

BookInfo.objects.filter(id=1).update(
    name='lvlvl',
    pub_date='2021-1-1'

BookInfo.objects.filter(id=1).update(
    name='射雕英雄传',
    pub_date='1980-05-01'
)

book = BookInfo.objects.get(id=5)
book.delete()

new_book=BookInfo.objects.create(
    name='heima',
    pub_date='2020-1-1'
)


BC = BookInfo.objects.create(
    name='123',
    pub_date='2000-1-1'

)
BookInfo.objects.filter(id=6).delete()

BookInfo.objects.get(id=1)



BookInfo.objects.get(id=7).delete()


from book.models import BookInfo
BookInfo.objects.all()


BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))


























