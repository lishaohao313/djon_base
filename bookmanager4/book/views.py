from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo

# Create your views here.
def index(request):
    # BookInfo.objects.create(name='aaa',
    #                         pub_date='1998-1-3',
    #                         readcount=300)
    # BookInfo.objects.get(id=6).delete()
    # BookInfo.objects.filter(readcount=58).update(readcount=608)

    return HttpResponse('好好学习')

def shop(request,city_id,mobile):
    data=request.GET
    print(data)

    return HttpResponse('奋发图强')

def register(request):
    data=request.POST
    print(data)

    return HttpResponse('register')

def json(request):
    body=request.body
    body_str=body.decode()
    # print(body_str)
    import json
    body_dict=json.loads(body_str)
    # print(body_dict)
    print(request.META)

    return HttpResponse('json')

def method(request):
    print(request.method)

    return HttpResponse('method')