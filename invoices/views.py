from datetime import datetime
from decimal import Decimal
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.urls import reverse
from fpdf import FPDF, HTMLMixin
from xhtml2pdf import pisa

from invoices.forms import InvoiceForm, InvoiceRecordAdd, InvoiceEditForm
from invoices.models import Invoice, InvoiceRecord
from products.models import Product


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
        form = InvoiceForm(request.POST)
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
            'form': InvoiceForm()
        }

        return render(request, 'invoices/new_invoice.html', context)


@login_required()
def view_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice_items = InvoiceRecord.objects.filter(invoice=invoice)
    context = {
        'invoice': invoice,
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

            product = invoice_record.product
            product.quantity_stock -= invoice_record.quantity
            product.save()

            invoice_record.save()
            invoice.save()
            return HttpResponseRedirect(reverse(view_invoice, kwargs={'invoice_id': invoice.id}) + '?info=success')
        else:
            return render(request, 'invoices/new_invoice_record.html', {'form': form})

    else:
        form = InvoiceRecordAdd(initial={'quantity': 0})
        form.fields['product'].queryset = Product.objects.filter(is_active=True)
        context = {
            'form': form
        }

        return render(request, 'invoices/new_invoice_record.html', context)


@login_required()
def edit_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        form = InvoiceEditForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return HttpResponseRedirect(reverse(invoice_list) + '?info=success-edit')
        else:
            return render(request, 'invoices/edit_invoice.html', {'form': form, 'invoice_nr': invoice.invoice_nr})

    else:
        context = {
            'form': InvoiceEditForm(instance=invoice),
            'invoice_nr': invoice.invoice_nr
        }

        return render(request, 'invoices/edit_invoice.html', context)


@login_required()
def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice_records = InvoiceRecord.objects.filter(invoice=invoice)
    if 'd' in request.GET and request.GET['d'] == 'yes':
        invoice_records.delete()
        invoice.delete()
        return HttpResponseRedirect(reverse(invoice_list) + '?info=delete')
    else:
        return render(request, 'invoices/delete_invoice.html', {'invoice': invoice})


@login_required()
def delete_invoice_record(request, record_id):
    invoice_record = get_object_or_404(InvoiceRecord, pk=record_id)
    if 'd' in request.GET and request.GET['d'] == 'yes':
        invoice_record.delete()
        invoice_record.invoice.recalculate()
        return HttpResponseRedirect(
            reverse(view_invoice, kwargs={'invoice_id': invoice_record.invoice.id}) + '?info=delete')
    else:
        return render(request, 'invoices/delete_invoice_record.html', {'invoice_record': invoice_record})


class HtmlPdf(FPDF, HTMLMixin):
    pass


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required()
def generate_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice_items = InvoiceRecord.objects.filter(invoice=invoice)
    context = {
        'invoice': invoice,
        'items': invoice_items
    }
    pdf = render_to_pdf('invoices/invoice_pdf.html', context)

    return HttpResponse(pdf, content_type='application/pdf')


@login_required()
def invoice_stats_graph(request):
    labels = []
    data = []
    invoices = Invoice.objects.order_by('-invoice_date').all()[:100]

    for invoice in invoices:
        labels.append(datetime.fromisoformat(str(invoice.invoice_date)).strftime("%Y-%m-%d"))
        data.append(invoice.price_gross)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required()
def stats(request):
    return render(request, 'invoices/stat.html')
