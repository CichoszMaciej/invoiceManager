from django.contrib import admin

# Register your models here.
from invoices.models import InvoiceRecord, Invoice, InvoiceStatus, InvoiceType

admin.site.register(InvoiceRecord)
admin.site.register(Invoice)
admin.site.register(InvoiceStatus)
admin.site.register(InvoiceType)
