from django.shortcuts import render, redirect
from authapp.models import Company
from partnersapp.forms import CompanyForm


def partners_list(request):
    partners = Company.objects.all()
    context = {
        'partners': partners,
        'page_title': 'Партнеры компании',
        'bred_title': 'Партнеры компании'
    }
    return render(request, 'partnersapp/partners_list.html', context)


def partner_detail(request, pk):
    partner = Company.objects.get(pk=pk)
    context = {
        'partner': partner,
        'page_title': 'Описание компании',
        'bred_title': 'Описание компании'
    }
    return render(request, 'partnersapp/partner_detail.html', context)


def partner_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/partners')
    else:
        form = CompanyForm()
    context = {
        'form': form,
        'page_title': 'Добавление компании',
        'bred_title': 'Добавление компании'
    }
    return render(request, 'partnersapp/company_create.html', context)
