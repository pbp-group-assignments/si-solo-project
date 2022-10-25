from django import forms

class DaftarPelakuUsaha(forms.Form):
    nik = forms.CharField(label = 'NIK')