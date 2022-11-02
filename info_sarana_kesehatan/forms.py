from django import forms
from django.forms import ModelForm, Select
from info_sarana_kesehatan.models import HealthCenter

class HealthCenterForm(ModelForm):
    class Meta:
        model = HealthCenter
        fields = '__all__'
        labels = {
            "name": "Nama tempat layanan kesehatan:",
            "address": "Alamat:",
            "location_url": "URL lokasi layanan kesehatan di Google Maps:",
            "image": "Foto tempat layanan kesehatan:"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Nama tempat layanan kesehatan'})
        self.fields['address'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Alamat'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Kontak'})
        self.fields['image'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['location_url'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'https://goo.gl/maps/...'})

class DeleteHealthCenterForm(ModelForm):
    healthcenter = forms.ModelChoiceField(
            label="Tempat layanan kesehatan yang akan dihapus:",
            queryset = HealthCenter.objects.all()
        )
    
    class Meta:
        model = HealthCenter
        fields = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['healthcenter'].widget.attrs.update({'class': 'form-control mb-2'})