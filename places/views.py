from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from places.forms import PlaceForm
from places.models import Place


@login_required()
def list_places(request):
    places = Place.objects.all()

    info = ''
    if 'info' in request.GET:
        info = request.GET['info']

    context = {
        'places': places,
        'length': len(places),
        'info': info
    }

    return render(request, 'places/places_list.html', context)


@login_required()
def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return HttpResponseRedirect(reverse(list_places) + '?info=success')
        else:
            return render(request, 'places/new_place.html', {'form': form})

    else:
        context = {
            'form': PlaceForm()
        }

        return render(request, 'places/new_place.html', context)
