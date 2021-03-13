from django.db import models


class Product(models.Model):
    name = models.CharField(null=True, max_length=64, name='Nazwa')
    description = models.CharField(null=True, max_length=255, name='Opis')
    price_net = models.DecimalField(null=True, decimal_places=2, max_digits=16, name='Cena Netto')
    price_gross = models.DecimalField(null=True, decimal_places=2, max_digits=16, name='Cena Brutto')
    price_vat = models.DecimalField(null=True, decimal_places=2, max_digits=16, name='Wartość VAT')
    vat_rate = models.IntegerField(null=True, name='Stawka VAT')
    is_active = models.BooleanField(default=True, name='Czy jest aktywny?')
    quantity_stock = models.DecimalField(null=True, decimal_places=3, max_digits=16, name='Stan magazynowy')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '(' + str(self.quantity_stock) + ')'
