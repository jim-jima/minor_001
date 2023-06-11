from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name = "main"),
    path("order", views.order, name="order"),
    path("gallery", views.gallery, name="gallery"),
    path("scheme", views.scheme, name="scheme"),
    path("contacts", views.contacts, name="contacts")
]