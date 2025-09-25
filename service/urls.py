from django.urls import path
from . import views



urlpatterns = [
    path('', views.service, name='service'),
    path('reserve-system/', views.reserve, name='reserve'),
    path('ec-site/', views.ec_site, name='ec_site'),
]