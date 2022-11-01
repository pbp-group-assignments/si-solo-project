from dataclasses import field
from django import forms
from layanan_pengaduan.models import Pengaduan

class FormPengaduan(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['judul_pengaduan', 'deskripsi_pengaduan']