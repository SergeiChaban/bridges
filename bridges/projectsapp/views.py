from django.shortcuts import render, get_object_or_404

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions


def projects(request):
    projects = Project.objects.all()
    products = TechnicalSolutions.objects.all()

    content = {
        'projects': projects,
        'products': products
    }
    return render(request, 'projectsapp/grid.html', content)


def project(request, pk):
    title = 'Проекты компании'
    item = get_object_or_404(Project, pk=pk)
    gallery = ProjectImage.objects.all()
    solutions = ProjectHasTechnicalSolutions.objects.all()

    content = {
        'page_title': title,
        'project': item,
        'gallery': gallery,
        'solutions': solutions
    }
    return render(request, 'projectsapp/project.html', content)


def product(request, slug):
    title = "Технические решения"
    item = get_object_or_404(TechnicalSolutions, slug=slug)
    material_list = item.material_content.all()
    project_list = item.project_set.all()

    content = {
        'page_title': title,
        'product': item,
        'material_list': material_list,
        'projects': project_list
    }
    return render(request, 'productsapp/product.html', content)

