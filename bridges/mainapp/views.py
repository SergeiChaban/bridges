from django.shortcuts import render
from projectsapp.models import ProjectImage
from projectsapp.views import TechnicalSolutions

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



    return render(request, 'mainapp/index.html')


class LastProjectList(TechnicalSolutions):

    """docstring for LastProjectList"""

    def get_queryset(self):
        return super().get_queryset().order_by('-pk')[:3]
