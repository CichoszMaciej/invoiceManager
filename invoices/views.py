import json
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from invoices.forms import InvoiceCreate, InvoiceRecordAdd
from invoices.models import Invoice, InvoiceRecord
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
            invoice.price_gross = 0
            invoice.price_net = 0
            invoice.price_vat = 0
            invoice.paid = 0
            invoice.month = invoice.invoice_date.month
            invoice.year = invoice.invoice_date.year
            next_num = Invoice.objects.filter(year=invoice.year, month=invoice.month, place=invoice.place).count() + 1
            invoice.invoice_nr = str(invoice.invoice_type.symbol) + '/' + str(invoice.place.invoice_code) + '/'
            invoice.invoice_nr += str(invoice.year) + '/' + str(invoice.month) + '/' + str(next_num)
            invoice.save()
            return HttpResponseRedirect(reverse(invoice_list) + '?info=success')
        else:
            return render(request, 'invoices/new_invoice.html', {'form': form})

    else:
        context = {
            'form': InvoiceCreate()
        }

        return render(request, 'invoices/new_invoice.html', context)


@login_required()
def view_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice_items = InvoiceRecord.objects.filter(invoice=invoice)
    context = {
        'items': invoice_items
    }

    return render(request, 'invoices/view_invoice.html', context)


@login_required()
def add_invoice_record(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        form = InvoiceRecordAdd(request.POST)
        if form.is_valid():
            invoice_record = form.save(commit=False)
            invoice_record.invoice = invoice
            invoice_record.price_gross = float(invoice_record.product.price_gross) - float(form.data.get('discount'))
            invoice_record.price_net = round(invoice_record.price_gross / (
                    1 + (float(invoice_record.product.vat_rate.value) / 100)), 2)
            invoice_record.price_vat = invoice_record.price_gross - invoice_record.price_net
            invoice_record.vat_rate = int(invoice_record.product.vat_rate.value)
            invoice_record.total_price_gross = invoice_record.price_gross * float(invoice_record.quantity)
            invoice_record.total_price_net = invoice_record.price_net * float(invoice_record.quantity)
            invoice_record.total_price_vat = invoice_record.price_vat * float(invoice_record.quantity)
            invoice.price_gross += Decimal(invoice_record.total_price_gross)
            invoice.price_net += Decimal(invoice_record.total_price_net)
            invoice.price_vat += Decimal(invoice_record.total_price_vat)
            invoice_record.save()
            invoice.save()
            return HttpResponseRedirect(reverse(invoice_list) + '?info=success')
        else:
            return render(request, 'invoices/new_invoice_record.html', {'form': form})

    else:
        context = {
            'form': InvoiceRecordAdd(initial={'quantity': 0})
        }

        return render(request, 'invoices/new_invoice_record.html', context)
