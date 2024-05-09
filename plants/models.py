from django.db import models


class Plant(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_liked = models.BooleanField(default=False)
    image = models.FileField(upload_to='plant_images/', blank=True)
    image_path = models.CharField(max_length=255, blank=True)
