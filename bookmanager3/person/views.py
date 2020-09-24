from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('人才饭店')
def shop1(request,a,b):
    print(a,b)
    return HttpResponse('传智黑马')