from django import forms

class KebutuhanPokokForms(forms.Form):
    namaKebutuhan = forms.CharField(max_length=150, label='NamaKebutuhan')
    hargaKebutuhan = forms.CharField(max_length=50, label='HargaKebutuhan')
    deskripsiKebutuhan = forms.CharField(max_length=150, label='DeskripsiKebutuhan')