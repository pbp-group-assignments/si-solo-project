from dataclasses import field
from django import forms
from layanan_pengaduan.models import Pengaduan

class FormPengaduan(forms.ModelForm):
    class Meta:
        # judul_pengaduan = forms.CharField(label='judul_pengaduan', max_length=50)
        # deskripsi_pengaduan = forms.CharField(label='deskripsi_pengaduan', max_length=150)
        model = Pengaduan
        fields = ['judul_pengaduan', 'deskripsi_pengaduan']