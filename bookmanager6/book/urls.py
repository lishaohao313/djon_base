# urlpatterns = [
from django.urls import path
from book.views import index, shop, ceo, RegisterView,OrderView
from django.urls import converters
from django.urls.converters import register_converter
from book.views import post_text,post_json
from book.views import cookie,get_cookie
from book.views import session,get_session

class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

register_converter(MobileConverter,'pon')

urlpatterns= [
    path('index/',index),
    path('<pon:mobile>/<b>/',shop),
    path('ceo/',ceo),
    path('post_text/',post_text),
    path('post_json/',post_json),
    path('cookie/',cookie),
    path('get_cookie/',get_cookie),
    path('session/',session),
    path('get_session/',get_session),
    path('163.go/',RegisterView.as_view()),
    path('163.glo/',OrderView.as_view()),
]







'''class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
'''