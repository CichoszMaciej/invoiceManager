from django.forms import ModelForm

from clients.models import Client


class ClientCreate(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
