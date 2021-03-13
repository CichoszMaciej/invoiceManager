from django.urls import path

from products.views import product_list, add_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product')
]
