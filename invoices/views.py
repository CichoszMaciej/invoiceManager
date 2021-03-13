from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from invoices.forms import InvoiceCreate
from invoices.models import Invoice
from products.forms import ProductCreate


@login_required()
def invoice_list(request):
    invoices = Invoice.objects.all()
    info = ''
    if 'info' in request.GET:
        info = request.GET['info']
    context = {
        'invoices': invoices,
        'length': len(invoices),
        'info': info
    }

    return render(request, 'invoices/invoices_list.html', context)


@login_required()
def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceCreate(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return HttpResponseRedirect(reverse(invoice_list) + '?info=success')
        else:
            return render(request, 'invoices/new_invoice.html', {'form': form})

    else:
        context = {
            'form': InvoiceCreate()
        }

        return render(request, 'invoices/new_invoice.html', context)
