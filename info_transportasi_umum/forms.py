from django import forms
from django.forms import ModelForm, Select
from info_transportasi_umum.models import Transportation, Route, StopPoint

class TransportationForm(ModelForm):
    class Meta:
        model = Transportation
        fields = '__all__'
        labels = {
            "name": "Nama transportasi umum:",
            "description": "Deskripsi:",
            "image": "Foto transportasi umum:"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Nama transportasi'})
        self.fields['description'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Deskripsi transportasi...'})
        self.fields['image'].widget.attrs.update({'class': 'form-control mb-2'})

class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        labels = {
            "transportation": "Transportasi:",
            "from_to": "Rute:"
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['transportation'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['from_to'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Lokasi awal - Lokasi akhir'})

class StopPointForm(ModelForm):
    class Meta:
        model = StopPoint
        fields = '__all__'
        labels = {
            "route": "Rute:",
            "stop_name": "Nama titik pemberhentian:",
            "stop_location": "URL lokasi titik pemberhentian di Google Maps:"
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['stop_name'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Nama lokasi titik pemberhentian'})
        self.fields['stop_location'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'https://goo.gl/maps/...'})

class DeleteTransportationForm(ModelForm):
    transportation = forms.ModelChoiceField(
        label="Transportasi yang akan dihapus:",
        queryset = Transportation.objects.all()
        )
    
    class Meta:
        model = Transportation
        fields = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['transportation'].widget.attrs.update({'class': 'form-control mb-2'})