from django.forms import ModelForm

from places.models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
