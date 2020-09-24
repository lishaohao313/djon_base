from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('index')

from book.models import BookInfo
book=BookInfo(name='Django',
              pub_date='2000-1-1',
              readcount=10  )
book.save()

BookInfo.objects.create(name='Django',
              pub_date='2000-1-1',
              readcount=10)

book=BookInfo.objects.get(id=6)
book.name='运维开发入门'
book.save()


BookInfo.objects.filter(id=6).update(name='爬虫入门',commentcount=6)


book=BookInfo.objects.get(id=6)
book.delete()

BookInfo.objects.filter(id=5).delete()


BookInfo.objects.all()
try:
    book=BookInfo.objects.get(id=6)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

'''查询编号为1的图书
查询书名包含'湖'的图书
查询书名以'部'结尾的图书
查询书名为空的图书
查询编号为1或3或5的图书
查询编号大于3的图书
查询1980年发表的图书
查询1990年1月1日后发表的图书'''
from book.models import BookInfo,PeopleInfo
book=BookInfo.objects.get(id=1)
print(book)
BookInfo.objects.filter(name__contains='湖')
BookInfo.objects.filter(name__endswith='部')
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(id__in=[1,3,5])
BookInfo.objects.filter(pub_date__year=1980)
BookInfo.objects.filter(pub_date__gt='1900-1-1')

'查询阅读量大于等于评论量的图书。' \
'查询阅读量大于2倍评论量的图书。' \
'查询阅读量大于20，并且编号小于3的图书。' \
'查询阅读量大于20的图书，改写为Q对象如下。'
'查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现' \
'查询编号不等于3的图书。'
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))
book=BookInfo.objects.filter(readcount__gte=F('commentcount'))
print(book)
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
BookInfo.objects.filter(readcount__gt=20,id__lt=3)
BookInfo.objects.filter(readcount__gt=20)
from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))
from django.db.models import Sum,Count
'查询图书的总阅读量。' \
'查询图书总数。' \
'''查询图书，要求图书人物为"郭靖"
查询图书，要求图书中人物的描述包含"八"'''\
'查询图书，要求图书人物为"郭靖"' \
'查询书名为“天龙八部”的所有人物。' \
'查询图书阅读量大于30的所有人物'
from book.models import PeopleInfo

BookInfo.objects.aggregate(Sum('readcount'))
BookInfo.objects.count()
book=BookInfo.objects.filter(peopleinfo__name='郭靖')
BookInfo.objects.filter(peopleinfo__description__contains='八')
person=PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__readcount__gt=30)

