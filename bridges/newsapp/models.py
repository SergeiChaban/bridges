# -*- coding: utf-8 -*-

from imagekit.models.fields import  ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill, Adjust

from django.db import models

from productsapp.models import TechnicalSolutions

# Create your models here.
class News(models.Model):
    """ Модель новости"""
    name = models.CharField(verbose_name='название', max_length=256, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    # image = models.ImageField(upload_to='news_avatars', blank=True)
    image = ProcessedImageField(upload_to='news_avatars', processors = [ResizeToFill(840, 470)], format="JPEG", options={'quality': 90}, blank=True)
    creation_date = models.DateTimeField(verbose_name='создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id)])

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_products(self):
        return self.solutions.select_related()

    def __unicode__(self):
        return self.name

class NewsHasTechnicalSolutions(models.Model):
    """ Модель связи технических решений применяемых на объекте с указанием их объема  """
    name = models.CharField(verbose_name='название конструкции или участка', max_length=256, blank=True, null=True)
    news = models.ForeignKey(News, verbose_name='Новость', related_name="solutions",
                                on_delete=models.CASCADE)
    techsol = models.ForeignKey(TechnicalSolutions, verbose_name='Техническое решение', related_name='news',
                                on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name='Объем работ', max_digits=18, decimal_places=2)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Тех решение проекта'
        verbose_name_plural = 'Тех решения проекта'

