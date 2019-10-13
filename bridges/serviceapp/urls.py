from django.contrib import admin
from django.urls import path
from serviceapp.views import ServicesList, ServiceDetail

app_name = 'serviceapp'

urlpatterns = [
    path('', ServicesList.as_view(), name='services_url'),
    path('<slug:slug>/', ServiceDetail.as_view(), name='service_detail_url')
]
