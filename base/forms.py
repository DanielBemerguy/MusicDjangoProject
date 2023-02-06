from django.forms import ModelForm
from .models import Band, Music


class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        exclude = ['host', 'participants']

class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = "__all__"
        exclude = ['host']

