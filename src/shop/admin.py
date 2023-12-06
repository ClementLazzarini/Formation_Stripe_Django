from django.contrib import admin
from shop.models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "stock")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("reference", "status")


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
