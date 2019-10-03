from django.forms import ModelForm
from django import forms
from contactapp.models import ContactApplication


class ContactForm(ModelForm):
    class Meta:
        model = ContactApplication
        fields = ('name', 'phone', 'email', 'subject', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя*'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail*'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Номер телефона*', }),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема сообщения*', }),
            'message': forms.Textarea(
                attrs={'placeholder': 'Введите текст сообщения'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
