from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('price', views.price, name='price'),
    path('elements', views.elements, name='elements'),
]
