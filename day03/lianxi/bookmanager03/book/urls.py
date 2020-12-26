from django.urls import path
from book.views import index,book


urlpatterns = [
    path('index/', index),
    path('<cat_id>/<detail_id>/',book),
]
