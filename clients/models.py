from django.db import models


class Client(models.Model):
    nip = models.CharField(max_length=30, null=True, verbose_name="NIP")
    client_name = models.CharField(max_length=30, null=True, verbose_name= "Nazwa Klienta")
    address = models.CharField(max_length=64, null=True, verbose_name="Adres")
    city = models.CharField(max_length=64, null=True, verbose_name="Miasto")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name + ' (' + self.nip + ')'
