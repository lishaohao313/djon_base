from django.http import HttpResponse
from django.shortcuts import render
from book.models import  BookInfo

# Create your views here.
def index(request):
    BookInfo.objects.create(name='aabb',
                            pub_date='1990-1-1',
    )


    return HttpResponse('ok')

def shop(request,city_id,shop_id):
    # print(city_id,shop_id)
    query_params=request.GET
    # print(query_params)
    order=query_params.getlist('order')
    print(order)
    return HttpResponse('天才饭店')