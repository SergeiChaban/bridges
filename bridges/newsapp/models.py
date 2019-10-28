from django.db import models

# Create your models here.
class News(models.Model):
    """ Модель новости"""
    name = models.CharField(verbose_name='название', max_length=256, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='аватарка', blank=True)
    creation_date = models.DateTimeField(verbose_name='создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id)])

    def get_pictures(self):
        return self.images.select_related()

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# СВЯЗАНО
class NewsImage(models.Model):
    """ Галерея фотографий для проекта строительства """
    news = models.ForeignKey(News, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                related_name="images")
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='news_images', blank=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Фотография новости'
        verbose_name_plural = 'Фотографии новостей'
