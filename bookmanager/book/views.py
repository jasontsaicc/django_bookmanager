from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse
# Create your views here.
"""
views 
1.就是python函數
2.函數的第一個參數就是請求 和請求相關的是httprequest的實例對象
3.我們要返回一個響應 httpresponse 的實例對象/子類實例對象


"""
def index(request):
    return HttpResponse('index')