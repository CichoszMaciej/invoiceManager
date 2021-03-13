from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from clients.forms import ClientCreate
from clients.models import Client


@login_required()
def list_clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/clients_list.html', context)


@login_required()
def add_client(request):
    context = {
        'form': ClientCreate()
    }
    return render(request, 'clients/new_client.html', context)
