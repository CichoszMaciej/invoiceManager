from django.db import models


class Place(models.Model):
    name = models.CharField(null=True, max_length=64)
    address = models.CharField(null=True, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
