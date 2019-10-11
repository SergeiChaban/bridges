from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit

from authapp.models import Company, Users
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
    image = models.ImageField(upload_to='аватарка', blank=True)
    status = models.CharField(verbose_name='статус', max_length=24, choices=STATUS_CHOICES, blank=True)
    creation_date = models.DateTimeField(verbose_name='создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    city = models.CharField(verbose_name='город', max_length=512, blank=True, null=True)
    address = models.CharField(verbose_name='адрес', max_length=512, blank=True, null=True)
    techsol = models.ManyToManyField(TechnicalSolutions, through='ProjectHasTechnicalSolutions')
    participant = models.ManyToManyField(Company, blank=True)
    manager = models.ManyToManyField(Users, default=1, related_name='manager')
    coordinate = models.CharField(verbose_name='координаты', max_length=34, null=True, blank=True)
    map_mark = models.SlugField(verbose_name='id метки на карте', max_length=128, blank=True)
    text_for_map = models.TextField(verbose_name='текст для метки', max_length=240, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='активен', default=False)

    def __str__(self):
        return f"{self.name} ({self.city})"

    def get_pictures(self):
        return self.images.select_related()

    def get_products(self):
        return self.solutions.select_related()

    def get_companies(self):
        return self.companies.select_related()

    def get_managers(self):
        return self.managers.select_related()

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


def pre_save_map_mark(sender, instance, *args, **kwargs):
    if not instance.map_mark:
        map_mark = slugify(translit(instance.name, reversed=True)).replace('-', '_')
        instance.map_mark = map_mark


pre_save.connect(pre_save_map_mark, sender=Project)


# СВЯЗАНО
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


# СВЯЗАНО
class ProjectHasTechnicalSolutions(models.Model):
    """ Модель связи технических решений применяемых на объекте с указанием их объема  """
    name = models.CharField(verbose_name='название', max_length=256, unique=False, blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                related_name="solutions")
    techsol = models.ForeignKey(TechnicalSolutions, blank=True, null=True, default=None, on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name='значение', max_digits=18, decimal_places=2, null=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тех решение проекта'
        verbose_name_plural = 'Тех решения проекта'


# СВЯЗАНО
class ProjectCompany(models.Model):
    """ Модель связи компаний на объекте """
    name = models.CharField(verbose_name='название', max_length=256, unique=False, blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                related_name="companies")
    company = models.ForeignKey(Company, blank=True, null=True, default=None, on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name='значение', max_digits=18, decimal_places=2, null=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


# СВЯЗАНО
class ProjectManagers(models.Model):
    """ Модель связи людей на объекте """
    name = models.CharField(verbose_name='название', max_length=256, unique=False, blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                related_name="managers")
    manager = models.ForeignKey(Users, blank=True, null=True, default=None, on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name='значение', max_digits=18, decimal_places=2, null=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
