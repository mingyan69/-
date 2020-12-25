from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse('ok')




from book.models import BookInfo

book = BookInfo.objects.get(id=2)

book.peopelinfo_set.all()




from book.models import PeopelInfo

person = PeopelInfo.objects.get(id=6)
person.book

from book.models import PeopelInfo
from django.core.paginator import Paginator
people = PeopelInfo.objects.all()
paginator=Paginator(object_list=people,per_page=2)
persons = paginator.page(2)
persons.object_list
paginator.num_pages