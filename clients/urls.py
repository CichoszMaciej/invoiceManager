from django.urls import path

from clients.views import list_clients, add_client, toggle_client, edit_client

urlpatterns = [
    path('', list_clients, name='list_clients'),
    path('add/', add_client, name='add_client'),
    path('edit/<int:client_id>', edit_client, name='edit_client'),
    path('toggle/<int:client_id>', toggle_client, name='toggle_client')
]
