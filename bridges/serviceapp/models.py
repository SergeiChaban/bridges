from django.db import models

# Create your models here.

class Service(models.Model):

    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='services')
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.title