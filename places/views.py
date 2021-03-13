from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from places.models import Place


@login_required()
def list_places(request):
    places = Place.objects.all()
    context = {
        'places': places
    }

    return render
