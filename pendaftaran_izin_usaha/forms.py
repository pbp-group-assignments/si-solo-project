from django import forms

class DaftarPelakuUsaha(forms.Form):
    nik = forms.CharField(label = 'NIK')

class DaftarUsaha(forms.Form):
    namaUsaha = forms.CharField(label='NamaUsaha', max_length=50)
    alamatUsaha = forms.CharField(label='AlamatUsaha', max_length=150)
    nomorTeleponUsaha = forms.CharField(label='NomorTeleponUsaha', max_length=13)