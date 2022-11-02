from django import forms

class DaftarWisataForms(forms.Form):
    namaWisata = forms.CharField(max_length=150, label='NamaWisata')
    hargaWisata = forms.CharField(max_length=50, label='HargaWisata')
    deskripsiWisata = forms.CharField(max_length=150, label='DeskripsiWisata')
