from django import forms

class Register(forms.Form):
    namaLengkap =  forms.CharField(label = 'Nama Lengkap')
    nomorTelepon = forms.CharField(label='Nomor Telepon')
    alamat = forms.CharField(label = 'Alamat Tempat Tinggal')