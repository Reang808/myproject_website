from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('price/', views.price, name='price'),
    path('features/', views.features, name='features'),
    path('privacy/', views.privacy, name='privacy'),
]