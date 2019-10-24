# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from .models import Service
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .forms import ServiceForm

# @login_required
# def service_list(request):
#     services = Service.objects.all().exclude(is_active=False)
#     context ={
#         'service_list': services,
#     }
#     return render(request, 'serviceapp/service_list.html', context)


# @login_required
# def service_detail(request, slug):
#     service = get_object_or_404(Service, slug=slug)
#     context = {
#         'service_detail': service,
#     }
#     return render(request, 'serviceapp/service_detail.html', context)


class ServicesList(ListView):

    model = Service
    context_object_name = 'services'
    template_name = 'servicesapp/services.html'

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ServicesList, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем ее некоторым значением
        context['page_title'] = 'Услуги'
        return context

class ServiceCreate(View):
    def get(self, request):
        form = ServiceForm()
        return render(request,'servicesapp/service_create.html', context={'form':form})

    def post(self, request):
        bound_form = ServiceForm(request.POST)

        if bound_form.is_valid():
            new_service = bound_form.save()
            return redirect(new_service)
        return render(request, 'servicesapp/service_create.html', context={'form':bound_form})


class ServiceDetail(DetailView):

    model = Service


    # def get_queryset(self):
    #     return Service.objects.all()

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ServiceDetail, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем ее некоторым значением
        services = Service.objects.all()
        context['page_title'] = 'Услуга'
        context.update({'services': services
                        })

        return context