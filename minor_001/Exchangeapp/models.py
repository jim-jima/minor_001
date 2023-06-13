from django.db import models

class ExchangeModel(models.Model):
    money = models.IntegerField(unique=True, help_text="Введите денежную сумму, а мы придумаем, как её разменять!", default=0)
    by_500 = models.IntegerField(default=0)
    by_100 = models.IntegerField(default=0)
    by_10 = models.IntegerField(default=0)
    by_2 = models.IntegerField(default=0)
    remainder = models.IntegerField(default=0)

    class Meta:
        ordering = ('-money',)
        verbose_name = 'Размен валюты'
        verbose_name_plural = 'Размен валюты'

    def __int__(self):
        return self.money