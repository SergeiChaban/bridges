from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView

from .models import Users


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'page_title': 'Авторизация на сайте',
        'bred_title': 'Авторизация'
    }


class UserProfileView(DetailView):
    model = Users
    template_name = 'authapp/profile.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class UserLogoutView(LogoutView):
    extra_context = {
        'page_title': 'Авторизация на сайте',
        'bred_title': 'Авторизация на сайте'
    }
    template_name = 'authapp/logout.html'
    extra_context = {
        'page_title': 'Выход с сайта',
        'bred_title': 'Выход с сайта'
    }
