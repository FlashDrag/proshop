from django.contrib import admin

from .models import Product, Review, Order, OrderItem, ShippingAddress


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "count_in_stock")


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = OrderItemAdminInline,


admin.site.register(Review)
admin.site.register(ShippingAddress)
