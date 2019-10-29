from django.db import models

# Create your models here.
class News(models.Model):
    """ Модель новости"""
    DEVELOPMENT = 'разработка'
    EXPERTISE = 'экспертиза'
    TENDER = 'аукцион'
    EXECUTING = 'строительство'
    FINISHING = 'сдача'
    PAYMENT = 'выплата'
    DONE = 'завершен'

    TYPEREL_CHOICES = (
        (DEVELOPMENT, 'разработка'),
        (EXPERTISE, 'экспертиза'),
        (TENDER, 'аукцион'),
        (EXECUTING, 'строительство'),
        (FINISHING, 'сдача'),
        (PAYMENT, 'выплата'),
        (DONE, 'завершен'),
    )
    name = models.CharField(verbose_name='название', max_length=256, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='аватарка', blank=True)
    creation_date = models.DateTimeField(verbose_name='создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    typeRel = models.CharField(verbose_name='тип', max_length=24, choices=TYPEREL_CHOICES, blank=True)

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id)])

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
