from django.urls import path

from invoices.views import invoice_list, add_invoice

urlpatterns = [
    path('', invoice_list, name='invoice_list'),
    path('add/', add_invoice, name='add_invoice')
]
