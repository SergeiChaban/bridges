from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from ordersapp.forms import OrderItemForm, OrderForm
from ordersapp.models import Order, OrderItem
from productsapp.models import TechnicalSolutions


def order_create(request, pk):
    product = TechnicalSolutions.objects.get(pk=pk)
    order = Order()
    order_form = OrderForm(instance=order)
    OrderInlineFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        formset = OrderInlineFormSet(request.POST)
        if order_form.is_valid():
            created_form = order_form.save(commit=False)
            created_form.user = request.user
            formset = OrderInlineFormSet(request.POST, instance=created_form)
            if formset.is_valid():
                created_form.save()
                formset.save()
                return redirect(product.get_absolute_url())
    else:
        order_form = OrderForm()
        formset = OrderInlineFormSet()
    context = {
        'form': order_form,
        'formset': formset,
        'product': product,
        'page_title': 'Заказ услуги',
        'bred_title': 'Заказ услуги'
    }
    return render(request, 'ordersapp/order_create.html', context)