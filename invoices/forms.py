from django.forms import ModelForm, DateInput, DecimalField

from invoices.models import Invoice, InvoiceRecord


class InvoiceCreate(ModelForm):
    class Meta:
        model = Invoice
        fields = ('place', 'invoice_status', 'invoice_type', 'client', 'invoice_date', 'sales_date', 'payment_date')
        widgets = {
            'invoice_date': DateInput(attrs={'type': 'date'}),
            'sales_date': DateInput(attrs={'type': 'date'}),
            'payment_date': DateInput(attrs={'type': 'date'})
        }


class InvoiceRecordAdd(ModelForm):
    discount = DecimalField(decimal_places=2, initial=0, max_digits=10, min_value=0, label='Obniżka w PLN na sztuce')

    class Meta:
        model = InvoiceRecord
        fields = ('product', 'quantity')
