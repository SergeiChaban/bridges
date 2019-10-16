from django.shortcuts import render
from authapp.models import Company, Users


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
