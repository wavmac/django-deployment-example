from django.contrib import admin
from django.urls import path

from .views import index, other, relative

app_name = 'basic_app'

urlpatterns = [
    path('other/',other,name='other'),
    path('relative/',relative,name='relative')
]
