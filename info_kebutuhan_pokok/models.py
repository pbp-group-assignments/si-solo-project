from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Kebutuhan_Pokok(models.Model):
    item = models.CharField(max_length=100)
    harga = models.IntegerField()
    image = models.URLField()
    