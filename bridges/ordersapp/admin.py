from django.contrib import admin
from ordersapp.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'status', 'is_active',)
    list_display_links = ('user',)
    inlines = [
        OrderItemInline,
    ]

