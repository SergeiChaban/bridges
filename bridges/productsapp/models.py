from imagekit.models.fields import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill

from django.db import models

from servicesapp.models import Service
# --------------------------------   МОДЕЛИ ЕДИНИЦ ИЗМЕРЕНИЙ  -------------------------------------
from django.urls import reverse


class MeasureTypes(models.Model):
    """
    Меры измерений: килограммы, квадратные метры, мегапаскали и др.
    """
    name = models.CharField(verbose_name='единица измерения', max_length=28, unique=True)
    shortcut = models.CharField(verbose_name='ед.изм.', max_length=10, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.shortcut

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


# -----------------------    МОДЕЛИ ПРОДУКТОВ (ТЕХНИЧЕСКИХ РЕШЕНИЙ)   -------------------------------------


class TechnicalSolutions(models.Model):
    """
    Готовые технические решения (группа материалов собранных в готовый к применению продукт "под ключ"
    и продвигаемый на рынок)
    """
    name = models.CharField(verbose_name='название материала', max_length=128, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=128, unique=True)
    measure = models.ForeignKey(MeasureTypes, verbose_name='Единица измерения', on_delete=models.CASCADE, default=1)
    image = ProcessedImageField(upload_to='products_images', processors=[ResizeToFill(370, 220)], format='JPEG',
                                options={'quality': 60})
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=500, blank=True)
    short_desc = models.TextField(verbose_name='краткое описание материала', blank=True, null=True)
    description = models.TextField(verbose_name='описание материала', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def get_absolute_url(self):
        return reverse('products:product', args=[str(self.slug)])

    def __str__(self):
        return f"{self.name}"

    def get_projects(self):
        return self.projects.select_related().distinct('project_id')

    def get_works(self):
        return self.works.select_related().order_by('pk')

    def get_all_docs(self):
        pass

    class Meta:
        verbose_name = 'Техническое решение'
        verbose_name_plural = 'Технические решения'


class TechnicalSolutionsImage(models.Model):
    """
    Дополнительные картинки к готовому решению
    """
    material = models.ForeignKey(TechnicalSolutions, blank=True, null=True, default=None, on_delete=models.CASCADE)
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='products_images', blank=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.alt_desc

    class Meta:
        verbose_name = 'Фотография технического решения'
        verbose_name_plural = 'Фотографии технических решений'


# -----------------------    МОДЕЛИ МАТЕРИАЛОВ   -------------------------------------


class MaterialCategory(models.Model):
    """
    Категории материалов: типа грунтовки, мастики, краски, инструмент и др.
    """
    name = models.CharField(verbose_name='категория материала', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория материала'
        verbose_name_plural = 'Категории материалов'


class Material(models.Model):
    """
    Конкретные материалы (торговые марки): Рабберфлекс-55, Гипердесмо, Матакрил и др.
    """
    name = models.CharField(verbose_name='название материала', max_length=128, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=500, unique=True)
    category = models.ForeignKey(MaterialCategory, verbose_name='категория материала', on_delete=models.CASCADE)
    measure = models.ForeignKey(MeasureTypes, verbose_name='Единица измерения', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images', blank=True)
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    short_desc = models.CharField(verbose_name='краткое описание материала', max_length=500, blank=True, null=True)
    description = models.TextField(verbose_name='описание материала', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class MaterialImage(models.Model):
    """
    Дополнительные картинки к материалам
    """
    material = models.ForeignKey(Material, blank=True, null=True, default=None, on_delete=models.CASCADE)
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='products_images', blank=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.alt_desc

    class Meta:
        verbose_name = 'Фотография материалов'
        verbose_name_plural = 'Фотографии материалов'


# --------------------------------------------    МОДЕЛИ РАБОТ   ------------------------------------------------


class WorkCategory(models.Model):
    """
    Категории работ: типа подготовительные работы, основные работы, испытания, проверка качества.
    """
    name = models.CharField(verbose_name='категория работ', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'


class Work(models.Model):
    """
    Конкретные работы по техническому решению, например: продувка сжатым воздухом, грунтование,
    нанесение мастики и т.д.
    """
    name = models.CharField(verbose_name='название работ', max_length=128, unique=True)
    category = models.ForeignKey(WorkCategory, verbose_name='категория работ', on_delete=models.CASCADE)
    measure = models.ForeignKey(MeasureTypes, verbose_name='Единица измерения', on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material, blank=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    file = models.FileField(upload_to='products_files', blank=True)
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    short_desc = models.CharField(verbose_name='краткое описание материала', max_length=500, blank=True, null=True)
    description = models.TextField(verbose_name='описание материала', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class WorkImage(models.Model):
    """
    Дополнительные картинки к работам
    """
    work = models.ForeignKey(Work, blank=True, null=True, default=None, on_delete=models.CASCADE)
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='work_images', blank=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.alt_desc

    class Meta:
        verbose_name = 'Фотография работ'
        verbose_name_plural = 'Фотографии работ'


# --------------------------------------------    МОДЕЛИ СВЯЗИ   ------------------------------------------------


class ProductWork(models.Model):
    product = models.ForeignKey(TechnicalSolutions, related_name='works', on_delete=models.CASCADE)
    work = models.ForeignKey(Work, verbose_name='Вид работы', on_delete=models.CASCADE)
    material = models.ManyToManyField(Material, verbose_name='Применяемые материалы', blank=True)
    consumption = models.DecimalField(verbose_name='расход материала', max_digits=8, decimal_places=2, blank=True,
                                      null=True)
    value = models.DecimalField(verbose_name='трудозатраты', max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Перечень работ продукта'
        verbose_name_plural = 'Перечень работ продукта'


class TechnicalSolutionsHasService(models.Model):
    technicalsolutions = models.ForeignKey(TechnicalSolutions, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='услуга', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.service}"