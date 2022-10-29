from django.db import models
from sisolo.models import User

# Create your models here.
class Pengaduan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_pengaduan = models.DateField()
    judul_pengaduan = models.CharField(max_length=255)
    deskripsi_pengaduan = models.TextField(null=True)
    status_pengaduan = models.BooleanField(default=False)