from django.forms import ModelForm
from info_kebutuhan_pokok.models import Kebutuhan_Pokok

class Create(ModelForm):
    class Meta:
        model = Kebutuhan_Pokok
        fields = ['item', 'harga', 'image' ]