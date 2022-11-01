from django.db import models

# Create your models here.
class Berita(models.Model):
    news_title = models.CharField(max_length=500)
    news_date = models.DateField()
    news_highlight = models.TextField()
    news_image = models.ImageField()
    