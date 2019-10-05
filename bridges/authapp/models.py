from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(AbstractUser):
    GENDER_CHOICES = (
        (None, 'не указан'),
        ('male', 'мужчина'),
        ('female', 'женщина'),
    )
    # у AbstractUser есть поля: password, last_login, is_superuser, username, first_name, last_name, email, is_staff,
    # is_active и date_joined. Создадим дополнительные поля:
    patronymic = models.CharField(verbose_name='Отчество', max_length=150, default='', null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=50, default='', null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=50, default='', null=True, blank=True)
    company = models.CharField(verbose_name='Компания', max_length=50, default='', null=True, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=50, default='', null=True, blank=True)
    project = models.CharField(verbose_name='Проект', max_length=50, default='', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        ordering = ['-date_joined']


class Company(models.Model):
    """
    полное название*, сокращенное название*, форма организации (ООО, ПАО, ОА, ИП и др.), город, категория*, ИНН*,
    категория организации (внешний ключ на CategoryCompany), email, phone, address
    """
    pass


class CategoryCompany(models.Model):
    """
    название категории,  комментарий model.
    примеры категорий: designer (проектный институт), contractor (подрядная организация), customer (заказчик),
    dealer (дилер), reseller (перекупщик), partner (партнер), agent (агент), supplier (поставщик), competitor (
    конкурент), researcher (исследовательская организация), expertise (экспертиза)
    """
    pass
