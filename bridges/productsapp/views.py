from django.shortcuts import render, get_object_or_404
from productsapp.models import TechnicalSolutions, Material
from projectsapp.models import ProjectHasTechnicalSolutions
from projectsapp.models import Project
from researchapp.models import Document


def products(request):
    title = "Технические решения"
    technical_solutions = TechnicalSolutions.objects.all().order_by('pk')
    # all_products = Product.objects.filter(category__slug=slug).exclude(is_active=False)

    content = {
        'page_title': title,
        'products': technical_solutions
    }
    return render(request, 'productsapp/products.html', content)


def product(request, slug):
    title = "Технические решения"
    item = get_object_or_404(TechnicalSolutions, slug=slug)
    material_list = item.material_content.all()
    projects = item.project_set.all()
    docs = Document.objects.filter(techsol__pk=item.pk)
    researches = docs.filter(type__in=(2, 3,))
    documents = docs.filter(type__id=1)
    feedback = docs.filter(type__id=4)

    content = {
        'page_title': title,
        'product': item,
        'material_list': material_list,
        'projects': projects,
        'researches': researches,
        'documents': documents,
        'feedback': feedback
    }
    return render(request, 'productsapp/product.html', content)
