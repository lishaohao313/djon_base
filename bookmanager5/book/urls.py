from django.urls import path
from book.views import index,shop,register,json,method
from django.urls import converters
from django.urls.converters import register_converter
from book.views import response
# from book.views import cookie,get_cookie,session,get_session
from book.views import set_cookie,get_cookie,set_session,get_session
from book.views import LogView

class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
register_converter(MobileConverter,'mobile')


urlpatterns=[
    path('index/',index),
    path('<int:a>/<mobile:mobile>/',shop),
    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('response/',response),
    # path('cookie/',cookie),
    # path('get_cookie/',get_cookie),
    # path('session/',session),
    # path('get_session/',get_session),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('163.log/',LogView.as_view()),

]


'''class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)'''