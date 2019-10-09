from django.shortcuts import render
from .models import Service
# Create your views here.

def services(request):

	services = Service.objects.all()
	title = "Наши услуги"
	context = {
		'page_title': title,
		'services':services
	}

	return render(request, 'serviceapp/services.html', context)


def service_detail(request, slug):

	service = Service.objects.get(slug__iexact=slug)
	title = "Описание услуги"
	context = {
		'page_title': title,
		'service':service
	}

	return render(request, 'serviceapp/service-detail.html', context)