from django.urls import path

from invoices.views import invoice_list, add_invoice, add_invoice_record, view_invoice, edit_invoice, delete_invoice

urlpatterns = [
    path('', invoice_list, name='invoice_list'),
    path('<int:invoice_id>', view_invoice, name='view_invoice'),
    path('edit/<int:invoice_id>', edit_invoice, name='edit_invoice'),
    path('add/', add_invoice, name='add_invoice'),
    path('delete/<int:invoice_id>', delete_invoice, name='delete_invoice'),
    path('add-record/<int:invoice_id>', add_invoice_record, name='add_invoice_record')
]
