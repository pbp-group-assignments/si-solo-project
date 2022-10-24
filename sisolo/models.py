from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(default = "Pengguna", max_length = 15)
    namaPemilik = models.CharField(max_length=60, blank=True) #Maks 60 karena mengikuti maksimal karakter untuk nama di E-KTP -> Permendagri Nomor 73 Tahun 2022
    nomorTeleponPemilik = models.CharField(max_length=13, blank=True)
    alamatPemilik = models.TextField(blank=True)