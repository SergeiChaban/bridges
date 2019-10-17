from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from productsapp.forms import ProductUpdateForm
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
    feedback = docs.filter(type__id=4).order_by('-pk')

    content = {
        'projects': item.get_projects(),
        'works': item.get_works(),
        'page_title': title,
        'bred_title': title,
        'product': item,
        'researches': researches,
        'documents': documents,
        'feedback': feedback
    }
    return render(request, 'productsapp/product.html', content)


def product_update(request, slug):
    product = get_object_or_404(TechnicalSolutions, slug=slug)
    product_form = ProductUpdateForm(instance=product)
    if request.method == 'POST':
        product_form = ProductUpdateForm(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(product.get_absolute_url())
    context = {
        'product_form': product_form,
        'page_title': 'Обновление технических решений',
        'bred_title': 'Обновление техрешений',
        'product': product
    }
    return render(request, 'productsapp/product_update.html', context)
