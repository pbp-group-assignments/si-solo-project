from django import forms

class Register(forms.Form):
    namaLengkap =  forms.CharField(label = 'Nama Lengkap')
    nomorTelepon = forms.IntegerField(label='Nomor Telepon')
    alamat = forms.CharField(label = 'Alamat Tempat Tinggal')