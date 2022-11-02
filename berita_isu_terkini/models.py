from django.db import models
from pendaftaran_izin_usaha.models import Usaha

# Create your models here.
class Berita(models.Model):
    penulis = models.ForeignKey(Usaha, on_delete=models.CASCADE)
    judul = models.CharField(max_length=250, blank=True)
    tanggal = models.CharField(max_length=50, blank=True)
    highlight = models.CharField(max_length=500, blank=True)
    