from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.



class ServiceCategory(models.Model):
    name = models.CharField(verbose_name='категория услуги', max_length=128, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=154, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{0}/{1}/{2}'.format('services_images', instance.slug, filename)

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название услуги', max_length=128, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=154, unique=True)
    image = models.ImageField(upload_to= image_folder, blank=True)
    description = models.TextField(verbose_name='описание услуги', blank=True)
    is_active = models.BooleanField(verbose_name='показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



def pre_save_services_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)
        instance.slug = slug

pre_save.connect(pre_save_services_slug, sender=Service)