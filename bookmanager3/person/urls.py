from django.urls import path
from person.views import index,shop1

urlpatterns = [
    path('index1/',index),
    path('<a>/<b>/',shop1),
    ]