from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('人才饭店')
# def shop1(request,a,b):
#     # print(a,b)
#     quest_bak=request.GET
#     print(quest_bak)
#     return HttpResponse('传智黑马')
def index(request,a,b):
    print(a,b)
    c=request.GET
    print(c)


    return HttpResponse('船只黑马')