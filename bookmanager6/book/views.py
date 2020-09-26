from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('ok')

def shop(request,mobile,b):
    return HttpResponse('shop')

def ceo(request):
    data_dict=request.GET
    data_str=data_dict.getlist('a')

    return HttpResponse(data_str)

def post_text(request):
    data_dict=request.POST
    print(data_dict)

    return HttpResponse('post')

def post_json(request):
    data=request.body
    data_dict=data.decode()
    print(data_dict)
    # import json
    # data_str=json.loads(data_dict)

    return HttpResponse(data_dict)

