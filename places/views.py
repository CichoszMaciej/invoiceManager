from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


@login_required()
def toggle_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.is_active = not place.is_active
    place.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def edit_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return HttpResponseRedirect(reverse(list_places) + '?info=success-edit')
        else:
            return render(request, 'places/edit_place.html', {'form': form, 'place_name': place.name})

    else:
        return render(request, 'places/edit_place.html',
                      {'form': PlaceForm(instance=place), 'place_name': place.name})
