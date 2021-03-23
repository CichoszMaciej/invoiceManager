from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from invoices.models import Invoice


@login_required()
def index(request):
    invoices = Invoice.objects.filter(invoice_date=datetime.now().date())
    sum_today = 0
    for i in invoices:
        sum_today += i.price_gross

    context = {
        'sum_today': sum_today
    }
    return render(request, 'main/index.html', context)
