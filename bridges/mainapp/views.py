from django.shortcuts import render

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project


def index(request):
    latest_projects = Project.objects.all().order_by('pk')[:6]
    products = TechnicalSolutions.objects.all().order_by('pk')
    context = {
        'latest_projects': latest_projects,
        'products': products
    }
    return render(request, 'mainapp/index.html', context)
