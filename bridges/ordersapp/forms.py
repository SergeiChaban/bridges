from django import forms
from ordersapp.models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', 'status', 'is_active')


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ()
