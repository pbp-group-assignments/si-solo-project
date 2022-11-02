from unittest.util import _MAX_LENGTH
from django.db import models
from pendaftaran_izin_usaha.models import Usaha

# Create your models here.
class KebutuhanPokok(models.Model):
    tokoKebutuhan = models.ForeignKey(Usaha, on_delete=models.CASCADE)
    namaKebutuhan = models.CharField(max_length=150, blank=True)
    hargaKebutuhan = models.CharField(max_length=50, blank=True)
    deskripsiKebutuhan = models.CharField(max_length=150, blank=True)
    