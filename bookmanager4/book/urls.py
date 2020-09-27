# urlpatterns = [
from django.urls import path
from book.views import index,shop,register,json,method
from django.urls import converters
from django.urls.converters import register_converter
class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
register_converter(MobileConverter,'thoop')

urlpatterns=[
    path('index/',index),
    path('<int:city_id>/<thoop:mobile>/',shop),
    path('register/',register),
    path('json/',json),
    path('method/',method),
]


'''class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)'''