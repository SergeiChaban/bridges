from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'serviceapp'

urlpatterns = [
    path('', services, name='services_url'),
    path('<str:slug>', service_detail, name='service-detail_url')
]
