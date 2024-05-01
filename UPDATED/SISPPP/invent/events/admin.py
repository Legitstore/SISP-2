from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'BossInventory Dashboard'
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','unityprice', 'quantity')
    list_filter = ['name']
    # OR USE THIS ('category',)
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff',  'price', 'sellingprice', 'order_quantity', 'date')
admin.site.register(Order, OrderAdmin)