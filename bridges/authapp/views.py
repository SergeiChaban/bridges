from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'authapp/login.html'


class UserLogoutView(LogoutView):
    template_name = 'authapp/logout.html'
