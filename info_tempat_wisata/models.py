from django.db import models
from pendaftaran_izin_usaha.models import Usaha

# Create your models here.
class DaftarWisata(models.Model):
    tempatWisata = models.ForeignKey(Usaha, on_delete=models.CASCADE)
    namaWisata = models.CharField(max_length=150, blank=True)
    hargaWisata = models.CharField(max_length=150, blank=True)
    deskripsiWisata = models.CharField(max_length=150, blank=True)
