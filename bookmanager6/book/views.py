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

def cookie(request):
    response= HttpResponse('cookie')
    response.set_cookie('name','aa',max_age=3600)

    return response

def get_cookie(request):
    data1=request.COOKIES.get('name')

    return HttpResponse(data1)
def session(request):
    name='itheima'
    request.session['name']=name
    return HttpResponse('session')
def get_session(request):
    name=request.session['name']
    return HttpResponse(name)

from django.views import View

class RegisterView(View):
    def get(self,request):
        return HttpResponse('get get get')
    def post(self,request):
        return HttpResponse('post post post')


'''多继承，个人中心登录
    如果登录用户 可以访问
    如果没登录 不能访问'''
from django.contrib.auth.mixins import LoginRequiredMixin
class OrderView(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('GET 这个页面必须登录')
    def post(self,request):
        return HttpResponse('POST 这个页面必须登录')