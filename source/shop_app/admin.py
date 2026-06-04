from django.contrib import admin

from shop_app.models import Product, Category

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'prod_title', 'prod_desc', 'category', 'date_of_add', 'price']
    list_filter = ['price']
    search_fields = ['prod_title', 'prod_desc', 'category', 'date_of_add', 'price']
    fields = ['prod_title', 'prod_desc', 'category', 'date_of_add', 'price', 'product_image']
    readonly_fields = ['date_of_add']

admin.site.register(Product, ProductsAdmin)
admin.site.register(Category)
