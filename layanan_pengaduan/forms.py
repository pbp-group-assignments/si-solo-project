from django import forms

class FormPengaduan(forms.Form):
    judul_pengaduan = forms.CharField(label='judul_pengaduan', max_length=50)
    deskripsi_pengaduan = forms.CharField(label='deskripsi_pengaduan', max_length=150)