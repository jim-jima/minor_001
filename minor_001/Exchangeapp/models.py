from django.db import models

class ExchangeModel(models.Model):
    money = models.IntegerField(help_text="Введите денежную сумму, а мы придумаем, как её разменять!", default=0)
    by_500 = models.IntegerField(default=0)
    by_100 = models.IntegerField(default=0)
    by_10 = models.IntegerField(default=0)
    by_2 = models.IntegerField(default=0)
    remainder = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Размен валюты'

    def __int__(self):
        return self.money