from django import forms
from ordersapp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service']

