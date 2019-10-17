from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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











