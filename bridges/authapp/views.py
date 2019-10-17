from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from projectsapp.models import ProjectManagers
from .forms import RegisterUserForm, LoginUserForm, CompanyUsersForm
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
    company_user = CompanyUsers.objects.filter(user_id=pk)
    company_user_form = CompanyUsersForm(instance=company_user)
    if request.method == 'POST':
        company_user_form = CompanyUsersForm(request.POST, instance=company_user)
        if company_user_form.is_valid():
            company_user_form.save()
            return HttpResponseRedirect(company_user.get_absolute_url())
    context = {
        'form': company_user_form,
        'company_user': company_user
    }
    return render(request, 'authapp/profile_update.html', context)
