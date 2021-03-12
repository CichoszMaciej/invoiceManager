from django.db import models


class Product(models.Model):
    name = models.CharField(null=True, max_length=64)
    description = models.CharField(null=True, max_length=255)
    price_net = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    price_gross = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    price_vat = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    vat_rate = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
