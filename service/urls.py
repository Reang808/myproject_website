from django.urls import path
from . import views



urlpatterns = [
    path('', views.service, name='service'),
    path('reserve/', views.reserve, name='reserve'),
    path('linebizconnect/', views.linebizconnect, name='linebizconnect'),
    path('ec_site/', views.ec_site, name='ec_site'),
]