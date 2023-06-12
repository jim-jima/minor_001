from django.shortcuts import render, redirect
from .forms import ExchangeForm
from django.template import RequestContext
from .models import ExchangeModel
from django.shortcuts import get_object_or_404


def error404(request):
    return render(request, "error404.html")

def exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            calc = form.save()
            money = int(calc)
            print(calc)
            calc.by_500 = money//500
            calc.by_100 = (money - calc.by_500 * 500) // 100
            calc.by_10 = (money - calc.by_500 * 500 - calc.by_100 * 100) // 10
            calc.by_2 = (money - calc.by_500 * 500 - calc.by_100 * 100 - calc.by_10 * 10 ) // 2
            calc.remainder = money - calc.by_500 * 500 - calc.by_100 * 100 - calc.by_10 * 10 - calc.by_2 * 2
            calc.save()
            print(ExchangeModel.objects.last().money)
            print(ExchangeModel.objects.last().by_500)
            print(ExchangeModel.objects.last().by_100)
            print(ExchangeModel.objects.last().by_10)
            print(ExchangeModel.objects.last().by_2)
            print(ExchangeModel.objects.last().remainder)
        else:
            return render(request, 'error404.html')

    form = ExchangeForm()
    return render(request, 'exchange.html', {'form': form}, RequestContext(request))

def get_result(request):
    pass