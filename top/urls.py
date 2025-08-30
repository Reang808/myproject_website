from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('price/', views.price, name='price'),
    path('features/', views.features, name='features'),
]