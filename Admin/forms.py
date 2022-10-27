from django import forms

class AlasanDitolak(forms.Form):
    alasanDitolak = forms.CharField(label='AlasanDitolak', max_length=150)

class NomorIzinUsaha(forms.Form):
    nomorIzinUsaha = forms.CharField(label='AlasanDitolak', max_length=50)