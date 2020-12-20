from pay.views import order
from django.conf.urls import  url

urlpatterns = [

    url(r'^order/$', order),
]
