from django import forms
from authapp.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ()
