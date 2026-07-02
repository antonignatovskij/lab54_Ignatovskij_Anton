from django.urls import path
from .views import products_view, product_add_view, product_view, category_add_view, product_update_view, product_delete_view

urlpatterns = [
    path('', products_view, name='products_list'),
    path('products/', products_view, name='products_list_v2'),
    path('categories/add/', category_add_view, name='add_category'),
    path('products/add/', product_add_view, name='add_product'),
    path('product/<int:pk>/', product_view, name='product_detail'),
    path('product/<int:pk>/update/', product_update_view, name='product_update'),
    path('product/<int:pk>/delete/', product_delete_view, name='product_delete'),
]