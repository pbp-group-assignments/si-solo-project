from django import forms
from saran_pembangunan_kota.models import Saran

class FormSaran(forms.Form):
    class Meta:
        model = Saran
        fields = ['nama', 'email', 'saran_pembangunan']