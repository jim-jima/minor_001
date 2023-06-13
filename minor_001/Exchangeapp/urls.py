from django.urls import path
from . import views


urlpatterns = [
    path('error404/', views.error404, name='error404'),
    path('', views.exchange, name='exchange'),
    path('result/<int:money>/', views.get_result, name='result')
]
