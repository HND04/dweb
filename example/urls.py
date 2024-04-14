# example/urls.py
from django.urls import path

from example.views import index,home


urlpatterns = [
    path('', index),
    path('index/', home),
]