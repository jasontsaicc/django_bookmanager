from django.shortcuts import render
from django.conf.urls import include, url
from django.http import HttpRequest ,HttpResponse
# Create your views here.

def order(request):
    return HttpResponse("pay.urls.py")