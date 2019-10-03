from django.shortcuts import render
from serviceapp.models import Service
# Create your views here.

def services(request):
	services = Service.objects.all()
	context:{
		'services':services
	}
	return render(request, 'serviceapp/services.html', context)

# def services_detail(request):
# 	return render(request, 'serviceapp/services-detail.html'