from django.urls import path

from invoices.views import invoice_list, add_invoice, add_invoice_record, view_invoice

urlpatterns = [
    path('', invoice_list, name='invoice_list'),
    path('<int:invoice_id>', view_invoice, name='view_invoice'),
    path('add/', add_invoice, name='add_invoice'),
    path('add-record/<int:invoice_id>', add_invoice_record, name='add_invoice_record')
]
