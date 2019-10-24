from django.urls import path
from servicesapp.views import ServicesList, ServiceDetail, ServiceCreate

app_name = 'servicesapp'

urlpatterns = [
    path('', ServicesList.as_view(), name='services_url'),
    path('create/', ServiceCreate.as_view(), name='service_create_url'),
    path('<slug:slug>/', ServiceDetail.as_view(), name='service_detail_url')
]
