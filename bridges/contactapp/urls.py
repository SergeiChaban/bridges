from django.contrib import admin
from django.urls import path
from contactapp import views as contactapp

app_name = 'contactapp'

urlpatterns = [
    path('', contactapp.index, name='index'),
]
