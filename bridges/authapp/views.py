from django.contrib.auth.decorators import login_required
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


@login_required
def restricted_area(request):
    user = request.user
    user_companies = CompanyUsers.objects.filter(user_id=user.pk)
    user_projects = ProjectManagers.objects.filter(manager_id=user.pk)
    context = {
        'section': 'restricted_area',
        'page_title': 'Личный кабинет',
        'bred_title': 'Личный кабинет',
        'user_companies': user_companies,
        'user_projects': user_projects,
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



    # class RegisterUserView(CreateView):
    #     model = Users
    #     form_class = RegisterUserForm
    #     extra_context = {
    #         'page_title': 'Регистрация на сайте',
    #         'bred_title': 'Регистрация'
    #     }
    #     template_name = 'authapp/register1.html'
    #     success_url = reverse_lazy('auth:login')
    #
    #
    # class UserLoginView(LoginView):
    #     authentication_form = LoginUserForm
    #     extra_context = {
    #         'page_title': 'Авторизация на сайте',
    #         'bred_title': 'Авторизация'
    #     }
    #     template_name = 'authapp/1_login.html'
    #

    # class UserProfileView(DetailView):
    #     model = Users
    #     extra_context = {
    #         'page_title': 'Профиль пользователя',
    #         'bred_title': 'Профиль пользователя'
    #     }
    #     template_name = 'authapp/profile.html'
    #
    #     def get_context_data(self, *args, **kwargs):
    #         context = super().get_context_data(*args, **kwargs)
    #         return context





