from django.contrib import admin
from .models import Product, Order, CartItem, LineItem

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display =['slug', 'name', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',  'date','delivered' , 'paid']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'product']


class LineItemAdmin(admin.ModelAdmin):
    list_display = [ 'product', 'quantity', 'order']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem, OrderItemAdmin)
admin.site.register(LineItem, LineItemAdmin)