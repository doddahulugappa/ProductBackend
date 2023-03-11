from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Product, Category, Cart, CartItem, ActiveUser


# Register your models here.
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']


class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'quantity', 'rating']


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'count', 'total', 'updated', 'timestamp', 'completed']
    readonly_fields = ['count', 'total']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity']


class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'activated', 'activation_time']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(ActiveUser, ActiveUserAdmin)
