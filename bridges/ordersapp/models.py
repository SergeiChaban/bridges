from django.db import models
from django.conf import settings
from django.db import models
from servicesapp.models import Service


class Order(models.Model):
    PROCEEDED = 'PRD'
    READY = 'RDY'
    CANCEL = 'CNC'

    SERVICE_STATUS_CHOICES = (
        (PROCEEDED, 'обрабатывается'),
        (READY, 'обработан'),
        (CANCEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='услуга', on_delete=models.CASCADE)
    order_number = models.IntegerField(verbose_name='номер заказа пользователя', default=0)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус', max_length=3, choices=SERVICE_STATUS_CHOICES, default=PROCEEDED)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        permissions = (
            ('orders_view', 'Можно видеть все заказы'),
        )

    def __str__(self):
        return 'Заказ: № {}'.format(self.id)


