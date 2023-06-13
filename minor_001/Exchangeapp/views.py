from django.shortcuts import render, redirect
from .forms import ExchangeForm
from django.template import RequestContext
from .models import ExchangeModel
from django.shortcuts import get_object_or_404
from statistics import median, mean


def error404(request):
    return render(request, "404.html")

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
            return redirect('result', money=money)
        else:
            try:
                return redirect('result', money=int(form.data['money']))
            except:
                return redirect('error404')

    form = ExchangeForm()
    return render(request, 'exchange.html', {'form': form}, RequestContext(request))

def get_result(request, money):
    result = get_object_or_404(ExchangeModel, money=money)
    all = ExchangeModel.objects.filter(money__gt=0)
    all_money = [int(obj) for obj in all]
    context = {
        'money':result.money,
        'by_500':result.by_500,
        'by_100':result.by_100,
        'by_10':result.by_10,
        'by_2':result.by_2,
        'remainder':result.remainder,
        'all': all,
        'median' : median(all_money),
        'average': mean(all_money)
    }

    return render(request, 'result.html', context)