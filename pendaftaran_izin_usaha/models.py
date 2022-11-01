from django.db import models
from sisolo.models import User

# Create your models here.
class Usaha(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    namaPemilik = models.CharField(max_length=60, blank=True) #Maks 60 karena mengikuti maksimal karakter untuk nama di E-KTP -> Permendagri Nomor 73 Tahun 2022
    nomorTeleponPemilik = models.CharField(max_length=13, blank=True)
    alamatPemilik = models.TextField(blank=True)
    namaUsaha = models.TextField(blank=True)
    jenisUsaha = models.TextField(blank=True)
    alamatUsaha = models.TextField(blank=True)
    nomorTeleponUsaha = models.CharField(max_length=13, blank=True)
    statusPendaftaran = models.TextField(default='Diajukan', blank=True)
    nomorIzinUsaha = models.TextField(blank=True)

class PelakuUsaha(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    namaPemilik = models.CharField(max_length=60, blank=True) #Maks 60 karena mengikuti maksimal karakter untuk nama di E-KTP -> Permendagri Nomor 73 Tahun 2022
    nomorTeleponPemilik = models.CharField(max_length=13, blank=True)
    alamatPemilik = models.TextField(blank=True)
    nik = models.CharField(max_length=16, blank=True)
    status = models.TextField(default='Diproses', blank=True)
    pesan = models.TextField(blank=True)