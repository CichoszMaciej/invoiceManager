from django.forms import ModelForm

from products.models import Product


class ProductCreate(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'cost', 'gain', 'vat_rate', 'quantity_stock', 'is_active')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'cost', 'price_net', 'vat_rate', 'quantity_stock', 'is_active')
