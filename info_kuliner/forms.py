from django import forms

class MenuKulinerForms(forms.Form):
    namaMenu = forms.CharField(max_length=150, label='NamaMenu')
    hargaMenu = forms.CharField(max_length=50, label='HargaMenu')
    deskripsiMenu = forms.CharField(max_length=150, label='DeskripsiMenu')