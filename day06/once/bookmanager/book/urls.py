from django.urls import path
from book.views import index
from book.views import JDLogin


urlpatterns = [
    path('index/',index),
    path('jd/',JDLogin.as_view())
    # 这里的括号是先运行as_view装饰器  获取到最后返回的view函数  来调用
    # 这个函数起到 判断get 和 post的作用
]