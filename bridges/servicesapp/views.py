# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from .models import Service
from django.views.generic import CreateView
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


