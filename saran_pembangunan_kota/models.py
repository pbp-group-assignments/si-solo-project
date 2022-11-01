from django.db import models
from sisolo.models import User

# Create your models here.
class Saran(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    saran_pembangunan = models.TextField()
