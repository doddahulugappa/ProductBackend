from django.contrib import admin
from .models import Product, Category, Cart, Entry, ActiveUser


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'quantity', 'rating']


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_entries', 'count', 'total', 'updated', 'timestamp']

    def get_entries(self, obj):
        return "\n".join([str(p) for p in obj.user.all()])


class EntryAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']


class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'activated', 'activation_time']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(ActiveUser, ActiveUserAdmin)
