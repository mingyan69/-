from django.urls import path
from book.views import index
from book.views import JDLogin
from book.views import JDLogin,CenterView


urlpatterns = [

    path('index/',index),
    path('jd/',JDLogin.as_view()),
    path('center/',CenterView.as_view()),


]