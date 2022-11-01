from django.db import models

# Create your models here.

class Transportation(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Route(models.Model):
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)
    from_to = models.CharField(max_length=255)

    def __str__(self):
        return self.transportation.name + ': ' + self.from_to

class StopPoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_name = models.CharField(max_length=255)
    stop_location = models.URLField(max_length=255)

    def __str__(self):
        return self.route.__str__() + ': ' + self.stop_name