from django import forms
from django.forms import ModelForm

from .models import Users


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
