from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from productsapp.models import TechnicalSolutions
from researchapp.models import Document


class ProductsView(ListView):
    template_name = 'productsapp/products.html'
    context_object_name = 'all_products'
    extra_context = {
        'page_title': 'Технические решения для транспортного строительства',
        'bred_title': 'Технические решения'
    }

    def get_queryset(self):
        return TechnicalSolutions.objects.all().order_by('pk')


def product(request, slug):
    item = get_object_or_404(TechnicalSolutions, slug=slug)
    title = item.name
    docs = Document.objects.filter(techsol__pk=item.pk)
    researches = docs.filter(type__in=(2, 3,))
    documents = docs.filter(type__id=1)
    feedback = docs.filter(type__id=4)

    content = {
        'page_title': title,
        'bred_title': title,
        'product': item,
        'researches': researches,
        'documents': documents,
        'feedback': feedback
    }
    return render(request, 'productsapp/product.html', content)
