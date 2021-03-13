from django.urls import path

from clients.views import list_clients, add_client

urlpatterns = [
    path('', list_clients, name='list_clients'),
    path('add/', add_client, name='add_client')
]
