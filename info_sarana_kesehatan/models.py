from django.db import models

# Create your models here.

class HealthCenter(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location_url = models.URLField(max_length=255)
    contact = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name