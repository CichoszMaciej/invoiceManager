from django.forms import ModelForm

from products.models import Product


class ProductCreate(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'cost', 'gain', 'vat_rate', 'quantity_stock')
