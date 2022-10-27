from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(default = "Pengguna", max_length = 15)
    namaLengkap = models.CharField(max_length=60, blank=True)
    nomorTeleponPemilik = models.CharField(max_length=13, blank=True)
    alamatPemilik = models.TextField(blank=True)