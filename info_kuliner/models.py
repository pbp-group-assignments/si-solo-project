from django.db import models
from pendaftaran_izin_usaha.models import Usaha

# Create your models here.
class MenuKuliner(models.Model):
    tempatKuliner = models.ForeignKey(Usaha, on_delete=models.CASCADE)
    namaMenu = models.CharField(max_length=150, blank=True)
    hargaMenu = models.CharField(max_length=50, blank=True)
    deskripsiMenu = models.CharField(max_length=150, blank=True)