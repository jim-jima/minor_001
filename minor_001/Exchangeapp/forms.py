from django import forms
from .models import ExchangeModel

class ExchangeForm(forms.Form):
    model = ExchangeModel
    money = forms.IntegerField(help_text="Введите денежную сумму, а мы придумаем, как её разменять!")