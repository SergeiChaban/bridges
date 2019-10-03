from django.contrib import admin
from django.urls import path
from serviceapp import views as serviceapp

app_name = 'serviceapp'

urlpatterns = [
    path('', serviceapp.services, name='services'),
    # path('', serviceapp.services_detail, name='services-detail'),
]
