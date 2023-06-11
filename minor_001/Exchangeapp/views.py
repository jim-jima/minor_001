from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ExchangeForm


class Exchange(CreateView):
    form_class = ExchangeForm
    template_name = 'tut budet shablon'
