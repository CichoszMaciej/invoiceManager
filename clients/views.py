from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from clients.forms import ClientCreate
from clients.models import Client


@login_required()
def list_clients(request):
    clients = Client.objects.all()

    info = ''
    if 'info' in request.GET:
        info = request.GET['info']

    context = {
        'clients': clients,
        'info': info
    }
    return render(request, 'clients/clients_list.html', context)


@login_required()
def add_client(request):
    if request.method == 'POST':
        form = ClientCreate(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return HttpResponseRedirect(reverse(list_clients) + '?info=success')
        else:
            return render(request, 'clients/new_client.html', {'form': form})

    else:
        context = {
            'form': ClientCreate()
        }

        return render(request, 'clients/new_client.html', context)
