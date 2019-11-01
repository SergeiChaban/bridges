from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from ordersapp.forms import OrderForm
from ordersapp.models import Order
from productsapp.models import TechnicalSolutions


def order_create(request, pk):
	product = TechnicalSolutions.objects.get(pk=pk)
	users_orders = Order.objects.filter(user=request.user)
	count_orders = len(users_orders)
	if request.method == 'POST':
		order_form = OrderForm(request.POST)
		if order_form.is_valid():
			created_form = order_form.save(commit=False)
			created_form.user = request.user
			if count_orders == 0:
				created_form.order_number = 1
			else:
				created_form.order_number = count_orders + 1
			created_form.save()
			return redirect(product.get_absolute_url())
	else:
		order_form = OrderForm()
	context = {
		'form': order_form,
		'product': product,
		'users_orders': users_orders,
		'page_title': 'Заказ услуги',
		'bred_title': 'Заказ услуги'
	}
	return render(request, 'ordersapp/order_create.html', context)
