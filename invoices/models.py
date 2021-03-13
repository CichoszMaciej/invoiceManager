from django.db import models

from clients.models import Client
from products.models import Product


class InvoiceStatus(models.Model):
    name = models.CharField(null=True, max_length=64)

    def __str__(self):
        return self.name


class InvoiceType(models.Model):
    name = models.CharField(null=True, max_length=64)
    symbol = models.CharField(null=True, max_length=4)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    invoice_status = models.ForeignKey(InvoiceStatus, null=True, on_delete=models.DO_NOTHING)
    invoice_type = models.ForeignKey(InvoiceType, null=True, on_delete=models.DO_NOTHING)
    invoice_nr = models.CharField(null=True, max_length=128)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    price_gross = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    price_net = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    price_vat = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    sales_date = models.DateField(null=True)
    invoice_date = models.DateField(null=True)
    payment_date = models.DateField(null=True)
    paid = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.invoice_nr


class InvoiceRecord(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price_gross = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    price_net = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    price_vat = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    vat_rate = models.IntegerField(null=True)
    quantity = models.DecimalField(null=True, decimal_places=3, max_digits=16)
    total_price_gross = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    total_price_net = models.DecimalField(null=True, decimal_places=2, max_digits=16)
    total_price_vat = models.DecimalField(null=True, decimal_places=2, max_digits=16)

    def __str__(self):
        return self.product.name
