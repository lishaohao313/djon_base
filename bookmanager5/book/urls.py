from django.urls import path
from book.views import index,shop,register,json,method
from django.urls import converters
from django.urls.converters import register_converter
from book.views import response

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
    path('response/',response)
]


'''class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)'''