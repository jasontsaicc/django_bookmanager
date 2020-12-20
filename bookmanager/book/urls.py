from django.conf.urls import url
from book.views import index

# index/
# 第一個參數正則表達式
# 第二個參數是：views函數名
urlpatterns = [
    url(r'^index/$',index),
]