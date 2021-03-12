from django.contrib import admin

# Register your models here.
from invoices.models import InvoiceRecord, Invoice

admin.site.register(InvoiceRecord)
admin.site.register(Invoice)