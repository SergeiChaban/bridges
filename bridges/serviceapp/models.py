from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Service(models.Model):

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services_images', blank=True)
    available = models.BooleanField(default=True)


    # def get_absolute_url(self):
    # 	return reverse('service_detail_url', kwargs={'slug':self.slug})


    def __str__(self):
        return self.title