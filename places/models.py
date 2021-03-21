from django.db import models


class Place(models.Model):
    name = models.CharField(null=True, max_length=64, verbose_name='Nazwa')
    address = models.CharField(null=True, max_length=255, verbose_name='Adres')
    invoice_code = models.CharField(null=True, max_length=5, verbose_name='Kod faktury')
    timestamp = models.DateTimeField(auto_now_add=True)
    nip = models.CharField(null=True, max_length=64, verbose_name='NIP')
    is_active = models.BooleanField(null=False, default=True, verbose_name='Czy aktywny?')

    def __str__(self):
        return self.name
