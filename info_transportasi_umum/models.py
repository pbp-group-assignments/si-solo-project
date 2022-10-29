from django.db import models

# Create your models here.

class Transportation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

class Route(models.Model):
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)
    from_to = models.CharField(max_length=255)

class StopPoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_name = models.CharField(max_length=255)
    stop_location = models.URLField(max_length=255)