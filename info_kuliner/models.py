from django.db import models

# Create your models here.
class TempatKuliner(models.Model):
    kuliner_title = models.CharField(max_length=255)
    kuliner_description = models.TextField()
    kuliner_highlight = models.TextField()