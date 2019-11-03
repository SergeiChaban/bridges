from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import inlineformset_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from ordersapp.models import Order
from django.views.generic import View, CreateView
from .forms import *
from .models import *


@login_required
def restricted_area(request):
    user = request.user
    user_companies = CompanyUsers.objects.filter(user_id=user.pk, works=True)
    user_projects = ProjectManagers.objects.filter(manager_id=user.pk)
    user_orders = Order.objects.filter(user_id=user.pk)
    context = {
        'section': 'restricted_area',
        'page_title': 'Личный кабинет',
        'bred_title': 'Личный кабинет',
        'user_companies': user_companies,
        'user_projects': user_projects,
        'user_orders': user_orders
    }
    return render(request, 'authapp/restricted_area.html', context)


def register(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active = False
            new_user.save()
            return render(request, 'authapp/register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterUserForm()
    return render(request, 'authapp/register.html', {'form': user_form})


def user_profile(request, pk):
    user_companies = CompanyUsers.objects.filter(user_id=pk, works=True)
    user = get_object_or_404(Users, pk=pk)
    user_projects = ProjectManagers.objects.filter(manager_id=pk)
    context = {
        'user': user,
        'user_projects': user_projects,
        'user_companies': user_companies,
        'page_title': 'Профиль пользователя',
        'bred_title': 'Профиль пользователя'
    }
    return render(request, 'authapp/user_profile.html', context)


def company_self_user_update(request, pk):
    company_user = get_object_or_404(Users, pk=pk)
    company_user_form = UsersForCompanyUsersForm(instance=company_user)
    InlineFormset = inlineformset_factory(Users, CompanyUsers, form=CompanyUsersForm, extra=1)
    formset = InlineFormset(instance=company_user)
    if request.method == 'POST':
        company_user_form = UsersForCompanyUsersForm(request.POST, instance=company_user)
        formset = InlineFormset(request.POST)
        if company_user_form.is_valid():
            updated_company_user_form = company_user_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_company_user_form)
            if formset.is_valid():
                updated_company_user_form.save()
                formset.save()
                return HttpResponseRedirect(updated_company_user_form.get_self_absolute_url())
    context = {
        'form': company_user_form,
        'formset': formset,
        'user': company_user,
        'page_title': 'Редактор компаний пользователя',
        'bred_title': 'Редактор компаний пользователя'
    }
    return render(request, 'authapp/self_profile_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def profile_self_user_update(request, pk):
    user = get_object_or_404(Users, pk=pk)
    user_form = UsersForEditProfileForm(instance=user)
    if request.method == 'POST':
        user_form = UsersForEditProfileForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(user.get_self_absolute_url())
    context = {
        'form': user_form,
        'page_title': 'Редактор профиля пользователя',
        'bred_title': 'Редактор профиля пользователя'
    }
    return render(request, 'authapp/self_profile_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def project_self_user_update(request, pk):
    project_user = get_object_or_404(Users, pk=pk)
    project_user_form = UsersForProjectManagersForm(instance=project_user)
    InlineFormset = inlineformset_factory(Users, ProjectManagers, form=ProjectManagersForm, extra=1)
    formset = InlineFormset(instance=project_user)
    if request.method == 'POST':
        project_user_form = UsersForCompanyUsersForm(request.POST, instance=project_user)
        formset = InlineFormset(request.POST)
        if project_user_form.is_valid():
            updated_project_user_form = project_user_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_project_user_form)
            if formset.is_valid():
                updated_project_user_form.save()
                formset.save()
                return HttpResponseRedirect(updated_project_user_form.get_self_absolute_url())
    context = {
        'form': project_user_form,
        'formset': formset,
        'page_title': 'Редактор проектов пользователя',
        'bred_title': 'Редактор проектов пользователя'
    }
    return render(request, 'authapp/self_profile_update.html', context)


class ProjectsManagerCreateView(CreateView):
    pass


@user_passes_test(lambda u: u.is_superuser)
def company_user_update(request, pk):
    company_user = get_object_or_404(Users, pk=pk)
    company_user_form = UsersForCompanyUsersForm(instance=company_user)
    InlineFormset = inlineformset_factory(Users, CompanyUsers, form=CompanyUsersForm, extra=1)
    formset = InlineFormset(instance=company_user)
    if request.method == 'POST':
        company_user_form = UsersForCompanyUsersForm(request.POST, instance=company_user)
        formset = InlineFormset(request.POST)
        if company_user_form.is_valid():
            updated_company_user_form = company_user_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_company_user_form)
            if formset.is_valid():
                updated_company_user_form.save()
                formset.save()
                return HttpResponseRedirect(updated_company_user_form.get_absolute_url())
    context = {
        'form': company_user_form,
        'formset': formset,
        'form_user': company_user,
        'page_title': 'Редактор компаний пользователя',
        'bred_title': 'Редактор компаний пользователя'
    }
    return render(request, 'authapp/user_profile_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def profile_user_update(request, pk):
    user = get_object_or_404(Users, pk=pk)
    user_form = UsersForEditProfileForm(instance=user)
    if request.method == 'POST':
        user_form = UsersForEditProfileForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(user.get_absolute_url())
    context ={
        'form': user_form,
        'form_user': user,
        'page_title': 'Редактор профиля пользователя',
        'bred_title': 'Редактор профиля пользователя'
    }
    return render(request, 'authapp/user_profile_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def project_user_update(request, pk):
    project_user = get_object_or_404(Users, pk=pk)
    project_user_form = UsersForProjectManagersForm(instance=project_user)
    InlineFormset = inlineformset_factory(Users, ProjectManagers, form=ProjectManagersForm, extra=1)
    formset = InlineFormset(instance=project_user)
    if request.method == 'POST':
        project_user_form = UsersForCompanyUsersForm(request.POST, instance=project_user)
        formset = InlineFormset(request.POST)
        if project_user_form.is_valid():
            updated_project_user_form = project_user_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_project_user_form)
            if formset.is_valid():
                updated_project_user_form.save()
                formset.save()
                return HttpResponseRedirect(updated_project_user_form.get_absolute_url())
    context = {
        'form': project_user_form,
        'formset': formset,
        'form_user': project_user,
        'page_title': 'Редактор проектов пользователя',
        'bred_title': 'Редактор проектов пользователя'
    }
    return render(request, 'authapp/user_profile_update.html', context)


def company_self_user_list(request, pk):
    user_companies_list = CompanyUsers.objects.filter(user_id=pk).order_by('-works')
    context = {
        'user_companies_list': user_companies_list,
        'page_title': 'Список компаний пользователя',
        'bred_title': 'Список компаний пользователя'
    }
    return render(request, 'authapp/self_list.html', context)


def company_user_list(request, pk):
    user = get_object_or_404(Users, pk=pk)
    user_companies_list = CompanyUsers.objects.filter(user_id=pk).order_by('-works')
    context = {
        'user_companies_list': user_companies_list,
        'user': user,
        'page_title': 'Список компаний пользователя',
        'bred_title': 'Список компаний пользователя'
    }
    return render(request, 'authapp/user_list.html', context)
