from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryCreateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)
urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('products/', ProductListView.as_view(), name='products_list_v2'),
    path('categories/add/', CategoryCreateView.as_view(), name='add_category'),
    path('products/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]