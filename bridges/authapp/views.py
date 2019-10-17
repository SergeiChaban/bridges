from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from projectsapp.models import ProjectManagers
from .forms import *
from .models import *


class RegisterUserView(CreateView):
    model = Users
    form_class = RegisterUserForm
    extra_context = {
        'page_title': 'Регистрация на сайте',
        'bred_title': 'Регистрация'
    }
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')


class UserLoginView(LoginView):
    authentication_form = LoginUserForm
    extra_context = {
        'page_title': 'Авторизация на сайте',
        'bred_title': 'Авторизация'
    }
    template_name = 'authapp/login.html'





class UserLogoutView(LogoutView):

    extra_context = {
        'page_title': 'Выход с сайта',
        'bred_title': 'Выход с сайта'
    }
    template_name = 'authapp/logout.html'


def company_users_update(request, pk):
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
        'user': company_user,
        'page_title': 'Редактор компаний пользователя',
        'bred_title': 'Редактор компаний пользователя'
    }
    return render(request, 'authapp/profile_update.html', context)


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
        'page_title': 'Редактор профиля пользователя',
        'bred_title': 'Редактор профиля пользователя'
    }
    return render(request, 'authapp/profile_update.html', context)


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
        'page_title': 'Редактор профиля пользователя',
        'bred_title': 'Редактор профиля пользователя'
    }
    return render(request, 'authapp/profile_update.html', context)