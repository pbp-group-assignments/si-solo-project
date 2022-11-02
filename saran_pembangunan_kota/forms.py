from dataclasses import field
from django import forms
from saran_pembangunan_kota.models import Saran

class FormSaran(forms.ModelForm):
    class Meta:
        model = Saran
        fields = ['nama', 'email', 'saran_pembangunan']