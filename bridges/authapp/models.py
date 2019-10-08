from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# модель содержит информацию о категории компании, например: проектный институт, подрядная организация, заказчик и др.
class CategoriesCompanies(models.Model):
    name_category = models.CharField(verbose_name='Категория компании*', max_length=50, unique=True)
    description = models.CharField(verbose_name='Описание категории', max_length=300, default='', null=True, blank=True)

    class Meta:
        verbose_name = "Категорию компании"
        verbose_name_plural = "Категории компаний"
        ordering = ["name_category"]

    def __str__(self):
        return self.name_category.title()


# модель содержит подробную информацию о компании
class Companies(models.Model):
    FORMS_COMPANIES = (
        (None, 'не указано'),
        ('IP', 'ИП'),
        ('OOO', 'ООО'),
        ('OAO', 'ОАО'),
        ('ZAO', 'ЗАО'),
        ('PAO', 'ПАО'),
        ('AO', 'АО'),
        ('NAO', 'НАО'),
        ('NKO', 'НКО'),
        ('ANO', 'АНО'),
        ('GBU', 'ГБУ'),
    )
    name_company = models.CharField(verbose_name='Полное название компании*', max_length=70, null=True, blank=True)
    short_name = models.CharField(verbose_name='Короткое название', max_length=30, blank=True, null=True)
    form_company = models.CharField(verbose_name='Форма', max_length=3, choices=FORMS_COMPANIES, blank=True, null=True)
    category_company = models.ManyToManyField(CategoriesCompanies, verbose_name='Категория компании*')
    inn = models.CharField(verbose_name='ИНН*', max_length=30, unique=True)
    city = models.CharField(verbose_name='Город', max_length=30, default='', null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=300, default='', null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=30, default='', null=True, blank=True)
    email = models.CharField(verbose_name='Эл. почта', max_length=30, default='', null=True, blank=True)

    class Meta:
        verbose_name = "Новую компанию"
        verbose_name_plural = "Компании"
        ordering = ["name_company"]

    def __str__(self):
        return self.name_company.title()

    def get_category_company(self):  # т.к. модели связаны, получаем конкретную категорию компании
        return ",".join([str(p) for p in self.category_company.all()])


# модель содержит информацию о всех пользователях, включая superuser, сотрудников компании и простых пользователей
class Users(AbstractUser):
    GENDER_CHOICES = (
        (None, 'не указан'),
        ('male', 'мужчина'),
        ('female', 'женщина'),
    )
    # у AbstractUser есть поля: username, password, last_login, first_name, last_name, email, is_superuser, is_staff,
    # is_active и date_joined. Создадим дополнительные поля:
    username = models.CharField(verbose_name='Логин*', max_length=50, unique=True)  # переопределили из-за verbose_name
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, default='', null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон*', max_length=50, default='не указан')
    city = models.CharField(verbose_name='Город', max_length=50, default='', null=True, blank=True)
    # company = models.CharField(verbose_name='Компания', max_length=50, default='', null=True, blank=True)
    company = models.ManyToManyField(Companies, verbose_name='Компания')
    position = models.CharField(verbose_name='Должность', max_length=50, default='', null=True, blank=True)
    project = models.CharField(verbose_name='Проект', max_length=50, default='', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователя"
        ordering = ['-date_joined']
