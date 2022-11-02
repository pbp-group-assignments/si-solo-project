from django.db import models

# Create your models here.
class TempatWisata(models.Model):
    wisata_title = models.CharField(max_length=255)
    wisata_description = models.TextField(blank=True)
    wisata_highlight = models.TextField(blank=True)
    wisata_image = models.ImageField(blank=True)
    image_url = models.TextField(default='https://www.bnaibrith.ca/wp-content/uploads/2020/07/placeholder.png')