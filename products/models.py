from django.db import models


class VatRate(models.Model):
    value = models.IntegerField(null=False)

    def __str__(self):
        return str(self.value) + '%'


class Product(models.Model):
    name = models.CharField(null=True, max_length=64, verbose_name='Nazwa')
    description = models.CharField(null=True, max_length=255, verbose_name='Opis')
    cost = models.DecimalField(null=True, decimal_places=2, max_digits=16, verbose_name="Koszt")
    gain = models.DecimalField(null=True, decimal_places=0, max_digits=16, verbose_name="Marża")
    vat_rate = models.ForeignKey(VatRate, on_delete=models.DO_NOTHING, verbose_name='Stawka VAT')
    price_net = models.DecimalField(null=True, decimal_places=2, max_digits=16, verbose_name='Cena Netto')
    price_gross = models.DecimalField(null=True, decimal_places=2, max_digits=16, verbose_name='Cena Brutto')
    price_vat = models.DecimalField(null=True, decimal_places=2, max_digits=16, verbose_name='Wartość VAT')
    is_active = models.BooleanField(default=True, verbose_name='Czy jest aktywny?')
    quantity_stock = models.DecimalField(null=True, decimal_places=3, max_digits=16, verbose_name='Stan magazynowy')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '(' + str(self.quantity_stock) + ')'
