from django.urls import path
from partnersapp import views as partnersapp

app_name = 'partnersapp'

urlpatterns = [
    path('', partnersapp.partners_list, name='partners_list'),
    path('partner/<int:pk>', partnersapp.partner_detail, name='partner_detail'),
    path('partner/create', partnersapp.partner_create, name='partner_create'),
]
