from django.urls import path
from . import views

urlpatterns = [
    path('', views.Exchange.as_view(), name='signup')]
