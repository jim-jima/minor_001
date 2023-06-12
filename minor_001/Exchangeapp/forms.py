from django import forms
from .models import ExchangeModel

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = ExchangeModel
        fields = ('money',)
