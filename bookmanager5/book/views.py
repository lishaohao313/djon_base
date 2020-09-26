from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

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




# def cookie(request):
#     response = HttpResponse('ok')
#     response.set_cookie('itcast1', 'python1')  # 临时cookie
#     response.set_cookie('itcast2', 'python2', max_age=3600)  # 有效期一小时
#     return response
#
#
# def get_cookie(request):
#     data=request.COOKIES.get('itcast2')
#
#     return HttpResponse(data)
#
# def session(request):
#     itcast2='python2'
#
#     request.session['itcast2']=itcast2
#     return HttpResponse('ok')
#
# def get_session(request):
#     data=request.session['itcast2']
#
#     return HttpResponse(data)

def set_cookie(request):
    # username=request.GET.get('username')
    # response = HttpResponse('ok')
    # response.set_cookie('name',username)


    response=HttpResponse('ok')
    response.set_cookie('username','localhose',max_age=360)
    return response

def get_cookie(request):
    data=request.COOKIES.get('username')
    return HttpResponse(data)
def set_session(request):
    username='host'
    request.session['name']=username
    return HttpResponse('123')

def get_session(request):
    datr=request.session['name']
    return HttpResponse(datr)

# from django.views import View
# class LogView(View):
#     def get(self,request):
#         return HttpResponse('get get get')
#     def post(self,request):
#         return HttpResponse('post post')

class LogView(View):
    def get(self,request):
        return HttpResponse('get get get')
    def post(self,request):
        return HttpResponse('POsT PORT post')