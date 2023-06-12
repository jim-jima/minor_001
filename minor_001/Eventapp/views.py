from django.http import HttpResponse
from django.shortcuts import render



def main_page(request):
    return render(request, "main.html", {"main": "active"})


def gallery(request):
    return render(request, "gallery.html", {"gallery": "active"})


def order(request):
    return render(request, "order.html", {"order": "active"})


def scheme(request):
    return render(request, "scheme.html", {"scheme": "active"})


def contacts(request):
    return render(request, "contacts.html", {"contacts": "active"})