from django.urls import path

from places.views import list_places, add_place, edit_place, toggle_place

urlpatterns = [
    path('', list_places, name='list_places'),
    path('add/', add_place, name='add_place'),
    path('edit/<int:place_id>', edit_place, name='edit_place'),
    path('toggle/<int:place_id>', toggle_place, name='toggle_place')
]
