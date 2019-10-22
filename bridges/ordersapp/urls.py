from django.urls import path
from ordersapp import views as ordersapp

app_name = 'productsapp'

urlpatterns = [
    path('order/create/<int:pk>', ordersapp.order_create, name='order_create'),
    # path('order/list', ordersapp.order_create, name='order_create'),
]
