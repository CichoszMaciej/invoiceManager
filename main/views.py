from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from invoices.models import Invoice


@login_required()
def index(request):
    context = {
        'sum_today': 500.00
    }
    return render(request, 'main/index.html', context)
