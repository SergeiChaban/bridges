from django.db import models


class ContactApplication(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=128)
    phone = models.CharField(verbose_name='номер телефона', max_length=24)
    email = models.CharField(verbose_name='email', max_length=24)
    subject = models.CharField(verbose_name='Тема сообщения', max_length=96)
    message = models.CharField(verbose_name='Сообщение', max_length=768)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.subject)

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
