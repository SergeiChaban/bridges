from django.db import models
from productsapp.models import TechnicalSolutions


class Project(models.Model):
    """ Модель проекта строительства со статусом """
    DEVELOPMENT = 'разработка'
    EXPERTISE = 'экспертиза'
    TENDER = 'аукцион'
    EXECUTING = 'строительство'
    FINISHING = 'сдача'
    PAYMENT = 'выплата'
    DONE = 'завершен'

    STATUS_CHOICES = (
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
    image = models.ImageField(upload_to='projects_images', blank=True)
    status = models.CharField(verbose_name='статус', max_length=24, choices=STATUS_CHOICES, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    city = models.CharField(verbose_name='город', max_length=512, blank=True, null=True)
    address = models.CharField(verbose_name='адрес', max_length=512, blank=True, null=True)
    latitude = models.FloatField(verbose_name='широта', null=True)
    """ для привязки координат на карте """
    longitude = models.FloatField(verbose_name='долгота', null=True)
    """ для привязки координат на карте """
    contractor = models.CharField(verbose_name='подрядчик', max_length=512, blank=True, null=True)
    customer = models.CharField(verbose_name='заказчик', max_length=512, blank=True, null=True)
    designer = models.CharField(verbose_name='проектировщик', max_length=512, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.city})"
    #
    # def get_pictures(self):
    #     return self.images.all

    # def get_data(self):
    #     return self.solutions.all

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectImage(models.Model):
    """ Галерея фотографий для проекта строительства """
    project = models.ForeignKey(Project, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                related_name="images")
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='products_images', blank=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.alt_desc

    class Meta:
        verbose_name = 'Фотография проекта'
        verbose_name_plural = 'Фотографии проектов'


class ProjectHasTechnicalSolutions(models.Model):
    """ Модель связи технических решений применяемых на объекте с указанием их объема  """
    name = models.CharField(verbose_name='название', max_length=256, unique=False, blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, default=None, on_delete=models.CASCADE)
    tech_sol = models.ManyToManyField(TechnicalSolutions)
    value = models.FloatField(verbose_name='значение', null=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тех решение проекта'
        verbose_name_plural = 'Тех решения проекта'
