from django.forms import ModelForm

from invoices.models import Invoice


class InvoiceCreate(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
