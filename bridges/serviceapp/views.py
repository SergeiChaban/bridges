from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .models import Service
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
# Create your views here.


class ServicesList(ListView):

    model = Service
    context_object_name = 'services'
    template_name = 'serviceapp/services.html'

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ServicesList, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['page_title'] = 'Услуги'
        return context




class ServiceDetail(DetailView):


    model = Service


    # def get_queryset(self):
    #     return Service.objects.all()

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ServiceDetail, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        services = Service.objects.all()
        context['page_title'] = 'Услуга'
        context.update({'services': services
                        })

        return context