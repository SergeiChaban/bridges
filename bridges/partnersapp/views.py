from django.contrib.postgres.search import SearchVector
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.urls import reverse
from authapp.models import Company, CompanyUsers
from partnersapp.forms import CompanyForm, CompanyUsersForm, CompanyUserUpdateForm, SearchForm
from django.db.models import Q


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


def partner_delete(request, pk):
    partner = get_object_or_404(Company, pk=pk)
    context = {
        'partner': partner,
        'page_title': 'Удаление компании',
        'bred_title': 'Удаление компании'
    }
    return render(request, 'partnersapp/company_delete.html', context)


def partner_delete_confirm(request, pk):
    get_object_or_404(Company, pk=pk).delete()
    return HttpResponseRedirect(reverse('partners:partners_list'))


def partner_user_update(request, pk):
    company = Company.objects.get(pk=pk)
    company_form = CompanyUserUpdateForm(instance=company)
    UserInlineFormSet = inlineformset_factory(Company, CompanyUsers, form=CompanyUsersForm, extra=1)
    formset = UserInlineFormSet(instance=company)
    if request.method == "POST":
        company_form = CompanyUserUpdateForm(request.POST)
        if id:
            company_form = CompanyUserUpdateForm(request.POST, instance=company)
            formset = UserInlineFormSet(request.POST)
            if company_form.is_valid():
                created_company = company_form.save(commit=False)
                created_company.form = request.form
                created_company.category = request.category
                formset = UserInlineFormSet(request.POST, instance=created_company)
                if formset.is_valid():
                    created_company.save()
                    formset.save()
                    return HttpResponseRedirect(created_company.get_absolute_url())
    context ={
        'company_form': company_form,
        'formset': formset,
        'page_title': 'Добавление сотрудника',
        'bred_title': 'Добавление сотрудника',
        'company': company
    }
    return render(request, "partnersapp/company_user_create.html", context)


def company_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        companies = Company.objects.filter(
            Q(name__icontains=q) | Q(inn__icontains=q) | Q(phone__icontains=q)
        ).order_by('name')
        context = {
            'page_title': 'Результаты поиска',
            'bred_title': 'Результаты поиска',
            'founded_products': companies,
            'query': q,
        }
        return render(request, 'partnersapp/search.html', context)
    else:
        context = {
            'page_title': 'Результаты поиска',
            'bred_title': 'Результаты поиска',
        }
        return render(request, 'partnersapp/search.html', context)

