from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo,PeopleInfo

# Create your views here.

def index(request):
    # BookInfo.objects.create(name='金瓶梅',
    #                          pub_date='1990-1-1',
    #                           readcount=30)
    # BookInfo.objects.filter(readcount=30).update(readcount=50)
    # BookInfo.objects.all()
    '''查询编号为1的图书
查询书名包含'湖'的图书
查询书名以'部'结尾的图书
查询书名为空的图书
查询编号为1或3或5的图书
查询编号大于3的图书
查询1980年发表的图书
查询1990年1月1日后发表的图书'''
    # BookInfo.objects.filter(name__contains='湖')
    # BookInfo.objects.get(id=1)
    # BookInfo.objects.filter(name__endswith='部')
    # BookInfo.objects.filter(name__isnull=True)

    # BookInfo.objects.filter(id__in=[1,3,5])
    # BookInfo.objects.filter(id__gt=3)
    # BookInfo.objects.filter(pub_date__year__gt=1980)
    # BookInfo.objects.filter(pub_date__gt='1990-1-1')


    return HttpResponse('我要学编程')
def shop(request,a,mobile):
    data=request.GET

    print(data)

    return HttpResponse('shop')

def register(request):
    data=request.POST
    print(data)
    print(type(data))
    return HttpResponse('register')
def json(request):
    body=request.body
    body_str=body.decode()
    # print(body_str)
    import json
    body_dict=json.loads(body_str)
    print(body_dict)
    # print(type(body_dict))
    print(request.META)

    return HttpResponse('josn')

def method(request):
    print(request.method)
    return HttpResponse('method')
from django.http import HttpResponse,JsonResponse
def response(request):
    info={'name':'itcadd',
          'password':1236}
    res=JsonResponse(data=info)

    # res= HttpResponse('response')
    # res['name']='itcasst'
    return res
