from django.forms import ModelForm
from django import forms
from berita_isu_terkini.models import Berita

class BeritaForms(forms.Form):
    judul = forms.CharField(max_length=150, label='Judul')
    tanggal = forms.CharField(max_length=50, label='Tanggal')
    highlight = forms.CharField(max_length=150, label='Highlight')