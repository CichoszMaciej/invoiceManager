from django.urls import path

from places.views import list_places, add_place

urlpatterns = [
    path('', list_places, name='list_places'),
    path('add/', add_place, name='add_place')
]
