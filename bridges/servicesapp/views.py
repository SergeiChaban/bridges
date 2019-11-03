from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import *


def services_list(request):
    # services = Service.objects.all().exclude(is_active=False)
    context ={
        # 'service_list': services,
        'page_title': 'Услуги компании',
        'bred_title': 'Услуги компании',
    }
    return render(request, 'servicesapp/services_list.html', context)


def services_single(request, pk):
    service = get_object_or_404(Service, pk=pk)
    context = {
        'service_detail': service,
        'page_title': service,
        'bred_title': service,
    }
    return render(request, 'servicesapp/services_detail.html', context)
 