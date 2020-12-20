"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
"""
1.urlpatterns 是固定寫法 裡面的值是列表
2.在瀏覽器的網址 會和urlpatterns 依照順序匹配
    匹配成功 會導入相對應的模塊
    不成功返回404
3.urlpatterns 中的元素是url
    第一個參數是正則
    r = 轉譯
    ^ = 嚴格的開始
    $ = 嚴格的結束
4.http://ip:port/path/?key=value
    http://ip:port/ 和get/post不參與正則匹配

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    url(r'^',include('book.urls')),
    url(r'^pay/', include('pay.urls')),
]
