from django.contrib import admin
from .models import User,Order,Products

# Register your models here.
admin.site.register(User)
# admin.site.register(Products)
admin.site.register(Order)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

    def get_queryset(self, request):
        # Ensures the query uses the correct database 'products_db'
        queryset = super().get_queryset(request)
        return queryset.using('products_db')

admin.site.register(Products, ProductsAdmin)