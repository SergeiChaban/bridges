from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class RegisterUserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'password', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Введите логин*'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'придумайте пароль*'}),
            'phone': forms.TextInput(attrs={'placeholder': 'и укажите телефон для связи*', }),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин*'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'и пароль*'}))

    class Meta:
        model = Users
        AuthenticationFormFields = ('username', 'password')
        exclude = []


class UsersForEditProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'first_name',
            'patronymic',
            'last_name',
            'gender',
            'birthday',
            'phone',
            'email',
            'is_active',
        ]
        # exclude = []


class UsersForCompanyUsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = []


class CompanyUsersForm(forms.ModelForm):
    class Meta:
        model = CompanyUsers
        exclude = ()
