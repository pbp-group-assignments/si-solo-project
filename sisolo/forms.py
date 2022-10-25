from django import forms

class Register(forms.Form):
    nomorTelepon = forms.IntegerField(label='Nomor Telepon')
    alamat = forms.CharField(label = 'Alamat Tempat Tinggal')