from django.db import models

# Create your models here.

class Service(models.Model):

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services_images', blank=True)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.title