from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from clients.forms import ClientForm
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
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return HttpResponseRedirect(reverse(list_clients) + '?info=success')
        else:
            return render(request, 'clients/new_client.html', {'form': form})

    else:
        context = {
            'form': ClientForm()
        }

        return render(request, 'clients/new_client.html', context)


@login_required()
def toggle_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.is_active = not client.is_active
    client.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            c = form.save(commit=False)
            c.save()
            return HttpResponseRedirect(reverse(list_clients) + '?info=success-edit')
        else:
            return render(request, 'clients/edit_client.html', {'form': form, 'client_name': client.client_name})

    else:
        return render(request, 'clients/edit_client.html',
                      {'form': ClientForm(instance=client), 'client_name': client.client_name})
