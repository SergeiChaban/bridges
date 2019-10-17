from django import forms

from productsapp.models import TechnicalSolutions


class ProductForm(forms.ModelForm):
    class Meta:
        model = TechnicalSolutions
        fields = []


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = TechnicalSolutions
        fields = ['name', 'short_desc', 'description', 'image', 'is_active']
