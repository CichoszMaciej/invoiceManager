from django.db import models


class Client(models.Model):
    nip = models.CharField(max_length=30, null=True)
    regon = models.CharField(max_length=30, null=True)
    client_name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=64, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name + ' (' + self.nip + ')'
