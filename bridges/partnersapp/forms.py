from django import forms
from authapp.models import Company, CompanyUsers


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ()


class CompanyUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = []


class CompanyUsersForm(forms.ModelForm):
    class Meta:
        model = CompanyUsers
        exclude = ()
