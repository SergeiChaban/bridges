from django.contrib import admin
from django.urls import path
from researchapp import views as researchapp


app_name = 'researchapp'

urlpatterns = [
    path('', researchapp.research, name='research'),
]
